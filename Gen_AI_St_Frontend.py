import streamlit as st
import google.generativeai as genai
import os
import json

def validate_api_key(api_key):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Test")
        return True
    except Exception as e:
        return False

def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
def save_chat_history(username, messages):
    # Create a 'chat_history' folder if it doesn't exist
    if not os.path.exists('chat_history'):
        os.makedirs('chat_history')
    
    # Save the chat history in the 'chat_history' folder
    file_path = os.path.join('chat_history', f"{username}_chat_history.json")
    with open(file_path, "w") as f:
        json.dump(messages, f)


def load_chat_history(username):
    file_path = os.path.join('chat_history', f"{username}_chat_history.json")
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def home_page():
    st.title("Chat with Gemini AI")
    
    # Username input
    username = st.text_input("Enter your username:", key="username_input")
    
    # API key input
    api_key = st.text_input("Enter your Google API key:", type="password", key="api_key_input")
    
    if st.button("Authenticate"):
        if username and api_key:
            with st.spinner("Validating API key..."):
                if validate_api_key(api_key):
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.session_state.api_key = api_key
                    st.success(f"Welcome, {username}! API key is valid.")
                    
# In the home_page function, update the following line:
                    st.session_state.messages = load_chat_history(username)
                else:
                    st.error("Invalid API key. Please try again.")
        else:
            st.warning("Please enter both username and API key.")

    if 'authenticated' in st.session_state and st.session_state.authenticated:
        # Chat interface
        if 'messages' not in st.session_state:
            st.session_state.messages = []

        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        if prompt := st.chat_input("What is your question?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = get_gemini_response(prompt)
                message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
            # Save chat history
            save_chat_history(st.session_state.username, st.session_state.messages)

        # File upload
        uploaded_file = st.file_uploader("Choose a file", type=['txt', 'pdf', 'docx', 'png', 'jpg', 'jpeg'])
                                # And in the file upload section:
        save_chat_history(st.session_state.username, st.session_state.messages)
        if uploaded_file is not None:
            file_contents = uploaded_file.read()
            st.write("File uploaded successfully:")
            st.write(uploaded_file.name)
            # Handle different file types
            if uploaded_file.type.startswith('image'):
                st.image(file_contents, caption=uploaded_file.name)
                file_message = f"I've uploaded an image named {uploaded_file.name}."
            elif uploaded_file.type == 'application/pdf':
                file_message = f"I've uploaded a PDF file named {uploaded_file.name}."
            else:
                try:
                    file_text = file_contents.decode('utf-8')
                except UnicodeDecodeError:
                    file_text = file_contents.decode('latin-1')
                st.text_area("File contents:", file_text, height=200)
                file_message = f"I've uploaded a file named {uploaded_file.name}. Its contents are: {file_text[:1000]}..."

            st.session_state.messages.append({"role": "user", "content": file_message})
            save_chat_history(st.session_state.username, st.session_state.messages)

def main():
    home_page()
    st.markdown("---")
    st.markdown("Powered by Google's Gemini AI | [Documentation](https://ai.google.dev/docs)")

if __name__ == "__main__":
    main()
