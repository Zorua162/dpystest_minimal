"""
The main Urmw bot class
"""
# import sys
# import traceback
import logging

import discord as dc
from discord.ext import commands
from decouple import config


class Bot(commands.Bot):
    """Discord bot"""

    def __init__(self, event_loop):
        """ Init the bot"""

        # Shortening the reference space for accessing the event loop
        self.loop = event_loop
        self.logger = logging.getLogger('Bot')

        # A mapping of guild ids to guild-specific data structures,

        # The bot token and challonge api key
        intents = dc.Intents.default()
        intents.members = True
        intents.message_content = True
        intents.presences = True

        super().__init__('?', event_loop=event_loop, intents=intents, help_command=None)

    def run(self):
        """
        Called from the startup file
        """
        # Old way of starting bot, abstracts away event loop which is needed for testing
        super().run(config("BOT_TOKEN"))

    async def setup_hook(self):
        for guild in self.guilds:
            await guild.create_text_channel("setup_hook_channel")
        channel = dc.utils.get(guild.channels, name="setup_hook_channel")
        await channel.send("Message from setup hook")
