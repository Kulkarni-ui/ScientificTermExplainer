# 🔬 Scientific Term Explainer

An AI-powered web app that explains scientific terms in plain language — with real-world examples, multilingual support, and related concept suggestions.

🚀 *Live Demo:* https://scientific-term-explainer.vercel.app

---

## 📸 Screenshots
<img width="1600" height="762" alt="image" src="https://github.com/user-attachments/assets/2bb7cab7-ccf2-43cb-95e8-7840c937304e" />
<img width="875" height="823" alt="image" src="https://github.com/user-attachments/assets/cc659518-2ed3-44bf-b571-ee5f87e0b939" />

---

## ✨ Features

* 🤖 **AI-Powered Explanations** — Generates clear and accurate explanations using Groq LLM
* 🌍 **Multilingual Support (17 Languages)** — Includes English, Hindi, Kannada, Tamil, French, Spanish, Japanese, Arabic, and more
* 💡 **Real-World Examples** — Helps users understand concepts practically
* 🔗 **Related Concepts** — Suggests connected topics for deeper learning
* ⚡ **High Performance** — Uses Groq’s fast inference API for quick responses

---

## 🧠 How It Works

1. User enters a scientific term in the input field
2. Frontend sends request to Flask backend
3. Flask API calls Groq LLM with the query
4. LLM generates:

   * Explanation
   * Real-world examples
   * Related concepts
5. Response is displayed dynamically on the UI

---

## 🧪 Example

**Input:** Photosynthesis

**Output:**
Photosynthesis is the process by which plants convert sunlight into chemical energy. It occurs in the chloroplasts using chlorophyll and produces oxygen as a byproduct.

---

## 🚀 Tech Stack

`Python` · `Flask` · `Groq API` · `HTML` · `CSS` · `JavaScript` · `Vercel`

---

## 📁 Project Structure

```
├── api/            # Flask API / serverless functions
├── static/         # CSS & JS assets
├── templates/      # HTML templates
├── requirements.txt
└── vercel.json     # Deployment configuration
```

---

## ⚙️ Getting Started

### 🔧 Prerequisites

* Python 3.8+
* Groq API Key → https://console.groq.com

---

### 🪜 Installation

```bash
# Clone repository
git clone https://github.com/ScientificTermExplainer/ScientificTermExplainer.git

# Navigate into project
cd ScientificTermExplainer

# Install dependencies
pip install -r requirements.txt

# Add API key
echo "GROQ_API_KEY=your_key_here" > .env

# Run application
flask run
```

---

## 🚀 Deployment

This project is pre-configured for **Vercel deployment**.

1. Run:

```bash
vercel
```

2. Add environment variable in Vercel:

* `GROQ_API_KEY`

---

## 🚀 Uniqueness

* 🌍 Supports **17 languages** for scientific explanations
* 🧠 Combines explanation + examples + related concepts in one response
* ⚡ Uses **Groq API** for ultra-fast inference
* 🎯 Focuses on **simplifying complex scientific terms for beginners**

---

## 🔮 Future Enhancements

* 🎤 Voice input support
* 📷 Image-based term recognition
* 📚 Personalized learning recommendations
* 📱 Mobile app version

---

##  Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

## 📜 License

This project is for educational purposes.

---

<p align="center">Built with ❤️ using Flask · Groq · Vercel</p>
