import curses
import curses.textpad

def main(stdscr):
    # Clear screen
    stdscr.clear()
    
    # Create a window for the textpad
    height, width = 20, 50  # Dimensions of the textpad
    win = curses.newwin(height, width, 5, 5)
    
    # Enable scrolling for the window
    win.scrollok(True)
    
    # Create a textpad in the window
    pad_height = 100  # Total number of lines in the pad
    pad_width = width  # Width of the textpad matches the window width
    pad = curses.newpad(pad_height, pad_width)

    # Generate some content for the textpad (100 lines of text)
    for i in range(pad_height-1):
        pad.addstr(i, 0, f"Line {i + 1}: This is an example of scrollable text in the textpad.")

    # Define the position where the textpad starts being displayed (starting at the top)
    start_row = 0
    start_col = 0

    # Show the initial content in the window
    while True:
        # Refresh the window and display the current content of the pad
        pad.refresh(start_row, start_col, 0, 0, height - 1, width - 1)
        
        # Get user input for scrolling
        key = stdscr.getch()
        
        if key == curses.KEY_UP and start_row > 0:
            start_row -= 1  # Move the view up
        elif key == curses.KEY_DOWN and start_row < pad_height - height:
            start_row += 1  # Move the view down
        elif key == ord('q'):  # Press 'q' to quit
            break

        # Redraw the screen
        stdscr.refresh()

# Initialize curses and run the main function
curses.wrapper(main)
