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
		for i in CMDS:
			if inp[0] == CMDS[i]['cmd']:
				if(check_regex(inp, CMDS[i]['re_inp'])):
					return 1
		print('Invalid input format')
		return -1
	except Exception as e:
		print(e)
		return -1

if __name__ == '__main__':
	inp = ''
	db = "dbname='1901vaTapaueR' user='1901vaTapaueR' host='200.134.10.32' password='413189'"
	while(1): # quits when inp = CMDS['QUIT']['cmd']
		print("\nEnter a command: (use -h to get some help)")
		inp = input()
		# Parse input string
		inp = parse_input(inp)
		# Check if list of strings is valid
		if(check_format(inp) == 1):
			args = []
			for i in inp:
				if i != ';':
					args.append(i)
			if(inp[0] == CMDS['INSERT']['cmd']):
				INSERT(args, db)
			elif(inp[0] == CMDS['DELETE']['cmd']):
				DELETE(args, db)
			elif(inp[0] == CMDS['UPDATE']['cmd']):
				UPDATE(args, db)
			elif(inp[0] == CMDS['LIST']['cmd']):
				LIST(args, db)
			elif(inp[0] == CMDS['ADD_FRIEND']['cmd']):
				ADD_FRIEND(args, db)
			elif(inp[0] == CMDS['QUIT']['cmd']):
				QUIT(args, db)
				break
			elif(inp[0] == CMDS['HELP']['cmd']):
				HELP(args, db)
