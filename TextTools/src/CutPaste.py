def cut(flag,indexs,files):
    indexs = indexs.split(",")
    for i in range(0,len(indexs)):
        indexs[i] = int(indexs[i])
        if indexs[i]<1: #starts at 1
            return
    
    for filePath in files:
        file = open(filePath)
        lines = file.readlines()
        file.close()
        
        allLines = []     #[column][row]
        for line in lines:
            splitLine = line[:-1].split(",") #[:-1] to avoid the newline
            allLines.append(splitLine)

        for line in allLines:
                for row in range(0,len(line)):
                    if row+1 in indexs:
                        print(line[row], end = '')

                        if row<len(indexs) and row>0:
                            print(",", end='')
                print()



def findLongestList(lists): # helper function for paste. finds the longest list out of lists.
    maxLength = 0
    longest = lists[0]
    for l in lists:
    	if len(l)>maxLength:
    		maxLength = len(l)
    		longest = l
    return longest


def paste(files):
    lines = [] # list of the lines for each file
    for filePath in files:
        file = open(filePath)
        lines.append(file.readlines())
        file.close()

    longestFile = findLongestList(lines) #get the list of lines from the longest file
    
    for column in range(0, len(longestFile)):# from 0 to the length of the longest file
        for row in range(0,len(files)):# from 0 to the number of files
            field = lines[row] # this is the list of lines from a file

            if column<len(field):# make sure it doesn't try to print indexes that don't exist
                print(field[column][:-1], end = '') #[:-1] to avoid the newline character.
            
            if row<len(files)-1:
                print(",", end = '') # only print ',' after the word if its not the last column
        print() # newline
