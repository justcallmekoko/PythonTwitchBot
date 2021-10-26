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

	@commands.command(name='test', aliases=['t'])
	async def test_command(self, ctx):
		await ctx.send(f'Hello {ctx.author.name}')

	@commands.command(name='help', aliases=['h'])
	async def help_command(self, ctx):
		await ctx.send(f'{ctx.author.name} Get a full list of commands at https://github.com/justcallmekoko/PythonTwitchBot')

	@commands.command(name='discord', aliases=['d'])
	async def discord_command(self, ctx):
		await ctx.send(f'{ctx.author.name} Come be a part of the community on discord https://discord.gg/invite/M2YWpfjAvM')

	@commands.command(name='socials', aliases=['s'])
	async def socials_command(self, ctx):
		await ctx.send(f'YouTube: https://www.youtube.com/justcallmekoko')
		await ctx.send(f'Instagram: https://www.instagram.com/just.call.me.koko')
		await ctx.send(f'Twitter: https://twitter.com/jcmkyoutube')

bot = Bot()
bot.run()
