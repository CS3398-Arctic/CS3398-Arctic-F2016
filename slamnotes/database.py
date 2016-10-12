"""
Module to handle database interaction.
"""

import MySQLdb as mariadb

def find_note_by_id (id):
    """Find a note by id, returns a dictionary with the notes' data,
    or None (TODO) if the note does not exist.
    
    Keyword arguments:
    id -- the id of the note to find
    """
    
	mariadb_connection = mariadb.connect(user='root', passwd='4Rct!c', db = 'primary_db')
	cursor = mariadb_connection.cursor()
	query = ("SELECT note_body, created_by, note_date FROM notes "
		"WHERE note_ID LIKE '%s'" %(id))
	cursor.execute(query)
	for(note_body, created_by, note_date) in cursor:
		note_dict = {
			'body' : note_body.decode('utf-8'),
			'author' : created_by,
			'note_date' : note_date,
			}
		print("%s, %s, %s " % (note_body.decode('utf-8'), created_by, note_date))
	cursor.close()
	mariadb_connection.close()
	return note_dict
