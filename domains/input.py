#please run file : output
#data
from math import *
import numpy as np
from main import *
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

#enter student infos
nbStudents=int(input("Enter number of students : "))
for i in range(nbStudents):
    nameStudent=input("Name of student : ")
    idStudent=input("Id of student : ")
    dobStudent=input("dob of student : ")

#check id students already exists
    list=[nameStudent,idStudent,dobStudent]
    fileStudents= open ("students.txt","r") 
    nbStudents=len(fileStudents.readlines()) 
    fileStudents= open ("students.txt","r")  
    tab=fileStudents.readline()
    a=0
    while nbStudents!=0:
        file=tab.split(",")
        tab=fileStudents.readline()
        if file[1]==list[1]:
            a+=1
        nbStudents-=1
    fileStudents.close()
    if a==0:
        with  open ("students.txt","a") as fileStudents:
            list=[nameStudent,idStudent,dobStudent]
            for word in list:
                fileStudents.write(str(word)+",")
            fileStudents.write("\n")
            fileStudents.close()
    
    students+=[Students(nameStudent,idStudent,dobStudent)]
backgroundThread = BackgroundThread(3)
backgroundThread.start() 
print("Creation of the student list...")
backgroundThread.join()


#enter course infos
while True:
    nbCourses=int(input("Enter number of Courses : "))
    if nbCourses<0:
        print("Error, please select a correct number")
    else:
        break
for i in range(nbCourses):
    list=[]
    nameCourse=input("Name of course : ")
    idCourse=input("Id of course : ")
    while True:
        credits=floor(((int(input("Enter number total of hours for this course :  ")))/15)*10)/10
        if credits<1:
            print("Error, please select a correct number")
        else:
            break

#check id courses already exists
    list=[nameCourse,idCourse,credits]
    fileCourses= open ("courses.txt","r") 
    nbCourses=len(fileCourses.readlines()) 
    fileCourses= open ("courses.txt","r")  
    tab=fileCourses.readline()
    a=0
    while nbCourses!=0:
        file=tab.split(",")
        tab=fileCourses.readline()
        if file[0]==list[0]:
            a+=1
        nbCourses-=1
    fileCourses.close()
    if a==0:
        with  open ("courses.txt","a") as fileCourses:
            list=[nameCourse,idCourse,credits]
            for word in list:
                fileCourses.write(str(word)+",")
            fileCourses.write("\n")
            fileCourses.close()
    courses+=[Courses(nameCourse,idCourse,credits)]
  
backgroundThread = BackgroundThread(3)
backgroundThread.start() 
print("Creation of the course list...")
backgroundThread.join()
    
#enter course mark
allMarks= Marks()
allMarks.enterMarks()


