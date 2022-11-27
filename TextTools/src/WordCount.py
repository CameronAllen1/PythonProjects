def wc(files):
    lineTotal = 0
    wordTotal = 0
    byteTotal = 0  	    	       
    for filePath in files:
        file = open(filePath)
        lines = file.readlines() # read lines
        file.seek(0) # reset cursor to beginning of file
        readFile = file.read()
        words = readFile.split() # read whole file and then split by whitespace
    
        byte = len(readFile) # get number of bytes (characters) in file

        lineTotal += len(lines)
        wordTotal += len(words)
        byteTotal += byte
        print('{lines:>5} {words:>5} {byte:>5} {filePath:>5}'.format(lines = len(lines), words = len(words), byte=byte, filePath = filePath)) #print values while right justifying them

    if len(files)>1:
        print('{0:>5} {1:>5} {2:>5} {3:>5}'.format(lineTotal, wordTotal, byteTotal, "total")) #print values while right justifying them
