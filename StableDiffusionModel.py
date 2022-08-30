from cgitb import reset
import sys
import os
import torch
from diffusers import StableDiffusionPipeline
from torch import autocast
from dotenv import load_dotenv
load_dotenv()
 
args = sys.argv
MODEL_ID = "CompVis/stable-diffusion-v1-4"
DEVICE = "cuda"
YOUR_TOKEN = os.environ.get("API_TOKEN")

def generate(prompt):
  pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID, revision="fp16", torch_dtype=torch.float16, use_auth_token=YOUR_TOKEN)
  pipe.to(DEVICE)

  with autocast(DEVICE):
    image = pipe(prompt, guidance_scale=7.5)["sample"][0]
    result = image.save("test.png")
    return result

