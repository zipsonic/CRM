import curses
import csv
import os
from curses import panel
from clients import Client
from readwrite import *

def enter_client(clientlist: list[Client]) -> None:
    curses.curs_set(1)
    panelheight: int = curses.LINES-2
    panelwidth: int = int(curses.COLS/2) -1
    entrywin: curses._CursesWindow = curses.newwin(panelheight,panelwidth,1,int(curses.COLS/2))
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
        entrywin.addstr(1, 1, f"Enter Client Data. ESC to Exit")
        entrywin.addstr(panelheight-1,5,"[F5 SAVE CLIENT]")

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

    
def main(stdscr: 'curses._CursesWindow') -> None:
    curses.curs_set(0)
    stdscr.clear()

    #initialize Client List
    clientlist: list[Client] = read_list()

    # Sample Data ---- REMOVE ME
    # clientlist.append(Client(
    #     "Johnathan",
    #     "Dough",
    #     "jd@example.net",
    #     "2138675309"
    # ))
    # clientlist.append(Client(
    #     "Jane",
    #     "Doe",
    #     "jdoe@example.net",
    #     "3108675309"
    # ))
    # End Sample Data ----- REMOVE ME

    #Initialize color pairs
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2,curses.COLOR_BLACK, curses.COLOR_GREEN)

    while True:

        #Initialize/Re-Initialize Main Screen
        stdscr.bkgd(' ', curses.color_pair(1))
        stdscr.box()
        stdscr.addstr(curses.LINES-1,5,"[F2 Enter Client]")
        stdscr.addstr(curses.LINES-1,curses.COLS-15,"[ESC to Exit]")

        startx: int = int(curses.COLS / 2)
        starty: int = 0

        for i, client in enumerate(iterable=clientlist):
            for j, line in enumerate(iterable=client.get_contact_info().split("\n")):
                stdscr.addstr((starty + j + 1 ) + ( i * 3),startx,line)

        stdscr.refresh()

        key: int = stdscr.getch()

        if key == curses.KEY_F2:
            key = key
            enter_client(clientlist)

        if key == 27:
            break
    if len(clientlist) > 0:
        save_list(clientlist)
        


if __name__ == "__main__":
    curses.wrapper(main)

