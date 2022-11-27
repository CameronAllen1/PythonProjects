# Software Development Plan
* Cameron Allen

## Phase 0: Requirements Specification *(10%)*

* The goal of the textTools assignment is to recreate the basic unix text processing functions in python.
* The solution needs to deal with multiple user input arguments and needs to function almost identically to the unix commands.
* A good solution will be able to be used with the driver (tt.py) and should produce output identical to the unix commands.
* I already know how to work with text and files
* I might struggle with using the arguments from the command line in python. (I'm not super familiar with sys.argv)
* Another challenge I might face is just the sheer amount of tools. It's a lot of work and so I need to stay on track and manage my time.



## Phase 1: System Analysis *(10%)*

### INPUT OF DRIVER
* Command (The actual unix command that is being recreated in python).
* Filenames (Arguments of command).
* Flags (Some commands have optional flags).

### OUTPUT OF DRIVER
* Correctly manipulated text.
* Output can be redirected to a file or displayed in the terminal.

### INPUT OF COMMANDS
* Flags.
* Patterns
* List of filepaths/names.

### OUTPUT OF COMMANDS
* Prints correctly manipulated text.

### KEY FUNCTIONS (just some of them)
* cat( list of file paths )
    * Output : Concatenated text of all the files.
    * Function will loop over all the files provided and print out their contents in order.

* findLongestList(list of lists) - a helper function for paste
    * Output : The longest list in the input list
    * Function will loop over lists, compare the lengths, and then return the longest list.

* isValidField(field) - a helper function for the cut section of tt.py
    * Output : A true or false depending on if the field is valid.
    * Function will look at field ( a string that has integers separated by commas) and determine if it contains valid integers.

* wc (list of file paths)
    * Output : Formated line count, word count, byte count, and file paths. If there are multiple files then it will print totals.
    * Function will count lines, words and characters (bytes) of the files and display them

* grep (flag, pattern, file paths)
    * Output : Display all lines in the files that have the pattern in them. (reverse if it has the -v flag)
    * Function will loop over all the files and check each line and see if it matches.

* usage( error, tool)
    * Output : Depending on the error and the tool, the function will output an error message or a message on how to use the commands.
    * Function will look at the error and the tool and display relavant information about that tool or error.

## Phase 2: Design *(30%)*

*   **DO NOT COPY AND PASTE YOUR PYTHON CODE HERE!!!**
*   Write *pseudocode* that captures how each function works
    *   **Pseudocode != source code**
    *   If we find too much finished code here, *you will receive a zero*!
    *   It should look like *basic English* with extra indentation
*   Explain what happens to your functions in the face of *good and bad input*
    *   Make a note about *bad inputs* down in **Phase 4**; these will become your *test cases*

### cat(args : list containing filepaths):
```
def cat(args):
    for each file in args
        open the file
        print its contents
        close the file
```

### tac(args : list containing filepaths):
```
def cat(args):
    for each file in args
        open the file
        read its lines
        iterate in reverse over lines and print them
        close the file
```

### grep( flag : boolean, pattern : string, files : list containing filepaths)
```
def grep(flag ,pattern, files):
    for each file in files
        open the file and read lines
        close the file
        iterate over the lines
            if the flag is false:
                if the pattern is present in the line add the line into a matches list
            if the flag is true:
                if the pattern is present in the line add the line into a notMatches list
        print the matching lines
```
### head(flag : boolean, limit : string, files : list containing filepaths)
```
def head(flag, limit, files):
    cast limit to int (all input from sys.argv comes as a string)
    for each file:
        open file and read the lines
        get the first (limit) lines of the file(ex. if limit was 5 it would get the first 5 lines)
        if there is more than one file:
            print the header with the filepath ("==> {filePath} <==")
        print the limited lines
        close the file
```
### tail(flag : boolean, limit : string, files : list containing filepaths)
```
def tail(flag, limit, files):
    cast limit to int (all input from sys.argv comes as a string)
        for each file:
            open file and read the lines
            get the last (limit) lines of the file(ex. if limit was 5 it would get the last 5 lines)
            if there is more than one file:
                print the header with the filepath ("==> {filePath} <==")
            print the limited lines
            close the file
```
### wc(files : list containing filepaths)
```
def wc(files):
    for each file:
        open the file and read the lines
        reset file cursor and then read the whole text as a string

        get lineCount by length of readlines()
        get wordCount by length of the whole file that is split by whitespace (spaces, newlines)
        get byteCount by getting the length of the whole file

        print formatted lineCount, wordCount, and byteCount
```
### cut(flag : boolean, indexes : string, files : list of filepaths)
```
def cut(flag,indexs,files):
    split indexes by commas (indexes is a field of integers separated by commas that comes in as a string)
    cast indexes to ints and ignore if less than 1 (indexes start from 1)

    for each file:
        open the file
        read the lines
        close the file

    for each line:
        split the line by commas and get rid of the newline on the end
        add the split lines to a list called allLines (specific words can be accessed from allLines by [column][row])

    for each line in allLines:
        for each row:
            if row is in the indexes:
                print the word at allLines[line][row]
                print comma if its not the only or last one in the row
        print a newline

```
### findLongestList(lists : a list filled with lists)
```
def findLongestList(lists):
    set a maxLength to zero
    set the longestList to the first list
    for each list:
        if the list is longer than maxLength:
            update maxLength
            update longestList
    return the longestList
```
### paste(files : list containing filepaths):
```
def paste(files):
    for each file:
        read lines

        findLongestList() of the lines

        for each row and column:
            get the field of a line (lines[row])
            if column is in range for the field:
                print the word at that column
            print commas between words and a newline between lines
```
### sort(files : list containing filepaths)
```
def sort(files):
    for each file:
        read the file
        add all of the lines to a list
        close the file
    use python's sort() on the list
    print all the lines in the list    
```
### isValidField(field : string)
* a helper function for the cut section of tt.py. a field is a string with ints separated by commas. validates by checking if all the numbers can be cast to ints. 
```
def isValidField(field):
    split the field by commas
    try to cast the numbers to ints
    if it didn't work:
        return false
    else:
        return true
```

### usuage(error : string , tool : the tool that threw the error)
```
def usage(error = None, tool = None):
    if there is no error or tool input:
        print general usage for all of the tools
    otherwise print the error and the usage for the specified tool
```



## Phase 3: Implementation *(15%)*

*   **DO NOT COPY AND PASTE YOUR PYTHON CODE HERE!!!**
*   Write *code* in the `src/` directory
    *   Copy the outlines from Phase 2 into your `.py` files, and *translate* from English into Python
*   As you translate, you will *encounter problems* that were not foreseen earlier
    *   E.g. things that you learned, things that didn't go according to plan, etc.
    *   Here you can write a brief description of *what* changed and *why*
*   If everything went swimmingly, say so here


* During implementation I was able to get the correct values, but the text formatting (newlines, commas) was difficult. I learned to slice strings to avoid the newlines at the end when they come from readlines().
* Cut and Paste were the most difficult for me. They're hard to understand because of all the loops and different files and lines that you have to work with.
* Originally for wordcount I was reading the file with read() and then splitting it by whitespace. This seemed to work but actually added an empty string to the result. This caused my line count to be off. Fixed by switching to use readlines().
* Other than formatting issues, the problems were pretty easy for me to solve.
* Implementation took a bit longer than I expected. This was mostly due to me getting distracted and also the formatting issues.

## Phase 4: Testing & Debugging *(30%)*

*   For the bad inputs you thought of back in **Phase 2**, write a *test case* that you can run to prove that your functions work as expected
    *   It is not necessarily bad if a function crashes if you can explain *why* and *how* it happens
*   Write the test cases you have *personally run*
    *   The *exact command* you used
    *   Copy & paste the program's *output*
    *   Be precise so that your grader can replicate your experience
*   For any bugs discovered, describe their *cause* and *remedy*

* Bad Input:
    * Missing flags
    * Missing values for flags
    * Missing files or unaccessable files
    * Too few arguments
    * Incorrect type of arguments (ex. putting an int where a flag is expected)

* I was very conscious of the possible bad input a user could put in and tried to catch all of it in tt.py.

### Test Cases
* Because there are just so many tools these are the general tests I did for each of them. I also did specific tests for the tools that have unique inputs.
```
testing too few arguments
py src/tt.py cat|tac|grep|wc|cut|paste|sort|head|tail
Error: Too few arguments

        {error message and usage for tool}
```
```
testing non accessable file
py src/tt.py tool (options) FILE_DNE
    file = open(filePath)
FileNotFoundError: [Errno 2] No such file or directory: 'FILE_DNE'
```
```
testing no arguments after flag
py src/tt.py grep|tail|head|cut -flag

Error: Too few arguments

        {error message and usage for tool}
```
```
testing invalid field for cut
py src/tt.py cut -f abc data/names8

Error: A comma-separated field specification is required

        tt.py cut [-f LIST] FILENAME...
    Remove comma-separated sections from each line of files
    -f  List of comma-separated integers indicating fields to output (default is LIST=1)
```

```
Also ran the testInvalidUsage script but I still did a lot of manual testing because I don't think it covers ALL of the cases
./scripts/testInvalidUsage.sh

Gracefully handle invalid usages of the tools
TEST$ py src/tt.py head -n data/forgot_number
Error: Number of lines is required

        tt.py head|tail [-n N] FILENAME...
    Output the first or last part of files
    -n  Number of lines to print (default is N=10)
TEST$ py src/tt.py tail -n data/forgot_number
Error: Number of lines is required

        tt.py head|tail [-n N] FILENAME...
    Output the first or last part of files
    -n  Number of lines to print (default is N=10)
TEST$ py src/tt.py grep ONLY_PATTERN
Error: Please provide a pattern and at least one filename

        tt.py grep [-v] PATTERN FILENAME...
    Print lines of files matching PATTERN
    -v  Invert matching; print lines which DO NOT match PATTERN
TEST$ py src/tt.py grep -v ONLY_PATTERN
Error: Please provide a pattern and at least one filename

        tt.py grep [-v] PATTERN FILENAME...
    Print lines of files matching PATTERN
    -v  Invert matching; print lines which DO NOT match PATTERN
TEST$ py src/tt.py cut -f data/forgot_field
Error: A comma-separated field specification is required

        tt.py cut [-f LIST] FILENAME...
    Remove comma-separated sections from each line of files
    -f  List of comma-separated integers indicating fields to output (default is LIST=1)
```
* I tested my bad input cases as I was implementing so it should be okay.

## Phase 5: Deployment *(5%)*

*   *Important:* complete **Phase 6** first!
    *   (I know it's backwards, just go with it)
*   **YOU DON'T NEED TO WRITE ANYTHING IN THIS PHASE**
    *   Just follow this checklist
*   **Push** your final commit to GitLab
*   **Verify** that your final commit was received by *browsing* to its project page on GitLab
    *   Ensure the project's *URL is correct*
    *   Review that all required files are present *in the correct location*
    *   Check that unwanted files *have not* been committed
    *   Add *final touches* to your documentation, including the Sprint Signature and this Plan
*   **Validate** that your submission is complete and correct by *cloning* it to a new location on your computer and re-running it
	*	Run your program from the *command line* so you can see how it will behave when your grader runs it
        *   **Testing in PyCharm is not good enough!**
    *   Re-run your *test cases* to avoid nasty surprises



## Phase 6: Maintenance

* If a bug was reported, It would probably take me around a day or two to fix it completely. I think the area thats most likely to break is my tt.py driver.
* I put comments explaining things when they could be unclear throughout my code. I believe other people and my future self will be able to understand it.
* The tt.py driver is probably the sloppiest and hard to understand part of the project.
* The reason for this is because I put all of the conditions for each tool in the same place. A better practice might be to separate it into different functions or files.
* I believe that my program should work on capable hardware and across operating systems.
* The only issue I could see is because of the difference between the newline characters of windows and unix systems. I think that readlines() takes care of this problem so it should still work.
