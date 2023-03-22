#please run file : output
#data
from math import *
import numpy as np
import os
import pickle
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

class Marks:
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
                with open ("marks.txt","a") as fileMarks:
                    fileMarks.write(str(students[x].name)+" in "+str(courses[i-1].nameCourse)+": "+str(mark)+",\n")
                    fileMarks.close()
                x+=1
                
    def showMarks(self):
        n=0
        for i in range (len(courses)):
            print("\nin",courses[i].nameCourse,":")
            for i in range(len(students)):
                print(f"Student {students[i].name} has mark {marks[n]}")
                n+=1
    def gpa(self):
        Arr=np.array([])
        n=0
        m=0
        totalcredits=0
        newlistMarks=[]
        for i in range (len(students)):
            print("\nthe student",students[i].name,"has mark :")
            n=m
            m+=1
            for i in range(len(courses)):
                print(f"in {courses[i].nameCourse} {marks[n]}")
                newlistMarks.append(marks[n])
                n+=len(students)
        for y in range(len(students)):
            calculGpa=0
            for i in range(len(courses)):
                calculGpa+=(newlistMarks[i*(y+1)])*courses[i].credits
                totalcredits+=courses[i].credits
            calculGpa=calculGpa/totalcredits
            Arr=np.append(Arr,floor(calculGpa*10)/10)
            print(f"Students {students[y].name} has a GPA of {floor(calculGpa*10)/10} ")
        Arr=np.sort(Arr,axis=0)
        print(f"\nThis is the list of gpa descending : {Arr}")