import sys

from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QVBoxLayout,QPushButton

class Pencere(QWidget):
    def __init__(self):

        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.radyo_yazisi = QLabel("Hangi dili daha çok seviyorsun")
        self.java = QRadioButton("Java")
        self.python = QRadioButton("Python")
        self.php = QRadioButton("Php")

        self.yazi_alani = QLabel("")
        self.buton = QPushButton("Gönder")

        v_box = QVBoxLayout()
        v_box.addWidget(self.radyo_yazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.php)
        v_box.addWidget(self.python)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)



        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.buton.clicked.connect(lambda : self.click(self.python.isChecked(),self.java.isChecked(),self.php.isChecked(),self.yazi_alani))

        self.setWindowTitle("Radio buton")

        self.show()

    def click(self,pyhton,java,php,yazi_alaani):
        if python:
            yazi_alaani.setText("Python")
        elif php:
            yazi_alaani.setText("Php")
        elif java:
            yazi_alaani.setText("Java")

app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())

