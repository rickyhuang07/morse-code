try:
    import board
    import neopixel
    from adafruit_apds9960.apds9960 import APDS9960
    import touchio
except ModuleNotFoundError:
    pass
else:
    from src.interact import run

    # Setup board
    i2c = board.I2C()
    apds = APDS9960(i2c)
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 2, brightness=0.1)
    touch = touchio.TouchIn(board.TOUCH2)
    apds.enable_proximity = True
    print("Loaded Trinkey...")

    # Call our run function
    run(apds, pixels, touch)
