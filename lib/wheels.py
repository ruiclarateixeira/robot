import RPi.GPIO as GPIO

motor_left_forward_pin = 18
motor_left_backward_pin = 16

motor_right_forward_pin = 15
motor_right_backward_pin = 13

def init():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motor_left_forward_pin, GPIO.OUT)
    GPIO.setup(motor_left_backward_pin, GPIO.OUT)
    GPIO.setup(motor_right_forward_pin, GPIO.OUT)
    GPIO.setup(motor_right_backward_pin, GPIO.OUT)

def move_forward():
    print "Moving forward"
    GPIO.output(motor_left_forward_pin, GPIO.HIGH)
    GPIO.output(motor_left_backward_pin, GPIO.LOW)
    GPIO.output(motor_right_forward_pin, GPIO.HIGH)
    GPIO.output(motor_right_backward_pin, GPIO.LOW)

def stop():
    GPIO.output(motor_left_forward_pin, GPIO.LOW)
    GPIO.output(motor_right_forward_pin, GPIO.LOW)

def diagnostics():
    init()
    move_forward()
    sleep(1)
    stop()
