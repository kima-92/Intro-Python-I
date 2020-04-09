"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# Modes
"""
'r'     The file will be READ only  (default, if no argument is passed in)
'w'     The file will be WRITE only (an existing file with the same name will be erased)
'a'     Opens the file for APPENDING; Any data written to the file ia atomatically ADDED TO THE END
'+r'    Opens the file for both READING and WRITING
"""

# YOUR CODE HERE
with open("foo.txt", "r") as foo:
    data = foo.read()
    print(data)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open("bar.txt", "w") as bar:

    text = ("""Praise the rain; the seagull dive
The curl of plant, the raven talk—
Praise the hurt, the house slack
The stand of trees, the dignity—
Praise the dark, the moon cradle
The sky fall, the bear sleep—
Praise the mist, the warrior name
The earth eclipse, the...""")

    bar.write(text)