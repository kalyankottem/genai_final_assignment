# AI Multi-Agent Marketing System

An academic MBA Business Analytics project demonstrating a Generative AI-powered multi-agent marketing system for cultural trend analysis, campaign generation, linguistic localization, and AI risk mitigation.

---

# PROJECT STRUCTURE

```bash
project-folder/

│── app.py
│── cultural_scraper.py
│── risk_mitigation.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

# SYSTEM REQUIREMENTS

Before running the project, install:

- Python 3.10 or above
- Ollama
- LLaMA 3 model

---

# INSTALLATION & EXECUTION GUIDE

## Step 1 — Download the Project

Download the repository ZIP file from GitHub.

Click:

```bash
Code → Download ZIP
```

Extract the ZIP file to your computer.

---

## Step 2 — Install Python

Download Python:

https://www.python.org/downloads/

IMPORTANT:
While installing Python, enable:

```bash
Add Python to PATH
```

Verify installation:

```bash
python --version
```

---

## Step 3 — Open Project Folder

Open terminal or command prompt inside the extracted project folder.

---

## Step 4 — Install Required Libraries

Run:

```bash
pip install -r requirements.txt
```

This installs:

- streamlit
- ollama

---

## Step 5 — Install Ollama

Download Ollama:

https://ollama.com/download

Install it normally.

Verify installation:

```bash
ollama --version
```

---

## Step 6 — Download LLaMA 3 Model

Run:

```bash
ollama pull llama3
```

This downloads the LLaMA 3 model locally.

---

## Step 7 — Start Ollama Server

Run:

```bash
ollama serve
```

Keep this terminal running.

---

## Step 8 — Run the Streamlit Application

Open a NEW terminal inside the project folder.

Run:

```bash
streamlit run app.py
```

---

## Step 9 — Open the Application

If Streamlit does not automatically open, visit:

```bash
http://localhost:8501
```

---

# APPLICATION WORKFLOW

1. Select city
2. Generate cultural insights
3. Generate or manually enter campaign
4. Localize campaign
5. Run risk mitigation analysis
6. Review outputs

---

# AI AGENTS USED

| Agent | Function |
|---|---|
| Cultural Scraper | Generates cultural insights |
| Synthetic Visualist | Generates visual campaign concepts |
| Campaign Generator & Linguistic Localizer | Creates localized campaigns |
| Risk Mitigation Agent | Detects campaign risks |

---

# OUTPUTS GENERATED

The system generates:
- Cultural insights
- Fashion styles
- Tone styles
- Base campaigns
- Localized campaigns
- Risk analysis reports

---
