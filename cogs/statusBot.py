import discord
from discord.ext import commands, tasks

class StatusBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.update_status.start()  # Inicia a tarefa de atualizar o status

    @tasks.loop(hours=1)
    async def update_status(self):
        activity = discord.CustomActivity(name=f"🗡Asgard")
        await self.bot.change_presence(activity=activity)

    @update_status.before_loop
    async def before_update_status(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(StatusBot(bot))
