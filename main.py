from twitchio.ext import commands
import random




#=================
#UNCOMMENT ON RELEASE
#=================

bot = commands.Bot(
    token='oauth:[PLACEHOLDER]',
    client_id='[PLACEHOLDER]',
    nick='[PLACEHOLDER]',
    prefix='!',
    initial_channels=['[PLACEHOLDER]']
)


#Basic Twitch Commands with Song Requests System
@bot.event
async def event_message(message):
    if message.author.name.lower() == bot.nick.lower():
        return
    await bot.handle_commands(message)

@bot.command(name='socials')
async def socials(ctx):
    await ctx.send(f'YouTube:  | Discord: ')

#Song Request System
#========================================================
#Delete this section if you do not want song requests
#This section was designed for OperationCaboose on TwitchTV
#========================================================

@bot.command(name='songrequest')
async def song(ctx):
    await ctx.send(f'Placing song in the queue!')

@bot.command(name='song')
async def song(ctx):
    await ctx.send(f'current song: {ctx.message}')


#Yu-Gi-Oh Streamer Commands
#========================================================
#Delete this section if you do not want Yu-Gi-Oh Commands
#This section was designed for Averyxstream on TwitchTV
#========================================================

#Generates a random Bamu (Bullshit avery made up) deck
@bot.command(name='bamu')
async def bamu(ctx):
    await ctx.send(f'test')

#Generates a random Edison deck
@bot.command(name='edison')
async def edison(ctx):
    edison_list = [
        "Earthbound", "Cyberdark", "Neos", "Insect", "Ninja", "Ojama", "Reptile", "Roids", "Tryhard DAD"
    ]
    await ctx.send(f'The chosen edison deck is: {random.choice(edison_list)}')

#Generates a random Deck
@bot.command(name='randomdeck')
async def randomdeck(ctx):
    await ctx.send(f'test')

if __name__ == "__main__":
    print("🚀 Launching bot . . .")

    bot.run()
