from telethon import TelegramClient
import time
from datetime import datetime

# Replace these with your own API credentials
api_id = '23223277'
api_hash = 'YOUR_API_HASH'

# Create the client
client = TelegramClient('session_name', api_id, api_hash)

# The recipient's username or chat ID
receiver = '721639032'

# Your message content
message_1 = 'Good Morning my love! Mathara podu d chellam 💖'
message_2 = 'Good Night my love! Mathara podu d chellam 🌙'

# Function to send messages
async def send_message():
    # Send the "Good Morning" message at a specific time
    current_time = datetime.now()
    if current_time.hour == 8 and current_time.minute == 0:  # 8:00 AM
        await client.send_message(receiver, message_1)
    
    # Send the "Good Night" message at a specific time
    if current_time.hour == 20:30 and current_time.minute == 0:  # 08:30 PM
        await client.send_message(receiver, message_2)

# Main function to start the client and run the loop
async def main():
    await client.start()  # This will ask OTP once if not already logged in

    while True:
        await send_message()  # Call the send_message function to check and send
        time.sleep(60)  # Check every minute to match the scheduled times

# Run the script
with client:
    client.loop.run_until_complete(main())
