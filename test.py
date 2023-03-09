import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
print("HELLO")
def Main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    BLUE_AND_BLACK=curses.color_pair(1)
    MAGENTA_AND_BLACK=curses.color_pair(2)
    CYAN_AND_BLACK=curses.color_pair(3)
    stdscr.clear()
    stdscr.addstr(2,3,"WELCOME !",BLUE_AND_BLACK | curses.A_BOLD)
    stdscr.addstr(2,13,"Press any key for starting...",CYAN_AND_BLACK | curses.A_DIM )
    stdscr.attron(MAGENTA_AND_BLACK)
    rectangle(stdscr,1,1,3,43)
    stdscr.attroff(MAGENTA_AND_BLACK)
    stdscr.refresh()
    stdscr.getch()
    curses.endwin()
wrapper(Main)



input("how r u?")