from git import Repo
import os

if os.path.exists('.git'):
	repo = Repo()
	changedFiles = [item.a_path for item in repo.index.diff(None)]
	print repo.untracked_files  # print test: [u'test.py', u'test2.py']
	print changedFiles # print test: [u'README.md']
else:
	print '.git is not found.'