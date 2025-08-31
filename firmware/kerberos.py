import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners.encoder import RotaryioEncoder
from kmk.modules.holdtap import HoldTap

# Based on: https://github.com/moritz-john/kmk-config-klor
class Kerberos(KMKKeyboard):
    col_pins=(
        board.GP8,
        board.GP9,
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13,
    )
    row_pins = (
        board.GP21,
        board.GP20,
        board.GP19,
        board.GP18,
    )
    diode_orientation = DiodeOrientation.COL2ROW
    encoder_a = board.GP14
    encoder_b = board.GP15
    encoder_divisor = 4

    oled_SDA = board.GP4
    oled_SCL = board.GP5

    uart_rx = board.GP0
    uart_tx = board.GP1

    buzzer_pin = board.GP2

    # Coord mapping:
    # First three row: alphanumeric keys
    # Two extra keys: for upper thumb cluster
    # Three keys: for lower thumb cluster (main thumbs for miryoku)
    # Encoders: First is click, second CW, third CCW
    coord_mapping = [
         0,  1,  2,  3,  4,  5,        26, 27, 28, 29, 30, 31,
         6,  7,  8,  9, 10, 11,        32, 33, 34, 35, 36, 37,
        12, 13, 14, 15, 16, 17,        38, 39, 40, 41, 42, 43,
                        21, 22,        45, 46,
               19, 20, 23,                 44, 47, 48,
        18, 24, 25,                                49, 50, 51
    ]

    def __init__(
        self,
        oled=False,
        speaker=False,
    ):
        # create and register the scanner(s)
        self.matrix = [
            MatrixScanner(
                # required arguments:
                column_pins=self.col_pins,
                row_pins=self.row_pins,
                # optional arguments with defaults:
                columns_to_anodes=self.diode_orientation,
                interval=0.02,  # Debounce time in floating point seconds
                max_events=64,
            ),
            RotaryioEncoder(
                pin_a=self.encoder_a,
                pin_b=self.encoder_b,
                divisor=self.encoder_divisor,
            ),
        ]

        # Hold tap must be loaded first:
        # https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/split_keyboards.md#split-keyboards
        holdtap = HoldTap()
        # optional: set a custom tap timeout in ms
        # holdtap.tap_time = 300
        self.modules.append(holdtap)


        # Split code:
        split = Split(
            split_flip=False,  # If both halves are the same, but flipped, set this True
            split_side=None,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
            split_type=SplitType.UART,  # Defaults to UART
            uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
            data_pin=self.uart_rx,  # The primary data pin to talk to the secondary device with
            data_pin2=self.uart_tx,  # Second uart pin to allow 2 way communication
            uart_flip=True,  # Reverses the RX and TX pins if both are provided
            use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
        )
        self.modules.append(split)

        self.setup_oled(oled)
        self.setup_speaker(speaker)


    # OLED Code:
    def setup_oled(self, oled):
        if oled:
        #     from kmk.extensions.peg_oled_Display import (
        #         Oled,
        #         OledDisplayMode,
        #         OledReactionType,
        #         OledData,
        #     )

        #     # --8<-- [start:oled]
        #     oled_ext = Oled(
        #         OledData(
        #             corner_one={
        #                 0: OledReactionType.STATIC,
        #                 1: ["Layer"],
        #             },
        #             corner_two={
        #                 0: OledReactionType.LAYER,
        #                 1: ["0", "1", "2"],
        #             },
        #             corner_three={
        #                 0: OledReactionType.LAYER,
        #                 1: ["BASE", "RAISE", "LOWER"],
        #             },
        #             corner_four={
        #                 0: OledReactionType.LAYER,
        #                 1: ["qwerty", "nums", "sym"],
        #             },
        #         ),
        #         toDisplay=OledDisplayMode.TXT,
        #         flip=True,
        #         # oHeight=64,
        #     )
        #     # --8<-- [end:oled]
        #     self.extensions.append(oled_ext)
            pass

    # Speaker Code:
    def setup_speaker(self, speaker):
        if speaker:
            # import digitalio
            # import pwmio
            # import time

            # buzzer = pwmio.PWMOut(self.buzzer_pin, variable_frequency=True)
            # OFF = 0
            # ON = 2**15
            # buzzer.duty_cycle = ON
            # buzzer.frequency = 2000
            # time.sleep(0.2)
            # buzzer.frequency = 1000
            # time.sleep(0.2)
            # buzzer.duty_cycle = OFF
            pass

    # NOQA

    # flake8: noqa
    # fmt: off
    # coord_mapping = [
    #         1,  2,  3,  4,  5,         31, 30, 29, 28, 27,
    #     6,  7,  8,  9, 10, 11,         37, 36, 35, 34, 33, 32,
    #    12, 13, 14, 15, 16, 17, 23, 49, 43, 42, 41, 40, 39, 38,
    #            19, 20, 21, 22,         48, 47, 46, 45,
    #                    24, 25,         51, 50,
    # ]
    # fmt: on