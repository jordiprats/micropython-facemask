# micropython-facemask

## bill of materials

* ESP32
* micrphone with MAX4466 amplifier
* 8x8 display with MAX7219 microcontroller

## connections

| max7219 | esp32 |
|---------|-------|
| VCC     | 5V    |
| GND     | GND   |
| DIN     | G23   |
| CS      | G5    |
| CLK     | G18   |


| max4466 | esp32 |
|---------|-------|
| VCC     | 3.3V  |
| GND     | GND   |
| OUT     | G32   |
