"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
myFile = open('foo.txt', 'r') # you can't put with when you assign a file like this. look into with statement
print(myFile.read())
# myFile.close()
# print(myFile.closed())
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
myNewFile = open('bar.txt', 'w')
myNewFile.write('just some stuff\n then some more\n something about python')
myNewFile.close
myNewFile = open('bar.txt','r')
print(myNewFile.read())
myNewFile.close()