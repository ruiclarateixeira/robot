import RPi.GPIO as GPIO
from time import sleep

motor_left_forward_pin = 18
motor_left_backward_pin = 16

motor_right_forward_pin = 13
motor_right_backward_pin = 15

def init():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motor_left_forward_pin, GPIO.OUT)
    GPIO.setup(motor_left_backward_pin, GPIO.OUT)
    GPIO.setup(motor_right_forward_pin, GPIO.OUT)
    GPIO.setup(motor_right_backward_pin, GPIO.OUT)
    diagnostic()

def move_forward():
    print "Moving forward"
    GPIO.output(motor_left_forward_pin, GPIO.HIGH)
    GPIO.output(motor_left_backward_pin, GPIO.LOW)
    GPIO.output(motor_right_forward_pin, GPIO.HIGH)
    GPIO.output(motor_right_backward_pin, GPIO.LOW)

def stop():
    GPIO.output(motor_left_forward_pin, GPIO.LOW)
    GPIO.output(motor_right_forward_pin, GPIO.LOW)

def diagnostic():
    move_forward()
    sleep(0.1)
    stop()
    return "All systems up!"
