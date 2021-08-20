import discord
import os
import json
import random
import asyncio
from mcrcon import MCRcon as r
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import CommandError
from dotenv import load_dotenv
from colorama import init
from colorama import Fore, Back, Style

# TODO:
# - Add status command (pls status)
# - Add README
# - Add Windows support
# - Add install script
# - maybe put on AUR?
# - Fix gnome-terminal not working via systemd

init()
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

class c:
	reset = Style.RESET_ALL
	status = Style.BRIGHT + Fore.BLUE + ":: " + Fore.WHITE
	error = Style.BRIGHT + Fore.RED + "[!]" + Fore.WHITE
	warning = Fore.YELLOW + Fore.RED + "[?]" + Fore.WHITE
	misc = Style.DIM


print(c.status + "Bot starting..." + c.reset)
bot = commands.Bot(command_prefix=["pls ","Pls ","PLS ","please ","Please ","PLease ","PLEASE ", "pwease ", "Pwease ", "PWEASE "], help_command=None)

async def is_owner(ctx):
	if ctx.author.id == os.getenv('OWNER_ID'):
		return True
	else:
		return False

@bot.event
async def on_ready():
	print("")
	print(c.status + "Bot started!" + c.reset)

	servers = list(bot.guilds)
	print(f"Connected on {str(len(servers))} servers:")
	print('\n'.join(server.name for server in servers))
	print("")

@bot.command()
async def help(ctx):
	embed=discord.Embed(title="All commands", description='Use the prefix "pls" to use them!')
	embed.set_author(name="Version: v1.1.0", url="https://github.com/daniel071/onlinepls")
	embed.add_field(name="pls online", value="Starts the server", inline=False)
	embed.add_field(name="pls offline", value="Stops the server (Admins only)", inline=False)
	embed.add_field(name="pls help", value="Displays this message", inline=False)
	await ctx.channel.send(embed=embed)

@bot.command()
async def online(ctx):
	infoMessage = random.choice(compliments)
	await ctx.channel.send(infoMessage)
	try:
		with r('localhost', os.getenv('RCON_PASS')) as mcr:
			pass
	except ConnectionRefusedError:
		await ctx.channel.send(":white_check_mark: Server started!")
		os.system('''
        gnome-terminal -- sh -c "cd {mcDirectory}; source ./start.sh"
		'''.format(mcDirectory=os.getenv('MC_DIRECTORY')))
		print(c.misc + ctx.author.name + "has started the server")
	else:
		await ctx.channel.send(":triumph: Server is already online... SMH ")



@bot.command()
async def offline(ctx):
	if str(ctx.author.id) in json.loads(os.getenv('ADMINS')):
		infoMessage = random.choice(compliments)
		await ctx.channel.send(infoMessage)

		try:
			with r('localhost', os.getenv('RCON_PASS')) as mcr:
				resp = mcr.command('stop')
			print(c.misc + ctx.author.name + "has stopped the server")
		except ConnectionRefusedError:
			await ctx.channel.send(":triumph: Imagine trying to stop a server that is already offline... ")
		else:
			await ctx.channel.send(":x: Server stopped!")
	else:
		# A friend asked me to add this feature, not me. So I added it.
		# This will run if you are not allowed to run the command.
		if "pls offline" == ctx.message.content.lower():
			await ctx.channel.send("Ahem. Please use correct English grammar. Please say Please instead of 'pls'. Thank you Aarnav.")
		elif "please offline" == ctx.message.content.lower():
			await ctx.channel.send("Actually, add an 'uwu' to the end of that for my amusement. Thank you.")
		elif "please offline uwu" == ctx.message.content.lower():
			await ctx.channel.send("One UwU is great and all, but I want more, Aarnav. I want you to add an extra owo on the end of that as well.")
		elif "please offline uwu owo" == ctx.message.content.lower():
			await ctx.channel.send("Almost there. Now translate it to furry talk")
		elif "pwease offline mowde pwweaase daddy ~" == ctx.message.content.lower():
			await ctx.channel.send("Perfect. Now, the last step is to admit that you are a homosexual.")
			await asyncio.sleep(3)
			await ctx.channel.send("Say 'pwease offline mowde pwweaase daddy ~' followed by your admission.")
		elif "homosexual" in ctx.message.content.lower() and "no" not in ctx.message.content.lower() and "not" not in ctx.message.content.lower():
			await ctx.channel.send("Excellent. Please wait 10 seconds while I shut down the server... :smile:")
			await asyncio.sleep(10)
			await ctx.channel.send("You throught this was an offline command? Lied to!! Trolled!!!")
		else:
			await ctx.channel.send("You fucked it up Aarnav. Now do it all over again.")

		# await ctx.channel.send("I'm sorry Dave, I'm afraid I can't do that.")


@bot.event
async def on_message(ctx):
	if bot.user.mentioned_in(ctx):
		if "online" in ctx.message.content.lower():
			await online(ctx)
		elif "offline" in ctx.message.content.lower():
			await offline(ctx)
		else:
			await ctx.channel.send("You can type 'pls help' for more info")

	await bot.process_commands(ctx)

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, CommandNotFound):
		await ctx.channel.send(":angry: You know this command doesn't exist, right? LLLLL")
	else:
		print(c.error + "An unhandled error has occured." + c.reset + error)
		await ctx.channel.send(":flushed: Looks like Daniel f*cked up something again. Pls spam his DMs so he fixes it!!")
		await ctx.channel.send("```{error}```".format(error=error))



bot.run(os.getenv('TOKEN'))
