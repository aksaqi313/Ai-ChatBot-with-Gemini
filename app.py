import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="wide",
)

# Custom CSS for a premium look
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1e1e2f 0%, #121212 100%);
        color: #ffffff;
    }
    .stChatFloatingInputContainer {
        bottom: 20px;
        background-color: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 10px;
    }
    .stChatMessage {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        margin-bottom: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .stButton>button {
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 10px 25px;
        font-weight: bold;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: rgba(0, 0, 0, 0.5);
    }
    h1 {
        background: -webkit-linear-gradient(#ff4b2b, #ff416c);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        margin-bottom: 0px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar for settings
with st.sidebar:
    st.title("⚙️ Settings")
    st.markdown("---")
    
    api_key_env = os.getenv("GOOGLE_API_KEY")
    api_key = st.text_input("Google API Key", value=api_key_env if api_key_env else "", type="password")
    
    model_name = st.selectbox(
        "Select Model",
        ["gemini-1.5-pro", "gemini-1.5-flash"],
        index=0
    )
    
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
    
    st.markdown("---")
    if st.button("Clear Chat History"):
        st.session_state.chat = None
        st.rerun()

# Configure Gemini
if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(
            model_name=model_name,
            generation_config={"temperature": temperature}
        )
        
        # Initialize Gemini Chat history object
        if "chat" not in st.session_state or st.session_state.chat is None:
            st.session_state.chat = model.start_chat(history=[])
            
    except Exception as e:
        st.error(f"Failed to configure Gemini: {e}")
        st.stop()
else:
    st.warning("Please provide a Google API Key in the sidebar to start chatting.")
    st.info("You can get an API key from [Google AI Studio](https://aistudio.google.com/apikey).")
    st.stop()

# Role mapping
def role_to_streamlit(role):
    return "assistant" if role == "model" else role

# App Layout
st.title("🚀 Gemini AI Chatbot")
st.caption("A premium conversational experience powered by Google Gemini")
st.markdown("---")

# Display chat history
if st.session_state.chat:
    for message in st.session_state.chat.history:
        with st.chat_message(role_to_streamlit(message.role)):
            st.markdown(message.parts[0].text)

# Chat Input
if prompt := st.chat_input("Ask me anything..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    try:
        with st.spinner("Thinking..."):
            response = st.session_state.chat.send_message(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
            
    except Exception as e:
        st.error(f"An error occurred: {e}")