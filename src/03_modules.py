"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print(f"This is the name of the script: { sys.argv[0] }")
print(f"Number of arguments: { len(sys.argv) }")
print(f"The arguments are: { str(sys.argv) }")

print(f"\nCommand line arguments in sys.argv: {sys.argv[0]}")

# Print out the OS platform you're using:
# YOUR CODE HERE
print("\nOS platform:")

import platform
print(f"\nOS platform: {platform.system()}")

# Print out the version of Python you're using:
# YOUR CODE HERE
print(f"\nPython version: {platform.python_version()}")


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(f"\nProcess ID: {os.getpid()}")

# Print the current working directory (cwd):
# YOUR CODE HERE
print(f"\nCurrent working directory: {os.getcwd()}")

# Print out your machine's login name
# YOUR CODE HERE
print(f"\nMachine's login name: {os.getlogin()}")
