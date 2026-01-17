import signal
import sys

def register_shutdown(cleanup):
    def handler(sig, frame):
        cleanup()
        sys.exit(0)

    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)
