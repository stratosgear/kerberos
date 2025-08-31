import board

from kmk.scanners import DiodeOrientation

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

col_pins = (board.GP6,)
row_pins = (board.GP20,)

diode_orientation = DiodeOrientation.COL2ROW

keyboard = KMKKeyboard()

keyboard.col_pins = col_pins
keyboard.row_pins = row_pins
keyboard.diode_orientation = diode_orientation

keyboard.keymap = [[KC.A,]]


if __name__ == '__main__':
    keyboard.go()