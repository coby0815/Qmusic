from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel

import os
import uuid

import torch
import numpy as np
import scipy.io.wavfile as wavfile
from transformers import AutoProcessor, MusicgenForConditionalGeneration

app = FastAPI()

# 允许前端跨域访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 静态文件目录（用来放生成的 .wav）
STATIC_DIR = "static"
os.makedirs(STATIC_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class Prompt(BaseModel):
    prompt: str


# ---------- 加载 MusicGen 模型 ----------
print("Loading MusicGen model (this may take a while)...")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
model.to(device)
model.eval()

print("Model loaded on", device)


def generate_music_file(prompt: str) -> str:
    """
    使用 Hugging Face transformers 里的 MusicGen 生成音乐，
    保存到 static 目录下，返回文件名。
    """
    base_name = f"music_{uuid.uuid4().hex[:8]}"
    out_path = os.path.join(STATIC_DIR, base_name + ".wav")

    # 文本转模型输入
    inputs = processor(
        text=[prompt],
        padding=True,
        return_tensors="pt",
    ).to(device)

    # 生成音频；max_new_tokens 越大，音乐越长也越慢
    with torch.no_grad():
        audio_values = model.generate(
            **inputs,
            do_sample=True,
            max_new_tokens=512,
        )

    # audio_values: [batch, channels, samples]
    audio = audio_values[0, 0].cpu().numpy().astype(np.float32)
    sampling_rate = model.config.audio_encoder.sampling_rate

    # 写成 wav 文件
    wavfile.write(out_path, rate=sampling_rate, data=audio)

    return base_name + ".wav"


@app.post("/generate")
async def generate_music(p: Prompt):
    print("收到的 prompt:", p.prompt)

    try:
        file_name = generate_music_file(p.prompt)
        audio_url = f"/static/{file_name}"
        return JSONResponse({"audio_url": audio_url})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
