from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
MESSAGE = os.getenv("MESSAGE")

bot = Bot(token=BOT_TOKEN)
scheduler = BlockingScheduler()

def send_message():
    bot.send_message(chat_id=CHAT_ID, text=MESSAGE)

# Schedule the job for Morning 8:00 AM
scheduler.add_job(send_message, 'cron', hour=8, minute=0)

# Schedule the job for Night 8:30 PM
scheduler.add_job(send_message, 'cron', hour=20, minute=30)

if __name__ == "__main__":
    print("Bot is running...")
    scheduler.start()
