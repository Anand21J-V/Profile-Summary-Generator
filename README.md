# 🧠 Professional Summary Generator

A sleek and simple web app built with Streamlit that uses Groq’s LLaMA 3.3 70B Versatile model to generate professional summaries (long and short) for job applicants based on their name, designation, and experience.

---

# Deployed On Streamlit
https://profile-summary-generator.streamlit.app/

---

## 🚀 Features

- Generate **two AI-powered summaries**:  
  - 📜 **Long Summary** (100 words)  
  - 📝 **Short Summary** (50 words)
- Built with **Streamlit** for interactive UI
- Connects to **Groq API** (LLaMA 3.3 model)
- Instant **JSON output** + download support
- Elegant design with easy-to-use form inputs

---

## 🧰 Tech Stack

- Python 🐍
- Streamlit 🎈
- Groq API 🔗
- LLaMA 3.3-70B Versatile 🧠
- dotenv for environment variable management

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/profile-summary-generator.git
cd profile-summary-generator
````

2. **Create and activate a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📤 Example Output

```json
{
  "long_summary": "John Doe is a seasoned Software Engineer with over 5 years of experience in full-stack development...",
  "short_summary": "John Doe is a Software Engineer with 5 years' experience in building scalable and robust web applications..."
}
```

---

## 📁 File Structure

```
📂 profile-summary-generator
├── app.py               # Main Streamlit application
├── .env                 # API key (not committed)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ✅ Requirements

* Python 3.8+
* Groq account & API key

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Anand Vishwakarma**
📧 [anandvishwakarma21j@gmail.com](mailto:anandvishwakarma21j@gmail.com)
🏫 OP Jindal University | CSE
