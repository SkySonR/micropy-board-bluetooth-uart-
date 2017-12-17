import pyb

pin_x5 = pyb.Pin('X5', pyb.Pin.IN, pyb.Pin.PULL_DOWN) # Grey button
pin_x6 = pyb.Pin('X6', pyb.Pin.IN, pyb.Pin.PULL_DOWN) # Yellow Button
pin_x7 = pyb.Pin('X7', pyb.Pin.IN, pyb.Pin.PULL_DOWN) # Orange Button

X1_pin = pyb.Pin('X1', pyb.Pin.OUT_PP) # Green LED
X2_pin = pyb.Pin('X2', pyb.Pin.OUT_PP) # Light Blue LED
X3_pin = pyb.Pin('X3', pyb.Pin.OUT_PP) # Yellow LED

uart = pyb.UART(1, 9600) # init with given baudrate
uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters

def wait_pin_change(pin1, pin2, pin3):
    """
    Wait for pin to change value. Assign the value
    to 'pin_number' variable after 'time_delay' (equal 5).
    """
    cur_value_pin1 = pin1.value() # equel 0 (default value)
    cur_value_pin2 = pin2.value() # equel 0 (default value)
    cur_value_pin3 = pin3.value() # equel 0 (default value)
    time_delay = 5
    active = 0
    pin_number = 0
    if pin1.value() != cur_value_pin1 or pin2.value() != cur_value_pin2 or pin3.value() != cur_value_pin3: # if some button swithed
        while active < time_delay:
           if pin1.value() != cur_value_pin1: # if value changed
               pin_number = 1 # Orange button
               pyb.delay(500)
               cur_value_pin1 = pin1.value()
           elif pin2.value() != cur_value_pin2: # if value changed
               pin_number = 2 # Grey button
               pyb.delay(500)
               cur_value_pin2 = pin2.value()
           elif pin3.value() != cur_value_pin3: # if value changed
               pin_number = 3 # Yellow button
               pyb.delay(500)
               cur_value_pin3 = pin3.value()
           else:
               print(active)
               active +=1
               pyb.delay(1000)
        return pin_number

def send_data(pin):
    """
    Write data to 'UART' port.
    When data arrived - switch on LED.
    """
    if pin == 1:
        uart.write('~') # Unsertenly
        if uart.read():
            X1_pin.value(1) # Switch on X1 LED
            pyb.delay(1500)
            X1_pin.value(0) # Switch off X1 LED
    elif pin == 2:
        uart.write('-') # No
	if uart.read():
            X2_pin.value(1) # Switch on X2 LED
            pyb.delay(1500)
            X2_pin.value(0) # Switch off X2 LED
    elif pin == 3:
        uart.write('+') # Yes
        if uart.read():
            X3_pin.value(1) # Switch on X3 LED
            pyb.delay(1500)
            X3_pin.value(0) # Switch off X3 LED
    else:
        pass # skip iteration

if __name__ == '__main__':
    while True:
        try:
            send_data(wait_pin_change(pin_x5, pin_x7, pin_x6)) # Result of wait_pin_change function applied as input to send_data function
        except:
            pyb.delay(1000) # Wait 1 second
