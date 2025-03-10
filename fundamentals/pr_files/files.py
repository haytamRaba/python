 # before we can read the contents of the file we must tell python which 
 # which file we are going to work with and what we will be doing with 
 # the file
 ## this is done with the : open() function
 ### open() returns a "file handle" - a var used to perform operations on
 ### on the file

#### handle = open( filename , mode )

fhand = open('words.txt')

for line in fhand:
  line=line.rstrip()
  print(line.lower())
# print by default print with a newline 