import time
import network
import json
import urequests
#for the display
from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

network_name = 'WiFi NETWORK NAME'
password = 'WiFi PASSWORD'
# Register with weatherapi.com to get a free API key
weather_api_key = 'API_KEY_HERE'

lcd.putstr("Connect WiFi")
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(network_name, password)


lcd.clear()
lcd.putstr("Get ip address")
r = urequests.get("https://ip4.seeip.org/jsonip")
print(r.content)
ip_data = json.loads(r.content)
print("My ip address is", ip_data["ip"])

lcd.clear()
lcd.putstr("Get location")
r = urequests.get("http://ip-api.com/json/%s" % (ip_data["ip"]))
geo_data = json.loads(r.content)
# Encode post_code for Weather API URL
post_code = geo_data["zip"].replace(" ", "%20")
print(post_code)
lcd.clear()
lcd.putstr("downloading \nweather")
r = urequests.get("http://api.weatherapi.com/v1/forecast.json?key=" + weather_api_key + "%20&q=" + post_code + "&days=1&aqi=no&alerts=no")
weather_data = json.loads(r.content)
r.close()



#for the first button, which advances forward
button = Pin(15, Pin.IN, Pin.PULL_DOWN)
#for the seconed button, which addvances backwards
button_2 = Pin(14, Pin.IN, Pin.PULL_DOWN)

def redraw(lcd, count):
    lcd.clear()
    if count == 1:
        lcd.putstr(weather_data["current"]["last_updated"])
    elif count == 2:
        lcd.putstr("%s %s" % (weather_data["location"]["country"], weather_data["location"]["name"] ))
    elif count == 3:
        lcd.putstr("Temperature %.1f C %.1f F" % (weather_data["current"]["temp_c"], weather_data["current"]["temp_f"] ))
    elif count == 4:
        lcd.putstr("%.2f uv" % (weather_data["current"]["uv"]))
    elif count == 5:
        lcd.putstr("%.2f mph wind" % (weather_data["current"]["wind_mph"]))
    elif count == 6:
        lcd.putstr(weather_data["current"]["condition"]["text"])
        count = 0
    else:
        lcd.putstr("error", count)#not manditory
        

count = 1
redraw(lcd, count) # Draw the first field and then loop waiting for button presses
while True:
    if button.value():
        count = count + 1
        if count > 6:
            count = 1
        redraw(lcd, count)
    elif button_2.value():
        count = count - 1
        if count == 0:
            count = 5
        redraw(lcd, count)
    time.sleep(0.3)