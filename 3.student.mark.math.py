from math import *
import numpy as np
#data
students=[]
courses=[]
marks=[]

#class functions
class Students:
    def __init__(self,name,id,dob):
        self.name = name
        self.id= id
        self.dob= dob
             
class Courses:
    def __init__(self,nameCourse,idCourse,credits):
        self.nameCourse= nameCourse
        self.idCourse= idCourse
        self.credits=credits

class Marks :
    def enterMarks(self):
        i=0
        for obj in courses:
            print("in",courses[i].nameCourse," : ")
            i+=1
            x=0
            for obj in students:
                print("what is the marks for",students[x].name," : ")
                mark=floor(int(input(""))*10)/10
                marks.append(mark)
                x+=1
    def showMarks(self):
        n=0
        for i in range (len(courses)):
            print("\nin",courses[i].nameCourse,":")
            for i in range(len(students)):
                print(f"Student {students[i].name} has mark {marks[n]}")
                n+=1
    def gpa(self):
        for i in range (len(students)):
            for obj in courses:
                calculGpa=

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
    credits=floor(((int(input("Enter number total of hours for this coruse :  ")))/15)*10)/10
    courses+=[Courses(nameCourse,idCourse,credits)]

#enter course mark
allMarks= Marks()
allMarks.enterMarks()
        
#show list students
print("\nListing students :")
for obj in students:
    print(obj.name, obj.id, obj.dob, sep=' / ')

#show list courses
print("\nListing courses :")
for obj in courses:
    print(obj.nameCourse, obj.idCourse, obj.credits , sep=' / ')
    
#show course Marks
allMarks.showMarks()