import discord
from discord.ext import commands

prefix = input('enter the msg u want: ')
token = input('enter ur token: ')
urid = input('enter ur id: ')

intents = discord.Intents.default()
intents.members=True

client = commands.Bot(help_command=None, command_prefix=prefix, self_bot=True, case_insensitive=True, intents=intents)

@client.event
async def on_ready():
    vex = await client.fetch_user(825076850635046985)
    print(f'loaded sb on {client.user}')
    print(f'ur token: {token}')
    print(f'prefix: {prefix}')
    print(f'made by {vex}')
    
@client.command()
async def massdm(ctx,*,msg):
    if ctx.author.id != urid:
        pass
    else:
        for member in ctx.guild.membes:
            await member.send(msg + member.mention)
           
try:
    client.run(token, bot=True)
except:
    print('inavlid token')
