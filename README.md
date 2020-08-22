# micropython-facemask

## bill of materials

* ESP32
* microphone with MAX4466 amplifier
* 8x8 display with MAX7219 microcontroller

## connections

### 8x8 display

| max7219 | esp32 |
|---------|-------|
| VCC     | 5V    |
| GND     | GND   |
| DIN     | G23   |
| CS      | G5    |
| CLK     | G18   |

### microphone

| max4466 | esp32 |
|---------|-------|
| VCC     | 3.3V  |
| GND     | GND   |
| OUT     | G32   |

## dependencies

* [mcauser/micropython-max7219](https://github.com/mcauser/micropython-max7219)
