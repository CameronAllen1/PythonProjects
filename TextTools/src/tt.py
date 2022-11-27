import sys  	    	       

from Concatenate import cat, tac  	    	       
from CutPaste import cut, paste  	    	       
from Grep import grep  	    	       
from Partial import head, tail  	    	       
from Sorting import sort  	    	       
from WordCount import wc  	    	       
from Usage import usage  	    	       


def isValidField(field):
    splitField = field.split(",")
    for number in splitField:
        try:
            int(number)
        except:
            return False
    return True





if len(sys.argv) < 2:  	    	       
    usage()  	    	       
    sys.exit(1)  	    	       
else:
    tool = sys.argv[1]

if tool == "cat":
	if len(sys.argv)<3: # no arguments after cat were given
		usage(error = "Too few arguments",tool = tool )
	cat(sys.argv[2:]) #get all arguments from 2 and on.


elif tool == "tac":
	if len(sys.argv)<3:
		usage(error = "Too few arguments",tool = tool ) # I call this if statement in each tool because some of the tools have flags or different error messages.
	tac(sys.argv[2:])


elif tool == "wc":
	if len(sys.argv)<3:
		usage(error = "Too few arguments",tool = tool )
	wc(sys.argv[2:])


elif tool == "grep":
    if len(sys.argv)<4: # has at least 3 inputs (grep, pattern, filename)
        usage(error = "Please provide a pattern and at least one filename",tool = tool )
    
    if sys.argv[2] == "-v": #has the -v flag with it
        if len(sys.argv)<5: #has at least all these arguments because of flag (grep, flag, pattern, filename)
            usage(error = "Please provide a pattern and at least one filename",tool = tool )
        grep(True,sys.argv[3],sys.argv[4:]) #(flag, pattern, files)
    else:
        grep(False,sys.argv[2],sys.argv[3:])


elif tool == "head":
    if len(sys.argv)<3: # has at least 2 inputs (head, file)
        usage(error = "Too few arguments", tool = tool)
    if sys.argv[2] == "-n":
        if len(sys.argv)<5: # needs to have (head, flag, limit, file)
            usage(error = "Number of lines is required", tool = tool)

        try:
        	int(sys.argv[3]) #makes sure than N can be cast to an int. otherwise call usage
        except:
        	usage(error = "Number of lines is required", tool = tool)

        head(True, sys.argv[3], sys.argv[4:]) # (flag, limit, files)

    else:
        head(False, 10, sys.argv[2:])


elif tool == "tail": # Tail is pretty much exactly the same as head
    if len(sys.argv)<3: # has at least 2 inputs (tail, file)
        usage(error = "Too few arguments", tool = tool)
    if sys.argv[2] == "-n":
        if len(sys.argv)<5: # needs to have (tail, flag, limit, file)
            usage(error = "Number of lines is required", tool = tool)

        try:
        	int(sys.argv[3]) #makes sure than N can be cast to an int. otherwise call usage
        except:
        	usage(error = "Number of lines is required", tool = tool)

        tail(True, sys.argv[3], sys.argv[4:]) # (flag, limit, files)

    else:
        tail(False, 10, sys.argv[2:])


elif tool == "sort":
	if len(sys.argv)<3: # no arguments after sort were given
		usage(error = "Too few arguments",tool = tool )
	sort(sys.argv[2:])


elif tool == "paste":
	if len(sys.argv)<3: # no arguments after paste were given
		usage(error = "Too few arguments",tool = tool )
	paste(sys.argv[2:])



elif tool == "cut":
    if len(sys.argv)<3: # no arguments after cut were given
        usage(error = "Too few arguments",tool = tool)
    if sys.argv[2] == "-f":
        if len(sys.argv)<4: # no argument was given after the flag
            usage(error = "Too few arguments",tool = tool)
        if not(isValidField(sys.argv[3])):
            usage(error = "A comma-separated field specification is required",tool = tool)
        if len(sys.argv)<5:
            usage(error = "A comma-separated field specification is required",tool = tool) # needs to have (cut, flag, indexes, files)
        cut(True,sys.argv[3],sys.argv[4:])
    else:
        cut(False,"1",sys.argv[2:]) # gives 1 as a string cause sys.argv always gives arguments as a string and the tool uses .split() on it
    
	    	       
