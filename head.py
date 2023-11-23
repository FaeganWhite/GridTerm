from datetime import datetime
import time
import os
import sys
import cursor

# Get the current date and time
def get_time():
     return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Move the cursor to the beginning of the line and clear the line
def clear_line():
    sys.stdout.write('\x1b[1G')  # Move to the start of the line
    sys.stdout.write('\x1b[2K')  # Clear the line

#
def update_head():
    #
    new_head_text = f"Phone OS V1 - Notifications: 0 - Time: {get_time()}"
    remaining = os.get_terminal_size().columns - len(new_head_text) - 2
    buffer = "█" * (remaining // 2)
    return buffer + " " + new_head_text + " " + buffer

if __name__ == "__main__":
    cursor.hide()
    while True:
        #
        clear_line()
        #
        print(update_head(), end='\r')
        #
        sys.stdout.flush()
        #
        time.sleep(0.2)