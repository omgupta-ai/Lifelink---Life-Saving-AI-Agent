import streamlit as st 
import requests 

BACKEND_URL = "http://localhost:8000/ask"

st.set_page_config(page_title = "Mental Health Therapist Agent")

st.markdown("""
    <style>
    /* 1. Background Gradient */
    .stApp {
        background: linear-gradient(to bottom right, #f0f4f8, #e0e7ff);
    }

    /* 2. Style the Chat Messages */
    [data-testid="stChatMessage"] {
        background-color: white;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 10px;
        box-shadow: 0 4px 8px -1px rgba(0, 0, 0, 0.1);
    }

    /* 3. Make the Title Pop */
    h1 {
        color: #1e3a8a;
        font-family: 'Helvetica Neue', sans-serif;
        text-align: center;
        padding-bottom: 2rem;
    }

    /* 4. Improve Sidebar/Input area */
    .stChatInputContainer {
        padding-bottom: 20px;
    }

    /* Target the User messages and align to right */
    [data-testid="stChatMessage"]:has(div[aria-label="Chat message from user"]) {
        flex-direction: row-reverse;
        text-align: right;
        background-color: #ffffff; /* Light powder blue like sky */
        margin-left: auto;
        margin-right: 0;
        width: fit-content;
        max-width: 80%;
    }

    /* Target the Assistant messages and keep them on the left */
    [data-testid="stChatMessage"]:has(div[aria-label="Chat message from assistant"]) {
        background-color: #ffffff;
        margin-right: auto;
        margin-left: 0;
        width: fit-content;
        max-width: 80%;
    }
    </style>
    """, unsafe_allow_html=True)
# ----------------------------------------------------


st.title("🪼Lifelink - a life saving AI Agent")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Heyy Champ! How are you feeling today?")
if user_input:
    st.session_state.chat_history.append({"role":"user", "content":user_input})
    try:
        response = requests.post(BACKEND_URL, json={"message": user_input})
        response.raise_for_status()  # This will catch 404/500 errors
        
        data = response.json()
        res_text = data.get("response") or "I'm sorry, I couldn't process that."
        tool_text = data.get("tool_called") or "None"
        
        st.session_state.chat_history.append({
            "role": "assistant", 
            "content": f"{res_text}"
        })
    except Exception as e:
        st.error(f"Failed to reach backend: {e}")

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

