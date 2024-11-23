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

    #Initialize which page of clients to display
    listpage: int = 0
    #Calculate max clients that can be displayed at one time
    maxdisplayclients: int = int(curses.LINES/2) - 1

    while True:

        #Calculate the max amount of clientlist pages - Can change on update
        maxpages: int = int(len(clientlist)/maxdisplayclients) - 1

        if len(clientlist) % maxdisplayclients > 0:
            maxpages += 1

        startx: int = int(curses.COLS / 5 * 3)

        #Initialize/Re-Initialize Main Screen
        stdscr.bkgd(' ', curses.color_pair(1))

        stdscr.box()
        
        stdscr.addstr(curses.LINES-1,5,"[F2 Enter Client]")
        stdscr.addstr(curses.LINES-1,curses.COLS-15,"[ESC to Exit]")

        for _ in range (curses.LINES-2):
            stdscr.addch(_+1,startx-1,curses.ACS_VLINE)

        if listpage == maxpages:
            endindex: int = len(clientlist) % maxdisplayclients
        else:
            endindex = maxdisplayclients

        for i in range(0, endindex):
            starty: int = 1 + (i * 2)
            index: int = (listpage * maxdisplayclients) + i
            line1: str = f"{clientlist[index].last_name}, {clientlist[index].first_name}"
            line2: str = f"   {clientlist[index].display_phone()}| {clientlist[index].email}"
            stdscr.addstr(starty,startx,line1)
            stdscr.addstr(starty+1,startx,line2)

        stdscr.refresh()

        key: int = stdscr.getch()

        if key == curses.KEY_F2:
            key = key
            enter_client(clientlist)

        if key == 27: #ESC Exits
            break

        if key == curses.KEY_DOWN:
            if listpage < maxpages:
                listpage += 1

        if key == curses.KEY_UP:
            if listpage > 0:
                listpage -= 1

        stdscr.clear()

    if len(clientlist) > 0:
        save_list(clientlist)
        
if __name__ == "__main__":
    curses.wrapper(main)

