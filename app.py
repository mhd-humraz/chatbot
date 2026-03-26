import streamlit as st

st.set_page_config(page_title="Campus Bot", page_icon="🤖")

st.title(" Assistant Bot")
st.write("👋 Hi! Ask me anything!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input
user_input = st.chat_input("Type your message...")

def chatbot_reply(user_input):
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return "Hey there! 👋 How can I help you?"
    
    elif "your name" in user_input:
        return "I'm your Assistant Bot 🤖"
    
    elif "joke" in user_input:
        return "😂 Why did the programmer quit? Because he didn't get arrays!"
    
    elif "study" in user_input:
        return "📚 Tip: Study 25 mins + 5 min break (Pomodoro method!)"
    
    elif "exam" in user_input:
        return "📝 Stay calm, revise key points, and sleep well!"
    
    elif "bye" in user_input:
        return "Goodbye! 👋 Have a great day!"
    
    else:
        return "Hmm 🤔 I'm still learning. Try asking something else!"

# When user sends message
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    reply = chatbot_reply(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
