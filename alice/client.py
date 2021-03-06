"""Alice bot client"""
import logging
import discord

from alice.commands import help_message, remindme, remindmeat
from alice.reminder import Reminder

class AliceClient(discord.Client):
    """The Discord bot."""

    def __init__(self):
        """Initilaze Discord bot.
        """
        super().__init__()

    async def on_ready(self):
        """When the bot has logged into discord."""
        logging.info(f'Logged in as {self.user}')
        Reminder.client = self
        Reminder.load()
        Reminder.check_reminders.start() # pylint: disable=E1101

    async def on_message(self, message):
        """A message is written in any of channels the bot is invited to."""

        if message.content.startswith('/remindme at'):
            await remindmeat.reply(message)

        elif message.content.startswith('/remindme'):
            await remindme.reply(message)

        elif message.content.startswith('/help'):
            await help_message.reply(message)
