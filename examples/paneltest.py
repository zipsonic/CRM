import curses
import curses.panel
import time

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Set up the window and panel
    height, width = 10, 40
    win = curses.newwin(height, width, 5, 5)  # Create a window at position (5, 5)
    panel = curses.panel.new_panel(win)  # Create a panel for the window

    # Display initial information
    win.addstr(1, 1, "Panel 1: Initial Information")
    win.refresh()
    
    # Wait for a moment before hiding the panel
    time.sleep(2)

    # Hide the panel
    panel.hide()
    stdscr.addstr(10, 1, "Data Under Panel")
    stdscr.refresh()
    time.sleep(2)

    # Update panel content with different information
    win.clear()  # Clear the window content
    win.addstr(1, 1, "Panel 1: Updated Information")
    win.refresh()

    # Show the panel again
    panel.show()
    stdscr.refresh()

    # Wait for a while before the program ends
    time.sleep(2)

    panel.hide()
    stdscr.refresh()
    time.sleep(2)

# Initialize curses and run the main function
curses.wrapper(main)
