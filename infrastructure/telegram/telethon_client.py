from telethon import TelegramClient as TelethonClientLib, events
from app.interfaces.telegram_client import TelegramClient


class TelethonClient(TelegramClient):
    def __init__(self, api_id: int, api_hash: str, channel: str):
        self.client = TelethonClientLib("session", api_id, api_hash)
        self.channel = channel

    def listen(self, on_message):
        @self.client.on(events.NewMessage(chats=self.channel))
        async def handler(event):
            on_message(event.raw_text)

        self.client.start()
        self.client.run_until_disconnected()
