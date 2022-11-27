def sort(files):
    allLines = []
    for filePath in files:
        file = open(filePath)
        for line in file.readlines():
        	allLines.append(line)
        file.close()
    allLines.sort()

    for line in allLines: #for each file that contributed to allLines
    	print(line, end = '')  	    	       
    	       
