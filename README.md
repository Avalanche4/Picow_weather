# Picow_weather
It downloads the weather forcast using a wireless connection, and displays it on a lcd  display, with two buttons to change what it displays.
Requires an account with weatherapi.com

# PicoW weather display 
![picow-weather-display](https://user-images.githubusercontent.com/109281779/179016934-224a2b74-aae6-4662-a2ac-50432a58513e.jpg)

# Helpful information
* White button is for moving to the next element.
* Blue button is for moving to the previous element.


| Pin number| Pin type|where the cable is going |
| --- | --- | --- | 
| 1| I2CO SDA | SDA Connection |
| 2 | I2CO SCL |SCL connection|
| 19 | GP14  |Blue button |
| 20 | GP15 |White button|
| 40 | VBUS |VCC  connetion|
| 38 | GND |GND connection | 
| 38 | GND |Negative Rail on bread board|
| 36 | 3V3(OUT)|Posative Rail on bread board|

# Equipment:
* Pico w
* Two buttons
* I2C HD44780 (adapter for the display)
* I2C LCD screen

# Resources:
IP lookup - https://ip4.seeip.org/ 

IP geo location -  https://ip-api.com/

Weather API - https://www.weatherapi.com/

LCD display driver - TomsHardware - https://www.tomshardware.com/how-to/lcd-display-raspberry-pi-pico

Pico Button tutorial - https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/6

