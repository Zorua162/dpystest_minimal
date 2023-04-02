"""Testing"""
import pytest
import discord.ext.test as dpytest


@pytest.mark.asyncio
async def test_ping(bot):
    """Test if the ping command works"""
    await dpytest.message("?ping")
    assert dpytest.verify().message().contains().content("pong")
