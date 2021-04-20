"""Alice Discord Bot."""

from alice.client import AliceClient
import os

client = AliceClient()
client.run(os.environ.get("ALICE_BOT_KEY"))
