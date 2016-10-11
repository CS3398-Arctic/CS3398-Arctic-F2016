import itertools
import datetime

class slamenote:
    #Creates incremented id for object. To use, write object.id
    id_generator = itertools.count(0) #starts first object at id 1
    def __init__(self):
        self.id = next(self.id_generator) #increments id
        self.createdDate = datetime.date.today() #object has day it was made
  
    def setAuthor(self, name):
        self.author = name
    def getAuthor(self):
        return self.author
    
    def setSchool(self, school):
        self.school = school
    def getSchool(self):
        return self.school
    
    def setMajor(self, major):
        self.major = major
    def getMajor(self):
        return self.major
    
    def setCourse(self, course):
        self.course = course
    def getCourse(self):
        return self.course

    def setInstr(self, instr):
        self.instr = instr
    def getInstr(self):
        return self.instr

    def setUnit(self, unit):
        self.unit = unit
    def getUnit(self):
        return self.unit

    def setSection(self, section):
        self.section = section
    def getSection(self):
        return self.section
