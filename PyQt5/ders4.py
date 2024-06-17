import sys

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)



    pencere = QtWidgets.QWidget()
    okay = QtWidgets.QPushButton("tamam")
    cansel = QtWidgets.QPushButton("iptal")
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cansel)

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)


    pencere.setLayout(v_box)
    pencere.setWindowTitle("PyQt5 Ders 4")

    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(app.exec_())

Pencere()