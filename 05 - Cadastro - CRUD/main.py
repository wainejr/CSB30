from crud_commands import *

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
	while(not(inp == QUIT['cmd']):
		inp = raw_input():
		inp = inp.split(" ")
		
		switch(
