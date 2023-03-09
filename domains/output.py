###please run this file###
from math import *
import numpy as np
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
from input import *
from time import *



#show list students
print("\nListing students :")
for obj in students:
    print(obj.name, obj.id, obj.dob, sep=' / ')

#show list courses
print("\nListing courses :")
for obj in courses:
    print(obj.nameCourse, obj.idCourse, obj.credits , sep=' / ')
    
#show course Marks ang gpa
print("")
allMarks.showMarks()
allMarks.gpa()

sleep(5)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    BLACK_AND_GREEN=curses.color_pair(1)
    RED_AND_BLACK=curses.color_pair(2)
    stdscr.clear()
    stdscr.addstr(2,5,"THANK YOU BYE",BLACK_AND_GREEN | curses.A_BOLD )
    stdscr.attron(BLACK_AND_GREEN)
    rectangle(stdscr,1,1,3,20)
    stdscr.attroff(BLACK_AND_GREEN)
    stdscr.refresh()
    stdscr.getch()
    curses.endwin()
wrapper(main)

