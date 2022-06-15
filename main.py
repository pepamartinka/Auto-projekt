uartdata = ""
connected = 0
bluetooth.set_transmit_power(7)
bluetooth.start_uart_service()
pin_L = DigitalPin.P12
pin_R = DigitalPin.P15
automaticpomoc=0
rightmotor = PCAmotor.Motors.M1
leftmotor = PCAmotor.Motors.M2
x=200
y=x+30

#přepíná automaticpomoc 
def on_button_pressed_a():
    global automaticpomoc
    if automaticpomoc==0:
        automaticpomoc=1
    else:
        automaticpomoc=0



#AUTOMATICKY
while connected ==0:
    pins.set_pull(pin_R, PinPullMode.PULL_NONE)
    read_R = pins.digital_read_pin(pin_R)
    pins.set_pull(pin_L, PinPullMode.PULL_NONE)
    read_L = pins.digital_read_pin(pin_L)
    
    if read_R==0 and read_L==0:
        PCAmotor.motor_run(leftmotor, x)
        PCAmotor.motor_run(rightmotor, y)

    if read_R==1 and read_L==1:
        PCAmotor.motor_run(leftmotor, x)
        PCAmotor.motor_run(rightmotor, y)  
        
    if read_L==1 and read_R==0:

        PCAmotor.motor_run(leftmotor,38)
        PCAmotor.motor_run(rightmotor,125) 
          
    if read_L==0 and read_R==1:
        PCAmotor.motor_run(leftmotor,120)
        PCAmotor.motor_run(rightmotor,38)

#MANUALNĚ
while connected==1:
        if uartdata == '0':
            PCAmotor.motor_stop_all()
        if uartdata == 'A':
            PCAmotor.motor_run(PCAmotor.Motors.M2, 255)
            PCAmotor.motor_run(PCAmotor.Motors.M1, 255)
        if uartdata == "B":
            PCAmotor.motor_run(PCAmotor.Motors.M2, -255)
            PCAmotor.motor_run(PCAmotor.Motors.M1, -255)
        if uartdata == "D":
            PCAmotor.motor_run(PCAmotor.Motors.M2, 255)
            PCAmotor.motor_run(PCAmotor.Motors.M1, 50)
        if uartdata == "C":
            PCAmotor.motor_run(PCAmotor.Motors.M2, 50)
            PCAmotor.motor_run(PCAmotor.Motors.M1, 255)


while connected==2: 
            pins.set_pull(pin_R, PinPullMode.PULL_NONE)
            read_R = pins.digital_read_pin(pin_R)
            pins.set_pull(pin_L, PinPullMode.PULL_NONE)
            read_L = pins.digital_read_pin(pin_L)
            
            if read_R==0 and read_L==0:
                PCAmotor.motor_run(leftmotor, x)
                PCAmotor.motor_run(rightmotor, y)
        
            if read_R==1 and read_L==1:
                connected=3
                #přepne se do connected3

            if read_L==1 and read_R==0:
        
                PCAmotor.motor_run(leftmotor,38)
                PCAmotor.motor_run(rightmotor,125)
                  
            if read_L==0 and read_R==1:
                PCAmotor.motor_run(leftmotor,120)
                PCAmotor.motor_run(rightmotor,38)
while connected==3:
    #vybereš co to má udělat
    if uartdata == 'A':
        PCAmotor.motor_run(leftmotor,50)
        PCAmotor.motor_run(rightmotor,50)

    if uartdata == 'A':
        PCAmotor.motor_run(leftmotor,50)
        PCAmotor.motor_run(rightmotor,-50)

    if uartdata == 'B':
        PCAmotor.motor_run(rightmotor,50)
        PCAmotor.motor_run(leftmotor,-50)

    basic.pause(100) #pauza=čas za kterou se s určitou rychlostí auto otočí o 90stupnu

    PCAmotor.motor_stop_all()
    connected=2
    #vrátí se do connected2

def on_bluetooth_connected():
    global connected, uartdata
    connected = 1
    while connected:
        uartdata = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global connected
    connected = 0
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)
