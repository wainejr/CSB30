'''
COMMANDS = {
	OPERATION_1: {
		'cmd': command, 
		'fmt': command format,
		'decr': command description			
	},
	OPERATION_2: {
		'cmd': command, 
		'fmt': command format,
		'decr': command description			
	},
	...
}
'''
CMDS = {

	'INSERT':{
		'cmd':'-i',
		'fmt':'NAME HOMETOWN',
		'dcr':'Insert person on database'
	},
	'DELETE':{
		'cmd':'-d',
		'fmt':'LOGIN || NAME',
		'dcr':'Delete person of database'
	},
	'UPDATE':{
		'cmd':'-u',
		'fmt':'[LOGIN || NAME] NEW_NAME NEW_HOMETOWN' 
		'dcr':'update person on database',
	},
	'LIST':{
		'cmd':'-l',
		'fmt':'',
		'dcr':'List persons on database'
	},
	'ADD_FRIEND':{
		'cmd':'-a',
		'fmt':'[LOGIN_1 || NAME_1] [LOGIN_2 || NAME_2]',
		'dcr':'Adds friend relationship'		
	},
	'QUIT':{
		'cmd':'-q',
		'fmt':'',
		'dcr':'Quits application'
	},
	'HELP':{
		'cmd':'-h',
		'dcr':'Prints commands, its format and description'
	}
}
