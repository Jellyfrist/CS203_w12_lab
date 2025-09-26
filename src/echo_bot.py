import streamlit as st
import random

st.title("Echo Bot")

# Add this after the title
if st.button("Clear Chat History"):
    st.session_state.messages = []
    st.rerun()  # Refresh the app to show cleared chat

# Add this in the sidebar
st.sidebar.write(f"Total messages: {len(st.session_state.messages)}")

# Replace the simple echo response with:
responses = [
    f"Echo: {prompt}",
    f"You said: {prompt}",
    f"I heard: {prompt}",
    f"Repeating: {prompt}"
]
response = random.choice(responses)

# Initialize
if "key" not in st.session_state:
    st.session_state.key = default_value

# Use
st.session_state.key.append(new_item)

# Display
for item in st.session_state.key:
    st.write(item)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
