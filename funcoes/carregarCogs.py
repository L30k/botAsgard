import os

async def carregar_cogs(bot):
    for arquivos in os.listdir('cogs'):
        if arquivos.endswith('.py'):
            await bot.load_extension(f"cogs.{arquivos[:-3]}")
            print(f"cog {arquivos} caregada!")