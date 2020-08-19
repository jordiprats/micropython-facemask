import time
import max7219
from machine import Pin, SPI, ADC

adc = ADC(Pin(32))

adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23))
ss = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 1)
display.fill(0)
display.show()

while True:
    valor = adc.read()

    print(valor)

    if valor > 3000:
        display.fill(0)
        display.text('O',0,0,1)
        display.show()
    elif valor > 2000:
        display.fill(0)
        display.text('o',0,0,1)
        display.show()
    elif valor > 1000:
        display.fill(0)
        display.text('(',0,0,1)
        display.show()
    else:
        display.fill(0)
        display.text('|',0,0,1)
        display.show()
    time.sleep_ms(100)
