# Stable Diffusion discord bot
Stable Diffusionというオープンソースの画像生成AIをDiscordで使用できるようにするためのBOTです。

# インストール
- PyTorch、Transformers、Diffusersをインストールします。<br>
初回にモデルのダウンロードが行われます。

- .envファイルを作成し、以下を記述してください。

```
API_TOKEN=<Hugging Faceのアクセストークン>
DISCORD_TOKEN=<Discordのアクセストークン>
```

# 使用法
ボットに対して
```
!create {作成したい画像の説明(英文)}
```
と送ると生成されるはずです。