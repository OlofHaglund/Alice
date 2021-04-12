"""Alice Discord Bot."""

import os
import discord

from alice.commands import help_message, remindme
from alice.reminder import Reminder


class AliceClient(discord.Client):
    """The Discord bot."""

    def __init__(self):
        """Initilaze Discord bot.
        """
        super().__init__()

    async def on_ready(self):
        """When the bot has logged into discord."""
        print('Logged on as', self.user)
        Reminder.check_reminders.start() # pylint: disable=E1101

    async def on_message(self, message):
        """A message is written in any of channels the bot is invited to."""
        if message.content.startswith('/remindme'):
            await remindme.reply(message)

        if message.content.startswith('/help'):
            await help_message.reply(message)

def run():
    client = AliceClient()
    client.run(os.environ.get("ALICE_BOT_KEY"))

if __name__ == "__main__":
    run()
