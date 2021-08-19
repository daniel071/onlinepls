import discord
import os
import asyncio
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import CommandError
from dotenv import load_dotenv

# TODO:
# - Make bot recover from restart, continuing to edit all existing messages
# - Add configuration to change settings for each specific server, such as time
#   to update message

load_dotenv()

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
	embed.set_author(name="Version: v0.1.0", url="https://github.com/daniel071/onlinepls")
	embed.add_field(name="pls online", value="Starts the server", inline=False)
	embed.add_field(name="pls offline", value="Stops the server (Admins only)", inline=False)
	embed.add_field(name="pls help", value="Displays this message", inline=False)
	await ctx.channel.send(embed=embed)

@bot.command()
async def online(ctx):
    await ctx.channel.send(":white_check_mark: Server starting!")

@bot.command()
async def offline(ctx):
    await ctx.channel.send(":x: Server stopping!")

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
