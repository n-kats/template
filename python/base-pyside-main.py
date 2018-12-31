import sys
import utils
from PySide.QtGui import QApplication, QWidget

if __name__ == '__main__':
	with QApplication(sys.argv) as app:
		with QWidget() as window:
			window.show()
		sys.exit(app.exec_())
