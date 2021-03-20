import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions, check
import json
import time

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    def is_modlog(self, ctx):
        with open('settings.json', 'r') as f:
            data = json.load(f)
            mdid = data['modlogsid']
        if mdid != 0:
            return mdid

    #-----------------------COMMANDS------------------------#


    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!', delete_after = 3)

    @commands.command()
    @has_permissions(kick_members = True)
    async def kick(self, ctx, member:discord.Member, *, reason = None):
        await member.kick(reason = reason)
        embed = discord.Embed(title=f"{member.name} has been Kicked by {ctx.author.name}👋", description=f"Reason >> {reason}", color=0x000142)
        with open('settings.json', 'r') as f:
            data = json.load(f)
            mdid = data['modlogsid']
        modlogs = ctx.guild.get_channel(mdid)
        await modlogs.send(embed = embed)#send it to modlogs channel
        embed = discord.Embed(title=f"{member.name} Kicked✅", color=0x66ff00)
        await ctx.send(embed = embed, delete_after = 3) #send it to the channel

    @commands.command()
    @has_permissions(ban_members = True)
    async def ban(self, ctx, member:discord.Member, *, reason = None):
        await member.ban(reason = reason)
        embed = discord.Embed(title=f"{member.name} has been Banned by {ctx.author.name}👋", description=f"Reason >> {reason}", color=0x000142)
        with open('settings.json', 'r') as f:
            data = json.load(f)
            mdid = data['modlogsid']
        modlogs = ctx.guild.get_channel(mdid)
        await modlogs.send(embed = embed)#send it to modlogs channel
        embed = discord.Embed(title=f"{member.name} Banned✅", color=0x66ff00)
        await ctx.send(embed = embed, delete_after = 3) #send it to the channel

    @commands.command()
    @has_permissions(ban_members = True)
    async def unban(self, ctx, *, member:discord.Member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(title=f"{member.name} Unbanned✅", color=0x66ff00)
                await ctx.send(embed = embed, delete_after = 3)
                return   #modlogs to be added (create a seperate function for it

    @commands.command()
    @has_permissions(manage_roles = True)
    async def addrole(self, ctx, user:discord.User, role:discord.Role):
        await user.add_roles(role)
        embed = discord.Embed(title=f"{user.name} has been given the {role.name} Role", description=f"Role Given by {ctx.author.name}", color=0x000142)
        with open('settings.json', 'r') as f:
            data = json.load(f)
            mdid = data['modlogsid']
        if mdid != 0:
            modlogs = ctx.guild.get_channel(mdid)
            await modlogs.send(embed = embed)#send it to modlogs channel
            embed = discord.Embed(title=f"{role.name} Role added to {user.name} ✅", color=0x66ff00)
            await ctx.send(embed = embed, delete_after = 3) #send it to the channel

    @commands.command()
    @has_permissions(manage_roles = True)
    async def verifymessage(self, ctx, messageid = discord.Message, emoji = discord.Emoji, role = discord.Role):
        pass

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, number:int):
        await ctx.channel.purge(limit = number)
        embed=discord.Embed(title=f"{number} Messages Cleared✅", color=0x66ff00)
        await ctx.send(embed=embed)
        embed=discord.Embed(title=f"{number} Messages Cleared in {ctx.channel.name}✅", description = f'Cleared by {ctx.author.name}',color=0x66ff00)


    #----------------Error-Handling-------------------#


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(title="You do not have the Permission to use this Command! ❌", color=0xa30000)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title="Incorrect Usage of the Command❌", color=0xa30000)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandNotFound):
            embed=discord.Embed(title="I do not Recognise this Command 😥", color=0xa30000)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Moderation(client))
