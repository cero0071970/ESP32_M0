# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, SoftI2C, SDCard
from machine import SPI, SoftSPI
import sdcard, time
import os
import ssd1306
import os
from time import sleep


spi=SoftSPI(2,sck=Pin(14), miso=Pin(12), mosi=Pin(13))
sd=sdcard.SDCard(spi,Pin(15))
os.mount(sd, "/sda")
archivo = open("/sda/AAAA.txt", 'w')
archivo.write ("archivo de Texto")
archivo.close()

# ESP32 Pin assignment
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
# i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.invert(0)      # display inverted
oled.text('CARLES BRUT!', 0, 0)
oled.text('======================', 0, 10)

directorio = os.listdir("/sda")
a=0
for i in directorio:
    #oled.text(i, 10, 20+10*a)

    if a >= 3:
        time.sleep(2)
        oled.scroll(0, -10)
        oled.text("                   ", 10, 40)
        oled.show()
        oled.text(str(a) + " " + i, 10, 40)
        oled.show()

    else:
        oled.text(str(a) + " " + i, 10, 20 + 10 * a)
        oled.show()

    a = a + 1
oled.show()

