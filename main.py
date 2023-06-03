from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice, QPoint
from PyQt5 import QtCore, QtWidgets
import sys

class AppStm(QMainWindow):
    def __init__(self):
      super(AppStm, self).__init__()
      loadUi('diseño.ui', self)

      self.click_posicion = QPoint()
      self.minimizar.clicked.connect(lambda: self.showMinimized())
      self.cerrar.clicked.connect(lambda: self.close())

      #Eliminar ventana de windows
      self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
      self.setWindowOpacity(1)
      self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
      self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

      #Tamaño de pantalla
      self.gripSize =10
      self.grip =  QtWidgets.QSizeGrip(self)
      self.grip.resize(self.gripSize, self.gripSize)
      #para poder mover ventana
      self.head.mouseMoveEvent= self.mover_ventana

      #conexion
      self.serial = QSerialPort()
      self.actualizar.clicked.connect(self.read_ports)
      self.conectar.clicked.connect(self.serial_connect)
      self.desconectar.clicked.connect(lambda: self.serial.close())
      #lectura de datos
      self.serial.readyRead.connect(self.read_data)
      #botones
      self.led1.clicked.connect(lambda: self.control_led1("click"))
      self.led1off.clicked.connect(lambda: self.control_led1off("click"))
      self.led2.clicked.connect(lambda: self.control_led2("click"))
      self.led2off.clicked.connect(lambda: self.control_led2off("click"))
      self.led3.clicked.connect(lambda: self.control_led3("click"))
      self.led3off.clicked.connect(lambda: self.control_led3off("click"))
      self.led4.clicked.connect(lambda: self.control_led4("click"))
      self.led4off.clicked.connect(lambda:self.control_led4off("click"))
      self.led5.clicked.connect(lambda: self.control_led5("click"))
      self.led5off.clicked.connect(lambda:self.control_led5off("click"))
      self.led6.clicked.connect(lambda: self.control_led6("click"))
      self.led6off.clicked.connect(lambda:self.control_led6off("click"))
      self.led7.clicked.connect(lambda: self.control_led7("click"))
      self.led7off.clicked.connect(lambda:self.control_led7off("click"))
      self.led8.clicked.connect(lambda: self.control_led8("click"))
      self.led8off.clicked.connect(lambda:self.control_led8off("click"))
      self.stop.clicked.connect(lambda: self.control_stop("click"))
      self.left.clicked.connect(lambda: self.control_left("click"))
      self.right.clicked.connect(lambda: self.control_right("click"))
      self.stop_2.clicked.connect(lambda: self.control_stop_2("click"))
      self.left_2.clicked.connect(lambda: self.control_left_2("click"))
      self.right_2.clicked.connect(lambda: self.control_right_2("click"))
      self.read_ports()

    def read_ports(self):
      self.bau= ['1200', '2400' , '4800' , '9600', '19200', '38400' , '115200']

      puertosLista=[]
      puertos = QSerialPortInfo().availablePorts()
      for i in puertos:
         puertosLista.append(i.portName())
      self.baudios.clear()
      self.puerto.clear()
      self.baudios.addItems(self.bau)
      self.puerto.addItems(puertosLista)
      self.baudios.setCurrentText("9600")
    
    def serial_connect(self):
       self.serial.waitForReadyRead(100)
       self.port = self.puerto.currentText()
       self.baud = self.baudios.currentText()
       self.serial.setBaudRate(int(self.baud))
       self.serial.setPortName(self.port)
       self.serial.open(QIODevice.ReadWrite)

    def read_data(self):
        if not self.serial.canReadLine(): return 
        rx = self.serial.readLine()
        x=str(rx, 'utf-8').strip()
        
    
    def send_data(self, data):
      data= data + "\n"
      if self.serial.isOpen():
         self.serial.write(data.encode())
    

    def control_led1(self, param):
      if param == 'click':
          led1 = 'a' 
      self.send_data(led1)

    def control_led1off(self, param):
      if param == 'click':
          led1 = 'b' 
      self.send_data(led1)

    def control_led2(self, param):
      if param == 'click':
          led2 = 'c'
      self.send_data(led2)

    def control_led2off(self, param):
      if param == 'click':
          led2 = 'd'
      self.send_data(led2) 

    def control_led3(self, param):
      if param == 'click':
          led2 = 'e'
      self.send_data(led2)

    def control_led3off(self, param):
      if param == 'click':
          led2 = 'f'
      self.send_data(led2)

    def control_led4(self, param):
      if param == 'click':
          led2 = 'g'
      self.send_data(led2)

    def control_led4off(self, param):
      if param == 'click':
          led2 = 'h'
      self.send_data(led2) 
       
    def control_led5(self, param):
      if param == 'click':
          led2 = 'i'
      self.send_data(led2)

    def control_led5off(self, param):
      if param == 'click':
          led2 = 'j'
      self.send_data(led2) 

    def control_led6(self, param):
      if param == 'click':
          led2 = 'k'
      self.send_data(led2)

    def control_led6off(self, param):
      if param == 'click':
          led2 = 'l'
      self.send_data(led2) 

    def control_led7(self, param):
      if param == 'click':
          led2 = 'm'
      self.send_data(led2)

    def control_led7off(self, param):
      if param == 'click':
          led2 = 'n'
      self.send_data(led2) 

    def control_led8(self, param):
      if param == 'click':
          led2 = 'ñ'
      self.send_data(led2)

    def control_led8off(self, param):
      if param == 'click':
          led2 = 'o'
      self.send_data(led2) 

    def control_stop(self, param):
      if param == 'click':
          stop = 't'
      self.send_data(stop) 

    def control_left(self, param):
      if param == 'click':
          left = 'p'
      self.send_data(left) 

    def control_right(self, param):
      if param == 'click':
          right = 'q'
      self.send_data(right) 

    def control_stop_2(self, param):
      if param == 'click':
          stop2 = 'u'
      self.send_data(stop2) 

    def control_left_2(self, param):
      if param == 'click':
          left2 = 'r'
      self.send_data(left2) 

    def control_right_2(self, param):
      if param == 'click':
          right2 = 's'
      self.send_data(right2) 
    
    def mousePressEvent(self, event):
      self.click_posicion = event.globalPos()
    
    def mover_ventana(self, event):
      if self.isMaximized()== False:
        if event.buttons() == QtCore.Qt.LeftButton:
          self.move(self.pos() + event.globalPos()-self.click_posicion)
          self.click_posicion = event.globalPos()
          event.accept()
        if event.globalPos().y() <= 5 or event.globalPos().x() <=5:
           self.showMaximized()
        else:
           self.showNormal() 

if __name__ == '__main__':
   app = QApplication(sys.argv)
   appStm = AppStm()
   appStm.show()
   sys.exit(app.exec_())