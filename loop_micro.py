import time
from machine import ADC, Pin

adc = ADC(Pin(32))

adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

while True:
    print(adc.read())
    time.sleep_ms(100)

