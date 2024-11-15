import curses

def main(stdscr):
    curses.curs_set(1)  # Show the cursor
    stdscr.clear()
    stdscr.refresh()

    # Define the input fields (y, x) positions
    fields = [
        (5, 15, "Last Name"),  # Field 1
        (7, 15, "First Name"),  # Field 2
        (9, 15, "Email Address"),  # Field 3
    ]
    current_field = 0
    input_data = [""] * len(fields)

    while True:
        stdscr.clear()

        # Draw instructions
        stdscr.addstr(1, 1, f"Field 1 {input_data[0]}, 'q' to quit.")

        # Display the input fields and their current values
        for i, (y, x, name) in enumerate(fields):
            # Display the label and the input data
            stdscr.addstr(y, x - len(name) - 1, f"{name}: ")
            stdscr.addstr(y, x, input_data[i])

        # Move the cursor to the active field, right after the colon and current input text
        y, x, name = fields[current_field]
        stdscr.move(y, x + len(input_data[current_field]))

        stdscr.refresh()
        key = stdscr.getch()

        # Quit if 'q' is pressed
        if key == ord('q'):
            break

        # Handle Tab key (ASCII code 9)
        elif key == 9:  # Tab key
            current_field = (current_field + 1) % len(fields)

        # Handle Enter key (ASCII code 10 or 13)
        elif key in [10, 13]:
            current_field = (current_field + 1) % len(fields)

        # Handle Backspace (ASCII code 127 or curses.KEY_BACKSPACE)
        elif key in [127, curses.KEY_BACKSPACE]:
            if input_data[current_field]:
                input_data[current_field] = input_data[current_field][:-1]

        # Handle character input
        elif 32 <= key <= 126:  # Printable ASCII range
            input_data[current_field] += chr(key)
    print(input_data[0])

if __name__ == "__main__":
    curses.wrapper(main)
