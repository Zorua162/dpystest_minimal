"""Minimal conftest"""
import glob
import os
import discord.ext.test as dpytest
import pytest
from discord.ext import commands
import discord
import pytest_asyncio
from bot import Bot
from discord.client import _LoopSentinel

@pytest_asyncio.fixture
async def bot(event_loop):
    """Initialise bot to be able to run tests on it"""
    # Create the bot, similar to how it is done in start_bot
    bot = Bot(event_loop)
    bot.add_command(ping)

    if isinstance(bot.loop, _LoopSentinel):
        await bot._async_setup_hook()

    # Configure the bot to be in a test environment (similar to bot.run)
    dpytest.configure(bot)
    return bot


@commands.command()
async def ping(ctx):
    """Send message to a channel where !ping was called"""
    await ctx.send("pong")


def pytest_sessionfinish():
    """Clean up files"""
    files = glob.glob('./dpytest_*.dat')
    for path in files:
        try:
            os.remove(path)
        except Exception as e:
            print(f"Error while deleting file {path}: {e}")
