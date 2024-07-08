import discord
from discord import app_commands
from discord.ext import commands
from classes_extras.menuDeConfirmacao import MenuDeConfirmacao

class LimparChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(name="limpar", description="Limpa todas as mensagens de um canal específico.")
    @app_commands.describe(canal="O canal onde todas as mensagens serão limpas")
    async def limparCanal(self, interaction: discord.Interaction, canal: discord.TextChannel):
        # Verifica se o usuário tem permissões de administrador
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("Você não tem permissão para usar este comando.", ephemeral=True)
            return

        confirm_view = MenuDeConfirmacao()
        await interaction.response.send_message(f'Você tem certeza que deseja limpar o canal {canal.mention}?', view=confirm_view, ephemeral=True)

        await confirm_view.wait()

        if confirm_view.value is None:
            await interaction.followup.send("Tempo esgotado. A ação de limpar o canal foi cancelada.", ephemeral=True)
        elif confirm_view.value:
            await interaction.followup.send(f'O canal {canal.mention} foi limpo com sucesso.', ephemeral=True)
            await canal.purge()
        else:
            await interaction.followup.send("Ação de limpar o canal foi cancelada.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(LimparChat(bot))
