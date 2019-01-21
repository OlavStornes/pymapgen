import sys
from gui import Ui_MainWindow
import simplex.Simplexworldgen as sw
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsRectItem, QGraphicsScene
from PyQt5.QtGui import QPainter, QColor, QPen


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_graphics()

        self.show()

    def init_graphics(self):
        self.scene = QGraphicsScene(self.ui.MainImage)
        self.ui.MainImage.setScene(self.scene)

    def simplex_run(self):

        args = {
            'height': self.ui.inputHeight.value(),
            'length': self.ui.inputLength.value(),
            'calc_a': self.ui.inputCalcA.value(),
            'calc_b': self.ui.inputCalcB.value(),
            'calc_c': self.ui.inputCalcC.value(),
            'gradual': self.ui.inputGradual.checkState()
        }

        simplex = sw.SimplexGenerator(args)
        self.ui.creationBar.setMaximum(args.get('height') * args.get('length'))

        counter = 0
        for p in simplex.createelevation():
            counter += 1
            item = QGraphicsRectItem(3 * p.get('x'), 3 * p.get('y'), 3, 3)
            item.setBrush(QColor(*simplex.decidebiome(p.get('elev'))))
            self.scene.addItem(item)
            self.ui.creationBar.setValue(counter)
            if args.get('gradual'):
                # Update for each 100th pixel to keep performance so-and-so
                if counter % 100 == 0:
                    QApplication.processEvents()

    def generateButton(self):
        self.simplex_run()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
