import streamlit as st
import google.generativeai as genai
import os
import json

# Configure API key
GOOGLE_API_KEY = 'Your API Key'
genai.configure(api_key=GOOGLE_API_KEY)

def get_gemini_response(user_input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_input)
    return response.text


def header():
    st.markdown("""
    <style>
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px;
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .nav-links {
        display: flex;
        gap: 30px;
    }
    .nav-link {
        color: white;
        text-decoration: none;
        font-weight: bold;
        transition: color 0.3s ease;
    }
    .nav-link:hover {
        color: #f0f0f0;
    }
    h1 {
        margin: 0;
        font-size: 2.5em;
    }
    </style>
    
    <div class="header">
        <h1>Q&A Platform</h1>
        <div class="nav-links">
            <a href="/" target="_self" class="nav-link">Home</a>
            <a href="/?page=about" target="_self" class="nav-link">About</a>
            <a href="/?page=contact" target="_self" class="nav-link">Contact</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
def footer():
    st.markdown("---")
    st.markdown("Powered by Google's Gemini AI | [Documentation](https://ai.google.dev/docs) | [Source Code](https://github.com/yourusername/your-repo)")

def save_chat_history(username, messages):
    with open(f"{username}_chat_history.json", "w") as f:
        json.dump(messages, f)

def load_chat_history(username):
    try:
        with open(f"{username}_chat_history.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def home_page():
    st.title("Chat with Gemini AI")
    
    # Username input
    if 'username' not in st.session_state:
        st.session_state.username = st.text_input("Enter your username:")
        if st.session_state.username:
            st.success(f"Welcome, {st.session_state.username}!")
            st.session_state.messages = load_chat_history(st.session_state.username)
        else:
            st.stop()
    
    # Initialize messages if not present
    if 'messages' not in st.session_state:
        st.session_state.messages = load_chat_history(st.session_state.username)

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
    uploaded_file = st.file_uploader("Choose a file", type=['txt', 'pdf', 'docx'])
    if uploaded_file is not None:
        file_contents = uploaded_file.read()
        st.write("File contents:")
        st.write(file_contents)
        
        # Add file content to chat history
        file_message = f"I've uploaded a file named {uploaded_file.name}. Its contents are: {file_contents.decode('utf-8')}"
        st.session_state.messages.append({"role": "user", "content": file_message})
        save_chat_history(st.session_state.username, st.session_state.messages)

def about_page():
    st.title("About")
    st.write("This is a Q&A platform powered by Google's Gemini AI.")

def contact_page():
    st.title("Contact")
    st.write("For any inquiries, please contact: example@email.com")

def main():
    header()

    # Get the current page from query parameters
    query_params = st.query_params
    page = query_params.get("page", ["home"])[0]

    if page == "home":
        home_page()
    elif page == "about":
        about_page()
    elif page == "contact":
        contact_page()

    footer()

if __name__ == "__main__":
    main()
