import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="ALERT.",
            message="Damn, Enough for today",
            timeout=5
        )
        time.sleep(3600)
