import max7219
from machine import Pin, SPI
spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23))
ss = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 1)
display.text('1',0,0,1)
display.show()
