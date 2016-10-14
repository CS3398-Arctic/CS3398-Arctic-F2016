#!/usr/bin/python3
#from ./slamnotes/slamnotes
import notes

def is_empty(found_notes):
	if found_notes:
		return False
	else:
		return True
		
found_notes = []

print("##############START##########START###############START#############START##############START################")

name = 'TestUser1'
found_notes = notes.load_note_by_name(name)
while is_empty(found_notes) == False:
	note = found_notes.pop()
	print(note)

print("############################################################################################################")

school = 'Texas State University'
found_notes = notes.load_note_by_school(school)
while is_empty(found_notes) == False:
	note = found_notes.pop()
	print(note)
	
print("############################################################################################################")

major = 'Classics'
found_notes = notes.load_note_by_major(major)
while is_empty(found_notes) == False:
	note = found_notes.pop()
	print(note)

print("############################################################################################################")

course = 'Literature 1311'
found_notes = notes.load_note_by_course(course)
while is_empty(found_notes) == False:
	note = found_notes.pop()
	print(note)
	
print("############################################################################################################")

instr = 'Adamson'
found_notes = notes.load_note_by_instr(instr)
while is_empty(found_notes) == False:
	note = found_notes.pop()
	print(note)
	
print("############################################################################################################")

unit = 'II'
found_notes = notes.load_note_by_unit(unit)
while is_empty(found_notes) == False:
	note = found_notes.pop()
	print(note)

print("############################################################################################################")

section = '1'
found_notes = notes.load_note_by_section(section)
while is_empty(found_notes) == False:
	note = found_notes.pop()
	print(note)

print("############################################################################################################")

test_ID = 1
found_notes = notes.load_note_by_id(test_ID)
while is_empty(found_notes) == False:
	note = found_notes.pop()
	print(note)


#submission testing, functional, ignore for now
"""notes.store_note("This was created for the express purpose of searching for multiple notes by"
				"the same author.", 
				"TestUser1", "Texas State University", "Classics", "Latin Graphical Design", 
				"Nero", "II", "IX")
"""
print("################END#############END###############END###############END##################END################")