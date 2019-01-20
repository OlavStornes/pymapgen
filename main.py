import sys
from gui import Ui_MainWindow
import simplex.Simplexworldgen as sw
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QStylePainter, QGraphicsRectItem, QGraphicsScene
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
            'calc_c': self.ui.inputCalcC.value()
        }

        simplex = sw.SimplexGenerator(self.ui.creationBar, args)
        elevation = simplex.createelevation()

        for y in range(0, args['height']):
            for x in range(0, args['length']):
                item = QGraphicsRectItem(3 * x, 3 * y, 3, 3)
                item.setBrush(QColor(*simplex.decidebiome(elevation[y][x])))
                self.scene.addItem(item)

    def generateButton(self):
        self.simplex_run()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
