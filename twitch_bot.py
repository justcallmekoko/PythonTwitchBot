#!/usr/bin/python

import os
import sys
import time
import random
import pkgutil
from dotenv import load_dotenv
from datetime import datetime
from twitchio.ext import commands

sys.dont_write_bytecode = True

random.seed(datetime.now())

class Bot(commands.Bot):

	def __init__(self):
		load_dotenv()
		TWITCH_TOKEN = os.getenv('TWITCH_TOKEN')
		RCON_PASSWORD = os.getenv('RCON_PASSWORD')
		RCON_IP = os.getenv('RCON_IP')
		NICK = str(os.getenv('NICK'))
		INITIAL_CHANNELS = str(os.getenv('INITIAL_CHANNELS'))
		CLIENT_ID=os.getenv('CLIENT_ID')
		API_TOKEN=os.getenv('API_TOKEN')
		PREFIX=os.getenv('PREFIX')
		HOST_USER=os.getenv('HOST_USER')
		super().__init__(token=TWITCH_TOKEN, prefix='!', initial_channels=['WillStunForFood'])

	async def event_ready(self):
		# We are logged in and ready to chat and use commands...
		print(f'Logged in as | {self.nick}')

	async def event_join(self, user, potato):
		print('User joined: ' + str(potato.name))

#	@bot.event
	async def event_message(self, message):
		try:
			print('[' + str(datetime.now()) + '][' + str(message.author.name) + '] ' + (message.content))
		except:
			pass

		# If you override event_message you will need to handle_commands for commands to work.
		try:
			await bot.handle_commands(message)
		except:
			pass

	@commands.command(name='test', aliases=['t'])
	async def test_command(self, ctx):
		await ctx.send(f'Hello {ctx.author.name}')

	@commands.command(name='help', aliases=['h'])
	async def help_command(self, ctx):
		await ctx.send(f'{ctx.author.name} Get a full list of commands at https://github.com/justcallmekoko/PythonTwitchBot')

	@commands.command(name='discord', aliases=['d'])
	async def discord_command(self, ctx):
		await ctx.send(f'{ctx.author.name} Come be a part of the community on discord https://discord.com/servers/willstunforfood-776211399918878760')

	@commands.command(name='socials', aliases=['s'])
	async def socials_command(self, ctx):
		await ctx.send(f'YouTube: https://www.youtube.com/justcallmekoko')
		await ctx.send(f'Instagram: https://www.instagram.com/just.call.me.koko')
		await ctx.send(f'Twitter: https://twitter.com/jcmkyoutube')
		await ctx.send(f'TikTok: https://www.tiktok.com/@just.call.me.koko')
		await ctx.send(f'Patreon: https://www.patreon.com/justcallmekoko')

bot = Bot()
bot.run()
