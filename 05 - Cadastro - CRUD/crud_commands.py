'''
COMMANDS = {
	COMMAND_NAME: {
		'cmd': command, 
		'fmt': command format,
		're_inp': ReGex arguments format,
		'decr':command description
	}, ...
}
'''

CMDS = {
	'INSERT':{
		'cmd':'-i',
		'fmt':'NAME ; HOMETOWN',
		're_inp':[['-i'],['.+'],[';'],['.+']],
		'dcr':'Insert person on database'
	},
	'DELETE':{
		'cmd':'-d',
		'fmt':'LOGIN || NAME',
		're_inp':[['-d'],['[0-9]+','.+']],
		'dcr':'Delete person of database'
	},
	'UPDATE':{
		'cmd':'-u',
		'fmt':'LOGIN || NAME ; NEW_NAME ; NEW_HOMETOWN',
		're_inp':[['-u'],['[0-9]+','.+'],[';'],['.+'], [';'], ['.+']],
		'dcr':'update person on database'
	},
	'LIST':{
		'cmd':'-l',
		'fmt':'',
		're_inp':[['-l']],		
		'dcr':'List persons on database'
	},
	'ADD_FRIEND':{
		'cmd':'-a',
		'fmt':'LOGIN_1 || NAME_1 ; LOGIN_2 || NAME_2',
		're_inp':[['-a'],['[0-9]+','.+'],[';'],['[0-9]+','.+']],
		'dcr':'Adds friend relationship'		
	},
	'QUIT':{
		'cmd':'-q',
		'fmt':'',
		're_inp':[['-q']],
		'dcr':'Quits application'
	},
	'HELP':{
		'cmd':'-h',
		'fmt':'',
		're_inp':[['-h']],
		'dcr':'Prints commands, its format and description'
	}
}


def HELP(args, db):
	'''
		Prints all commands format and description
		args[0]: '-h'
		db: database
	'''	
	sorted_cmds = []	
	for i in CMDS:
		sorted_cmds.append(i)
	sorted_cmds.sort()
	for i in sorted_cmds: # prints commands in alphabetic order
		print(i +": " + CMDS[i]['cmd'] + " " + CMDS[i]['fmt'])
		print(CMDS[i]['dcr'] + "\n")


def QUIT(args, db):
	'''
		Does things that has to do on quiting
		args[0]: '-q'
		db: database
	'''
	print("Quitting...")	
	a = 0


def ADD_FRIEND(args, db):
	'''
		Add friend relationship to database if possible
		args[0]: '-a'
		args[1]: NAME OR LOGIN of person 1
		args[2]: NAME OR LOGIN of person 2
		db: database
	'''
	print("Adding friends relationship...")
	a = 0


def LIST(args, db):
	'''
		Prints list of persons on database
		args[0]: '-l'
		db: database
	'''
	print("Listing persons...")
	a = 0


def UPDATE(args, db):
	'''
		Update person on database
		args[0]: '-u'
		args[1]: NAME or LOGIN of person to update
		args[2]: new person's name
		args[3]: new person's hometown
		db: database
	'''
	print("Updatin person...")
	a = 0


def DELETE(args, db):
	'''
		Delete person of database
		args[0]: '-d'
		args[1]: NAME or LOGIN of person to delete
		db: database
	'''
	print("Deleting person...")
	a = 0


def INSERT(args, db):
	'''
		Insert person on database
		args[0]: '-i'
		args[1]: person's name
		args[2]: person's hometown
		db: database
	'''
	print("Inserting person...")
	a = 0

