import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=API_KEY)


st.markdown(
    "<h1 style='text-align:center; color:orange;'>Taj's AI</h1>",
    unsafe_allow_html=True
)


prompt = st.chat_input("Ask Taj's AI anything...")

if prompt:
    st.write("You:", prompt)

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    st.write("Taj's AI:", response.text)