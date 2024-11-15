import curses
import signal

def handle_resize(stdscr):
    # Retrieve the new terminal size and update the screen
    curses.endwin()  # Reset curses state
    stdscr.clear()
    stdscr.refresh()
    update_screen(stdscr)

def update_screen(stdscr):
    height, width = stdscr.getmaxyx()
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLUE)
    WHITE_BLUE = curses.color_pair(1)
    stdscr.clear()
    stdscr.bkgd(' ', WHITE_BLUE)
    stdscr.border()
    stdscr.addstr(1, 1, f"Terminal size: {width}x{height}",WHITE_BLUE)
    stdscr.addstr(2, 1, "Resize the terminal to see the change. Press 'q' to quit.",WHITE_BLUE)
    stdscr.refresh()

def main(stdscr):
    # Setup signal handler for window resize
    signal.signal(signal.SIGWINCH, lambda signum, frame: handle_resize(stdscr))
    update_screen(stdscr)

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)
