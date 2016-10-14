import itertools
import datetime
import database_store
import database_search

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
	
def load_note_by_name(name):
	"""Creates dictionary of note that was found by author inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = database_search.find_note_by_user(name)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = note_data['school']
	newNote.major = note_data['major']
	newNote.course = note_data['course']
	newNote.instr = note_data['instr']
	newNote.unit = note_data['unit']
	newNote.section = note_data['section']
	newNote.date = note_data['date']
	return newNote
	
def load_note_by_school(school):
	"""Creates dictionary of note that was found by school inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = database_search.find_note_by_school(school)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = note_data['school']
	newNote.major = note_data['major']
	newNote.course = note_data['course']
	newNote.instr = note_data['instr']
	newNote.unit = note_data['unit']
	newNote.section = note_data['section']
	newNote.date = note_data['date']
	return newNote
	
def load_note_by_major(major):
	"""Creates dictionary of note that was found by major inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = database_search.find_note_by_major(major)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = note_data['school']
	newNote.major = note_data['major']
	newNote.course = note_data['course']
	newNote.instr = note_data['instr']
	newNote.unit = note_data['unit']
	newNote.section = note_data['section']
	newNote.date = note_data['date']
	return newNote

def load_note_by_course(course):
	"""Creates dictionary of note that was found by course inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = database_search.find_note_by_course(course)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = note_data['school']
	newNote.major = note_data['major']
	newNote.course = note_data['course']
	newNote.instr = note_data['instr']
	newNote.unit = note_data['unit']
	newNote.section = note_data['section']
	newNote.date = note_data['date']
	return newNote

def load_note_by_instr(instr):
	"""Creates dictionary of note that was found by instructor inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = database_search.find_note_by_instr(instr)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = note_data['school']
	newNote.major = note_data['major']
	newNote.course = note_data['course']
	newNote.instr = note_data['instr']
	newNote.unit = note_data['unit']
	newNote.section = note_data['section']
	newNote.date = note_data['date']
	return newNote	
	
def load_note_by_unit(unit):
	"""Creates dictionary of note that was found by unit inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = database_search.find_note_by_unit(unit)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = note_data['school']
	newNote.major = note_data['major']
	newNote.course = note_data['course']
	newNote.instr = note_data['instr']
	newNote.unit = note_data['unit']
	newNote.section = note_data['section']
	newNote.date = note_data['date']
	return newNote	

def load_note_by_section(section):
	"""Creates dictionary of note that was found by section inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = database_search.find_note_by_section(section)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = note_data['school']
	newNote.major = note_data['major']
	newNote.course = note_data['course']
	newNote.instr = note_data['instr']
	newNote.unit = note_data['unit']
	newNote.section = note_data['section']
	newNote.date = note_data['date']
	return newNote
	
def load_note_by_id(id):
	"""Creates dictionary of note that was found by ID inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = database_search.find_note_by_id(id)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = note_data['school']
	newNote.major = note_data['major']
	newNote.course = note_data['course']
	newNote.instr = note_data['instr']
	newNote.unit = note_data['unit']
	newNote.section = note_data['section']
	newNote.date = note_data['date']
	return newNote

#No build for this yet, if you're calling this and it's not working, that's why.
def load_note_by_date(date):
	"""Creates dictionary of note that was found by date inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	note_data = database_search.find_note_by_date(date)
	newNote.id = note_data['id']
	newNote.body = note_data['body']
	newNote.author = note_data['author']
	newNote.school = note_data['school']
	newNote.major = note_data['major']
	newNote.course = note_data['course']
	newNote.instr = note_data['instr']
	newNote.unit = note_data['unit']
	newNote.section = note_data['section']
	newNote.date = note_data['date']
	return newNote