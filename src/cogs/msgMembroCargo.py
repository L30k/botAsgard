import os

import discord
from discord.ext import commands, tasks


class MsgMenbroCargo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.role_id = os.getenv("ROLE_ID")

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        role = discord.utils.get(after.guild.roles, id=self.role_id)

        if role not in before.roles and role in after.roles:
            message = (
                "Olá, Guerreiros!\n\n"
                "Agora que você recebeu o cargo #TL, precisamos que responda a um formulário para realizarmos uma triagem completa "
                "e garantir que todos estejam prontos para as batalhas que virão.\n\n"
                "Sua participação é essencial para continuarmos crescendo como uma comunidade forte e organizada. Agradecemos a sua colaboração!\n\n"
                "🔗 Preencha o formulário de recrutamento e torne-se um(a) Asgardiano(a): [Recrutamento Asgard (Throne & Liberty)](https://docs.google.com/forms/d/e/1FAIpQLSfcJXnMao0WOSvrcfqtd_Gyw70T3nwHz7zfdiS0YkDSeC1MBA/viewform)"
            )
            try:
                await after.send(message)
            except discord.Forbidden:
                print(f'Não consegui enviar uma mensagem para {after.display_name}')


async def setup(bot):
    await bot.add_cog(MsgMenbroCargo(bot))
