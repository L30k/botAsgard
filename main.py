import discord
from discord.ext import commands
import os

# import funçôes
from funcoes.carregarCogs import *
from funcoes.carregarConfiguracoes import *

arquivo = carregarConfiguracoes("config.txt")

# Definir intenções
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.presences = True
intents.members = True

# Configurar o bot
prefixo = "!"
bot = commands.Bot(command_prefix=prefixo, intents=intents)

@bot.command()
async def sincronizar(ctx:commands.Context):
    if ctx.author.id == arquivo.get("MODERATOR_ID"):
        sincs = await bot.tree.sync()
        await ctx.reply(f"{len(sincs)} Comandos sincronizados", ephemeral=True)

# Evento que é chamado quando o bot está pronto
@bot.event
async def on_ready():
    await carregar_cogs(bot)
    print('Bot Iniciado!')


bot.run(arquivo.get("BOT_TOKEN"))
