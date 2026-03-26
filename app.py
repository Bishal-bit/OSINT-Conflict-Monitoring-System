
import streamlit as st
import pandas as pd
import json
import plotly.express as px

st.set_page_config(page_title="SAIG Conflict Monitor", layout="wide")

@st.cache_data
def load_data():
    with open('data_processed_events.json', 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    df['event_datetime_utc'] = pd.to_datetime(df['event_datetime_utc'])
    return df.sort_values('event_datetime_utc', ascending=False)

df = load_data()

# 1. SIDEBAR (Drill-Down Capability)
st.sidebar.title("🔍 Intelligence Filters")
location_filter = st.sidebar.multiselect("Filter by Location", options=df['location_text'].unique(), default=df['location_text'].unique())
filtered_df = df[df['location_text'].isin(location_filter)]

# 2. EXECUTIVE SUMMARY
st.title("🛡️ Strategic Conflict Monitor")
st.info(f"**Posture:** HIGH ALERT | **Primary Focus:** {', '.join(location_filter[:3])}...")

col1, col2, col3 = st.columns(3)
col1.metric("Total Events", len(filtered_df))
col2.metric("Avg Severity", round(filtered_df['severity_score'].mean(), 1))
col3.metric("Verified Ratio", f"{int((len(filtered_df[filtered_df['information_status']=='verified'])/len(filtered_df))*100)}%")

# 3. TREND VIEW (Escalation Signaling)
st.subheader("📈 Severity Trend (Escalation Signal)")
trend_df = filtered_df.groupby(filtered_df['event_datetime_utc'].dt.date)['severity_score'].mean().reset_index()
fig = px.line(trend_df, x='event_datetime_utc', y='severity_score', title="Daily Avg Severity", markers=True)
st.plotly_chart(fig, use_container_width=True)

# 4. LOCATION / MAP VIEW
st.subheader("📍 Kinetic Hotspots")
COORDS = {"Tehran": [35.68, 51.38], "Shiraz": [29.59, 52.58], "Jerusalem": [31.76, 35.21], "Tel Aviv": [32.08, 34.78]}
filtered_df['lat'] = filtered_df['location_text'].map(lambda x: COORDS.get(x, [None])[0])
filtered_df['lon'] = filtered_df['location_text'].map(lambda x: COORDS.get(x, [None, None])[1])
st.map(filtered_df.dropna(subset=['lat', 'lon'])[['lat', 'lon']])

# 5. EVENT FEED & PROVENANCE
st.subheader("📋 Intelligence Feed (Source Visibility)")
st.dataframe(filtered_df[['event_datetime_utc', 'source_name', 'location_text', 'claim_text', 'severity_score', 'information_status']], use_container_width=True)
