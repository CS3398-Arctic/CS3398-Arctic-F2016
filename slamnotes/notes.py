import itertools
import datetime
import database_store
import database_search

class note:
	pass

def store_note(body, author, school, major, course, instr, unit, section):
	"""Definition of class note. Defines note attributes and then stores
	note object into database_store.storeNote()
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
	database_store.store_note(newNote)     

def load_note_by_name(name):
	"""Creates dictionary of note that was found by author inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	notes_found = []
	database_search.find_note_by_user(name, notes_found)
	return notes_found	
	
def load_note_by_school(school):
	"""Creates dictionary of note that was found by school inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	notes_found = []
	database_search.find_note_by_school(school, notes_found)
	return notes_found
	
def load_note_by_major(major):
	"""Creates dictionary of note that was found by major inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	notes_found = []
	database_search.find_note_by_major(major, notes_found)
	return notes_found

def load_note_by_course(course):
	"""Creates dictionary of note that was found by course inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	notes_found = []
	database_search.find_note_by_course(course, notes_found)
	return notes_found

def load_note_by_instr(instr):
	"""Creates dictionary of note that was found by instructor inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	notes_found = []
	note_data = database_search.find_note_by_instr(instr, notes_found)
	return notes_found
	
def load_note_by_unit(unit):
	"""Creates dictionary of note that was found by unit inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	notes_found = []
	database_search.find_note_by_unit(unit, notes_found)
	return notes_found

def load_note_by_section(section):
	"""Creates dictionary of note that was found by section inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	notes_found = []
	database_search.find_note_by_section(section, notes_found)
	return notes_found
	
def load_note_by_id(id):
	"""Creates dictionary of note that was found by ID inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	notes_found = []
	note_data = database_search.find_note_by_id(id, notes_found)
	return notes_found

#No build for this yet, if you're calling this and it's not working, that's why.
def load_note_by_date(date):
	"""Creates dictionary of note that was found by date inside the 
	database_search.py file. Stores attributes found on Mariadb and stores them
	in dictionary's attributes. Returns the dictionary.
	"""
	newNote = note()
	notes_found = []
	database_search.find_note_by_date(date, notes_found)
	return notes_found