'''
COMMANDS = {
	OPERATION_1: {
		'cmd': command, 
		'fmt': command format,
		'decr':command description
	},
	OPERATION_2: {
		'cmd': command, 
		'fmt': command format,
		're_inp': ReGex input format,
		'decr': command description			
	},
	...
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
		'fmt':'[LOGIN || NAME] ; NEW_NAME ; NEW_HOMETOWN',
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
		'fmt':'[LOGIN_1 || NAME_1] ; [LOGIN_2 || NAME_2]',
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
