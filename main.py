from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice, QPoint
from PyQt5 import QtCore, QtWidgets
import numpy as np
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
      self.led2.clicked.connect(lambda:self.control_led2("click"))
      self.vel.valueChanged.connect(self.vel_m1)
      self.stop.clicked.connect(lambda: self.control_stop("click"))
      self.left.clicked.connect(lambda: self.control_left("click"))
      self.right.clicked.connect(lambda: self.control_right("click"))
      self.vel_2.valueChanged.connect(self.vel_m2)
      self.stop_2.clicked.connect(lambda: self.control_stop_2("click"))
      self.left_2.clicked.connect(lambda: self.control_left_2("click"))
      self.right_2.clicked.connect(lambda: self.control_right_2("click"))
      self.vel_3.valueChanged.connect(self.vel_sm)
      self.stop_3.clicked.connect(lambda: self.control_stop_3("click"))
      self.left_3.clicked.connect(lambda: self.control_left_3("click"))
      self.right_3.clicked.connect(lambda: self.control_right_3("click"))

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
        x=float(x)
        print(x)
    
    def send_data(self, data):
      data= data + "\n"
      print(data)
      if self.serial.isOpen():
         self.serial.write(data.encode())
    
    def vel_m1(self, event):
       self.vel.setValue(event)
       self.vel_porcentaje.setText(str(event))
       vel1= 'VEL=' + str(event) + '/'
       self.send_data(vel1)
    def vel_m2(self, event):
       self.vel_2.setValue(event)
       self.vel_porcentaje_2.setText(str(event))
       vel2= 'VEL2=' + str(event) + '/'
       self.send_data(vel2)
    def vel_sm(self, event):
       self.vel_3.setValue(event)
       self.vel_porcentaje_3.setText(str(event))
       vel3= 'VELS=' + str(event) + '/'
       self.send_data(vel3)

    def control_led1(self, param):
      if param == 'click':
          led1 = 'led1*' 
      self.send_data(led1)

    def control_led2(self, param):
      if param == 'click':
          led2 = 'led2*'
      self.send_data(led2) 
       
    def control_stop(self, param):
      if param == 'click':
          stop = 'stop*'
      self.send_data(stop) 

    def control_left(self, param):
      if param == 'click':
          left = 'left*'
      self.send_data(left) 

    def control_right(self, param):
      if param == 'click':
          right = 'right*'
      self.send_data(right) 

    def control_stop_2(self, param):
      if param == 'click':
          stop2 = 'stop2*'
      self.send_data(stop2) 

    def control_left_2(self, param):
      if param == 'click':
          left2 = 'left2*'
      self.send_data(left2) 

    def control_right_2(self, param):
      if param == 'click':
          right2 = 'right2*'
      self.send_data(right2) 

    def control_stop_3(self, param):
      if param == 'click':
          stop3 = 'stop3*'
      self.send_data(stop3) 

    def control_left_3(self, param):
      if param == 'click':
          left3 = 'left3*'
      self.send_data(left3) 

    def control_right_3(self, param):
      if param == 'click':
          right3 = 'right3*'
      self.send_data(right3) 
    
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