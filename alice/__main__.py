"""Alice Discord Bot."""

import os
from alice.client import AliceClient

client = AliceClient()
client.run(os.environ.get("ALICE_BOT_KEY"))
