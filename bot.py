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

# Schedule the job daily at 9:00 AM (adjust as needed)
scheduler.add_job(send_message, 'cron', hour=9, minute=0)

if __name__ == "__main__":
    print("Bot is running...")
    scheduler.start()
