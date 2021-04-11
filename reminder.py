"""Container for the reminder loop."""
import time

from queue import PriorityQueue
from discord.ext import tasks

class Reminder:
    """Container class for the reminder loop."""
    queue = PriorityQueue()

    @classmethod
    @tasks.loop(seconds=1)
    async def check_reminders(cls):
        """Loops once every second to check for reminders to send out."""
        # TODO: Create a pritory queue class with a peek function
        if not cls.queue.empty():
            item = cls.queue.get()
            if item[0] < time.time():
                await item[1].reply('Here is your reminder! Want some tea with that?')
                cls.queue.task_done()
            else:
                Reminder.queue.put(item)
