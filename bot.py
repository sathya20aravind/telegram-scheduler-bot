import os
from telethon import TelegramClient
import time
from datetime import datetime

# Retrieve API credentials from environment variables
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
receiver = os.getenv('RECEIVER_CHAT_ID')

message_1 = 'Good Morning my love! Mathara podu d chellam 💖'
message_2 = 'Good Night my love! Mathara podu d chellam 🌙'

# Create the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

async def send_message():
    current_time = datetime.now()
    if current_time.hour == 8 and current_time.minute == 0:  # 8:00 AM
        await client.send_message(receiver, message_1)
    if current_time.hour == 20 and current_time.minute == 30:  # 8:30 PM
        await client.send_message(receiver, message_2)

async def main():
    # Start the client, this will ask for OTP if it's the first time
    await client.start()
    while True:
        await send_message()
        time.sleep(60)  # Check every minute

with client:
    client.loop.run_until_complete(main())
