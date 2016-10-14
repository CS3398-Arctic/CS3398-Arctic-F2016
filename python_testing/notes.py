import itertools
import datetime
import store_database
import search_database

class note:
	pass

def store_note(body, author, school, major, course, instr, unit, section):
	"""Definition of class note. Defines note attributes and then stores
note object into store_database.storeNote()
	"""
	newNote = note()
	newNote.note_body = body
	newNote.created_by = author
	newNote.note_school = school
	newNote.note_major = major
	newNote.note_class = course
	newNote.note_instr = instr
	newNote.note_unit = unit
	newNote.note_section = section
	store_database.storeNote(newNote)      

def load_note_by_id(id):
	"""Creates dictionary of note that was found by ID inside the 
search_database.py file. Stores attributes found on Mariadb and stores them
in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = search_database.findNoteByID(id)
	newNote.id = id
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = note_data['school']
	newNote.major = note_data['major']
	newNote.course = note_data['course']
	newNote.instr = note_data['instr']
	newNote.unit = note_data['unit']
	newNote.section = note_data['section']
	newNote.note_date = note_data['note_date']
	return newNote
	
def load_note_by_name(name):
	"""Creates dictionary of note that was found by author inside the 
search_database.py file. Stores attributes found on Mariadb and stores them
in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = search_database.findNoteByUser(name)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = name
	newNote.school = note_data['school']
	newNote.major = note_data['major']
	newNote.course = note_data['course']
	newNote.instr = note_data['instr']
	newNote.unit = note_data['unit']
	newNote.section = note_data['section']
	newNote.note_date = note_data['note_date']
	return newNote
	
def load_note_by_school(school):
	"""Creates dictionary of note that was found by school inside the 
search_database.py file. Stores attributes found on Mariadb and stores them
in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = search_database.findNoteBySchool(school)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = school
	newNote.major = note_data['major']
	newNote.course = note_data['course']
	newNote.instr = note_data['instr']
	newNote.unit = note_data['unit']
	newNote.section = note_data['section']
	newNote.note_date = note_data['note_date']
	return newNote
	
def load_note_by_major(major):
	"""Creates dictionary of note that was found by major inside the 
search_database.py file. Stores attributes found on Mariadb and stores them
in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = search_database.findNoteByMajor(major)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = note_data['school']
	newNote.major = major
	newNote.course = note_data['course']
	newNote.instr = note_data['instr']
	newNote.unit = note_data['unit']
	newNote.section = note_data['section']
	newNote.note_date = note_data['note_date']
	return newNote

def load_note_by_course(course):
	"""Creates dictionary of note that was found by course inside the 
search_database.py file. Stores attributes found on Mariadb and stores them
in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = search_database.findNoteByCourse(course)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = note_data['school']
	newNote.major = note_data['major']
	newNote.course = course
	newNote.instr = note_data['instr']
	newNote.unit = note_data['unit']
	newNote.section = note_data['section']
	newNote.note_date = note_data['note_date']
	return newNote

def load_note_by_instr(instr):
	"""Creates dictionary of note that was found by instructor inside the 
search_database.py file. Stores attributes found on Mariadb and stores them
in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = search_database.findNoteByInstr(instr)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = note_data['school']
	newNote.major = note_data['major']
	newNote.course = note_data['course']
	newNote.instr = instr
	newNote.unit = note_data['unit']
	newNote.section = note_data['section']
	newNote.note_date = note_data['note_date']
	return newNote	
	
def load_note_by_unit(unit):
	"""Creates dictionary of note that was found by unit inside the 
search_database.py file. Stores attributes found on Mariadb and stores them
in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = search_database.findNoteByUnit(unit)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = note_data['school']
	newNote.major = note_data['major']
	newNote.course = note_data['course']
	newNote.instr = note_data['instr']
	newNote.unit = unit
	newNote.section = note_data['section']
	newNote.note_date = note_data['note_date']
	return newNote	

def load_note_by_section(section):
	"""Creates dictionary of note that was found by section inside the 
search_database.py file. Stores attributes found on Mariadb and stores them
in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = search_database.findNoteBySection(section)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = note_data['school']
	newNote.major = note_data['major']
	newNote.course = note_data['course']
	newNote.instr = note_data['instr']
	newNote.unit = note_data['unit']
	newNote.section = section
	newNote.note_date = note_data['note_date']
	return newNote	

def load_note_by_date(date):
	"""Creates dictionary of note that was found by date inside the 
search_database.py file. Stores attributes found on Mariadb and stores them
in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = search_database.findNoteByDate(date)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = note_data['school']
	newNote.major = note_data['major']
	newNote.course = note_data['course']
	newNote.instr = note_data['instr']
	newNote.unit = note_data['unit']
	newNote.section = note_data['section']
	newNote.note_date = date
	return newNote		
	
 
   
