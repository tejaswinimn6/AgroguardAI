 🌿 AgroGuard AI

📌 Overview
AgroGuard AI is a Streamlit-based AI web application that detects plant diseases from leaf images using Google Gemini AI and provides treatment recommendations along with risk prediction

❗ Problem Statement
- Farmers struggle to identify plant diseases early  
- Lack of expert agricultural guidance in rural areas  
- Crop loss due to delayed treatment  

 💡 Solution
AgroGuard AI helps users by:
- Uploading plant leaf images
- Detecting disease using Gemini AI
- Providing treatment and prevention steps
- Predicting disease risk using environmental factors


 ✨ Key Features
- 🌿 AI-based plant disease detection using Gemini API  
- 📸 Image upload via Streamlit  
- 🌱 Supports multiple crops (rice, tomato, potato, etc.)  
- 💊 Treatment and prevention recommendations  
- 🌡 Risk prediction based on temperature & humidity  
- ⚡ Simple and interactive UI  

🏗️ Architecture
User Input (Image + Climate Data)  
→ Streamlit UI  
→ Google Gemini AI Model  
→ Disease Analysis  
→ Treatment Output + Risk Prediction  

 ▶️ How to Run Locally

```bash
pip install streamlit pillow google-generativeai
streamlit run app.py

🔑 API Setup
Create a .streamlit/secrets.toml file:
TOML
GOOGLE_API_KEY = "your_api_key_here"

🔮 Future Scope
Offline AI model (no API dependency)
Mobile application version
Larger crop disease dataset
Smart irrigation recommendations

🏆 Hackathon Note
This project combines:
Generative AI (Gemini)
Agricultural problem-solving
Real-time risk prediction
Streamlit for fast deployment
