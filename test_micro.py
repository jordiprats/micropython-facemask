from machine import ADC, Pin

adc = ADC(Pin(32))

adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)
print(adc.read())

