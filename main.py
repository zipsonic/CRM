import curses
from curses import panel
from clients import Client

def enter_client() -> None:
    entrywin = curses.newwin(28,60,1,60)
    entrywin.bkgd(' ',curses.color_pair(2))
    entrypanel = panel.new_panel(entrywin)
    entrypanel.show()
    entrywin.box()
    entrywin.refresh()
    entrywin.getch()
    entrypanel.hide()
    entrywin.refresh()


def main(stdscr: 'curses._CursesWindow') -> None:
    curses.curs_set(0)
    stdscr.clear()

    #Initialize color pairs
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_GREEN)
    
    stdscr.bkgd(' ', curses.color_pair(1))
    stdscr.box()
    stdscr.addstr(curses.LINES-1,5,"[F2 Enter Client]")

    while True:

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_F2:
            key = key
            enter_client()
        


if __name__ == "__main__":
    curses.wrapper(main)

