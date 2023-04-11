"""Testing"""
import pytest
import discord.ext.test as dpytest


@pytest.mark.asyncio
async def test_ping(bot):
    """Test if the ping command works"""
    await dpytest.message("?ping")
    # assert dpytest.verify().message().contains().content("pong")
    assert dpytest.get_message().content == "pong"


@pytest.mark.asyncio
async def test_create_channel(bot):
    """Test if running a command on the bot can get a channel and send a message"""
    await dpytest.message("?create_channel")
    assert dpytest.verify().message().contains().content("got_channel")


@pytest.mark.asyncio
async def test_dc_utils_get(bot):
    """Test if running a command on the bot can get a channel and send a message"""
    await dpytest.message("?get_channel")
    assert dpytest.verify().message().contains().content("got_channel")


@pytest.mark.asyncio
async def test_setup_hook_was_called(bot):
    """Test if running a command on the bot can get a channel and send a message"""
    await dpytest.message("?get_channel")
    channel_names = [channel.name for channel in bot.guilds[0].channels]
    assert "setup_hook_channel" in channel_names
    assert dpytest.verify().message().contains().content("got_channel")


@pytest.mark.asyncio
async def test_channel_history_flatten(bot):
    """Test if running a command on the bot can get a channel and send a message"""
    print(bot.guilds)
    await dpytest.message("?get_channel_history")
    assert dpytest.verify().message().contains().content("got_channel")


@pytest.mark.asyncio
async def test_channel_history_simple(bot):
    """Test if running a command on the bot can get a channel and send a message"""
    print(bot.guilds)
    channel = bot.guilds[0].channels[0]
    await channel.send("test")
    assert len([msg async for msg in channel.history(limit=10)]) == 1


# @pytest.mark.asyncio
# async def test_send_command(bot):
# async def run_command(bot, command):
#     """Runs the given command"""
#     guild = bot.guilds[0]
#     member1 = guild.members[0]
#     await dpytest.message(f"!{command}", guild.channels[1], member1)
#
#
# @pytest.mark.asyncio
# async def test_ping_2(bot):
#     """Test if the ping command works"""
#     await run_command(bot, "ping")
#     assert "ms" in dpytest.get_message(peek=True).content
#
