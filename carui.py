import webiopi
from webiopi.utils.logger import info
from Raspi_MotorHAT import monster

def initiate():
    info("Initialize")
    #monster.initiate()

@webiopi.macro
def reverse():
    info("Go Reverse")
    #monster.reverse_speed_up()

@webiopi.macro
def forward():
    info("Go Forward")
    #monster.forward_speed_up()
    
@webiopi.macro
def slow_down():
    info("Slow Down")
    #monster.speed_down()

@webiopi.macro
def left():
    info("Turn Left")
    #monster.turn_left()

@webiopi.macro
def right():
    info("Turn Right")
    #monster.turn_right()

@webiopi.macro
def turn_completed():
    info("Turn completed")
    #monster.turn_completed()

@webiopi.macro  
def stop():
    info("Stop the motors")
    #monster.turnOffMotors()
    
initiate()