import discord
import discord.ext
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
import json 

class Settings(commands.Cog):

    def __init__(self, client):
        self.client = client

  #---------COMMANDS---------#

    @commands.command()
    @has_permissions(administrator = True)
    async def modlogs(self, ctx, channelid:int):
        with open('cogs/settings.json', 'r+') as f:
            data = json.load(f)
            data['modlogsid'] = channelid # <--- add `id` value.
            f.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, f, indent=4)
            f.truncate()     # remove remaining part            
        await ctx.send('Modlogs Channel Updated!')
    
    @commands.command()  #resets the modlogs channel
    @has_permissions(administrator = True)
    async def unmodlog(self, ctx, channelid:int):
        with open('cogs/settings.json', 'r+') as f:
            data = json.load(f)
            data['modlogsid'] = channelid # <--- add `id` value.
            f.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, f, indent=4)
            f.truncate()     # remove remaining part            
        await ctx.send('Modlogs Channel Updated!')

    @commands.command()
    @has_permissions(administrator = True)
    async def serverlogs(self, ctx, channelid:int):
        with open('cogs/settings.json', 'r+') as f:
            data = json.load(f)
            data['serverlogsid'] = channelid # <--- add `id` value.
            f.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, f, indent=4)
            f.truncate()     # remove remaining part            
        await ctx.send('Serverlogs Channel Updated!')


def setup(client):
    client.add_cog(Settings(client))