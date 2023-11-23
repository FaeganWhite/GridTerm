import cursor
import keyboard
import subprocess
import os
import time
import signal


def handler(signum, frame):
    pass



if __name__ == "__main__":

    signal.signal(signal.SIGINT, handler)

    # Set the terminal settings
    os.system('clear')

    # Establish the FSM
    state = "main"
    current_app = None
    while True:

        # In the main state
        if state == 'main':
            #
            os.system('clear')
            subprocess.run(['stty', '-echo'], check=True)
            cursor.hide()
            time.sleep(0.2)
            #
            key = keyboard.read_key()
            # Quit on Esc
            if key == 'esc':
                state = 'quit'
            # Launch Internet with I
            elif key == 'i':
                state = 'app'
                time.sleep(0.2)
                cursor.show()
                current_app = subprocess.Popen(["w3m", "https://www.duckduckgo.com"])
            # Launch Nano with N
            if key == 'n':
                state = 'app'
                time.sleep(0.2)
                current_app = subprocess.Popen(["nano"])
            # Launch Nano with N
            if key == 'y':
                state = 'app'
                time.sleep(0.2)
                current_app = subprocess.Popen(["yt"])
                subprocess.run(['stty', 'echo'], check=True)
            # Launch Calendar with C
            if key == 'c':
                state = 'app'
                time.sleep(0.2)
                current_app = subprocess.Popen(["calcure"])
            # Launch Mail with m
            if key == 'm':
                state = 'app'
                time.sleep(0.2)
                current_app = subprocess.Popen(["neomutt"])

        # In the internet state
        elif state == 'app':
            time.sleep(0.2)
            # Return to the main state if the app's closed
            if current_app.poll() is not None:
                state = 'main'
            # If it's still running
            else:
                # Poll the keyboard
                key = keyboard.read_key()
                # Break if escape pressed
                if key =='esc':
                    state = 'main'
                    current_app.terminate()

        # Otherwise, if in the quit state
        elif state == 'quit':
            # Clear the terminal
            os.system('clear')
            time.sleep(0.2)
            # Print a check message
            print("Are you sure you want to shutdown? (y/n)")
            # Get a key press
            key = keyboard.read_key()
            # If yes, kill the session and end the loop
            if key == 'y':
                subprocess.run(["tmux", "kill-session", "-t", "cyberdeck"])
                break
            # If no, return to the main state
            elif key == 'n':
                state = 'main'
                os.system('clear')
            # Otherwise ask again 
            else:
                os.system('clear')
                time.sleep(0.2)