def head(flag, limit, files):
    limit = int(limit) #limit is already made sure to be able to cast to int by the tt.py driver.
    for filePath in files:
        file = open(filePath)
        lines = file.readlines()
        limitedLines = lines[:limit]
        if len(files)>1:
            if not(filePath == files[0]): # I did this just so it matches the formatting of head
            	print()#newline
            print(f"==> {filePath} <==")

        for line in limitedLines:
            print(line, end = "")
        file.close()   	
	    	       


def tail(flag, limit, files):
    limit = int(limit) #limit is already made sure to be able to cast to int by the tt.py driver.
    for filePath in files:
        file = open(filePath)
        lines = file.readlines()
        limitedLines = lines[-1*limit:]
        if len(files)>1:
            if not(filePath == files[0]): # I did this just so it matches the formatting of head
            	print()
            print(f"==> {filePath} <==")

        for line in limitedLines:
            print(line, end = "")
        file.close()    	       
