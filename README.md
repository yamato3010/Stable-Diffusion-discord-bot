# Stable Diffusion discord bot
Stable Diffusionというオープンソースの画像生成AIをDiscordで使用できるようにするためのBOTです。  
実際に友人のDiscordサーバ上で運用しました。  

This is a BOT to enable the open source image generation AI called Stable Diffusion to be used on Discord.  
I actually ran it on a friend's Discord server.  

## Demo
[discordのスクリーンショット](https://user-images.githubusercontent.com/75778273/220875327-68f7b4a1-af0f-49c9-88d4-7d1c7652068f.png)

## Install
- PyTorch、Transformers、Diffusersをインストールします。  
初回にモデルのダウンロードが行われます。  
Install PyTorch, Transformers and Diffusers.  
The model will be downloaded for the first time.

- .envファイルを作成し、以下を記述してください。  
Create an .env file and write the following

```
API_TOKEN=<Hugging Face access token>
DISCORD_TOKEN=<Discord access token>
```

## Usage
ボットに対して
```
!create {作成したい画像の説明(英文)}
```
と送ると生成されるはずです。

for bots
```
!create {description of the image you want to create }
```
should generate the image.
