import streamlit as st
import requests
import os
import json
from dotenv import load_dotenv


# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"

# Function to get summary from Groq API
def get_summary(name, designation, experience):
    prompt = f"""
    Generate two professional summaries for a job applicant in JSON format with the following keys:
    - long_summary (exactly 100 words)
    - short_summary (exactly 50 words)

    Name: {name}
    Designation: {designation}
    Experience: {experience} years

    Output only valid JSON, no extra text.
    Example format:
    {{
        "long_summary": "....",
        "short_summary": "...."
    }}
    """

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=body, headers=headers)

    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        try:
            return json.loads(content)
        except Exception as e:
            return {"error": "Failed to parse JSON", "raw_response": content}
    else:
        return {"error": f"API call failed: {response.text}"}

# Streamlit UI
st.set_page_config(page_title="Professional Summary Generator", layout="centered")
st.title("🧠 Professional Summary Generator")

name = st.text_input("Enter Name")
designation = st.text_input("Enter Designation")
experience = st.number_input("Enter Experience (in years)", min_value=0.0, step=0.5)

if st.button("Generate Summary"):
    if name and designation and experience is not None:
        with st.spinner("Generating summaries..."):
            result = get_summary(name, designation, experience)

        if "error" in result:
            st.error(result.get("error"))
            st.text(result.get("raw_response", ""))
        else:
            st.markdown("### 📝 JSON Output")
            st.json(result)

    else:
        st.error("Please fill all inputs.")
