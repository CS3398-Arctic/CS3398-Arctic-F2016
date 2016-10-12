"""
Module to handle notes.
"""

import database

class note:
    """Object to hold a note's information."""
    pass
    

def load_note (id):
    """Load a note by id, returns a note object or None.
    
    Keyword arguments:
    id -- the id of the note to load
    """
    
    if not note_exists(id):
        # No note with given id exists. 
        return None
    
    the_note = note()
    note_data = database.find_note_by_id(id)
    
    the_note.id = id
    the_note.body = note_data['body']
    the_note.author = note_data['author']
    #the_note.school = note_data['school']
    #the_note.major = note_data['major']
    #the_note.course = note_data['course']
    #the_note.instr = note_data['instr']
    #the_note.unit = note_data['unit']
    #the_note.section = note_data['section']
    the_note.note_date = note_data['note_date']
    
    return the_note
    
def note_exists (id):
    """Check if a note exists by id, returns True or False.
    
    Keyword arguments:
    id -- the id of the note to check for
    """
    
    return database.findNoteByID(id) is not None