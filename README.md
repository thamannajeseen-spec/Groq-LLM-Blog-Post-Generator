# 📝 Blog Generator App using Groq LLM

This is an AI-powered blog post generator built with **Streamlit** and the **Groq API**. It allows users to instantly generate short, 100-word blog posts on any topic by leveraging the high-speed inference of Groq's LLM models (like Llama 3 or Mixtral).

## ✨ Features

* Generate unique blog posts instantly on any topic.
* Powered by Groq's fast-inference LLM models.
* Simple and clean web interface built with Streamlit.
* Secure API key management using a `.env` file.

## 📋 Requirements

* Python 3.10+
* `streamlit` - For the web interface
* `openai` - As the client for the Groq API
* `python-dotenv` - For loading the API key

Groq-LLM-Blog-Post-Generator/
│
├── .env             # Stores the API key (not uploaded)
├── blogg.py         # The main Streamlit app file
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
