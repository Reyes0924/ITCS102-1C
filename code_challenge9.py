import time

def countdown_timer():
    try:
        minutes = int(input("Enter minutes for the countdown: "))
        seconds = int(input("Enter seconds for the countdown: "))
        
        total_seconds = minutes * 60 + seconds

        if total_seconds <= 0:
            print("Please enter a positive duration.")
            return

        while total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            timer_format = '{:02d}:{:02d}'.format(mins, secs)
            print(timer_format, end='\r')
            time.sleep(1)
            total_seconds -= 1

        print("Countdown finished!")

    except ValueError:
        print("Invalid input. Please enter integers for minutes and seconds.")

if __name__ == "__main__":
    countdown_timer()