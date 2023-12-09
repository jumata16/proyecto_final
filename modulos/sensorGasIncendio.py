import RPi.GPIO as GPIO

def detectarGas(pulsador_encendido_pin, pulsador_apagado_pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pulsador_encendido_pin, GPIO.IN)
    GPIO.setup(pulsador_apagado_pin, GPIO.IN)

    while True:
        if GPIO.input(pulsador_encendido_pin) == GPIO.HIGH:
            while GPIO.input(pulsador_apagado_pin) == GPIO.LOW:
                pass
            return True
        
def detectarIncendio(pulsador_encendido_pin, pulsador_apagado_pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pulsador_encendido_pin, GPIO.IN)
    GPIO.setup(pulsador_apagado_pin, GPIO.IN)

    while True:
        if GPIO.input(pulsador_encendido_pin) == GPIO.HIGH:
            while GPIO.input(pulsador_apagado_pin) == GPIO.LOW:
                pass
            return True