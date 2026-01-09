"""Main module to monitor Telegram channel for job postings and send email alerts."""
import os
from telethon import TelegramClient, events
from dotenv import load_dotenv
from filters import is_relevant, contains_remote_option
from emailer import send_email

load_dotenv()

api_id = int(os.getenv("APP_ID"))
api_hash = os.getenv("API_HASH")
channel = os.getenv("TARGET_CHANNEL")

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=channel))
async def handler(event):
    """Handles new messages in the target channel."""
    text = event.message.text
    if not text:
        return

    # Check if the job posting is relevant and mentions remote options
    if is_relevant(text) and contains_remote_option(text):
        print("✅ MATCH FOUND")
        print(text)

        link = None
        if event.message.entities:
            for entity in event.message.entities:
                if hasattr(entity, "url"):
                    link = entity.url

            email_body = f"""
            New Job Alert 🚀

            {text}

            Link: {link if link else 'No link found'}
            """

            send_email(
            subject="New Developer / Data Job Found",
            content=email_body
            )

            print("📧 Email sent")
    else:
        print("❌ Job posted but no match")

async def main():
    """Main function to start the Telegram client."""
    await client.start()
    print("🤖 Listening to channel...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
