senzor1 = DigitalPin.P0
senzor2 = DigitalPin.P1
manual=0
connected=0

pins.set_pull(senzor1, PinPullMode.PULL_NONE)
pins.set_pull(senzor2, PinPullMode.PULL_NONE)
bluetooth.start_uart_service()
basic.show_string("S")

