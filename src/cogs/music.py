import discord
import requests
import os
import lavalink
from discord.ext import commands
from discord import utils, Embed

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        
        if not hasattr(bot, 'lavalink'):
            self.bot.music = lavalink.Client(self.bot.user.id)
            self.bot.music.add_node('localhost', 8080, 'pass', 'na', 'music-node')
            self.bot.add_listener(self.bot.music.voice_update_handler, 'on_socket_response')
            
        self.bot.music.add_event_hook(self.track_hook)
    
    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            guild_id = int(event.player.guild_id)
            await self.connect_to(guild_id, None)
      
    async def connect_to(self, guild_id: int, channel_id: str):
        ws = self.bot._connection._get_websocket(guild_id)
        await ws.voice_state(str(guild_id), channel_id)

    @commands.command(pass_context=True)
    async def join(self, ctx):
        print('test successful')
        # if not ctx.author.voice:
        #     await ctx.send("{} is not connected to a voice channel.".format(ctx.author.name))
        #     return
        # else:
        #     channel = ctx.author.voice.channel
        # await channel.connect()

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command(pass_context=True)
    async def play(self, ctx, url):
        string = 'adsfkndsf'

def setup(bot):
    bot.add_cog(Music(bot))