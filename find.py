import subprocess
import os
from terminaltables import AsciiTable


def find_f(sf):
	p = subprocess.Popen(['dir',sf,'/S','/B'], shell=True, stdout=subprocess.PIPE)
	hs = list(p.communicate()); nhs = []; no = 0 
	nhs += [['NO','FILE NAME','FILE PATH']]
	hs = hs[0].splitlines() #Splitting a string separated by “\r\n” into a list of lines?	
	for l in hs:
		no += 1; nhs += [[str(no),os.path.basename(l.decode('utf-8')),l.decode('utf-8')]] #print(l)

	ltt = AsciiTable(nhs)
	print('\n\n'+ltt.table)
	
	

while True:
	try:	
		f_str = input('\n\n CARI FILE [X/x for Exit] : ')		
		if f_str == 'x' or f_str == 'X':
			exit()
		find_f(f_str)
	except:
		break
