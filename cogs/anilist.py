import discord
from discord.ext import commands


class Anilist(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Anilist Cog initalized")

    #@commands.command()

def setup(client):
    client.add_cog(Anilist(client))