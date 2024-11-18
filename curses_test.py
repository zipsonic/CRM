import curses
from curses import panel
from clients import Client

def show_panel(panel_obj):
    """Show the panel and update the display."""
    panel_obj.show()
    panel.update_panels()
    curses.doupdate()

def hide_panel(panel_obj):
    """Hide the panel and update the display."""
    panel_obj.hide()
    panel.update_panels()
    curses.doupdate()

def data_entry_form(stdscr: "curses._CursesWindow",client1: Client):
    curses.curs_set(1)  # Make the cursor visible
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

    # Create the main window and a pop-up panel for data entry
    height, width = 10, 40
    start_y, start_x = 5, 10
    form_window = curses.newwin(height, width, start_y, start_x)
    form_window.bkgd(' ', curses.color_pair(1))
    form_panel = panel.new_panel(form_window)

    # Input text variable
    input_text = ""
    max_input_length = width - 4

    # Show the form panel
    show_panel(form_panel)

    form_window.clear()
    form_window.box()

    client_info = client1.get_contact_info()
    lines = client_info.splitlines()
    for i, line in enumerate(lines):
        if i + 2 < height - 1:
            form_window.addstr(i + 2, 2, line[:width - 4])

    # form_window.addstr(1, 2, )
    form_window.refresh()

    while True:
        # Display the input text
        #form_window.addstr(3, 2, input_text + " " * (max_input_length - len(input_text)))
        #form_window.move(3, 2 + len(input_text))
        form_window.refresh()

        # Get user input
        key = form_window.getch()

        if key in [10, 13]:  # Enter key
            hide_panel(form_panel)
            return input_text
        elif key == 27:  # ESC key to cancel
            hide_panel(form_panel)
            return None
        elif key in [curses.KEY_BACKSPACE, 127]:
            input_text = input_text[:-1]
        elif 32 <= key < 127:  # Printable characters
            if len(input_text) < max_input_length:
                input_text += chr(key)

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr(0, 0, "Press 'd' to open data entry form, or 'q' to quit.")
    stdscr.refresh()

    user_data = None

    client1 = Client(
        "Johnathan",
        "Dough",
        "jd@example.net",
        "2138675309"
    )

    while True:
        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == ord('d'):
            # Open the data entry form and get the result
            user_data = data_entry_form(stdscr,client1)
            stdscr.clear()
            if user_data is not None:
                stdscr.addstr(0, 0, f"Data entered: {user_data}")
            else:
                stdscr.addstr(0, 0, "Data entry canceled.")
            stdscr.addstr(1, 0, "Press 'd' to enter data again, or 'q' to quit.")
            stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)