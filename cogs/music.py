import discord
from discord.ext import commands
import lavalink
import re

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
        #  This is essentially the same as `@commands.guild_only()`
        #  except it saves us repeating ourselves (and also a few lines).

        if guild_check:
            await self.ensure_voice(ctx)
            #  Ensure that the client and command author share a mutual voicechannel.

        return guild_check

    async def ensure_voice(self, ctx):
        """ This check ensures that the client and command author are in the same voicechannel. """
        player = self.client.lavalink.player_manager.create(ctx.guild.id, endpoint=str(ctx.guild.region))

        should_connect = ctx.command.name in ('play',)

        if not ctx.author.voice or not ctx.author.voice.channel:
            return await ctx.send(f"{ctx.author.mention} Join a VoiceChannel first!")

        if not player.is_connected:
            if not should_connect:
                return await ctx.send('Not connected.')

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

    @commands.command()
    async def play(self, ctx, *, query: str):
        """ Plays music as per query"""
        player = self.client.lavalink.player_manager.get(ctx.guild.id)

        query = query.strip("<>")

        if not url_rx.match(query):
            query = f"ytsearch:{query}"

        results = await player.node.get_tracks(query)

        if not results or not results["tracks"]:
            return await ctx.send(f"{ctx.author.mention} nothing Found!")

        if results["loadType"] == "PLAYLIST_LOADED":
            print(results)

            tracks = results["tracks"]

            for track in tracks:
                player.add(requester=ctx.author.id, track=track)

            playlist = discord.Embed(color=discord.Color.light_grey())
            playlist.set_author(name="Playlist loaded!")
            playlist.description = f"\n Name - {results['playlistInfo']['name']} \n"
            playlist.description += f"\n Url - <{query}> \n"
            playlist.set_footer(text=f"Requested by - {ctx.author}")

            await ctx.send(embed=playlist)

        elif results["loadType"] == "TRACK_LOADED":

            track = results["tracks"][0]

            player.add(requester=ctx.author.id, track=track)

            single_url = discord.Embed(color=discord.Color.light_grey())
            single_url.set_author(name=f"Video loaded!")
            single_url.description = f"\n Name - {track['info']['title']} \n"
            single_url.description += f"\n By - {track['info']['author']} \n"
            single_url.description += f"\n Url - <{track['info']['uri']}> \n"
            single_url.set_footer(text=f"Requested by - {ctx.author}")

            await ctx.send(embed=single_url)

        if not player.is_playing:
            await player.play()

    @commands.command(aliases=['dc'])
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


def setup(client):
    client.add_cog(Music(client))
