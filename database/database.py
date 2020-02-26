import sqlite3
from pathlib import Path
import os

# Use below when run this scrip in the same dir
# path = os.path.dirname(os.path.abspath(__file__))
######

# Use below when like to chose database dir
# path = 'C:/Users/DELL/Desktop/t10/database'
######


# https://stackoverflow.com/questions/13912731/python-sqlite3-get-sqlite-connection-path
# Read command # http://osanai.org/61/

################################################################
# Get database dir path when run in another dir
def find_database_dir():

	##### Use when built app #####
	# pyinstaller mold_draw.py --debug all
	# pyinstaller mold_ui.py --debug all
	# pyinstaller mold_draw.py --noconsole
	# pyinstaller mold_ui.py --noconsole

	now_path = os.path.dirname(os.path.abspath(__file__))
	parent_dir = Path(now_path).parent.parent.parent.joinpath('database') # Database Dir
	path = str(parent_dir).replace('\\', '/')

	##### Use below when like to chose database dir / Hide when built app ##### 
	# path = 'C:/Users/DELL/Desktop/t13/database'
	##### 

	# print('\n############################################################\n')
	# print('##### Working with DATABASE: %s #####' % path)
	# print('\n############################################################\n')
	return path

################################################################
def sql(command):

	path = find_database_dir()
	DATABASE = os.path.join(path, 'database.db')
	print('############')
	print('Run comand with DATABASE: %s' % DATABASE)
	print('############')
	conn = None
	try:
		conn = sqlite3.connect(DATABASE)
		conn.execute(command)
		conn.commit()
		conn.close()
	except(Exception) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

################################################################
# Get data
def sql_get_list(command):

	path = find_database_dir()
	DATABASE = os.path.join(path, 'database.db')
	conn = None
	try:
		conn = sqlite3.connect(DATABASE)
		cur = conn.execute(command)
		return [list(i) for i in cur.fetchall()]
		conn.commit()
		conn.close()
	except (Exception) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

################################################################
# Get data to dict
def sql_get_dict(table_name):

	res = {}

	path = find_database_dir()
	DATABASE = os.path.join(path, 'database.db')
	conn = None
	command = "SELECT * from {}".format(table_name)
	try:
		conn = sqlite3.connect(str(DATABASE))
		cur = conn.execute(command)
		for row in cur.fetchall():
			res[row[0]] = row[1]
		conn.close()
	except (Exception) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
	return res

 ################## Create dimentions table ################## 
def create_table_dimentions():
	command = """
		CREATE TABLE IF NOT EXISTS dimentions
		(dimention TEXT PRIMARY KEY,
		value TEXT
		)"""
	sql(command)

################## Create setting table ################## 
def create_table_settings():
	command = """ CREATE TABLE IF NOT EXISTS settings
		(setting TEXT PRIMARY KEY,
		value TEXT)"""
	sql(command)


################################################################
def update_dimention(dimention, value):

	path = find_database_dir()
	DATABASE = os.path.join(path, 'database.db')
	conn = None

	exist_data = sql_get_dict(table_name='dimentions')
	if dimention in exist_data:
		command = """
			UPDATE dimentions SET value = '{}' WHERE dimention = '{}';
			""".format(value, dimention)
	else:
		command = """
			INSERT INTO dimentions(dimention, value) VALUES ('{}', '{}');
			""".format(dimention, value)
	try:
		conn = sqlite3.connect(DATABASE)
		conn.execute(command)
		conn.commit()
		conn.close()
	except(Exception) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

################################################################
def clear_all(table_name):
	command = 'DELETE FROM {};'.format(table_name)
	sql(command)

################################################################
def update_setting(setting, value):

	# DATABASE = 'database.db'
	path = find_database_dir()
	DATABASE = os.path.join(path, 'database.db')
	conn = None

	exist_data = sql_get_dict(table_name='settings')
	if setting in exist_data:
		command = """
			UPDATE settings SET value = '{}' WHERE setting = '{}';
			""".format(value, setting)
	else:
		command = """
			INSERT INTO settings(setting, value) VALUES ('{}', '{}');
			""".format(setting, value)
	try:
		conn = sqlite3.connect(DATABASE)
		conn.execute(command)
		conn.commit()
		conn.close()
	except(Exception) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()

################################################################
if __name__ == '__main__':

# Clear all
	# clear_all(table_name='dimentions')
	# clear_all(table_name='settings')

# See all
	print(sql_get_dict(table_name='dimentions'))
	print(sql_get_dict(table_name='settings'))

# Create dimentions table #  #REAL
	# command = """
	# 	CREATE TABLE IF NOT EXISTS dimentions
	# 	(dimention TEXT PRIMARY KEY,
	# 	value TEXT
	# 	)"""
	# sql(command)

# Create setting table
	# command = """ CREATE TABLE IF NOT EXISTS settings
	# 	(setting TEXT PRIMARY KEY,
	# 	value TEXT)"""
	# sql(command)


# Insert
	# update_dimention(dimention='t_rpl', value='')
	# update_setting(setting='save_path', value='bbb')



# See
	# command = """SELECT value FROM dimentions
	# 	WHERE dimention = w1;
	# 	"""
	# sql(command)
	# print(sql_get_list(command))


	# [w1, w2, h1, h2, t1, t2, w3, h3, t3, o1, o2, o3, ej, t_gpx, t_gpy, t_gpd, t_gph, t_gpl, t_rpx, t_rpy, t_rpd, 
	#  t_ppx, t_ppy, t_ppd, t_pph, f_gpx, f_gpy, f_gpd, f_gph, f_gpl, f_spx, f_spy, f_spd, f_spd2
	#  f_spd3, f_sph, f_sph2, f_sph3, f_prx, f_pry, f_prd, f_prd2, f_prh, f_prh2,
	#  f_ppx, f_ppy, f_ppd, f_pph  ]

	# ['w1', 'w2', 'h1', 'h2', 't1', 't2', 'w3', 'h3', 't3', 'o1', 'o2', 'o3', 'ej', 't_gpx', 't_gpy', 't_gpd', 't_gph', 't_gpl', 't_rpx', 't_rpy', 't_rpd', 't_rpl', 
	#  't_ppx', 't_ppy', 't_ppd', 't_pph', 'f_gpx', 'f_gpy', 'f_gpd', 'f_gph', 'f_gpl', 'f_spx', 'f_spy', 'f_spd', 'f_spd2',
	#  'f_spd3', 'f_sph', 'f_sph2', 'f_sph3', 'f_prx', 'f_pry', 'f_prd', 'f_prd2', 'f_prh', 'f_prh2',
	#  'f_ppx', 'f_ppy', 'f_ppd', 'f_pph'  ]

	# sqlite('DELETE FROM count_limit')
	# print(sqlite_get_list('SELECT * from count_limit'))




