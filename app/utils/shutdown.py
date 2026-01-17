from collections.abc import Callable
import signal
import sys

def register_shutdown(cleanup: Callable[[], None]) -> None:
    """Registers a shutdown handler to perform cleanup on termination signals."""

    def handler(sig: int, frame):
        """Handles termination signals by calling the cleanup function and exiting."""
        cleanup()
        sys.exit(0)

    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)
