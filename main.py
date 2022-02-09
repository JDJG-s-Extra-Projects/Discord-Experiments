import discord
from discord.ext import commands
import traceback

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("$"),
            intents=discord.Intents(guilds=True, messages=True),
            slash_commands=True,
        )

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")


bot = Bot()

@bot.event
async def on_error(event, *args, **kwargs):
 
  traceback.print_exc()

@bot.command(message_command=False)
async def file(ctx, file : discord.Attachment):

    file = await file.to_file(use_cached=False)
    await ctx.send(f"got your file {ctx.author}", file = file)

bot.run("TOKEN")
