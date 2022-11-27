def grep(flag ,pattern, files):
    matches = []
    notMatches = []
    for filePath in files:
        file = open(filePath)
        lines = file.readlines()
        for line in lines:
            if pattern in line: #for each file check for matches in each line.
                matches.append(line)
            else:
                notMatches.append(line)

    if flag==False:
    	for line in matches:
    		print(line, end = '')
    else:
    	for line in notMatches:
    		print(line, end = '')