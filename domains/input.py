#please run file output
from math import *
import numpy as np
from main import *
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

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

#enter student infos
nbStudents=int(input("Enter number of students : "))
for i in range(nbStudents):
    nameStudent=input("Name of student : ")
    idStudent=input("Id of student : ")
    dobStudent=input("dob of student : ")
    students+=[Students(nameStudent,idStudent,dobStudent)]

#enter course infos
nbCourses=int(input("Enter number of Courses : "))
for i in range(nbCourses):
    nameCourse=input("Name of course : ")
    idCourse=input("Id of course : ")
    credits=floor(((int(input("Enter number total of hours for this course :  ")))/15)*10)/10
    courses+=[Courses(nameCourse,idCourse,credits)]
    
#enter course mark
allMarks= Marks()
allMarks.enterMarks()