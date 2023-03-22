###please run this file###
#data
from math import *
import numpy as np
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

#homepage
def main2(stdscr):
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
wrapper(main2)

#data
from input import *
from time import *
import pickle 

#loading display
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

data=[]
with open("students.dat", "wb") as file:
    for obj in courses:
        data.append(obj.nameCourse)
    data.append("//")
    for obj in students:
        data.append(obj.name)
    pickle.dump(data, file)

file = open('students.dat', 'rb')
data = pickle.load(file)
file.close()

''' If you want to see what's inside the file students.dat 
nbc = 1
nbs=1
for item in data:
    while item!="//":
        print('The course ', nbc, ' is : ', item)
        nbc += 1
    print('The Students', nbs, ' is : ', item)
    nbs+=1
'''