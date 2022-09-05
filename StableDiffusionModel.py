from cgitb import reset
import os
import torch
from diffusers import StableDiffusionPipeline
from torch import autocast
from dotenv import load_dotenv
from transformers import pipeline
import gc
load_dotenv()
 
MODEL_ID = "CompVis/stable-diffusion-v1-4"
DEVICE = "cuda"
YOUR_TOKEN = os.environ.get("API_TOKEN")
translator = pipeline('translation', model='staka/fugumt-ja-en')

def generate(prompt):
  pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID, revision="fp16", torch_dtype=torch.float16, use_auth_token=YOUR_TOKEN)
  pipe.to(DEVICE)
  # translated = translator(prompt)[0]['translation_text']
  print(prompt)
  with autocast(DEVICE):
    image = pipe(prompt, guidance_scale=7.5)["sample"][0]
    image.save("test.png")
  del pipe,image
  gc.collect()
  return prompt

