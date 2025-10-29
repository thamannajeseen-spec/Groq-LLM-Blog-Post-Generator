# Groq LLM Blog Post Generator

This project is a simple web application built with Streamlit that uses the Groq API to generate short blog posts (approximately 100 words) based on a user-provided topic.

The application is designed to be run easily from a Google Colab notebook but can also be run on a local machine.


## 🚀 Features

* Simple and clean web interface powered by Streamlit.
* Connects to the high-speed Groq API for near-instant text generation.
* Generates a ~100-word blog post on any topic you provide.

## 🛠️ Technology Stack

* **Python**
* **Streamlit:** For the web app UI.
* **Groq API:** For the Large Language Model.
* **OpenAI Python Client:** Used as the client to interact with the Groq API.
* **Google Colab:** As the primary development and runtime environment.

---

## 🏃‍♂️ How to Run (in Google Colab)

This project is set up to run directly in Google Colab with minimal setup.

1.  **Open the Notebook**
    Open the `blogg.ipynb` file in Google Colab.

2.  **Get a Groq API Key**
    * Go to [GroqCloud](https://console.groq.com/keys).
    * Sign up for a free account.
    * Create a new API key and copy it.

3.  **Add Colab Secret**
    * In your Colab notebook, click the **key icon (🔑) in the left sidebar** to open the "Secrets" tab.
    * Create a new secret with the name: `GROK_KEY`
    * Paste your copied Groq API key into the "Value" field.
    * Make sure to **toggle "Notebook access" ON**.

4.  **Run the Notebook**
    * In the Colab menu, click **"Runtime"** > **"Run all"**.
    * The notebook will install `streamlit`, write the Python app script, and start the Streamlit server.

5.  **View Your App**
    * The output of the final cell will show several URLs. Click the **"External URL"** (it will look similar to `http://34.106.230.100:8501`).
    * This will open your running Streamlit application in a new browser tab!

---
