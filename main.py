import libtmux
import subprocess

def setup_status_bar(session):
    # Set server-wide options to hide the window list
    server.cmd('set-option', '-g', 'window-status-format', '')
    server.cmd('set-option', '-g', 'window-status-current-format', '')

    # Enable the status line and set it to the top of the screen
    session.set_option('status', 'on')
    session.set_option('status-position', 'top')

    # Set the content of the status bar
    session.set_option('status-left-length', 100)
    session.set_option('status-left', "Phone OS V1 - Notifications: 0")
    session.set_option('status-right', "#(date '+%d-%m-%Y %H:%M:%S')")

    session.cmd('set-option', 'status-style', 'bg=red')
    session.cmd('set-option', 'status-interval', '1')

if __name__ == "__main__":

    # Connect to the tmux server
    config_path = 'tmux.conf'
    server = libtmux.Server(config_file=config_path)

    # If the session already exists, kill the session
    session = server.find_where({"session_name": "cyberdeck"})
    if session:
        session.kill_session()

    # Start a new session named 'cyberdeck'
    session = server.new_session(session_name="cyberdeck")

    setup_status_bar(session)

    # Create a new window and split vertically
    window = session.new_window(attach=True, window_name="main")

    # Establish the head and body panes
    main = window.panes[0]
    main.select_pane()
    pane_id = main.id
    main.send_keys(f'python3 body.py')

    session.cmd('refresh-client')

    # Attach to the session to see everything in action
    session.attach_session()