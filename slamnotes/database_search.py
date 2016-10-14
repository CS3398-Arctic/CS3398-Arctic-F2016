#!/user/bin/python3
import MySQLdb as mariadb

def find_note_by_user(name, notes_found):
	"""connects/searches: mariadb, database: primary_db, table: notes,
	for all notes created by a user, stores them in a list, returns list.
	"""
	mariadb_connection = mariadb.connect(user='root', passwd='4Rct!c', 
	db='primary_db')
	cursor = mariadb_connection.cursor()
	query = ("SELECT note_body, created_by, note_school, note_major, "
		"note_course, note_instr, note_unit, note_section, note_ID, "
		"note_date FROM notes WHERE created_by LIKE '%s'" %(name))
	cursor.execute(query)
	for(note_body, created_by, note_school, note_major, 
		note_course, note_instr, note_unit, note_section, note_ID, 
		note_date) in cursor:
		note_dict = {
			'body' : note_body.decode('utf-8'),
			'author' : created_by,
			'school' : note_school,
			'major' : note_major,
			'course' : note_course,
			'instr' : note_instr,
			'unit' : note_unit,
			'section' : note_section,
			'id' : note_ID,
			'date' : note_date,
			}
		notes_found.append(note_dict)
	cursor.close()
	mariadb_connection.close()
	return notes_found
	
def find_note_by_school(school, notes_found):
	"""connects/searches: mariadb, database: primary_db, table: notes,
	for all notes related to a school, stores them in a list,
	returns list.
	"""
	mariadb_connection = mariadb.connect(user='root', passwd='4Rct!c', 
	db='primary_db')
	cursor = mariadb_connection.cursor()
	query = ("SELECT note_body, created_by, note_school, note_major, "
		"note_course, note_instr, note_unit, note_section, note_ID, "
		"note_date FROM notes WHERE note_school LIKE '%s'" %(school))
	cursor.execute(query)
	for(note_body, created_by, note_school, note_major, note_course, 
		note_instr, note_unit, note_section, note_ID, note_date) in cursor:
		note_dict = {
			'body' : note_body.decode('utf-8'),
			'author' : created_by,
			'school' : note_school,
			'major' : note_major,
			'course' : note_course,
			'instr' : note_instr,
			'unit' : note_unit,
			'section' : note_section,
			'id' : note_ID,
			'date' : note_date,
			}
		notes_found.append(note_dict)
	cursor.close()
	mariadb_connection.close()
	return notes_found

def find_note_by_major(major, notes_found):
	"""connects/searches: mariadb, database: primary_db, table: notes,
	for all notes related to a major, stores them in a list,
	returns list.
	"""
	mariadb_connection = mariadb.connect(user='root', passwd='4Rct!c', 
	db='primary_db')
	cursor = mariadb_connection.cursor()
	query = ("SELECT note_body, created_by, note_school, note_major, "
		"note_course, note_instr, note_unit, note_section, note_ID, "
		"note_date FROM notes WHERE note_major LIKE '%s'" %(major))
	cursor.execute(query)
	for(note_body, created_by, note_school, note_major, note_course, 
		note_instr, note_unit, note_section, note_ID, note_date) in cursor:
		note_dict = {
			'body' : note_body.decode('utf-8'),
			'author' : created_by,
			'school' : note_school,
			'major' : note_major,
			'course' : note_course,
			'instr' : note_instr,
			'unit' : note_unit,
			'section' : note_section,
			'id' : note_ID,
			'date' : note_date,
			}
		notes_found.append(note_dict)
	cursor.close()
	mariadb_connection.close()
	return notes_found

def find_note_by_course(course, notes_found):
	"""connects/searches: mariadb, database: primary_db, table: notes,
	for all notes related to a course, stores them in a list,
	returns list.
	"""
	mariadb_connection = mariadb.connect(user='root', passwd='4Rct!c', 
	db='primary_db')
	cursor = mariadb_connection.cursor()
	query = ("SELECT note_body, created_by, note_school, note_major, "
		"note_course, note_instr, note_unit, note_section, note_ID, "
		"note_date FROM notes WHERE note_course LIKE '%s'" %(course))
	cursor.execute(query)
	for(note_body, created_by, note_school, note_major, note_course, 
		note_instr, note_unit, note_section, note_ID, note_date) in cursor:
		note_dict = {
			'body' : note_body.decode('utf-8'),
			'author' : created_by,
			'school' : note_school,
			'major' : note_major,
			'course' : note_course,
			'instr' : note_instr,
			'unit' : note_unit,
			'section' : note_section,
			'id' : note_ID,
			'date' : note_date,
			}
		notes_found.append(note_dict)
	cursor.close()
	mariadb_connection.close()
	return notes_found

def find_note_by_instr(instr, notes_found):
	"""connects/searches: mariadb, database: primary_db, table: notes,
	for all notes related to an instructor, stores them in a list,
	returns list.
	"""
	mariadb_connection = mariadb.connect(user='root', passwd='4Rct!c', 
	db='primary_db')
	cursor = mariadb_connection.cursor()
	query = ("SELECT note_body, created_by, note_school, note_major, "
		"note_course, note_instr, note_unit, note_section, note_ID, "
		"note_date FROM notes WHERE note_instr LIKE '%s'" %(instr))
	cursor.execute(query)
	for(note_body, created_by, note_school, note_major, note_course, 
		note_instr, note_unit, note_section, note_ID, note_date) in cursor:
		note_dict = {
			'body' : note_body.decode('utf-8'),
			'author' : created_by,
			'school' : note_school,
			'major' : note_major,
			'course' : note_course,
			'instr' : note_instr,
			'unit' : note_unit,
			'section' : note_section,
			'id' : note_ID,
			'date' : note_date,
			}
		notes_found.append(note_dict)
	cursor.close()
	mariadb_connection.close()
	return notes_found
	
def find_note_by_unit(unit, notes_found):
	"""connects/searches: mariadb, database: primary_db, table: notes,
	for all notes related to a class unit, stores them in a list,
	returns list.
	"""
	mariadb_connection = mariadb.connect(user='root', passwd='4Rct!c', 
	db='primary_db')
	cursor = mariadb_connection.cursor()
	query = ("SELECT note_body, created_by, note_school, note_major, "
		"note_course, note_instr, note_unit, note_section, note_ID, "
		"note_date FROM notes WHERE note_unit LIKE '%s'" %(unit))
	cursor.execute(query)
	for(note_body, created_by, note_school, note_major, note_course, 
		note_instr, note_unit, note_section, note_ID, note_date) in cursor:
		note_dict = {
			'body' : note_body.decode('utf-8'),
			'author' : created_by,
			'school' : note_school,
			'major' : note_major,
			'course' : note_course,
			'instr' : note_instr,
			'unit' : note_unit,
			'section' : note_section,
			'id' : note_ID,
			'date' : note_date,
			}
		notes_found.append(note_dict)
	cursor.close()
	mariadb_connection.close()
	return notes_found
	
def find_note_by_section(section, notes_found):
	"""connects/searches: mariadb, database: primary_db, table: notes,
	for all notes related to a section, stores them in a list,
	returns list.
	"""
	mariadb_connection = mariadb.connect(user='root', passwd='4Rct!c', 
	db='primary_db')
	cursor = mariadb_connection.cursor()
	query = ("SELECT note_body, created_by, note_school, note_major, "
		"note_course, note_instr, note_unit, note_section, note_ID, "
		"note_date FROM notes WHERE note_section LIKE '%s'" %(section))
	cursor.execute(query)
	for(note_body, created_by, note_school, note_major, note_course, 
		note_instr, note_unit, note_section, note_ID, note_date) in cursor:
		note_dict = {
			'body' : note_body.decode('utf-8'),
			'author' : created_by,
			'school' : note_school,
			'major' : note_major,
			'course' : note_course,
			'instr' : note_instr,
			'unit' : note_unit,
			'section' : note_section,
			'id' : note_ID,
			'date' : note_date,
			}
		notes_found.append(note_dict)
	cursor.close()
	mariadb_connection.close()
	return notes_found

def find_note_by_id(id, notes_found):
	"""connects/searches: mariadb, database: primary_db, table: notes,
	for a particular note by its id #, stores it in a list
	and returns a very lonely dictionary.
	"""	
	mariadb_connection = mariadb.connect(user='root', passwd='4Rct!c', 
	db='primary_db')
	cursor = mariadb_connection.cursor()
	query = ("SELECT note_body, created_by, note_school, note_major, "
		"note_course, note_instr, note_unit, note_section, note_ID, "
		"note_date FROM notes WHERE note_ID LIKE '%s'" %(id))
	cursor.execute(query)
	for(note_body, created_by, note_school, note_major, note_course, 
		note_instr, note_unit, note_section, note_ID, note_date) in cursor:
		note_dict = {
			'body' : note_body.decode('utf-8'),
			'author' : created_by,
			'school' : note_school,
			'major' : note_major,
			'course' : note_course,
			'instr' : note_instr,
			'unit' : note_unit,
			'section' : note_section,
			'id' : note_ID,
			'date' : note_date,
			}
		notes_found.append(note_dict)
	cursor.close()
	mariadb_connection.close()
	return notes_found