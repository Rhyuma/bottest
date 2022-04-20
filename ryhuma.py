import os

from discord.ext import commands

ryhuma = commands.Bot("!")
print("Vamos Trabalhar")


def load_cogs(ryhuma):
    #ryhuma.load_extension("gcargo")
    for file in os.listdir("comandos"):
        if file.endswith(".py"):
            cog = file[:-3]
            ryhuma.load_extension(f"comandos.{cog}")


load_cogs(ryhuma)
ryhuma.run("OTY2MTU4MjkyNTMzNTQyOTUz.Yl9rBw.2jVtiIt5FMLXQCn3g34bckhFUwE")
