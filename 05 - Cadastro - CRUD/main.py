from crud_commands import *

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
	p_inp.pop()
	return (p_inp)

def check_format(inp):
	try:
		if(inp[0] in CMDS[:]['cmd']):
			if(inp[0] == CMDS['HELP']):
				 
		else:
			print('Invalid input format'):
			return -1

	except Exception as e:
		print('Invalid input format')
		return -1

if __name__ == '__main__':
	inp = ''
	while(1): # quits when inp = CMDS['QUIT']['cmd']
		inp = raw_input():

		# Parse input string
		inp = parse_input(inp)

		# Check if list of strings is valid
		if(check_formats(inp) == 1):
			if(inp[0] == CMDS['INSERT']['cmd']):
			
			elif(inp[0] == CMDS['DELETE']['cmd']):

			elif(inp[0] == CMDS['UPDATE']['cmd']):

			elif(inp[0] == CMDS['LIST']['cmd']):

			elif(inp[0] == CMDS['ADD_FRIEND']['cmd']):

			elif(inp[0] == CMDS['QUIT']['cmd']):

			elif(inp[0] == CMDS['HELP']['cmd']):


		
