import RPi.GPIO as GPIO
import time
import curses


class car:
    def __init__(self):
        self.motor_a_enable = 17
        self.motor_a_1 = 18
        self.motor_a_2 = 23
        self.motor_b_enable = 27
        self.motor_b_1 = 24
        self.motor_b_2 = 22

        # Set up GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.motor_a_enable, GPIO.OUT)
        GPIO.setup(self.motor_a_1, GPIO.OUT)
        GPIO.setup(self.motor_a_2, GPIO.OUT)
        GPIO.setup(self.motor_b_enable, GPIO.OUT)
        GPIO.setup(self.motor_b_1, GPIO.OUT)
        GPIO.setup(self.motor_b_2, GPIO.OUT)

        # PWM setup
        pwm_a = GPIO.PWM(self.motor_a_enable, 100)
        pwm_b = GPIO.PWM(self.motor_b_enable, 100)
        pwm_a.start(0)
        pwm_b.start(0)

        # Define GPIO pins (adjust as needed)

        def forward(self):
            GPIO.output(self.motor_a_1, GPIO.HIGH)
            GPIO.output(self.motor_a_2, GPIO.LOW)
            GPIO.output(self.motor_b_1, GPIO.HIGH)
            GPIO.output(self.motor_b_2, GPIO.LOW)
            print("ROBO FORWARD")

        def backward(self):
            GPIO.output(self.motor_a_1, GPIO.LOW)
            GPIO.output(self.motor_a_2, GPIO.HIGH)
            GPIO.output(self.motor_b_1, GPIO.LOW)
            GPIO.output(self.motor_b_2, GPIO.HIGH)
            print("ROBO BACKWARD")

        def left(self):
            GPIO.output(self.motor_a_1, GPIO.LOW)
            GPIO.output(self.motor_a_2, GPIO.HIGH)
            GPIO.output(self.motor_b_1, GPIO.HIGH)
            GPIO.output(self.motor_b_2, GPIO.LOW)
            print("ROBO LEFT")


        def right(self):
            GPIO.output(self.motor_a_1, GPIO.HIGH)
            GPIO.output(self.motor_a_2, GPIO.LOW)
            GPIO.output(self.motor_b_1, GPIO.LOW)
            GPIO.output(self.motor_b_2, GPIO.HIGH)
            print("ROBO RIGHT")

        def stop(self):
            GPIO.output(self.motor_a_1, GPIO.LOW)
            GPIO.output(self.motor_a_2, GPIO.LOW)
            GPIO.output(self.motor_b_1, GPIO.LOW)
            GPIO.output(self.motor_b_2, GPIO.LOW)
            # print("ROBO STOP")

        def main(stdscr):
            stdscr.nodelay(True)  # Enable non-blocking input
            try:
                while True:
                    key = stdscr.getch()

                    if key == curses.KEY_UP:
                            forward()
                    elif key == curses.KEY_DOWN:
                        backward()
                    elif key == curses.KEY_LEFT:
                        left()
                    elif key == curses.KEY_RIGHT:
                        right()
                    else:
                        stop()
            finally:
                print("CODE")



if __name__ == "__main__":
    rccar = car()
    curses.wrapper(rccar.main())  # Initialize curses and handle cleanup