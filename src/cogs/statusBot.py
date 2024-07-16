import discord
from discord.ext import commands, tasks

class StatusBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.status_messages = [
            "Protegendo os segredos de Asgard.",
            "Explorando os reinos de Asgard.",
            "Servindo fielmente Asgard.",
            "Guardando os portões de Asgard.",
            "Em busca de conhecimento em Asgard.",
            "Defendendo a honra de Asgard.",
            "Descobrindo os mistérios de Asgard.",
            "Construindo novos caminhos para Asgard.",
            "Navegando pelos ventos de Asgard.",
            "Celebrando a grandeza de Asgard."
        ]
        self.current_message_index = 0
        self.update_status.start()

    @tasks.loop(seconds=30)
    async def update_status(self):
        self.current_message_index = (self.current_message_index + 1) % len(self.status_messages)
        activity = discord.CustomActivity(name=self.status_messages[self.current_message_index])
        await self.bot.change_presence(activity=activity)

    @update_status.before_loop
    async def before_update_status(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(StatusBot(bot))