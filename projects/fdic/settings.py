"""
This module contains code useful for general project-wide housekeeping.
"""
from os.path import abspath, dirname

# Use some Python magic to dynamically determine the project directory.
# __file__ is a special Python attribute that references the current 
# file. So in this case, we get the full path to "constants.py" (minus the actual file name)
# We'll use this later to build the path to our output csv.
PROJECT_DIR = abspath(dirname( __file__))

# Alternatively, you could hard-code the path:
# WINDOWS_PROJECT_DIR = 'C:\\Documents and Settings\janedoe\fdic'
# MAC_PROJECT_DIR = '/Users/janedoe/fdic'
# LINUX_PROJECT_DIR = '/home/janedoe/fdic'
