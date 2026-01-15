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

---

## Project Structure

```text
musicgen_web_demo/
├── main.py        # FastAPI backend (MusicGen + API)
├── index.html     # Frontend: text input + button + <audio> player
└── static/        # Generated audio files (.wav) are stored here
