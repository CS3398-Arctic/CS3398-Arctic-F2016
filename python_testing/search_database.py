#!/user/bin/python3
import MySQLdb as mariadb

def findNoteByUser(name):
	mariadb_connection = mariadb.connect(user='root', passwd='4Rct!c', db='primary_db')
	cursor = mariadb_connection.cursor()
	query = ("SELECT note_body, created_by, note_school, note_major, "
		"note_class, note_instr, note_unit, note_section, note_ID, "
		"note_date FROM notes WHERE created_by LIKE '%s'" %(name))
	cursor.execute(query)
	for(note_body, created_by, note_school, note_major, note_class, note_instr,
		note_unit, note_section, note_ID, note_date) in cursor:
		note_dict = {
			'body' : note_body.decode('utf-8'),
			'author' : created_by,
			'school' : note_school,
			'major' : note_major,
			'course' : note_class,
			'instr' : note_instr,
			'unit' : note_unit,
			'section' : note_section,
			'id' : note_ID,
			'note_date' : note_date,
			}
		print("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (note_body.decode('utf-8'), created_by, note_date, created_by, note_school, note_major, note_class, note_instr, note_unit, note_section, note_ID, note_date))
	cursor.close()
	mariadb_connection.close()
	return note_dict

def findNoteByID(num):
	mariadb_connection = mariadb.connect(user='root', passwd='4Rct!c', db='primary_db')
	cursor = mariadb_connection.cursor()
	query = ("SELECT note_body, created_by, note_school, note_major, "
		"note_class, note_instr, note_unit, note_section, note_ID, "
		"note_date FROM notes WHERE note_ID LIKE '%s'" %(num))
	cursor.execute(query)
	for(note_body, created_by, note_school, note_major, note_class, note_instr,
		note_unit, note_section, note_ID, note_date) in cursor:
		note_dict = {
			'body' : note_body.decode('utf-8'),
			'author' : created_by,
			'school' : note_school,
			'major' : note_major,
			'course' : note_class,
			'instr' : note_instr,
			'unit' : note_unit,
			'section' : note_section,
			'note_date' : note_date,
			}
		print("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (note_body.decode('utf-8'), created_by, note_date, created_by, note_school, note_major, note_class, note_instr, note_unit, note_section, note_ID, note_date))
	cursor.close()
	mariadb_connection.close()
	return note_dict
