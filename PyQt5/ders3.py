import sys

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    buton = QtWidgets.QPushButton(pencere)
    buton.setText("burası bir butondur")
    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("merhaba dünya")
    etiket.move(200,30)
    buton.move(180,80)

    pencere.setWindowTitle("PyQt5 Ders 3")

    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(app.exec_())

Pencere()