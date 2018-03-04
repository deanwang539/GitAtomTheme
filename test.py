from git import Repo
repo = Repo()
print repo.index.diff("HEAD")
print repo.index.diff(None)
