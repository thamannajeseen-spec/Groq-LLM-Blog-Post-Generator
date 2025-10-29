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
* **Cloudflared:** To create a stable public URL for the Colab instance.

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

4.  **Update Your Notebook Cells**
    Your notebook should have several cells. Make sure the **last two cells** are set up as follows to run the app and the tunnel.

    * **Cell 1 (Run Cloudflared Tunnel):**
              Add a **new final cell** with these commands. This will download `cloudflared`, connect it to your Streamlit app (running on `localhost:8501`), and print your public URL.
        ```python
        !rm -f cloudflared-linux-amd64*
        !wget [https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64)
        !chmod +x cloudflared-linux-amd64
        !nohup ./cloudflared-linux-amd64 tunnel --url http://localhost:8501 &
        
        # Wait a few seconds for the tunnel to initialize
        import time
        time.sleep(5)
        
        # Get the public URL
        !grep -o 'https://.*\.trycloudflare.com' nohup.out
        
        ```

    * **Cell 2 (Run Streamlit in Background):**
        This cell runs your Streamlit app in the background using `nohup`.
        ```python
        !streamlit run blogg.py &
        ```

5.  **Run and View Your App**
    * In the Colab menu, click **"Runtime"** > **"Run all"**.
    * The **output of !grep -o 'https://.*\.trycloudflare.com' nohup.out will generate your public URL (e.g., `https://your-unique-name.trycloudflare.com`).
    * Click this URL to open your running Streamlit application in a new browser tab!

---

---
