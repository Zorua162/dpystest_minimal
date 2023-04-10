"""Minimal conftest"""
import glob
import os
import discord.ext.test as dpytest
import pytest # noqa
from discord.ext import commands
import discord as dc
import pytest_asyncio
from bot import Bot
from discord.client import _LoopSentinel


@pytest_asyncio.fixture
async def bot(event_loop):
    """Initialise bot to be able to run tests on it"""
    # Create the bot, similar to how it is done in start_bot
    bot = Bot(event_loop)
    bot.add_command(ping)
    bot.add_command(create_channel)
    bot.add_command(get_channel)

    if isinstance(bot.loop, _LoopSentinel):
        await bot._async_setup_hook()

    # Configure the bot to be in a test environment (similar to bot.run)
    dpytest.configure(bot)
    await bot.setup_hook()
    assert dpytest.get_message().content == "msg"

    return bot


@commands.command()
async def ping(ctx):
    """Send message to a channel where !ping was called"""
    await ctx.send("pong")


@commands.command()
async def create_channel(ctx):
    """Send message to a channel where !ping was called"""
    await ctx.guild.create_text_channel("test_channel")
    channel_names = [channel.name for channel in ctx.guild.channels]
    if "test_channel" in channel_names:
        await ctx.send("got_channel")
    else:
        await ctx.send("fail the test")


@commands.command()
async def get_channel(ctx):
    """Send message to a channel where !ping was called"""
    await ctx.guild.create_text_channel("test_channel")
    # channel = dc.utils.get(ctx.guild.channels, name="test_channel", type=dc.ChannelType.text)
    channel = dc.utils.get(ctx.guild.channels, name="test_channel")  # , type=dc.ChannelType.text)
    if channel is not None:
        await ctx.send("got_channel")
    else:
        await ctx.send("fail the test")


def pytest_sessionfinish():
    """Clean up files"""
    files = glob.glob('./dpytest_*.dat')
    for path in files:
        try:
            os.remove(path)
        except Exception as e:
            print(f"Error while deleting file {path}: {e}")
