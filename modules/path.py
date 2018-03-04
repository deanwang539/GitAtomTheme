import os

def is_work_tree(path):
	"""Check if 'path' is a valid git working tree.
	A working tree contains a '.git' directory.

	Arguments:
	    path (string): The path to check.

	Returns:
	    bool: True if path contains a '.git'
	"""
	return path and os.path.exists('.git')
