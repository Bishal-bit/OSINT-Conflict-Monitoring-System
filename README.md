🛡️ OSINT Conflict Monitoring System
📌 Overview

This project builds an end-to-end OSINT (Open-Source Intelligence) pipeline that collects, processes, and analyzes geopolitical event data from multiple sources.
The system transforms unstructured news data into structured, actionable intelligence.

🎯 Objectives
1. Aggregate data from multiple sources (RSS, APIs, web scraping)
2. Convert unstructured text into structured event data
3. Extract key intelligence (actors, locations, event types)
4. Assign confidence and severity scores
5. Provide a reproducible and scalable pipeline

📡 Data Sources
1. Google News → RSS-based ingestion
2. BBC News → RSS feed ingestion
3. ISW (Institute for the Study of War) → Web scraping (BeautifulSoup)
4. GDELT → API-based ingestion (JSON data)

🏗️ Architecture
Data Sources → Ingestion → Processing → Intelligence Extraction → Scoring → JSON Output → Dashboard

🔄 Pipeline Workflow
1. Data Ingestion
2. RSS parsing (Google, BBC)
3. API calls (GDELT)
4. Web scraping (ISW)
5. Data Processing
6. Cleaning and deduplication
7. Parsing text data
8. Intelligence Extraction
9. Actor detection
10. Location identification
11. Event classification
12. Scoring System
13. Confidence scoring (source + keywords)
14. Severity scoring (keyword-based rules)
15. Output
16. Structured JSON file for analysis

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

## 👤 Author

**Bishal Sarkar**  
Data Science @ IIT Guwahati  

Passionate about Machine Learning, RAG systems, and real-world AI applications.

- 🔗 GitHub: https://github.com/bishal-bit  
- 💼 LinkedIn: [https://linkedin.com/in/bishal-sarkar](https://www.linkedin.com/in/bishal-sarkar-b98106217/)  
- 📧 Email: bishal.sarkar2001@gmail.com

