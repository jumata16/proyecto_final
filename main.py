import MODULES.sensorVentanasPuerta as sensorVentanasPuerta
import MODULES.sensorGasIncendio as sensorGasIncendio
import MODULES.enviarMensaje as envio_correos

# Definir los pines para cada sensor
pines_sensor_ventana_sala = (10, 11) # cambiar por los pines que se usen
pines_sensor_ventana_habitacion = (12, 13) # cambiar por los pines que se usen
pines_sensor_puerta = (14, 15) # cambiar por los pines que se usen
pines_sensor_gas = (16, 17) # cambiar por los pines que se usen
pines_sensor_incendio = (18, 19) # cambiar por los pines que se usen

def verificar_sensor_ventana():
    if sensorVentanasPuerta.detectarVentanaSala(*pines_sensor_ventana_sala):
        envio_correos.enviar('destinatario@gmail.com', 'Alerta de ventana', 'La ventana de la sala está abierta.') # Cambiar destinatario

def verificar_sensor_ventana_habitacion():
    if sensorVentanasPuerta.detectarVentanaHabitacion(*pines_sensor_ventana_habitacion):
        envio_correos.enviar('destinatario@gmail.com', 'Alerta de ventana habitación', 'La ventana de la habitación está abierta.')

def verificar_sensor_puerta():
    if sensorVentanasPuerta.detectarPuerta(*pines_sensor_puerta):
        envio_correos.enviar('destinatario@gmail.com', 'Alerta de puerta', 'La puerta está abierta.')

def verificar_sensor_gas():
    if sensorGasIncendio.detectarGas(*pines_sensor_gas):
        envio_correos.enviar('destinatario@gmail.com', 'Alerta de gas', 'Se detectó gas.')

def verificar_sensor_incendio():
    if sensorGasIncendio.detectarIncendio(*pines_sensor_incendio):
        envio_correos.enviar('destinatario@gmail.com', 'Alerta de incendio', 'Se detectó un incendio.')

while True:
    verificar_sensor_ventana()
    verificar_sensor_ventana_habitacion()
    verificar_sensor_puerta()
    verificar_sensor_gas()
    verificar_sensor_incendio()