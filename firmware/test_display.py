# This script supports the Raspberry Pi Pico board and the Lilygo ESP32-S2 board
# Raspberry Pi Pico: http://educ8s.tv/part/RaspberryPiPico
# ESP32-S2 Board: http://educ8s.tv/part/esp32s2
# OLED DISPLAY: https://educ8s.tv/part/OLED096
#
import board, busio, displayio, i2cdisplaybus, os, terminalio, time
import adafruit_displayio_ssd1306
from adafruit_display_text.label import Label
from adafruit_display_shapes.rect import Rect

displayio.release_displays()

board_type = os.uname().machine
print(f"Board Type: {board_type}")

i2c = busio.I2C(scl=board.GP5, sda=board.GP4)
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
display.auto_refresh = False
# Make the display context
splash = displayio.Group()
display.root_group = splash

border = Rect(0, 16, 128, 48, outline=0xFFFFFF)
splash.append(border)

# Draw a label
text = "Mon Aug 24   14:08:15"
status = Label(terminalio.FONT, text=text, color=0xFFFFFF)
status.anchor_point = (0.0, 0.0)
status.anchored_position = (0, 2)


splash.append(status)

display.auto_refresh = True

line1 = Label(terminalio.FONT, text="12345678901234567890", color=0xFFFFFF)
line1.anchor_point = (0.0, 0.0)
line1.anchored_position = (4, 17)

line2 = Label(terminalio.FONT, text="12345678901234567890", color=0xFFFFFF)
line2.anchor_point = (0.0, 0.0)
line2.anchored_position = (4, 28)

line3 = Label(terminalio.FONT, text="12345678901234567890", color=0xFFFFFF)
line3.anchor_point = (0.0, 0.0)
line3.anchored_position = (4, 39)

line4 = Label(terminalio.FONT, text="L: Mouse Layer", color=0xFFFFFF)
line4.anchor_point = (0.0, 0.0)
line4.anchored_position = (4, 50)


splash.append(line1)
splash.append(line2)
splash.append(line3)
splash.append(line4)
while True:
    pass


#Mon Aug 13  12:39:34
#Kerberos


