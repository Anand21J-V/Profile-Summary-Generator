import streamlit as st
import requests
import os
import json
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"

def extract_json(text):
    try:
        # Try direct load first
        return json.loads(text)
    except:
        try:
            # Extract JSON substring and parse
            json_match = re.search(r'\{.*\}', text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            return None
    return None

# Function to get summary from Groq API
def get_summary(name, designation, experience):
    prompt = f"""
Generate two professional summaries for a job applicant ONLY as JSON with these exact keys:
- long_summary: exactly 100 words
- short_summary: exactly 50 words

Name: {name}
Designation: {designation}
Experience: {experience} years

IMPORTANT: Output only valid JSON and nothing else. No explanations or extra text.

Example:
{{
  "long_summary": "...",
  "short_summary": "..."
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
        result = extract_json(content)
        if result:
            return result
        else:
            return {"error": "Failed to parse JSON", "raw_response": content}
    else:
        return {"error": f"API call failed: {response.text}"}

# -------------------- Streamlit UI --------------------

st.set_page_config(page_title="Professional Summary Generator", layout="centered")

# Styles
st.markdown("""
<style>
.main {background-color: #f8f9fa;}
.stTextInput>div>div>input, .stNumberInput>div>div>input {
    border: 1px solid #ced4da;
    padding: 0.5rem;
    font-size: 16px;
}
.summary-box {
    background-color: #ffffff;
    border-left: 6px solid #4CAF50;
    padding: 1rem;
    margin-top: 1rem;
    border-radius: 8px;
    font-size: 15px;
    line-height: 1.6;
    white-space: pre-wrap;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🧠 Professional Summary Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Generate clean and professional summaries with just a few inputs.</p>", unsafe_allow_html=True)

st.markdown("---")
st.subheader("📝 Applicant Details")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Full Name", placeholder="e.g., John Doe")
with col2:
    designation = st.text_input("Designation", placeholder="e.g., Software Engineer")

experience = st.number_input("Years of Experience", min_value=0.0, step=0.5, help="Total relevant experience in years")

if st.button("🚀 Generate Summary"):
    if name and designation and experience is not None:
        with st.spinner("Generating summaries..."):
            result = get_summary(name, designation, experience)

        if "error" in result:
            st.error(result.get("error"))
            if "raw_response" in result:
                st.text_area("Raw API Response", result["raw_response"], height=200)
        else:
            st.markdown("### 📦 JSON Output")
            st.json(result)

            st.markdown("### 🧾 Long Summary (100 words)")
            st.markdown(f"<div class='summary-box'>{result['long_summary']}</div>", unsafe_allow_html=True)

            st.markdown("### ✏️ Short Summary (50 words)")
            st.markdown(f"<div class='summary-box'>{result['short_summary']}</div>", unsafe_allow_html=True)

            st.download_button(
                label="📥 Download Summary (JSON)",
                data=json.dumps(result, indent=2),
                file_name=f"{name.lower().replace(' ', '_')}_summary.json",
                mime="application/json"
            )
    else:
        st.warning("⚠️ Please fill all fields above to generate a summary.")
