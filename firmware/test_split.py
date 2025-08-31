import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP20, board.GP21,)
keyboard.row_pins = (board.GP19,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.A,KC.B,]
]

split = Split(
    #split_flip=True,  # If both halves are the same, but flipped, set this True
    #split_side=None,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    #split_type=SplitType.UART,  # Defaults to UART
    #split_target_left=True,  # Assumes that left will be the one on USB. Set to False if it will be the right
    #uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.GP0,  # The primary data pin to talk to the secondary device with
    data_pin2=board.GP1,  # Second uart pin to allow 2 way communication
    #uart_flip=True,  # Reverses the RX and TX pins if both are provided
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)
keyboard.modules.append(split)

if __name__ == '__main__':
    keyboard.go()
    
    