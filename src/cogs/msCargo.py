import discord
from discord import app_commands
from discord.ext import commands

class MsCargo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(name="enviar", description="Envia uma mensagem para todos os membros de um cargo específico.")
    @app_commands.describe(cargo="O cargo para o qual a mensagem será enviada", mensagem="A mensagem a ser enviada")
    async def enviar(self, interaction: discord.Interaction, cargo: discord.Role, mensagem: str):
        # Verifica se o usuário tem permissões de administrador
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("Você não tem permissão para usar este comando.", ephemeral=True)
            return

        # Obtém o servidor (guild) e os membros com o cargo especificado
        guild = interaction.guild
        membros = [membro for membro in guild.members if cargo in membro.roles]

        # Envia a mensagem para cada membro
        for membro in membros:
            try:
                await membro.send(mensagem)
            except Exception as e:
                print(f"Falha ao enviar mensagem para {membro.name}: {e}", ephemeral=True)

        await interaction.response.send_message(
            f"Mensagem enviada para {len(membros)} membros com o cargo {cargo.name}.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(MsCargo(bot))