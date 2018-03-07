from .git import Repo

"""GitRepo class creats repo object that represent the local git data tree

Note:
	You only need one object per sublime opening to dynamically monitor the changes in data tree

Git Flow:
1. untracked files(new added or deleted) -> use "git add" command to stage
2. unstaged files(modified) -> use "git add" command to stage
3. all files staged -> use "git commit" to commit

GitRepo functions:
1. get_untracked_files() returns all untracked files
2. get_unstaged_files() returns all modified files
3. get_staged_files() returns all staged files preparing for commit

"""
class GitRepo(object):
	def __init__(self, path):
		self.repo = Repo(path)
		self.branch = "master"
		self.add_del = set()
		self.modified = set()

	def get_current_branch(self):
		"""Return current branch

		Returns:
		    str: current branch
		"""
		return self.repo.active_branch.name

	def get_untracked_files(self):
		"""Return untracked files(newly added or deleted)

		Returns:
		    list: file's relative path
		"""
		return self.repo.untracked_files

	def get_unstaged_files(self):
		"""Return modified files

		Returns:
		    list: file's relative path
		"""
		return [item.a_path for item in self.repo.index.diff(None)]

	def get_staged_files(self):
		"""Return staged files

		Returns:
		    list: file's relative path
		"""
		return [item.a_path for item in self.repo.index.diff("HEAD")]

	def is_clean(self):
		"""Return if git repo is clean
		update add_del and modified sets

		Returns:
		    bool
		"""
		untracked_files = self.get_untracked_files()
		unstaged_files = self.get_unstaged_files()
		staged_files = self.get_staged_files()
		current_branch = self.get_current_branch()

		# if repo is clean
		if not (untracked_files or unstaged_files or staged_files):
			self.add_del = set()
			self.modified = set()
			self.branch = current_branch
			return True

		self.branch = current_branch
		self.add_del.update(untracked_files)
		self.modified.update(unstaged_files)
		return False
