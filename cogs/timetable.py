import discord
from discord.ext import commands, tasks
import datetime


class TimeTable(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.week_days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")

    @commands.Cog.listener()
    async def on_ready(self):
        self.check.start()

    @tasks.loop(minutes=1)
    async def check(self):
        current_time = datetime.datetime.utcnow()
        week_days = self.week_days
        time = datetime.datetime.strftime(current_time, "%H %M")
        day = week_days[datetime.datetime.weekday(current_time)]
        records = await self.client.db.check_todays_time_table(day, time)
        if records:
            for record in records:
                user_id = record["user_id"]
                work = record["work"]
                user = await self.client.fetch_user(user_id)
                await user.send(f"Time for - {work}")

    @commands.group(invoke_without_command=True, aliases=["tt"])
    async def time_table(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"{ctx.author.mention} please specify a Task :)", delete_after=10)

    @time_table.command()
    async def insert(self, ctx, day: str, time: str, *, text: str):
        async with ctx.channel.typing():
            await ctx.message.delete()
            day = day.lower()
            valid_time = " ".join(t for t in time.split(":"))
            work = await commands.clean_content().convert(ctx=ctx, argument=text)
            week_days = self.week_days
            open_dms = False
            user_id = ctx.author.id
            if day not in week_days:
                await ctx.send(f"{ctx.author.mention} please Specify a valid day, eg - Monday", delete_after=10)
                return
            if time.count(":") < 1:
                await ctx.send(f"{ctx.author.mention} please a valid time, eg - 10:10", delete_after=10)
                return
            try:
                await ctx.author.send(f"Time set for - {' '.join([day.title(), valid_time, work])}")
                open_dms = True
            except discord.Forbidden:
                await ctx.send(
                    "You cant use this because I need to DM you :), please change your Privacy settings to use this Command!", delete_after=10)
                open_dms = False
                await ctx.message.delete()
            if open_dms:
                await ctx.message.delete()
                await self.client.db.insert_time_table(day, user_id, valid_time, work)

    @time_table.command()
    async def delete(self, ctx, day: str, time: str):
        async with ctx.channel.typing():
            await ctx.message.delete()
            day = day.lower()
            valid_time = " ".join(t for t in time.split(":"))
            week_days = self.week_days
            user_id = ctx.author.id
            if day not in week_days:
                await ctx.send(f"{ctx.author.mention} please Specify a valid day, eg - Monday", delete_after=10)
                return
            if time.count(":") < 1:
                await ctx.send(f"{ctx.author.mention} please a valid time, eg - 10:10", delete_after=10)
                return
            records = await self.client.db.check_if_in_time_table(day, user_id, valid_time)
            if not records:
                await ctx.send(f"Task not Found :(")
                return
            else:
                await self.client.db.delete_from_time_table(day, user_id, valid_time)
                await ctx.send(f"Task Deleted successfully!")

    @time_table.command()
    async def all(self, ctx):
        async with ctx.channel.typing():
            user_id = ctx.author.id
            query = await self.client.db.select_all_from_time_table(user_id)
            if not query:
                await ctx.message.delete()
                await ctx.send(f"{ctx.author.mention} you dont have a schedule yet", delete_after=10)
                return

            records = []

            for record in query:
                schedule = f"Day - {str(record['day']).title()}, Time - {record['time']}, Work - {record['work']}"
                records.append(schedule)

            records = sorted(records, reverse=True)
            pager = commands.Paginator()

            for record in records:
                pager.add_line(record)

            for page in pager.pages:
                try:
                    await ctx.author.send(page)
                except discord.Forbidden:
                    await ctx.send(f"{ctx.author.mention} cant DM you!")


def setup(client):
    client.add_cog(TimeTable(client))
