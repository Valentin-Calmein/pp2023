###please run this file###
from math import *
import numpy as np
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
from input import *
from time import *
import os

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    BLACK_AND_GREEN=curses.color_pair(1)
    RED_AND_BLACK=curses.color_pair(2)
    stdscr.clear()
    stdscr.refresh()
    stdscr.attron(BLACK_AND_GREEN)
    rectangle(stdscr,1,1,3,20)
    stdscr.attroff(BLACK_AND_GREEN)
    stdscr.addstr(2,4,"Please Wait",BLACK_AND_GREEN | curses.A_BOLD )
    stdscr.refresh()
    sleep(1)
    stdscr.addstr(2,4,"Please Wait.",BLACK_AND_GREEN | curses.A_BOLD )
    stdscr.refresh()
    sleep(1)
    stdscr.addstr(2,4,"Please Wait..",BLACK_AND_GREEN | curses.A_BOLD )
    stdscr.refresh()
    sleep(1)
    stdscr.addstr(2,4,"Please Wait...",BLACK_AND_GREEN | curses.A_BOLD )
    stdscr.refresh()
    sleep(1.5)
    stdscr.clear()
    curses.endwin()

wrapper(main)
print("-------------------")
#show list students
print("\nListing students :")
for obj in students:
    print(obj.name, obj.id, obj.dob, sep=' / ')
print("\n-------------------")
#show list courses
print("\nListing courses :")
for obj in courses:
    print(obj.nameCourse, obj.idCourse, obj.credits , sep=' / ')
    
#show course Marks ang gpa
print("\n-------------------")
allMarks.showMarks()
print("\n-------------------")
allMarks.gpa()
print("\n-------------------\n")

