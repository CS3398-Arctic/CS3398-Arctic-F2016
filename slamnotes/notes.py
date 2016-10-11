import itertools
import datetime
from . import search_database

class note:
    pass
    

def loadNote(id):
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
        
   
