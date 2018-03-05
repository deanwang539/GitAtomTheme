import sublime
import sublime_plugin

try:
	from .modules import *
except ValueError:
	from modules import *
except ImportError:
    # Failed to import at least one module.
    # This can happen after upgrade due to internal structure changes.
    sublime.message_dialog(
        "GitGutter failed to reload some of its modules.\n"
        "Please restart Sublime Text!")

repo = GitRepo("C:/Study/Projects/GitAtomTheme")

print repo.is_clean()
print repo.add_del
print repo.modified
