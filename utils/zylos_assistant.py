import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

def get_zylos():

    api_key = os.getenv("GOOGLE_API_KEY")

    st.write("API Key Found:", api_key is not None)

    if api_key:
        st.write("First 8 chars:", api_key[:8])

    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3,
        google_api_key=api_key
    )