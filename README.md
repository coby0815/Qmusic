# Qmusic
# Text-to-Music Web Demo (Meta MusicGen + FastAPI)

This repository is a **small demo** showing how to:

- Use **Meta's open-source MusicGen** model (via Hugging Face `transformers`) to generate music from text, and  
- Expose it as a simple **web application** with a FastAPI backend and a static HTML/JS frontend.

> This project focuses on **system design and integration**: wrapping an existing LLM-style model (MusicGen) into a web service and embedding it into a web page.

---

## Features

- 🧠 **LLM-style music generation** using Meta's `facebook/musicgen-small`
- 🌐 **FastAPI** backend with a `/generate` endpoint
- 🎧 **Frontend**: simple HTML + CSS + JavaScript
- 🎵 Generated music is saved as `.wav` in a `static/` folder and played in a `<audio>` element
- 🔁 Hot reload in development using `uvicorn --reload`
- 


## How to Run the Web Demo

This project has **two parts**:

1. A Python **FastAPI backend** (`main.py`) that runs the MusicGen model  
2. A static **HTML frontend** (`index.html`) that calls the backend and plays the generated audio

You need to start the backend first, then open the HTML page in your browser.

---

### 1. Start the backend (FastAPI + MusicGen)

From the project root:

```bash
# 1) (optional) create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# 2) install dependencies (only needed the first time)
pip install --upgrade pip
pip install torch torchaudio
pip install transformers scipy fastapi "uvicorn[standard]"
mkdir static

# 3) run the FastAPI server
uvicorn main:app --reload



## Project Structure

```text
musicgen_web_demo/
├── main.py        # FastAPI backend (MusicGen + API)
├── index.html     # Frontend: text input + button + <audio> player
└── static/        # Generated audio files (.wav) are stored here
---
