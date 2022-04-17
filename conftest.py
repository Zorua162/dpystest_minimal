"""Minimal conftest"""
import glob
import os
import discord.ext.test as dpytest
import pytest
from discord.ext import commands
import discord


@pytest.fixture
def bot(event_loop):
    """Create the bot test environment to use with every test"""
    bot = commands.Bot(
        command_prefix="!", event_loop=event_loop, intents=discord.Intents.all()
    )
    bot.add_command(ping)
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
