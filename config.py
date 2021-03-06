"""Configuration file for air quality monitor."""
from machine import Pin

# Waveshare Display
baudrate = 20000000
sck = Pin(2)  # Marked CLK on Waveshare
mosi = Pin(15)  # Marked DIN on Waveshare
miso = Pin(23)  # Not used by Waveshare but must be supplied to SPI
cs = Pin(0)  # Marked CS on Waveshare
dc = Pin(4)  # Marked DC on Waveshare
rst1 = Pin(16)  # Marked RST on Waveshare
busy = Pin(17)  # Marked BUSY on Waveshare

# BME-280 and CCS811
scl = Pin(26)
sda = Pin(27)
# Following are CCS811 only
wake = Pin(33, Pin.OUT, value=0)  # Wake ccs811 by default, datasheet figure 4
int = Pin(34, Pin.IN, Pin.PULL_UP)  # Pulled down by CCS811
rst2 = 25  # Pin number only, create Pin when needed

# Battery measurement pin on Lolin D32 development board
battery = Pin(35)

# Control Switches (pulled down by switch)
sw1 = Pin(14, Pin.IN, Pin.PULL_UP)
sw2 = Pin(12, Pin.IN, Pin.PULL_UP)
sw3 = Pin(13, Pin.IN, Pin.PULL_UP)
