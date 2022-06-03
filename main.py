senzorL = DigitalPin.P0
senzorP= DigitalPin.P1
leftmotor= PCAmotor.Motors.M1
rightmotor= PCAmotor.Motors.M3
connected=0

bluetooth.start_uart_service()


if (pins.digital_read_pin(senzorL) and pins.digital_read_pin(senzorP)) == 0:
    PCAmotor.motor_run(leftmotor, 225)
    PCAmotor.motor_run(rightmotor, 225)

elif pins.digital_read_pin(senzorL) == 1 and pins.digital_read_pin(senzorP) == 0:
    PCAmotor.motor_run(leftmotor, 100)
    PCAmotor.motor_run(rightmotor, 180)

elif pins.digital_read_pin(senzorL) == 0 and pins.digital_read_pin(senzorP) == 1:
    PCAmotor.motor_run(leftmotor, 180)
    PCAmotor.motor_run(rightmotor, 100)

elif pins.digital_read_pin(senzorL) == 1 and pins.digital_read_pin(senzorP) == 1:
    PCAmotor.motor_run(leftmotor, 225)
    PCAmotor.motor_run(rightmotor, 225)

    
def on_bluetooth_connected():
    global connected
    basic.show_icon(IconNames.HEART)
    connected = 1
    while connected == 1:
        uartData = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
        console.log_value("data", uartData)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global connected
    basic.show_icon(IconNames.SAD)
    connected = 0
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)
