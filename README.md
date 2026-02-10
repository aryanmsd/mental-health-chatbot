<img width="1508" height="828" alt="image" src="https://github.com/user-attachments/assets/14b75471-b6d3-496e-8c6d-275c09273b56" />

# 🧠 AI Mental Health Support Chatbot

An **emotion-aware AI mental health support chatbot** built using **Transformers**, **Google Gemini**, and **Streamlit**.  
The chatbot detects user emotions and responds with empathetic, supportive messages while following **responsible AI and ethical guidelines**.

⚠️ This chatbot is for **emotional support only** and does **NOT** replace professional mental health care.

---

## 🔗 Live Demo

👉 **Live App:** https://mental-health-chatbot-8ivtaujxdqjm4t24aaeotj.streamlit.app/

---

## 🔍 Project Overview

This project demonstrates a real-world **Generative AI application** that combines:
- Emotion detection using a pretrained NLP model
- Context-aware response generation using Google Gemini
- A conversational UI built with Streamlit

The goal is to provide supportive, non-judgmental responses while ensuring user safety and ethical AI usage.

---

## 🚀 Features

- 🧠 **Emotion Detection** using GoEmotions (BERT-based model)
- 💬 **Empathetic AI Responses** powered by Google Gemini
- 🛡️ **Safety Layer** for high-risk mental health inputs
- 🗂️ **Conversation Memory** using Streamlit session state
- 🎨 **Chat UI with Bubbles & Emotion Badge**
- 🧹 **Clear Chat Functionality**
- ☁️ **Deployed on Streamlit Cloud**

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **Hugging Face Transformers**
- **PyTorch (CPU)**
- **Google Gemini (`google-genai`)**
- **NumPy**

---

## 📁 Project Structure
mental-health-chatbot/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│── emotion_detector.py
│── prompts.py
│── emotion_test.py
│── test.py
│── .streamlit/
│ └── secrets.toml (not committed)


---

## 🧠 Local vs Cloud Dependency Setup

This project uses **different dependency strategies** for local development and cloud deployment due to Python runtime differences.

### 🔹 Local Development (Windows / Python 3.11)
For local development, PyTorch is pinned to a stable CPU-only version to avoid DLL and NumPy compatibility issues on Windows.

- Python: 3.11.x  
- PyTorch: 2.1.2 (CPU)  
- NumPy: 1.26.4  
- Transformers: 4.36.2  

This setup ensures reliable local execution and smooth model loading.

---

### 🔹 Streamlit Cloud Deployment (Linux / Python 3.13)
Streamlit Cloud runs on Python 3.13, where older PyTorch versions are unavailable.  
For deployment, PyTorch is installed dynamically using relaxed constraints.

- PyTorch: >= 2.5.0  
- NumPy: < 2  
- Transformers: Compatible version range  

> This approach follows **industry-standard ML deployment practices**.

---

## 📦 Installation (Local Setup)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/aryanmsd/mental-health-chatbot.git
cd mental-health-chatbot

2️⃣ Create virtual environment
pip install -r requirements.txt

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add API key
Create .streamlit/secrets.toml:
GEMINI_API_KEY = "your_api_key_here"

5️⃣ Run the app
streamlit run app.py

🛡️ Responsible AI & Safety
❌ No medical diagnosis
❌ No therapy replacement
✅ Encourages healthy coping strategies
✅ Detects high-risk language and shows safety guidance
✅ Non-judgmental and empathetic responses

🧪Example Interaction

User:

I feel anxious about my future.

Detected Emotion:

Fear / Nervousness

AI Response:

“It sounds like you’re feeling overwhelmed. Worrying about the future is very common, and you’re not alone. Taking small steps and talking to someone you trust can really help.”

👨‍💻 Author
Aryan MSD
Computer Science Undergraduate | Generative AI Enthusiast

🔗 GitHub: https://github.com/aryanmsd

⭐ Support
If you found this project useful, feel free to ⭐ star the repository!

