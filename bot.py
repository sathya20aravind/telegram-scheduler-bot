import os
from telethon import TelegramClient
import time
from datetime import datetime

# Use environment variables for API credentials
api_id = os.getenv('23223277')
api_hash = os.getenv('dde3c4460bf46f0d41c43011423c2be4')
receiver = os.getenv('721639032')  # Chat ID instead of username

# Debugging: Print the values to check if they are being loaded correctly
print(f"API_ID: {api_id}")
print(f"API_HASH: {api_hash}")

message_1 = 'Good Morning my love! Mathara podu d chellam 💖'
message_2 = 'Good Night my love! Mathara podu d chellam 🌙'

client = TelegramClient('session_name', api_id, api_hash)

async def send_message():
    current_time = datetime.now()
    if current_time.hour == 8 and current_time.minute == 0:  # 8:00 AM
        await client.send_message(receiver, message_1)
    if current_time.hour == 20 and current_time.minute == 30:  # 8:30 PM
        await client.send_message(receiver, message_2)

async def main():
    await client.start()  
    while True:
        await send_message()  
        time.sleep(60)  # Check every minute

with client:
    client.loop.run_until_complete(main())
