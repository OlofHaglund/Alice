"""Alice Discord Bot."""
import logging
import os
from alice.client import AliceClient

logging.basicConfig(level=logging.INFO)

client = AliceClient()
client.run(os.environ.get("ALICE_BOT_KEY"))
