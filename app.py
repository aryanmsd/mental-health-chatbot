import streamlit as st
from google import genai
from transformers import pipeline

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Mental Health Support Chatbot",
    page_icon="🧠",
    layout="centered"
)
st.markdown("""
<style>
.chat-bubble-user {
    background-color: #1f2937;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 8px;
}
.chat-bubble-ai {
    background-color: #111827;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 12px;
}
.emotion-badge {
    display: inline-block;
    background-color: #2563eb;
    color: white;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 12px;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)


st.title("🧠 AI Mental Health Support Chatbot")
st.caption(
    "⚠️ This chatbot is for emotional support only and does NOT replace professional mental health care."
)

# -----------------------------
# LOAD EMOTION CLASSIFIER
# -----------------------------
@st.cache_resource
def load_emotion_model():
    return pipeline(
        "text-classification",
        model="bhadresh-savani/bert-base-go-emotion",
        top_k=None
    )

emotion_classifier = load_emotion_model()

def detect_emotion(text):
    emotions = emotion_classifier(text)[0]
    top_emotion = max(emotions, key=lambda x: x["score"])
    return top_emotion["label"]

# -----------------------------
# SAFETY CHECK
# -----------------------------
def high_risk(text):
    risk_words = [
        "suicide", "kill myself", "end my life",
        "self harm", "hurt myself", "die"
    ]
    return any(word in text.lower() for word in risk_words)

# -----------------------------
# PROMPT BUILDER
# -----------------------------
def build_prompt(user_input, emotion):
    return f"""
You are a calm, empathetic mental health support assistant.

User emotion detected: {emotion}

Rules:
- Be supportive, kind, and non-judgmental
- Do NOT provide medical diagnosis
- Encourage healthy coping strategies
- Suggest reaching out to trusted people when needed

User message:
{user_input}

Respond empathetically in a short and clear way.
"""

# -----------------------------
# GEMINI CONFIG
# -----------------------------
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def generate_ai_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

# -----------------------------
# SESSION STATE (CHAT MEMORY)
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


col1, col2 = st.columns([6, 1])

with col2:
    if st.button("🗑 Clear"):
        st.session_state.chat_history = []
        st.rerun()

# -----------------------------
# USER INPUT
# -----------------------------
user_input = st.text_area(
    "How are you feeling today?",
    height=150,
    placeholder="Type how you're feeling..."
)

# -----------------------------
# CHAT BUTTON
# -----------------------------
if st.button("Talk to AI"):

    if user_input.strip() == "":
        st.warning("Please enter a message so I can help.")
        st.stop()

    # SAFETY HANDLING
    if high_risk(user_input):
        st.error(
            "I'm really sorry you're feeling this way. "
            "You are not alone, and help is available. "
            "Please reach out to a trusted person or a mental health professional."
        )
        st.stop()

    # EMOTION DETECTION
    with st.spinner("Understanding your emotions..."):
        emotion = detect_emotion(user_input)

    # AI RESPONSE
    prompt = build_prompt(user_input, emotion)
    with st.spinner("Generating a supportive response..."):
        try:
            prompt = build_prompt(user_input, emotion)
            reply = generate_ai_response(prompt)
        except Exception:
            st.error("AI service is temporarily unavailable. Please try again.")
            st.stop()
    


    st.session_state.last_emotion = emotion
    if "last_emotion" in st.session_state:
        st.markdown(
            f"<div class='emotion-badge'>Emotion: {st.session_state.last_emotion}</div>",
            unsafe_allow_html=True
    )

    # SAVE CHAT HISTORY
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("AI", reply))

# -----------------------------
# DISPLAY CHAT HISTORY
# -----------------------------
if st.session_state.chat_history:
    st.subheader("💬 Conversation")

    for role, message in st.session_state.chat_history:
        if role == "You":
            st.markdown(
                f"<div class='chat-bubble-user'><b>You:</b> {message}</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div class='chat-bubble-ai'><b>AI:</b> {message}</div>",
                unsafe_allow_html=True
            )

