import curses
from clients import Client
from clientedit import enter_client
from readwrite import *

def main(stdscr: 'curses._CursesWindow') -> None:
    curses.curs_set(0)
    stdscr.clear()

    #initialize Client List
    clientlist: list[Client] = read_list()

    #Initialize color pairs
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

    while True:

        startx: int = int(curses.COLS / 5 * 3)

        #Initialize/Re-Initialize Main Screen
        stdscr.bkgd(' ', curses.color_pair(1))

        stdscr.box()
        
        stdscr.addstr(curses.LINES-1,5,"[F2 Enter Client]")
        stdscr.addstr(curses.LINES-1,curses.COLS-15,"[ESC to Exit]")

        for _ in range (curses.LINES-2):
            stdscr.addch(_+1,startx-1,curses.ACS_VLINE)

        for i, client in enumerate(iterable=clientlist):
            starty: int = 1 + (i * 2)
            line1: str = f"{client.last_name}, {client.first_name}"
            line2: str = f"   {client.display_phone()}| {client.email}"
            stdscr.addstr(starty,startx,line1)
            stdscr.addstr(starty+1,startx,line2)

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

