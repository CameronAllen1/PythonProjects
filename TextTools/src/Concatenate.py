def cat(args):
    for filePath in args:
        file = open(filePath)
        print(file.read(),end='') #print everything except the newline
        file.close()   	       
    # Chose not to concate file contents into one string for memory concerns. If the files are really big it could cause a huge string and not be good. Why not just print one at a time to the terminal? 	    	       


def tac(args):
    for filePath in args:
        file = open(filePath)
        lines = file.readlines()
        for line in reversed(lines):
        	print(line,end='')
        file.close()