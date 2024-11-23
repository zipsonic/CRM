import curses
import curses.panel
import time

def main(stdscr):
    # Disable cursor and configure the terminal for better usability
    curses.curs_set(0)
    stdscr.nodelay(1)  # Non-blocking input
    stdscr.timeout(100)  # Refresh screen every 100ms

    # Get screen dimensions (height, width)
    height, width = stdscr.getmaxyx()
    
    # Create a window with a starting width of 0 (the panel will be hidden initially)
    win_height = 10
    win_width = 2  # Start with 0 width
    win_y = 5
    win_x = width  # Start off-screen to the right

    # Create a new window and a panel
    win = curses.newwin(win_height, win_width, win_y, win_x)
    panel_obj = curses.panel.new_panel(win)
    
    # Text to display on the panel
    text = "This is a sliding drawer!"
    
    # Sliding animation loop (increasing the width of the window)
    for i in range(2, width, 2):  # Increase the width incrementally
        win_width = i  # Gradually increase the width
        win.resize(win_height, win_width)  # Resize the window to the new width
        win.clear()  # Clear the window to prevent overlapping text
        #win.addstr(1, 1, text)  # Add the text to the window
        win.box()
        curses.panel.update_panels()  # Update the panel
        stdscr.refresh()  # Refresh the screen
        time.sleep(0.01)  # Sleep to slow down the animation
        
        # Update the position of the panel to keep it off-screen for the next iteration
        win_x = width - win_width
        win.mvwin(win_y, win_x)  # Move the window horizontally
    
    # Wait for user input to close
    stdscr.getch()

# Run the program inside the curses wrapper to handle initialization/cleanup
curses.wrapper(main)
