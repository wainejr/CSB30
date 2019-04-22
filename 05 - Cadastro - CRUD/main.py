from crud_commands import *
import re

def check_regex(parse, regex):
	'''
		Check if parsed input is valid, given ReGex format
		regex(list(list())): list of list of valids formats
		parse(list()): parsed input
	'''
	if(len(regex) == len(parse)):
		for i in range(0, len(regex)):
			find = False
			for fmt in regex[i]:
				x = re.search(fmt, parse[i])
				if x != None:
					find = True
			if find == False:
				return False
		return True
	else:
		return False

def parse_input(inp):
	inp = inp.split(" ", 1)
	if(inp[0] == inp[-1]): # if the input has no arguments
		return [inp[0]]
	tmp = inp[1].split(';')
	args = [i.strip() for i in tmp]
	p_inp = [inp[0]]
	for arg in args:
		p_inp.append(arg)
		p_inp.append(';') # insert ';' between arguments
	p_inp.pop() # remove last ';'
	return (p_inp)

def check_format(inp):
	try:
		if inp[0] == CMDS['ADD_FRIEND']['cmd']:
			if(check_regex(inp, CMDS['ADD_FRIEND']['re_inp'])):
				return 1
			else:
				return -1
		elif inp[0] == CMDS['DELETE']['cmd']:
			if(check_regex(inp, CMDS['DELETE']['re_inp'])):
				return 1
			else:
				return -1

		elif inp[0] == CMDS['HELP']['cmd']:
			if(check_regex(inp, CMDS['HELP']['re_inp'])):
				return 1
			else:
				return -1

		elif inp[0] == CMDS['INSERT']['cmd']:
			if(check_regex(inp, CMDS['INSERT']['re_inp'])):
				return 1
			else:
				return -1

		elif inp[0] == CMDS['LIST']['cmd']:
			if(check_regex(inp, CMDS['LIST']['re_inp'])):
				return 1
			else:
				return -1

		elif inp[0] == CMDS['QUIT']['cmd']:
			if(check_regex(inp, CMDS['QUIT']['re_inp'])):
				return 1
			else:
				return -1

		elif inp[0] == CMDS['UPDATE']['cmd']:	 
			if(check_regex(inp, CMDS['UPDATE']['re_inp'])):
				return 1
			else:
				return -1

		else:
			print('Invalid input format')
			return -1

	except Exception as e:
		print('Excepction')
		return -1

if __name__ == '__main__':
	inp = ''
	while(1): # quits when inp = CMDS['QUIT']['cmd']
		inp = input()
		db = 0
		# Parse input string
		inp = parse_input(inp)
		# Check if list of strings is valid
		if(check_format(inp) == 1):
			if(inp[0] == CMDS['INSERT']['cmd']):
				INSERT(inp, db)
			elif(inp[0] == CMDS['DELETE']['cmd']):
				DELETE(inp, db)
			elif(inp[0] == CMDS['UPDATE']['cmd']):
				UPDATE(inp, db)
			elif(inp[0] == CMDS['LIST']['cmd']):
				LIST(inp, db)
			elif(inp[0] == CMDS['ADD_FRIEND']['cmd']):
				ADD_FRIEND(inp, db)
			elif(inp[0] == CMDS['QUIT']['cmd']):
				QUIT(inp, db)
				break
			elif(inp[0] == CMDS['HELP']['cmd']):
				HELP(inp, db)
