import discord
from discord.ext import tasks, commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
from discord import embeds
from discord import Activity
import os
import sys
import itertools
import time
import datetime
import json

server_msg = '[Ardox] '

PREFIX = '!'

TOKEN = open('token.txt', 'r')
TOKEN = TOKEN.read()

client = commands.Bot(command_prefix = PREFIX)

@client.command()
@has_permissions(administrator = True)
async def loadcog(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@has_permissions(administrator = True)
async def unloadcog(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
@has_permissions(administrator = True)
async def reloadcog(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(server_msg + f'reloaded {extension}')
    await ctx.send(f'Reloaded {extension} Cog')

#Loading the extensions

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(server_msg + f'{filename} cog loaded!')

@client.event
async def on_ready():
    print(server_msg + 'Started!')
    #await reload_prefix()
    act = discord.Activity(name = f'{PREFIX}help', type = discord.ActivityType.watching)
    await client.change_presence(status = discord.Status.online, activity = act)
    print(server_msg + "Bot Activity Updated")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(color=0xa30000)
        embed.add_field(name="Incorrect Usage for the Command.Please Check the Required Arguments!❌", value="", inline=True)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(color=0xa30000)
        embed.add_field(name="Incorrect Usage for the Command❌", value="", inline=True)
        await ctx.send(embed=embed)


print('[Ardox] Starting...')
client.run(TOKEN, reconnect = True)
print(server_msg + 'Ended')