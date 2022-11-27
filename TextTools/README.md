# Text Tools!
This is a program that I made to emulate the functions of normal unix system text tools.
This program takes arguments from the command line
This includes all these tools :
```
cat
paste
cut
grep
sort
wc
```
All of these tools work exactly like the unix tools and even can take flags and multiple options.

## Running the program
You can run the program by:
```
python src/tt.py [tool] [files/options]
```
tool is the name of the tool
files are paths to files
options are flags or other extra arguments

Running `python src/tt.py [tool]` will give you a usage message on how to use that tool.