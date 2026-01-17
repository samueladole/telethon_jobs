from typing import Protocol, Callable

class TelegramClient(Protocol):

    def listen(self, on_message: Callable[[str], None]) -> None:
        ...
