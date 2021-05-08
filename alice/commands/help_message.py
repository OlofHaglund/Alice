"""Methods connected to the /help command"""

from alice.commands import remindme

async def reply(message):
    """Sends private message to the caller"""
    response = f'''
Hi, I'm Alice I can do the following:
Remind you after a specific duration
{remindme.help_string(True)}

{remindme.help_string()}
'''

    await message.author.send(response)
    await message.add_reaction('\U0001F44D') #👍
