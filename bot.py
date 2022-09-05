from discord import Intents
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import gc
import re
from cgitb import reset
import torch
from diffusers import StableDiffusionPipeline
from torch import autocast
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()

intents = Intents.default()
intents.message_content = True

MODEL_ID = "CompVis/stable-diffusion-v1-4"
DEVICE = "cuda"
YOUR_TOKEN = os.environ.get("API_TOKEN")
translator = pipeline('translation', model='staka/fugumt-ja-en')

pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID, revision="fp16", torch_dtype=torch.float16, use_auth_token=YOUR_TOKEN)
pipe.to(DEVICE)
# translated = translator(prompt)[0]['translation_text']

def generate(prompt):
  with autocast(DEVICE):
    image = pipe(prompt, guidance_scale=7.5)["sample"][0]
    image.save("test.png")
  del image
  gc.collect()
  return prompt

bot = commands.Bot(
    command_prefix="!",
    description="GAI generates the image.",
    intents=intents,
)

@bot.command()
async def create(ctx, *, prompt):
    msg = await ctx.send(f"「{prompt}」\n 生成中・・・")
    generate(prompt=prompt)
    # if(re.search(r'[ぁ-んァ-ン]', prompt)):
    #     await msg.edit(content=f"「{prompt}」\n生成が完了しました \n文章は以下のように自動で翻訳されました\n{text}")
    # else:
    await msg.edit(content=f"「{prompt}」\n生成が完了しました")
    await ctx.send(file=discord.File("./test.png"))
    gc.collect()

bot.run(os.environ["DISCORD_TOKEN"])