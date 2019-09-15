import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200 )
time.sleep(1) #necessary to wait 1 sec to start seial commmunication


class receive_data_from_Arduino: #Object for receiving data from serial port. data between "<" and ">" get sorted out
 def __init__(self):
  self.string_received = ''
  self.reciving_data = False
  self.new_data = False
  self.data_interpreted = True
 def update(self):
  if (self.data_interpreted == True): # chech if earlier recived data are processed, must be before new data from buffer get readen
    for x in range(0, (ser.in_waiting-1)): #Read bytes available in serial buffer
     charReceived = ser.read().decode('utf-8', "ignore") #chech if char received is decode able, if not it ignored
     if(charReceived == '<'):  #Start saving data to string, when start character is received
      self.reciving_data = True
      self.string_received = ''
     elif(charReceived == '>'): #end char received, stop reading buffer and process data
      #set flagg for received message
      self.reciving_data = False
      self.new_data = True
      self.data_interpreted = False
      return
     elif(self.reciving_data == True): #append data to string
      self.string_received += charReceived
