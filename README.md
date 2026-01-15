## 1. Start the backend (FastAPI + MusicGen)

From the project root:

```bash
# 1) (optional) create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# 2) install dependencies (only needed the first time)
pip install --upgrade pip
pip install torch torchaudio
pip install transformers scipy fastapi "uvicorn[standard]"

# 3) (optional) create the static folder for generated audio
mkdir static

# 4) run the FastAPI server
uvicorn main:app --reload
You should see logs like:

text
Copy code
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
Project Structure
text
Copy code
musicgen_web_demo/
├── main.py      # FastAPI backend (MusicGen + API)
├── index.html   # Frontend: text input + button + <audio> player
└── static/      # Generated audio files (.wav) are stored here
2. Open the frontend
There are two simple options:

Option A: open index.html directly
Open the project folder in Finder / File Explorer.

Double-click index.html.

Your browser will open the demo page (URL will look like file:///.../index.html).

Make sure the backend is running on http://127.0.0.1:8000.

Option B (optional): serve via a simple HTTP server
bash
Copy code
python -m http.server 8080
Then open:

http://127.0.0.1:8080/index.html

in your browser.

On the page:

Type a description like lofi chill beat with soft piano and rain.

Click Generate Music.

Wait for the backend to generate audio.

Press play on the <audio> player to listen.
