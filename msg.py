

import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(intents=intents,command_prefix = '!')
channel=client.get_channel("813855932698066968")
@client.event
async def on_message(message):
    print(message.content)
    with open('msg.txt', 'a') as f:
        f.write(message.content + "\n")
        f.close()


client.run("OTgyMzQzMzQyMTIzNzk0NTIy.GS1oKG.P0WAgsDC_3YXb47N-EzPsmgv3wskpwB5ZXt-68")
