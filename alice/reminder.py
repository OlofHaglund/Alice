"""Container for the reminder loop."""
import logging
import json
import time

from queue import PriorityQueue
from discord.ext import tasks

class Reminder:
    """Container class for the reminder loop."""
    client = None
    queue = PriorityQueue()
    json_storage_location = "/var/lib/alice/data"

    @classmethod
    @tasks.loop(seconds=1)
    async def check_reminders(cls):
        """Loops once every second to check for reminders to send out."""
        if not cls.queue.empty():
            if cls.queue.queue[0][0] < time.time():
                item = cls.queue.get()
                channel = cls.client.get_channel(item[2])
                message = await channel.fetch_message(item[1])
                await message.reply('Here is your reminder! Want some tea with that?')
                cls.queue.task_done()
                await cls.save()

    @classmethod
    async def save(cls):
        """Save the queue to disk."""

        with open(cls.json_storage_location, 'w') as file:
            file.write(json.dumps(cls.queue.queue))

    @classmethod
    def load(cls):
        """Load the queue from the disk."""
        try:
            with open(cls.json_storage_location, 'r') as file:
                # check if file is empty
                file.seek(0)
                first_char = file.read(1)
                file.seek(0)
                if not first_char: # Empty file
                    logging.info("No data file to load")
                    return

                json_data = file.read()
                data = json.loads(json_data)
                for i in data:
                    cls.queue.put(i)
        except IOError:
            logging.info("File not accessible")
