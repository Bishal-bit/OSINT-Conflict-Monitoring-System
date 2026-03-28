🛡️ OSINT Conflict Monitoring System
📌 Overview

This project builds an end-to-end OSINT (Open-Source Intelligence) pipeline that collects, processes, and analyzes geopolitical event data from multiple sources.
The system transforms unstructured news data into structured, actionable intelligence.

🎯 Objectives
Aggregate data from multiple sources (RSS, APIs, web scraping)
Convert unstructured text into structured event data
Extract key intelligence (actors, locations, event types)
Assign confidence and severity scores
Provide a reproducible and scalable pipeline
📡 Data Sources
Google News → RSS-based ingestion
BBC News → RSS feed ingestion
ISW (Institute for the Study of War) → Web scraping (BeautifulSoup)
GDELT → API-based ingestion (JSON data)
🏗️ Architecture
Data Sources → Ingestion → Processing → Intelligence Extraction → Scoring → JSON Output → Dashboard
🔄 Pipeline Workflow
Data Ingestion
RSS parsing (Google, BBC)
API calls (GDELT)
Web scraping (ISW)
Data Processing
Cleaning and deduplication
Parsing text data
Intelligence Extraction
Actor detection
Location identification
Event classification
Scoring System
Confidence scoring (source + keywords)
Severity scoring (keyword-based rules)
Output
Structured JSON file for analysis
📊 Features
Multi-source data aggregation
Rule-based NLP extraction
Confidence scoring system
Severity classification
Modular and scalable pipeline
💻 How to Run Locally
1. Clone the repository
git clone <your-repo-link>
cd <project-folder>
2. Install dependencies
pip install -r requirements.txt
3. Run the application
streamlit run app.py
📁 Output
Processed data stored as:
data_processed_events.json
⚠️ Challenges
Inconsistent data formats across sources
Noisy and unstructured text
Web scraping limitations (403 errors)
Ambiguity in entity and location extraction
🚀 Future Improvements
Use NLP models (NER) for better extraction
Real-time streaming pipeline
Advanced visualization dashboard
Database integration
🤖 AI Usage Declaration

AI tools were used as a support system for debugging, structuring, and documentation.
All core design, implementation, and decision-making were done independently.

📚 Tech Stack
Python
Pandas
Requests
BeautifulSoup
Streamlit
👨‍💻 Author
Bishal Sarkar
