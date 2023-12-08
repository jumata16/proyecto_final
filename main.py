# pip install gpiozero lgpio RPi pigpio
from gpiozero import Button
from gpiozero import Device
from gpiozero.pins.mock import MockFactory
from modules import sensorventana1, sensorventana2, sensorgas, sensorincendios, puertaprincipal
import time

# Configura la factoría de pines a la factoría mock 
Device.pin_factory = MockFactory()

ventana1_sensor = Button(17)
ventana2_sensor = Button(18)
gas_sensor = Button(19)
incendio_sensor = Button(20)
puerta_principal = Button(21)


ventana1_sensor.when_pressed = sensorventana1.ventana1_activado()
ventana1_sensor.when_released = sensorventana1.ventana1_desactivado()

ventana2_sensor.when_pressed = sensorventana2.ventana2_activado()
ventana2_sensor.when_released = sensorventana2.ventana2_desactivado()

gas_sensor.when_pressed = sensorgas.gas_activado()
gas_sensor.when_released = sensorgas.gas_desactivado()

incendio_sensor.when_pressed = sensorincendios.incendio_activado()
incendio_sensor.when_released = sensorincendios.incendio_desactivado()


puerta_principal.when_pressed = puertaprincipal.puerta_principal_activada()
puerta_principal.when_released = puertaprincipal.puerta_principal_desactivado()


try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Sistema de seguridad detenido por el usuario")

    