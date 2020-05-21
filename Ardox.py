import discord 
import os
import sys
from discord.utils import get
import random
from discord import embeds
import time 
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
from discord.ext import tasks
from discord import Activity
import threading
import sqlite3

client = discord.Client()

TOKEN = 'NzA3MDc4NDQ5NzM0NjE1MDcx.XraSAQ.BiDLZFfefjEmITioP9r06FVFK4g'

prefix = '#'
#guild = client.get_guild(688009516410863647)
channels = ['bot-commands']

wlcmlist = ['We have waited so long to have you among us. At last, the time has come. We are most delightfully welcoming you to join us today!',
            'I am so glad to welcome you to my Server. Your presence in our Server is nothing less than a blessing to us!',
            'The times we spend with you is always so full of joy and happiness. Knowing that you\'ll be with us, brings the smile on our face. Welcome to our Server!',
            "The entire team of Designer's Club is honored to welcome you on board. Enjoy the facilities here and make sure your talents are fully utilized!",
            'We are delighted to have you among us. On behalf of all the members and the management, we would like to extend our warmest welcome and good wishes!',
            'The entire team of Designer\'s Club is thrilled to welcome you on board. We hope you\'ll do some amazing works here!',
            'Dear new member, I welcome you to Designer\'s Club with much love. I hope you would work for the motive of the Server as much as other members!']

imgurl = ['https://i.imgur.com/lZOA6s8.jpg','https://i.imgur.com/kLHHD12.jpg','https://i.imgur.com/JYk292J.png','https://i.imgur.com/U2a6L8U.png']

hihello = ['Hi','Hey There!','Hello','Yo']

bot = ['Designer#7099']

warnings = []

r = []
g = []
b = []

art_channels = ['test','gallery','graphic-design','product-design','photography','traditional-art','lightroom','motion','photoshop','interaction']

thirty_percent = 0
total_members  = 0

for i in range(256):
    r.append(i)
    g.append(i)
    b.append(i)

top_ten_names = ['','','','','','','','','','']
top_ten_count = [0,0,0,0,0,0,0,0,0,0]

names = []
count = []

def statistics(message):
    for no in count:
        for na in top_ten_count:
            if no > na and (names[count.index(no)] not in top_ten_names):
                indf = count.index(no)
                indg = top_ten_count.index(na)
                top_ten_count[indg] = no
                top_ten_names[indg] = names[indf]
                y_pos = np.arange(len(top_ten_names))
                plt.barh(y_pos,top_ten_count,align='center')
                plt.figure()
                plt.yticks(y_pos,top_ten_names)
                plt.xlabel('Messages')
                plt.ylabel('UserID')
                plt.savefig(fname = 'stats',transparent = False, bbox_inches='tight')
                
def conti(message):
    if str(message.author) != 'Ardox#9288':
        if str(message.author) in names:
            ind = names.index(str(message.author))
            count[ind] = count[ind] + 1
            if str(message.author) in top_ten_names:
                indh = top_ten_names.index(str(message.author))
                top_ten_count[indh] = top_ten_count[indh] + 1
        else:
            names.append(str(message.author))
            count.append(1)


'''@tasks.loop(seconds = 5)
async def change_presence():
    game1 = discord.Activity(name = str(total_members)+" Designers and !help",type = discord.ActivityType.watching)
    game2 = discord.Activity(name = prefix+"help", type = discord.ActivityType.listening)
    game = cycle([game1,game2])
    await client.change_presence(status = discord.Status.online, activity = (game1))'''


@client.event
async def on_ready():
    print("Ready!")
    global thirty_percent
    guild = client.get_guild(688009516410863647)
    print(guild)
    total_members = len(guild.members)
    print(total_members)
    thirty_percent = int((30/100)*total_members) + 1
    game1 = discord.Activity(name = str(total_members)+" Designers and #help",type = discord.ActivityType.watching)
    await client.change_presence(status = discord.Status.online, activity = (game1)) 
    #await client.change_presence(status = discord.Status.online, activity = next(game))
    #elif now == 120:
        #now = 0

@tasks.loop(seconds = 5)
async def change_presence():
    guild = client.get_guild(688009516410863647)
    print(guild)
    total_members = len(guild.members)
    game1 = discord.Activity(name = str(total_members - 1)+" Designers and #help",type = discord.ActivityType.watching)
    await client.change_presence(status = discord.Status.online, activity = (game1))

@client.event 
async def on_member_join(member):
    channel = member.guild.get_channel(688009922935652426)
    rules = member.guild.get_channel(689059207466582024)
    wlcmmsg = random.choice(wlcmlist)
    tm= len(member.guild.members)
    verifyrole = discord.utils.get(member.guild.roles, name = 'Member') #temp 
    col = discord.Color.from_rgb(random.choice(r), random.choice(g), random.choice(b))
    if int(str(tm+1)[-1]) == 1:
        welcome = discord.Embed(title="Welcome to Designer's Club",
                                    colour=col)
        welcome.add_field(name=random.choice(wlcmlist)+', You are '+ str(tm+1) + 'st Member of Designer\'s Club',value=member.mention)
        welcome.set_image(url = random.choice(imgurl))
        await channel.send(embed=welcome)
    elif int(str(tm+1)[-1]) == 2:
        welcome = discord.Embed(title="Welcome to Designer's Club",
                                   colour=col)
        welcome.add_field(name=random.choice(wlcmlist)+', You are '+ str(tm+1) + 'nd Member of Designer\'s Club',value=member.mention)
        welcome.set_image(url = random.choice(imgurl))
        await channel.send(embed=welcome)
        #on_ready()
    elif int(str(tm+1)[-1]) == 3:
        welcome = discord.Embed(title="Welcome to Designer's Club",
                                   colour=col)
        welcome.add_field(name=random.choice(wlcmlist)+', You are '+ str(tm+1) + 'rd Member of Designer\'s Club',value=member.mention)
        welcome.set_image(url = random.choice(imgurl))
        await channel.send(embed=welcome)
    else:
        welcome = discord.Embed(title="Welcome to Designer's Club",
                                   colour=col)
        welcome.add_field(name=random.choice(wlcmlist)+', You are '+ str(tm+1) + 'th Member of Designer\'s Club',value=member.mention)
        welcome.set_image(url = random.choice(imgurl))
        await channel.send(embed=welcome)
        #await member.add_roles(verifyrole)

@client.event
async def on_raw_reaction_add(payload):
    print(payload)
    emoji = payload.emoji.name
    channelid = 689059207466582024                #verifychannelID
    user = payload.member
    verifyrole = discord.utils.get(user.guild.roles, name = 'Member')
    if emoji == '✅' and payload.channel_id == channelid:
        await user.add_roles(verifyrole)
        await payload.message.reaction.remove(user = payload.member)
        print('yes')
 
        
    
@client.event
async def on_message(message):
        author_roles = discord.utils.get(message.author.roles, name = 'Staff')
        if message.content.startswith(prefix+'hi') or message.content.startswith('hi') or message.content.startswith('Hi'):
            await message.channel.send(random.choice(hihello))
            conti(message)
        elif (message.content.startswith(prefix+'help')):
            embed = discord.Embed(title = 'Bot Commands',
                                description = "The default prefix is '#'",
                                colour = discord.Colour.red(),
                                )
            embed.add_field(name = '#stats', value = 'Shows the top 10 contributors of this Server')
            embed.set_footer(text = str(datetime.now().time().hour) + ':' +str(datetime.now().time().minute))
            await message.author.send(embed = embed)
            await message.channel.purge(limit = 1)
            
        elif message.content.startswith(prefix+'clear'): 
            try:
                if author_roles:
                    s = message.content.split()
                    print(s)
                    n = int(s[1]) + 1
                    await message.channel.purge(limit = n)
                    conti(message)
                else:
                    noperm = discord.Embed(title = 'You Do Not have the Permission to use this command!', colour = discord.Color.red())
                    noperm.set_footer(text = str(datetime.now().time().hour) + ':' +str(datetime.now().time().minute))
                    await message.channel.send(embed = noperm)
                    conti(message)
            except:
                purge = discord.Embed(title = 'Incorrect Usage! Argument goes like this-', description = '!clear <Number of messages>', colour = discord.Colour.red() )
                purge.set_footer(text = str(datetime.now().time().hour) + ':' +str(datetime.now().time().minute))
                await message.author.send(embed = purge)    
        
        elif str(message.channel.category).lower() == 'art':
            if message.content.find('http') != -1:
                await message.add_reaction('👍')
            elif message.attachments:
                await message.add_reaction('👍')
            conti(message)
    
        elif message.content.startswith(prefix+'stats'):
            stats = discord.Embed(title = 'Coming Soon...', description = 'This feature is in development and will be added soon :)') 
            stats.set_footer(text = str(datetime.now().time().hour) + ':' +str(datetime.now().time().minute))
            await message.channel.send(embed = stats)
            conti(message)
            statistics(message)
            pic = discord.File('stats.png','stats.png')
            #await message.channel.send('stats.png',file = pic)
        
        elif message.content.startswith(prefix+'announce'): #date hour-minute
            pass #threading
        
        elif message.content.find('discord.gg') != -1:
            admin = discord.utils.get(message.author.roles, name = 'Admin')
            founder = discord.utils.get(message.author.roles, name = 'Founder')
            if admin or founder:
                pass
            elif str(message.author) in warnings:
                await message.author.ban
            else:
                warninv = discord.Embed(title = 'Warning! You will get banned if you invite in the server another time', description = 'Invites are banned in this Server', colour = discord.Color.red())
                warnings.append(str(message.author))
                await message.channel.purge(limit = 1)
                await message.author.send(embed = warninv)

        conti(message)
        print(names,count)
        print(top_ten_names,top_ten_count)
        
        
'''@client.event
async def on_reaction_add(reaction, user):
    if (reaction.message.channel in art_channels) and (reaction.count == 1):
        art_features = user.guild.get_channel(704554980782243900)
        indexl = reaction.message.content.find('http')
        link = reaction.message.content[indexl]
        acol = discord.Color.from_rgb(random.choice(r), random.choice(g), random.choice(b))
        artf = discord.Embed(title = 'Featured Art',colour = acol)
        artf.set_image(url = link)
        await art_features.send(embed = artf)
    elif reaction.emoji == '✅' and reaction.message.channel == 'roles':
        await user.add_roles(verifyrole)
        await payload.message.reaction.remove(user = payload.member)
        print('yes')'''
 
client.run(TOKEN)
