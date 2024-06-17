import sys

from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):



        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.checbox = QCheckBox("Python seviyor musunuz ? ")
        self.yazi_alani = QLabel("")
        self.buton = QPushButton("Bana tıkla")

        v_box = QVBoxLayout()

        v_box.addWidget(self.checbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.setWindowTitle("Check box")

        self.buton.clicked.connect(lambda : self.click(self.isChecked(),self.yazi_alani))


        self.show()

    def click(self,checkbox,yazi_alani):
        if checkbox:
            yazi_alani.setText("Python' ı seviyorsun")
        else:
            yazi_alani.setText("Niye sevmiyon")


app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())