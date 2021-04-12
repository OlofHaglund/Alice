"""Methods connect to the /remindme command"""
import re
import time

from alice.reminder import Reminder

def parse_time(message_string):
    """Parse the message for how many seconds to wait before reminding.

    Keyword arguements:
    message_string -- string to parse to seconds
    """
    match = re.match(r'([0-9]+)([sSmMhH])', message_string)
    if match[2].lower() == 'm':
        return int(match[1]) * 60
    if match[2].lower() == 'h':
        return int(match[1]) * 60 * 60
    return int(match[1])

async def reply(message):
    """Reply to use that their value had been accepted."""
    try:
        time_string = message.content.removeprefix('/remindme').strip()
        time_seconds = parse_time(time_string)
        Reminder.queue.put((time.time() + time_seconds, message))
        await message.reply(f'I will remind you in {time_string}')
    except Exception as e: # pylint: disable=W0703,C0103
        print(e)
        #TODO: respond with a help message
        await message.reply('I could not parse the value of /remindme')
