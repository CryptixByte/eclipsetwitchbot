from twitchio.ext import commands
import random

bot = commands.Bot(
    token='oauth:[PLACEHOLDER]',
    client_id='[PLACEHOLDER]',
    nick='[PLACEHOLDER]',
    prefix='!',
    initial_channels=['[PLACEHOLDER]']
)

#===============
#=DO NOT DELETE=
#===============

@bot.event
async def event_message(message):
    if message.author.name.lower() == bot.nick.lower():
        return
    await bot.handle_commands(message)

@bot.command(name='socials')
async def socials(ctx):
    await ctx.send(f'YouTube: [PLACEHOLDER] | Discord: [PLACEHOLDER] | X: [PLACEHOLDER]')

@bot.command(name='lurk')
async def lurk(ctx):
    await ctx.send(f'Thanks for lurking @{ctx.message.author.name}!')

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
    
#League Streamer Commands
#========================================================
#Delete this section if you do not want League of Legends Commands
#This section was designed for Averyxstream on TwitchTV
#========================================================    

#Inspired by Ultimate Bravery on random selections
@bot.command(name='ultimateavery')
async def ultimateavery(ctx):
    champions = [
        "Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe",
        "Aurelion Sol", "Aurora", "Azir", "Bard", "Bel'Veth", "Blitzcrank", "Brand", "Braum", "Briar", "Caitlyn",
        "Camille", "Cassiopeia", "Cho'Gath", "Corki", "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko", "Elise",
        "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas",
        "Graves", "Gwen", "Hecarim", "Heimerdinger", "Hwei", "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan IV",
        "Jax", "Jayce", "Jhin", "Jinx", "K'Sante", "Kai'Sa", "Kalista", "Karma", "Karthus", "Kassadin",
        "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", "Kog'Maw", "LeBlanc", "Lee Sin",
        "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi",
        "Milio", "Miss Fortune", "Mordekaiser", "Morgana", "Naafiri", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee",
        "Nilah", "Nocturne", "Nunu & Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana",
        "Quinn", "Rakan", "Rammus", "Rek'Sai", "Rell", "Renata Glasc", "Renekton", "Rengar", "Riven", "Rumble",
        "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed",
        "Sion", "Sivir", "Skarner", "Smolder", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench",
        "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch",
        "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz", "Vex", "Vi", "Viego", "Viktor",
        "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yone", "Yorick",
        "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra", "Mel", "Yunara"
    ]

    items_legendary = [
        "Abyssal Mask", "Archangel's Staff", "Ardent Censer", "Axiom Arc", "Banshee's Veil", "Black Cleaver", "Blackfire Torch", 
        "Blade of the Ruined King", "Bloodletter's Curse", "Bloodthirster", "Chempunk Chainsword", "Cosmic Drive", "Cryptbloom",
        "Dawncore", "Dead Man's Plate", "Death's Dance", "Echoes of Helia", "Eclipse", "Edge of Night", "Essence Reaver", "Experimental Hexplate",
        "Fimbulwinter", "Force of Nature", "Frozen Heart", "Guardian Angel", "Guinsoo's Rageblade", "Heartsteel", "Hextech Rocketbelt", 
        "Hollow Radiance", "Horizon Focus", "Hubris", "Hullbreaker", "Iceborn Gauntlet", "Immortal Shieldbow", "Imperial Mandate", 
        "Infinity Edge", "Jak'Sho", "Kaenic Rookern", "Knight's Vow", "Kraken Slayer", "Liandry's Torment", "Lich Bane", "Locket of the Iron Solari",
        "Lord Dominik's Regards", "Luden's Companion", "Mallignance", "Manamune", "Maw of Malmortius", "Mejai's Soulstealer", "Mercurial Scimitar",
        "Mikael's Blessing", "Morellonomicon", "Nashor's Tooth", "Navori Quickblades", "Phantom Dancer", "Rabadon's Deathcap", "Randuin's Omen",
        "Rapid Firecannon", "Ravenous Hydra", "Redemption", "Runaans Hurricane", "Rylai's Crystal Scepter", "Seraph's Embrace", "Serpent's Fang",
        "Serylda's Grudge", "Shadowflame", "Spirit Visage", "Sterak's Gage", "Stormrazor", "Sunfire Aegis", "The Collector", "Thornmail", "Titanic Hydra",
        "Umbral Glaive", "Void Staff", "Warmog's Armor", "Wit's End", "Zeke's Convergence", "Zhonya's Hourglass",
    ]

    items_boots = [
        "Berserker's Greaves", "Boots of Swiftness", "Boots of Lucidity", "Mercury's Threads", "Plateed Steelcaps", "Sorcerer's Shoes", "Symbiotic Soles"
    ]
    
    random_champion = random.choice(champions)
    random_legendary = random.sample(items_legendary, 5)

    await ctx.send(f'{random_champion} | {" ".join(random_legendary)}  {random.choice(items_boots)}')

@bot.command(name='bravery')
async def bravery(ctx):
    champions = [
        "Renekton", "Pantheon", "Shyvana", "Amumu", "Lissandra", "Malzahar", "Ashe", "Sivir", "Tahm Kench", "Milio"
    ]
    await ctx.send(f'It has been decided: {random.choice(champions)}')

#===============
#=DO NOT DELETE=
#===============

if __name__ == "__main__":
    print("🚀 Launching bot . . .")

    bot.run()




