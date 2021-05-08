"""Methods connect to the /remindme command"""
import logging
import time

from pytimeparse.timeparse import timeparse

from alice.reminder import Reminder

async def reply(message):
    """Reply to use that their value had been accepted."""
    try:
        time_string = message.content.removeprefix('/remindme').strip()
        time_seconds = timeparse(time_string)
        Reminder.queue.put(
            (time.time() + time_seconds,
            message.id,
            message.channel.id)
        )
        await Reminder.save()
        await message.reply(f'I will remind you in {time_string}')
    except Exception as e: # pylint: disable=W0703,C0103
        # TODO: respond with a help message
        logging.debug(f"couldn't parse remindme message: {message} e: {e}")
        await message.reply('I could not parse the value of /remindme')
