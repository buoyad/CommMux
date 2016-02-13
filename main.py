#!#/usr/bin/env python
import mavlink
import serial

radio = serial.Serial()
whoi = serial.Serial()
apm = serial.Serial()

radio.baudrate = 57600
whoi.baudrate = 9600
apm.baudrate = 57600

radio.port = '/dev/ttyUSB0'
whoi.port = '/dev/ttyUSB1'
apm.port = '/dev/ttyUSB2'

def mavlink_receive():
def radio_send( packet ):
def modem_receive():
def modem_send( sentence ):

def modem_handle( d ):
def mavlink_handle( packet ):

def apm_send( packet ):