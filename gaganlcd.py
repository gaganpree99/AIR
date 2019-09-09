from Adafruit_CharLCD import Adafruit_CharLCD
import math
import time
import os
import sys
from time import sleep
import Adafruit_CharLCD as LCD

# Raspberry Pi pin configuration:
lcd_rs = 27 # Note this might need to be changed to 21 for older revision Pi's.
lcd_en = 22
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,lcd_columns, lcd_rows, lcd_backlight)
n = 16
text=sys.argv[1]

for i in range(0,len(text)-13):

    lcd.move_left()
    lcd.set_cursor(i + 1, 0)
    lcd.message("You Said:")

    lcd.set_cursor(1, 1)
    lcd.message(text)
    sleep(0.3)
    
lcd.clear()