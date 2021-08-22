#All the code will be in one file. Don't hit:> by IIchigo7777

import discord
from discord import Game
import datetime
import time
import asyncio
from disocrd.ext import commands
from discord.ext.commands import Bot

client=commands.Bot( command_prefix="s!" )
client.remove_command("help")

@client.event
async def on_ready():
    print("Logged in")
    print(client.user.name)
    print(client.user.id)
    print("----------------")

#Change how we want the welcome message

@client.event
async def on_member_join(member):
    embed = discord.Embed(title="Welcome",color=0x9208ea,description=f"{member.mention}, Joined \nWelcome to the server :partying_face:".format(member))
    embed.set_footer(text="Developer by IIchigo#7777")
    msg = await ctx.send(discord.Object(id="852850462679892010"),embed=embed) #channel id in wich you wand to send welcome message

#Change how we want the welcome message

@client.command(pass_context=True)
async def hello(ctx):
    await ctx.send("Hello Friend :smile:")


client.run('') #your bot token