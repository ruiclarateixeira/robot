import RPi.GPIO as GPIO

motor_left_on_pin = 22
motor_left_forward_pin = 18
motor_left_backward_pin = 16

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motor_left_on_pin, GPIO.OUT)
    GPIO.output(motor_left_on_pin, GPIO.LOW)

    GPIO.setup(motor_left_forward_pin, GPIO.OUT)
    GPIO.setup(motor_left_backward_pin, GPIO.OUT)

def move_forward():
    print "Moving forward"
    GPIO.output(motor_left_forward_pin, GPIO.HIGH)
    GPIO.output(motor_left_backward_pin, GPIO.LOW)
    GPIO.output(motor_left_on_pin, GPIO.HIGH)

def stop():
    GPIO.output(motor_left_on_pin, GPIO.LOW)
