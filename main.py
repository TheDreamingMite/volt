import OPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

analog_pin = 0

# Настройка пина как вход
GPIO.setup(analog_pin, GPIO.IN)

try:
    while True:
        voltage_value = GPIO.input(analog_pin)
        print("Voltage value:", voltage_value)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
