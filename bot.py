from cgi import test
from pydoc import describe
import discord
from discord.ext.commands.core import guild_only
from matplotlib import testing
intents = discord.Intents.default()
from discord.ext import commands, tasks

from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.commands import bot
import json
import requests
import PIL
from PIL import Image, ImageFont, ImageDraw, ImageChops, ImageColor

loadFont = 'fonts/BurbankBigRegular-Black.ttf'

client = commands.Bot(command_prefix='lmaolololollo', intents=intents)
client.remove_command('help')
slash = SlashCommand(client, sync_commands = True)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="/help"))
    print("\nServers: " + str(len(client.guilds)))
    print("Bot is ready")

@slash.slash(name='generate', description='Generate a custom Naruto Banner!', options=[
    create_option(
        name='skin',
        description='What Naruto X Fortnite skin wold you like on the banner?',
        option_type=3,
        required=True,
        choices=[
            create_choice(
                name='naruto',
                value='naruto'
            ),
            create_choice(
                name='kakashi',
                value='kakashi'
            ),
            create_choice(
                name='sasuke',
                value='sasuke'
            ),
            create_choice(
                name='sakura',
                value='sakura'
            ),
            create_choice(
                name='hinata',
                value='hinata'
            ),
            create_choice(
                name='gaara',
                value='gaara'
            ),
            create_choice(
                name='itachi',
                value='itachi'
            ),
            create_choice(
                name='orochimaru',
                value='orochimaru'
            ),
        ]
    ),
    create_option(
        name='text',
        description='What text do you want on the banner?',
        option_type=3,
        required=True
    ),
    create_option(
        name='fontsize',
        description='Pick a custom font size! (Optional) (Default is 110)',
        option_type=4,
        required=False
    ),
    create_option(
        name='capitalize',
        description='Would you like to capitalize your text? (Optional)',
        option_type=3,
        required=False,
        choices=[
            create_choice(
                name='yes',
                value='yes'
            )
        ]
    ),
    create_option(
        name='custom_color',
        description='Add a custom color to your text! (Ex: #ffc72b)',
        option_type=3,
        required=False
    )
]
)
async def generate(ctx, skin:str, text:str, fontsize:int=None, capitalize:str=None, custom_color:str=None):
    background = Image.open(f'Images/b_{skin}.png')

    if capitalize != None:
        text = text.upper()

    if custom_color == None:
        color = (255, 255, 255)
    else:
        color = ImageColor.getcolor(custom_color, "RGB")
    
    if fontsize == None:
        size = 110
    else:
        size = fontsize

    draw=ImageDraw.Draw(background)
    font=ImageFont.truetype(loadFont,size)
    draw.text((530,250),text,font=font,fill=color, anchor='ms') # Writes name
    background.save('banner.png')

    await ctx.send('Heres your banner!', file=discord.File('banner.png'))

client.run('YOUR_TOKEN_HERE')
