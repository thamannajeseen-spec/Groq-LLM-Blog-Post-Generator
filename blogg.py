import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GROQ_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

model_name = "llama-3.3-70b-versatile" 

def get_response(topic):
    prompt = f"Write a blog post about {topic} with a length of approximately 100 words."

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user",
                 "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error from Groq API: {e}") 
        return None


st.set_page_config(page_title="Blog Post Generator")
st.header("Groq LLM Blog Post Generator")
topic_input = st.text_input("Blog Post Topic:", key="topic_input")
submit = st.button("Generate Blog Post")

if submit:
    if topic_input:
        response = get_response(topic_input)
        if response:
            st.subheader("Generated Blog Post:")
            st.write(response)
    else:
        st.warning("Please enter a topic.")
