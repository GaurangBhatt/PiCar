#!/usr/bin/python
from Raspi_MotorHAT.Raspi_MotorHAT import Raspi_MotorHAT
from Raspi_MotorHAT.Raspi_MotorHAT import Raspi_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)
frontMotor = mh.getMotor(3)
rearMotor = mh.getMotor(2)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

def forward_speed_up():
	rearMotor.run(Raspi_MotorHAT.FORWARD)
	rearMotor.setSpeed(200)
	time.sleep(0.01)
		
def reverse_speed_up():
	rearMotor.run(Raspi_MotorHAT.BACKWARD)
	rearMotor.setSpeed(200)
	time.sleep(0.01)

def speed_down():
	for i in reversed(range(255)):
		rearMotor.setSpeed(i)
		time.sleep(0.01)

def turn_left():
	frontMotor.run(Raspi_MotorHAT.FORWARD)
	frontMotor.setSpeed(150)
	time.sleep(0.01)
		
def turn_right():
	frontMotor.run(Raspi_MotorHAT.BACKWARD)
	frontMotor.setSpeed(150)
	time.sleep(0.01)

def turn_completed():
	frontMotor.run(Raspi_MotorHAT.RELEASE);
	time.sleep(0.01)
	
def initiate():
	frontMotor.setSpeed(150)
	
	# turn on motor
	rearMotor.run(Raspi_MotorHAT.RELEASE);
	frontMotor.run(Raspi_MotorHAT.RELEASE);
	
