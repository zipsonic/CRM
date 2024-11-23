import curses
from curses import panel
from clients import Client

def enter_client(clientlist: list[Client]) -> None:

    curses.curs_set(1)

    panelheight: int = curses.LINES - 1
    panelwidth: int = curses.COLS - int(curses.COLS / 5 * 3)

    entrywin: curses._CursesWindow = curses.newwin(panelheight,panelwidth,1,curses.COLS-panelwidth)
    entrywin.bkgd(' ',curses.color_pair(2))
    entrywin.keypad(True)
    entrypanel: panel._Curses_Panel = panel.new_panel(entrywin)
    entrypanel.show()
    entrywin.refresh()

    # Define the input fields (y, x) positions
    fields = [
        (5, 15, "Last Name"),  # Field 1
        (7, 15, "First Name"),  # Field 2
        (9, 15, "Email Address"),  # Field 3
        (11, 15, "Phone Number"),
    ]
    current_field = 0
    input_data = [""] * len(fields)

    while True:
        entrywin.clear()
        entrywin.box()

        # Draw instructions
        entrywin.addstr(1, 1, f"Enter Client Data.")
        entrywin.addstr(panelheight-1,5,"[F5 SAVE CLIENT]----------[ESC to Exit]")

        # Display the input fields and their current values
        for i, (y, x, name) in enumerate(fields):
            # Display the label and the input data
            entrywin.addstr(y, x - len(name) - 1, f"{name}: ")
            entrywin.addstr(y, x, input_data[i])


        # Move the cursor to the active field, right after the colon and current input text
        y, x, name = fields[current_field]
        entrywin.move(y, x + len(input_data[current_field]))

        entrywin.refresh()
        key = entrywin.getch()

        # Quit/Dont Save if esc is pressed
        if key == 27:
            input_data[0] = ""
            break
        
        # Save if F5 is pressed 
        if key == curses.KEY_F5:
            break

        # Handle Tab or Enter key (ASCII code 10 or 13)
        elif key in [9, 10, 13]:
            current_field = (current_field + 1) % len(fields)

        # Handle Backspace (ASCII code 127 or curses.KEY_BACKSPACE)
        elif key in [127, curses.KEY_BACKSPACE]:
            if input_data[current_field]:
                input_data[current_field] = input_data[current_field][:-1]

        # Handle character input
        elif 32 <= key <= 126:  # Printable ASCII range
            input_data[current_field] += chr(key)

    #check if all datafields are present
    savedata: bool = True

    for _ in range(4):
        if input_data[_] == "":
            savedata = False

    if savedata:
        clientlist.append(Client(input_data[1],input_data[0],input_data[2],input_data[3]))

    curses.curs_set(0)
    entrypanel.hide()
    entrywin.refresh()