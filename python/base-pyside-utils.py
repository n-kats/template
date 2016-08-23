from PySide.QtCore import QObject
def _enter(self):
	return self

def _exit(self, *args):
	pass

QObject.__enter__ = _enter
QObject.__exit__ = _exit
