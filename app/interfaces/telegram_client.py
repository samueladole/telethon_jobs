from typing import Protocol, Callable


class TelegramClient(Protocol):
    """Protocol for Telegram client."""

    def listen(self, on_message: Callable[[str], None]) -> None:
        """Listens for incoming messages and calls the provided callback."""
