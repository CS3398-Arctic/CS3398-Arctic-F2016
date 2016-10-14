#!/user/bin/python3
import MySQLdb as mariadb

def store_note(newNote):
	"""Definition of store note. Stores values into mariadb 
	database: primary_db table: notes()
	"""
	mariadb_connection = mariadb.connect(user='root', passwd='4Rct!c', db='primary_db')
	cursor = mariadb_connection.cursor()
	query = ("INSERT INTO notes VALUES (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\","
		"\"%s\", \"%s\", NULL, NOW())" % (newNote.note_body, newNote.created_by, 
		newNote.note_school, newNote.note_major, newNote.note_class, newNote.note_instr, 
		newNote.note_unit, newNote.note_section))
	cursor.execute(query)
	mariadb_connection.commit()
	cursor.close()
	mariadb_connection.close()