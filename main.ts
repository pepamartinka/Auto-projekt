let senzor1 = DigitalPin.P0
let senzor2 = DigitalPin.P1
let manual = 0
let connected = 0
pins.setPull(senzor1, PinPullMode.PullNone)
pins.setPull(senzor2, PinPullMode.PullNone)
bluetooth.startUartService()
basic.showString("S")
