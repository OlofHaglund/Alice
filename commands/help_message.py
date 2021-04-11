"""Methods connected to the /help command"""
async def reply(message):
    """Sends private message to the caller"""
    response = '''
    Hi, I'm Alice I can do the following:
    I can set a reminder for you by using the following command:
    ```
    /remindme [int][s/m/h]
    /remindme 10s
    ```
'''

    await message.author.send(response)
    await message.add_reaction('\U0001F44D') #👍
