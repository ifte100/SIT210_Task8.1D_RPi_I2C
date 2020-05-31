import smbus
import time

def loop():
    # Get I2C bus
    bus = smbus.SMBus(1)

    # MMA8452Q address, 0x1D
    # Select Control register, 0x2A(42)
    #       0x00(00)    StandBy mode
    bus.write_byte_data(0x1D, 0x2A, 0x00) ##writing 1 byte of data for standby mode
    # MMA8452Q address, 0x1D
    # Select Control register, 0x2A(42)
    #       0x01(01)    Active mode
    bus.write_byte_data(0x1D, 0x2A, 0x01) ##writing 1 byte of data for active mode
    # MMA8452Q address, 0x1D
    # Select Configuration register, 0x0E(14)
    #       0x00(00)    Set range to +/- 2g
    bus.write_byte_data(0x1D, 0x0E, 0x00)

    time.sleep(0.5)

    # MMA8452Q address, 0x1D
    # Read data back from 0x00(0), 7 bytes
    # Status register, X-Axis MSB, X-Axis LSB, Y-Axis MSB, Y-Axis LSB, Z-Axis MSB, Z-Axis LSB
    data = bus.read_i2c_block_data(0x1D, 0x00, 7)

    # Convert the data. It is in 12 bit so we convert like this-

    xAccl = (data[1] * 256 + data[2]) / 16
    if xAccl > 2047 :
        xAccl -= 4096

    yAccl = (data[3] * 256 + data[4]) / 16
    if yAccl > 2047 :
        yAccl -= 4096

    zAccl = (data[5] * 256 + data[6]) / 16
    if zAccl > 2047 :
        zAccl -= 4096

        # Output data to screen

    print ("Acceleration in X-Axis : %d" %xAccl)
    print ("Acceleration in Y-Axis : %d" %yAccl)
    print ("Acceleration in Z-Axis : %d" %zAccl)
    print (" ")

try:
    while True:
        loop()
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()


