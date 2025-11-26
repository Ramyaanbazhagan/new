import streamlit as st
import google.generativeai as genai

# -------------------------
# Sidebar – API key
# -------------------------
st.sidebar.title("🔑 Gemini API Settings")
api_key = st.sidebar.text_input("Enter your Gemini API Key:", type="password")

# Stop if key not entered
if not api_key:
    st.warning("⚠ Please enter your Gemini API key in the sidebar!")
    st.stop()

genai.configure(api_key=api_key)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# -------------------------
# UI
# -------------------------
st.title("🤖 Ramya's Gemini Chatbot")

if "chat_history" in st.session_state:
    pass
else:
    st.session_state["chat_history"] = []

# Display history
for role, content in st.session_state["chat_history"]:
    with st.chat_message(role):
        st.write(content)

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state["chat_history"].append(("user", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # Gemini response
    response = model.generate_content(user_input)
    bot_reply = response.text

    # Add bot message
    st.session_state["chat_history"].append(("assistant", bot_reply))
    with st.chat_message("assistant"):
        st.write(bot_reply)
