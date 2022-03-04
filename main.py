import discord
from discord.ext import commands
import traceback
import os
import dotenv
from discord.ui import Modal, TextInput

# Defines a custom Modal with questions
# that user has to answer. The callback function
# of this class is called when the user submits the modal


class Modal(Modal):
    def __init__(self) -> None:
        super().__init__("AddBot:")

        # Set the questions that will be shown in the modal
        # The placeholder is what will be shown when nothing is typed
        #self.add_item(TextInput(label="What reason do you have to add your bot?"))

        # Provide value argument to prefill the input
        # The style parameter allows you to set the style of the input
        # You can choose from short and long
        self.add_item(
            TextInput(
                label="Your Reason for Adding the bot is?:",
                value="",
                style=discord.TextInputStyle.long,
            )
        )

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's name or choice. The self object refers to the
        # Modal object, and the values attribute gets a list of the user's
        # answers. We only want the first one.
        await interaction.response.send_message(
            f"Sent Reason: {self.children[0].value} to my boss."
        )


class ModalView(discord.ui.View):
    @discord.ui.button(label="Open Modal", style=discord.ButtonStyle.green)
    async def open_modal(self, button: discord.Button, interaction: discord.Interaction):
        # Create the modal
        modal = Modal()

        # Sending a message containing our modal
        await interaction.response.send_modal(modal)


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


@bot.command()
async def form(ctx: commands.Context):
    """Sends a message with our modal"""

    # Create the view containing our modal
    view = ModalView()
    # Sending a message containing our view
    await ctx.send("Click to open modal:", view=view)


# Can also be used from slash commands directly
@bot.command(message_command=False)
async def modal(ctx: commands.Context):
    # Create the modal
    modal = Modal()

    # Sending our modal
    await ctx.interaction.response.send_modal(modal)

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

dotenv.load_dotenv()
bot.run(os.environ["TOKEN"])