"""Methods connect to the /remindme at command"""
import logging
import time

from dateutil.parser import parse

from alice.reminder import Reminder

async def reply(message):
    """Reply to use that their value had been accepted."""
    print("message", message)
    try:
        time_string = message.content.removeprefix('/remindme at').strip()
        date_time = parse(time_string)
        Reminder.queue.put(
            [
                date_time.timestamp(),
                message.id,
                message.channel.id
            ]
        )
        await Reminder.save()
        await message.reply(f'I will remind you at {time_string}')
    except Exception as e: # pylint: disable=W0703,C0103
        logging.debug(f"Couldn't parse remindme message: {message.content} e: {e}")
        await message.reply(help_string())


def help_string(short = False):
    """Print the help message for /remindme

    Arguments:
    short - If you want the short string or the long string. Boolean default to False
"""

    short_string = '`/remindme at YYYY-mm-dd hh:mm:ss`'

    if short:
        return short_string

    return f"""Valid formats for {short_string}
```
/remindme at 2021-08-19
/remindme at 2021-08-19 18:32
/remindme at 2021-08-19 18:32:50
```
"""
