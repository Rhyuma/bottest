from discord.ext import commands



class Gcargo(commands.Cog):
    '''
    Gerenciar cargos através de reações
    '''

    def __int__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reacao, usuario):
        print(reacao.emoji)
        if reacao.emoji == "🐸":
            cargo = usuario.guild.get_role(965312059258581053)
            await usuario.add_roles(cargo)
        elif reacao.emoji != "🐸":
            cargo = usuario.guild.get_role(965312193719582750)
            await usuario.add_roles(cargo)



def setup(ryhuma):
    ryhuma.add_cog(Gcargo(ryhuma))
