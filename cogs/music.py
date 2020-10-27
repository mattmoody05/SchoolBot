# discord imports
import discord
from discord.ext import commands

# other imports
import lavalink
import re
import aiohttp
import img


url_rx = re.compile(r'https?://(?:www\.)?.+')


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

        if not hasattr(client, 'lavalink'):  # This ensures the client isn't overwritten during cog reloads.
            client.lavalink = lavalink.Client(client.user.id)
            client.lavalink.add_node('127.0.0.1', 2333, 'password', 'eu', 'default-node')  # Host, Port, Password, Region, Name
            client.add_listener(client.lavalink.voice_update_handler, 'on_socket_response')

        lavalink.add_event_hook(self.track_hook)

    def cog_unload(self):
        """ Cog unload handler. This removes any event hooks that were registered. """
        self.client.lavalink._event_hooks.clear()

    async def cog_before_invoke(self, ctx):
        """ Command before-invoke handler. """
        guild_check = ctx.guild is not None

        if guild_check:
            await self.ensure_voice(ctx)

        return guild_check

    async def ensure_voice(self, ctx):
        """ This check ensures that the client and command author are in the same voicechannel. """
        player = self.client.lavalink.player_manager.create(ctx.guild.id, endpoint=str(ctx.guild.region))

        should_connect = ctx.command.name in ('play',)

        if not ctx.author.voice or not ctx.author.voice.channel:
            return await ctx.send(f"{ctx.author.mention} Join a VoiceChannel first!")

        if not player.is_connected:
            if not should_connect:
                return await ctx.send(f"{ctx.author.mention} Im not Connected!")

            permissions = ctx.author.voice.channel.permissions_for(ctx.me)

            if not permissions.connect or not permissions.speak:  # Check user limit too?
                return await ctx.send(f'{ctx.author.mention} I need the `CONNECT` and `SPEAK` permissions to play music')

            player.store('channel', ctx.channel.id)
            await self.connect_to(ctx.guild.id, str(ctx.author.voice.channel.id))
        else:
            if int(player.channel_id) != ctx.author.voice.channel.id:
                await self.connect_to(ctx.guild.id, str(ctx.author.voice.channel.id))

    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            guild_id = int(event.player.guild_id)
            await self.connect_to(guild_id, None)

    async def connect_to(self, guild_id: int, channel_id: str):
        """ Connects to the given voicechannel ID. A channel_id of `None` means disconnect. """
        ws = self.client._connection._get_websocket(guild_id)
        await ws.voice_state(str(guild_id), channel_id)

    @commands.group(invoke_without_command=True)
    async def music(self, ctx):
        await ctx.send(f"{ctx.author.mention} please specify a command!")

    @music.command()
    async def play(self, ctx, *, query: str):
        """ Plays music as per query"""
        player = self.client.lavalink.player_manager.get(ctx.guild.id)

        query = query.strip("<>")

        if not url_rx.match(query):
            url = f"https://www.youtube.com/results?search_query={query}"

            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    html = await response.text()

            pattern = r"\watch\?v=(\S{11})"
            fetch = re.findall(pattern, html)

            video_url = f"https://www.youtube.com/watch?v={fetch[0]}"

            return await self.play(ctx=ctx, query=video_url)

        results = await player.node.get_tracks(query)

        if results["loadType"] == "PLAYLIST_LOADED":

            tracks = results["tracks"]

            for track in tracks:
                player.add(requester=ctx.author.id, track=track)

            playlist = discord.Embed(color=discord.Color.light_grey())
            playlist.set_author(name="Playlist loaded!", icon_url = img.ImgMusic)
            playlist.description = f"\n Name - {results['playlistInfo']['name']} \n"
            playlist.description += f"\n Url - <{query}> \n"
            playlist.set_footer(text=f"Requested by - {ctx.author}")

            await ctx.send(embed=playlist)

        elif results["loadType"] == "TRACK_LOADED":

            track = results["tracks"][0]

            player.add(requester=ctx.author.id, track=track)

            single_url = discord.Embed(color=discord.Color.light_grey())
            single_url.set_author(name=f"Video loaded!", icon_url=img.ImgMusic)
            single_url.description = f"\n Name - {track['info']['title']} \n"
            single_url.description += f"\n By - {track['info']['author']} \n"
            single_url.description += f"\n Url - <{track['info']['uri']}> \n"
            single_url.set_footer(text=f"Requested by - {ctx.author}")

            await ctx.send(embed=single_url)

        elif results["loadType"] == "NO_MATCHES":
            await ctx.send(f"{ctx.author.mention} no results found!")

        if not player.is_playing:
            await player.play()

    @music.command(aliases=['dc'])
    async def disconnect(self, ctx):
        """ Disconnects the player from the voice channel and clears its queue. """
        player = self.client.lavalink.player_manager.get(ctx.guild.id)

        if not player.is_connected:
            return await ctx.send(f"{ctx.author.mention} Im not Connected!")

        if not ctx.author.voice or (player.is_connected and ctx.author.voice.channel.id != int(player.channel_id)):
            return await ctx.send(f"{ctx.author.mention} you are not in my voice Channel!")

        player.queue.clear()
        await player.stop()
        await self.connect_to(ctx.guild.id, None)
        await ctx.send(f"{ctx.author.mention} Disconnected Successfully!")

    @music.command()
    async def queue(self, ctx):
        """ Gives the queue of the songs """
        player = self.client.lavalink.player_manager.get(ctx.guild.id)
        queue = player.queue

        if not queue:
            return await ctx.send(f"{ctx.author.mention} No songs are in Queue!")

        async with ctx.channel.typing():
            pager = commands.Paginator()

            for song in queue:
                pager.add_line(song.title)

            for page in pager.pages:
                await ctx.send(page)
            return

    @music.command()
    async def current(self, ctx):
        """ Gives the current track playing """
        player = self.client.lavalink.player_manager.get(ctx.guild.id)
        current = player.current

        if not current:
            return await ctx.send(f"{ctx.author.mention} Nothing is currently Playing!")

        async with ctx.channel.typing():
            current_embed = discord.Embed(color=discord.Color.light_grey())
            current_embed.set_author(name="Current Song", icon_url = img.ImgMusic)
            current_embed.description = f"\nName - {current.title}\n"
            current_embed.description += f"\nUrl - {f'https://www.youtube.com/watch?v={current.identifier}'}\n"
            current_embed.set_footer(text=f"Requested by - {ctx.author}")
            return await ctx.send(embed=current_embed)

    @music.command()
    async def skip(self, ctx):
        """ Skips the current song """
        player = self.client.lavalink.player_manager.get(ctx.guild.id)

        await player.skip()
        await ctx.send(f"{ctx.author.mention} If there are no songs in the queue then the bot will quit")

    @music.command()
    async def pause(self, ctx):
        """ Pauses the current player """
        player = self.client.lavalink.player_manager.get(ctx.guild.id)
        state = player.paused

        if state:
            return await ctx.send(f"{ctx.author.mention} Player is already paused!")

        await player.set_pause(pause=True)

    @music.command()
    async def resume(self, ctx):
        """ Resumes the player """
        player = self.client.lavalink.player_manager.get(ctx.guild.id)
        state = player.paused

        if not state:
            return await ctx.send(f"{ctx.author.mention} player is already resumed!")

        await player.set_pause(pause=False)

    @music.command()
    async def volume(self, ctx, vol: int):
        """ Changes the volume of the player """
        if vol > 9999:
            return await ctx.send(f"{ctx.author.mention} please specify a volume lower than this")

        player = self.client.lavalink.player_manager.get(ctx.guild.id)
        volume = player.volume

        await player.set_volume(vol=vol)
        await ctx.send(f"{ctx.author.mention} Volume changed from {volume} to {vol}")


def setup(client):
    client.add_cog(Music(client))
