import time
from datetime import datetime


def set_alarm():
    """
    Set an alarm for a specific time.
    """
    print("Welcome to the Alarm Clock!")

    # Get the current time
    now = datetime.now()
    print(f"Current time: {now.strftime('%H:%M:%S')}")

    # Input alarm time from the user
    alarm_time_str = input("Enter the alarm time (HH:MM:SS): ")
    try:
        alarm_time = datetime.strptime(alarm_time_str, '%H:%M:%S').time()
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
        return

    # Calculate the alarm time for today
    alarm_datetime = datetime.combine(now.date(), alarm_time)

    # If the alarm time is earlier than the current time, set it for the next day
    if alarm_datetime < now:
        alarm_datetime += timedelta(days=1)

    print(f"Alarm set for {alarm_datetime.strftime('%H:%M:%S')}")

    # Wait until the alarm time
    while True:
        now = datetime.now()
        if now >= alarm_datetime:
            print("Alarm ringing! Time's up!")
            break
        # Sleep for a short time to avoid busy waiting
        time.sleep(1)


if __name__ == "__main__":
    set_alarm()
