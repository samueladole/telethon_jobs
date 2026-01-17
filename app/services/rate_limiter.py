from datetime import date

class RateLimiter:
    """A simple rate limiter that allows a maximum number of actions per day."""
    def __init__(self, max_per_day: int):
        self.max = max_per_day
        self.count = 0
        self.day = date.today()

    def allow(self):
        """Check if an action is allowed under the rate limit."""
        if date.today() != self.day:
            self.count = 0
            self.day = date.today()
        if self.count >= self.max:
            return False
        self.count += 1
        return True
