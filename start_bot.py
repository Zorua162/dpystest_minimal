"""
The startup file for UrmwBot
Creates the initial bot and runs
In addition sets up logging
"""
import asyncio
import os
import logging
from logging.handlers import RotatingFileHandler

from bot import Bot

# Sets up the logging level, INFO sometimes spammy using WARN if less info wanted in console
# logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

# Using a rotating file handler so that the log file won't be massive in the future
log = logging.getLogger()
log.setLevel(logging.DEBUG)

logging.getLogger('discord').setLevel(logging.INFO)
logging.getLogger('discord.http').setLevel(logging.WARNING)

# Create the logs folder if it doesn't already exist
if not os.path.exists('logs'):
    os.makedirs('logs')

file_handler = RotatingFileHandler("./logs/bot.log", mode='a', maxBytes=5*1024*1024,
                                   backupCount=2)
file_handler.setLevel(logging.DEBUG)

dt_fmt = '%Y-%m-%d %H:%M:%S'
fmt = logging.Formatter('[{asctime}] [{levelname:<7}] {name}: {message}', dt_fmt, style='{')
file_handler.setFormatter(fmt)
log.addHandler(file_handler)

# Setup logging to the console aswell for quick live debugging
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(fmt)
log.addHandler(stream_handler)
# Also want to log to console so add a stream handler too
event_loop = asyncio.get_event_loop()


def startup_bot():
    """
    Runs the startup of the Bot class, init handles the rest of the setup
    """
    bot = Bot(event_loop)
    # Simple gross way to add a command for testing
    @bot.command()
    async def ping(ctx):
        await ctx.send("pong!")
    bot.run()


if __name__ == "__main__":
    # Starts the whole thing going.
    # print("Discord bot loading")
    logging.getLogger("Bot").info("Discord bot loading")
    startup_bot()
