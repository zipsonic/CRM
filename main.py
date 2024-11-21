import curses
from curses import panel
from clients import Client

def enter_client(clientlist: list[Client]) -> None:
    curses.curs_set(1)
    entrywin: curses._CursesWindow = curses.newwin(28,60,1,60)
    entrywin.bkgd(' ',curses.color_pair(2))
    entrypanel: panel._Curses_Panel = panel.new_panel(entrywin)
    entrypanel.show()
    entrywin.box()
    entrywin.refresh()
    entrywin.getch()
    entrypanel.hide()

    curses.curs_set(0)
    entrywin.refresh()

    
def main(stdscr: 'curses._CursesWindow') -> None:
    curses.curs_set(0)
    stdscr.clear()

    #initialize Client List
    clientlist: list[Client] = []

    # Sample Data ---- REMOVE ME
    clientlist.append(Client(
        "Johnathan",
        "Dough",
        "jd@example.net",
        "2138675309"
    ))
    clientlist.append(Client(
        "Jane",
        "Doe",
        "jdoe@example.net",
        "3108675309"
    ))
    # End Sample Data ----- REMOVE ME

    #Initialize color pairs
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_GREEN)

    stdscr.bkgd(' ', curses.color_pair(1))
    stdscr.box()
    stdscr.addstr(curses.LINES-1,5,"[F2 Enter Client]")

    startx = 62
    starty = 0

    for i, client in enumerate(iterable=clientlist):
        for j, line in enumerate(iterable=client.get_contact_info().split("\n")):
            stdscr.addstr((starty + j + 1 ) + ( i * 3),startx,line)

    while True:

        stdscr.refresh()

        key: int = stdscr.getch()

        if key == curses.KEY_F2:
            key = key
            enter_client(clientlist)
        


if __name__ == "__main__":
    curses.wrapper(main)

