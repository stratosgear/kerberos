# This script supports the Raspberry Pi Pico board and the Lilygo ESP32-S2 board
# Raspberry Pi Pico: http://educ8s.tv/part/RaspberryPiPico
# ESP32-S2 Board: http://educ8s.tv/part/esp32s2
# OLED DISPLAY: https://educ8s.tv/part/OLED096
#
import board, busio, displayio, i2cdisplaybus, os, terminalio, time
import adafruit_displayio_ssd1306
from adafruit_display_text import label

displayio.release_displays()

board_type = os.uname().machine
print(f"Board Type: {board_type}")

i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
display.auto_refresh = False
# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(128, 48, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=16)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
#inner_bitmap = displayio.Bitmap(118, 54, 1)
inner_bitmap = displayio.Bitmap(126, 46, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=1, y=17)
splash.append(inner_sprite)

# Draw a label
text = "xx: Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
text_area.anchor_point = (0.0, 0.0)
text_area.anchored_position = (0, 0)

splash.append(text_area)

display.auto_refresh = True
while True:
    for y in range(64):
        text_area.anchored_position = (2, y)
        time.sleep(0.2)
        text_area.text = f"{y}: Hello"
    #pass


#Mon Aug 13  12:39:34
#Kerberos