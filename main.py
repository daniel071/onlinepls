import discord
import os
import random
import asyncio
from mcrcon import MCRcon as r
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import CommandError
from dotenv import load_dotenv

# TODO:
# - Make bot recover from restart, continuing to edit all existing messages
# - Add configuration to change settings for each specific server, such as time
#   to update message

load_dotenv()

complimentsText = '''
Hey Helper, how play game?
You’re a great person! Do you want to play some Hypixel games with me?
Your personality shines brighter than the sun!
Welcome to the hypixel zoo!
Maybe we can have a rematch?
In my free time I like to watch cat videos on youtube
I heard you like minecraft, so I built a computer so you can minecraft, while minecrafting in your minecraft.
I like pineapple on my pizza
I had something to say, then I forgot it.
Hello everyone! I’m an innocent player who loves everything Hypixel.
I like Minecraft pvp but you are truly better than me!
Behold, the great and powerful, my magnificent and almighty nemesis!
When nothing is right, go left.
Let’s be friends instead of fighting okay?
Your Clicks per second are godly. :flushed:
If the world in Minecraft is infinite…how can the sun revolve around it?
Pls give me doggo memes!
Blue is greenier than purple for sure
I sometimes try to say bad things and then this happens :(
I have really enjoyed playing with you! <3
What can’t the Ender Dragon read a book? Because he always starts at the End.
You are very good at this game friend.
I like to eat pasta, do you prefer nachos?
Sometimes I sing soppy, love songs in the car.
I love the way your hair glistens in the light
In my free time I like to watch cat videos on youtube
When I saw the guy with a potion I knew there was trouble brewing.
I enjoy long walks on the beach and playing Hypixel
Doin a bamboozle fren.
I need help, teach me how to play!
Can you paint with all the colors of the wind
'''
compliments = complimentsText.splitlines()
bot = commands.Bot(command_prefix='pls ', help_command=None)

async def is_owner(ctx):
	if ctx.author.id == os.getenv('OWNER_ID'):
		return True
	else:
		return False

@bot.event
async def on_ready():
	servers = list(bot.guilds)
	print(f"Connected on {str(len(servers))} servers:")
	print('\n'.join(server.name for server in servers))

@bot.command()
async def help(ctx):
	embed=discord.Embed(title="All commands", description='Use the prefix "pls" to use them!')
	embed.set_author(name="Version: v1.0.0", url="https://github.com/daniel071/onlinepls")
	embed.add_field(name="pls online", value="Starts the server", inline=False)
	embed.add_field(name="pls offline", value="Stops the server (Admins only)", inline=False)
	embed.add_field(name="pls help", value="Displays this message", inline=False)
	await ctx.channel.send(embed=embed)

@bot.command()
async def online(ctx):
	infoMessage = random.choice(compliments)

	try:
		with r('localhost', os.getenv('RCON_PASS')) as mcr:
			pass
	except ConnectionRefusedError:
		await ctx.channel.send(":white_check_mark: " + infoMessage)
		os.system('''
        gnome-terminal -e 'sh -c  "cd /home/daniel/Minecraft/arentnav; source ./start.sh"'
		''')
	else:
		await ctx.channel.send(":triumph: Server is already online... SMH ")



@bot.command()
async def offline(ctx):
	if ctx.author.id == os.getenv('OWNER_ID') or ctx.author.id == os.getenv('OWNER_TWO_ID'):
		infoMessage = random.choice(compliments)

		try:
			with r('localhost', os.getenv('RCON_PASS')) as mcr:
				resp = mcr.command('stop')
		except ConnectionRefusedError:
			await ctx.channel.send(":triumph: Imagine trying to stop a server that is already offline... ")
		else:
			await ctx.channel.send(":x: " + infoMessage)
	else:
		await ctx.channel.send("I'm sorry Dave, I'm afraid I can't do that.")


@bot.event
async def on_message(ctx):
    if bot.user.mentioned_in(ctx):
        await ctx.channel.send("You can type 'pls help' for more info")

    await bot.process_commands(ctx)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.channel.send(":angry: You know this command doesn't exist, right? LLLLL")
    else:
        await ctx.channel.send(":flushed: Looks like Daniel f*cked up something again. Pls spam his DMs so he fixes it!!")



bot.run(os.getenv('TOKEN'))
