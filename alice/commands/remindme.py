"""Methods connect to the /remindme command"""
import logging
import time

from pytimeparse.timeparse import timeparse

from alice.reminder import Reminder

async def reply(message):
    """Reply to use that their value had been accepted."""
    try:
        time_string = message.content.removeprefix('/remindme').strip()
        print(time_string)
        time_seconds = timeparse(time_string)
        Reminder.queue.put(
            [
                time.time() + time_seconds,
                message.id,
                message.channel.id
            ]
        )
        await Reminder.save()
        await message.reply(f'I will remind you in {time_string}')
    except Exception as e: # pylint: disable=W0703,C0103
        logging.debug(f"Couldn't parse remindme message: {message.content} e: {e}")
        await message.reply(help_string())


def help_string(short = False):
    """Print the help message for /remindme

    Arguments:
    short - If you want the short string or the long string. Boolean default to False
"""

    short_string = '`/remindme 1w 2d 3h 4m 5s`'

    if short:
        return short_string

    return f"""Valid formats for {short_string}
```
/remindme 5s
/remindme 5 sec
/remindme 5 seconds
/remindme 3m
/remindme 3.3m
/remindme 3 min
/remindme 1 minute
/remindme 3 minutes
/remindme 2h
/remindme 2hr
/remindme 2 hours
/remindme 6d
/remindme 6 days
/remindme 1w
/remindme 1wk
/remindme 1 week
/remindme 2 weeks

/remindme 1w 2d 3h 4m 5s
```
"""
