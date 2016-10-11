#!/user/bin/python3
import MySQLdb as mariadb

def findNoteByID(num):
	mariadb_connection = mariadb.connect(user='root', passwd='4Rct!c', db = 'primary_db')
	cursor = mariadb_connection.cursor()
	query = ("SELECT note_body, created_by, note_date FROM notes "
		"WHERE note_ID LIKE '%s'" %(num))
	cursor.execute(query)
	for(note_body, created_by, note_date) in cursor:
		note_dict = {
			'body' = note_body(),
			'author' = created_by,
			'note_date' = note_date,
			}
		print("%s, %s, %s " % (note_body.decode('utf-8'), created_by, note_date))
	cursor.close()
	mariadb_connection.close()
	return note_dict
