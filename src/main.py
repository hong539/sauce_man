import discord
from discord import app_commands
import yaml
# import traceback

# The guild in which this slash command will be registered.
# It is recommended to have a test guild to separate from your "production" bot
# TEST_GUILD = discord.Object(0)
# print(TEST_GUILD)

class MyClient(discord.Client):
    def __init__(self) -> None:
        # Just default intents and a `discord.Client` instance
        # We don't need a `commands.Bot` instance because we are not
        # creating text-based commands.
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

        # We need an `discord.app_commands.CommandTree` instance
        # to register application commands (slash commands in this case)
        self.tree = app_commands.CommandTree(self)

    def load_config(self, path):
        """Load configuration data from a YAML file.

        Args:
            path (str): The path to the YAML configuration file.
        """
        with open(path, "r") as config:
            self.config_data = yaml.safe_load(config)
            print("config_data type is:", type(self.config_data))
            print("bot token is:\n", self.config_data["bot"]["token"])
        return self.config_data
    
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        print(f'Message from {message.channel}:{message.author}: {message.content}')
        
        if message.author == client.user:
            return
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')
    
    # async def setup_hook(self) -> None:
    #     # Sync the application command with Discord.
    #     await self.tree.sync(guild=TEST_GUILD)


# class Feedback(discord.ui.Modal, title='Feedback'):
#     # Our modal classes MUST subclass `discord.ui.Modal`,
#     # but the title can be whatever you want.

#     # This will be a short input, where the user can enter their name
#     # It will also have a placeholder, as denoted by the `placeholder` kwarg.
#     # By default, it is required and is a short-style input which is exactly
#     # what we want.
#     name = discord.ui.TextInput(
#         label='Name',
#         placeholder='Your name here...',
#     )

#     # This is a longer, paragraph style input, where user can submit feedback
#     # Unlike the name, it is not required. If filled out, however, it will
#     # only accept a maximum of 300 characters, as denoted by the
#     # `max_length=300` kwarg.
#     feedback = discord.ui.TextInput(
#         label='What do you think of this new feature?',
#         style=discord.TextStyle.long,
#         placeholder='Type your feedback here...',
#         required=False,
#         max_length=300,
#     )

#     async def on_submit(self, interaction: discord.Interaction):
#         await interaction.response.send_message(f'Thanks for your feedback, {self.name.value}!', ephemeral=True)

#     async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
#         await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

#         # Make sure we know what the error actually is
#         traceback.print_exception(type(error), error, error.__traceback__)


# client = MyClient()


# @client.tree.command(guild=TEST_GUILD, description="Submit feedback")
# async def feedback(interaction: discord.Interaction):
#     # Send the modal with an instance of our `Feedback` class
#     # Since modals require an interaction, they cannot be done as a response to a text command.
#     # They can only be done as a response to either an application command or a button press.
#     await interaction.response.send_modal(Feedback())


# client.run(token= client.load_config("./my_self.yaml")["bot"]["token"])

if __name__ == "__main__":
    client = MyClient()
    client.run(token= client.load_config("./my_self.yaml")["bot"]["token"])