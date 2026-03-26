
import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="SAIG Conflict Monitor", layout="wide")

# Emergency Data Check
if not os.path.exists('data_processed_events.json'):
    dummy_data = [{"event_datetime_utc": "2026-03-26T12:00:00Z", "source_name": "System", "claim_text": "Awaiting Data Ingestion...", "severity_score": 5, "location_text": "Tehran", "information_status": "verified"}]
    with open('data_processed_events.json', 'w') as f_out:
        json.dump(dummy_data, f_out)

def load_data():
    with open('data_processed_events.json', 'r') as f_in:
        df = pd.DataFrame(json.load(f_in))
    df['event_datetime_utc'] = pd.to_datetime(df['event_datetime_utc'])
    return df.sort_values('event_datetime_utc', ascending=False)

try:
    df = load_data()
    st.title("🛡️ Strategic Conflict Monitor")
    st.info(f"System Status: LIVE | Primary Hotspot: {df['location_text'].mode()[0]}")

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Events", len(df))
    c2.metric("Avg Severity", round(df['severity_score'].mean(), 1))
    c3.metric("Latest Update", df['event_datetime_utc'].iloc[0].strftime('%H:%M UTC'))

    st.subheader("📍 Kinetic Hotspots")
    COORDS = {"Tehran": [35.68, 51.38], "Shiraz": [29.59, 52.58], "Jerusalem": [31.76, 35.21], "Tel Aviv": [32.08, 34.78]}
    df['lat'] = df['location_text'].map(lambda x: COORDS.get(x, [None])[0])
    df['lon'] = df['location_text'].map(lambda x: COORDS.get(x, [None, None])[1])
    st.map(df.dropna(subset=['lat', 'lon'])[['lat', 'lon']])

    st.subheader("📋 Intelligence Feed")
    st.dataframe(df[['event_datetime_utc', 'source_name', 'claim_text', 'severity_score']], use_container_width=True)
except Exception as e:
    st.error(f"Dashboard Error: {e}")
