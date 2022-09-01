from discord import Intents
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import gc
import re
from StableDiffusionModel import generate


load_dotenv()

intents = Intents.default()
intents.message_content = True

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