from kerberos import Kerberos
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.tapdance import TapDance


# fmt: off
# ↓ EDIT CONFIG HERE ↓
oled = False           # Options: True, False
speaker = False        # Options: True, False
# ↑ EDIT CONFIG HERE ↑
# fmt: on

keyboard = Kerberos(oled, speaker)

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

tapdance = TapDance()
# tapdance.tap_time = 750
keyboard.modules.append(tapdance)



# Enable debugging: http://kmkfw.io/docs/debugging/
# keyboard.debug_enabled = True


# Layer aliases
L_FUNCTION1 = 2
L_FUNCTION2 = 3
L_WINMGT = 4
L_SYMBOLS = 5
L_CURSOR = 6
L_NUMBERS = 7
L_SYSTEM = 8
L_MOUSE = 9
L_KERBEROS = 10

# Key aliases
xxxxxxx = KC.NO
_______ = KC.TRNS

TD_PAREN = KC.TD(KC.LPRN, KC.RPRN)
TD_BRACK = KC.TD(KC.LBRC, KC.RBRC)
TD_CURLY = KC.TD(KC.LCBR, KC.RCBR)

COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)
CUT = KC.LCTL(KC.X)

# Keymap
# fmt: off
keyboard.keymap = [

    # Layer 0: Colemak DH
    [
    # Alphanumerics
    TD_PAREN,    KC.Q,    KC.W,    KC.F,    KC.P,    KC.B,         KC.J,    KC.L,     KC.U,    KC.Y, KC.QUOT,  COPY,
    TD_BRACK,
                 KC.HT(KC.A, KC.MEH, tap_time=200),
                 KC.HT(KC.R, KC.LALT, tap_time=200),
                 KC.HT(KC.S, KC.LCTL, tap_time=200),
                 KC.HT(KC.T, KC.LSFT, tap_time=200),
                 KC.HT(KC.G, KC.LGUI, tap_time=200),
                                                                            KC.HT(KC.M, KC.RGUI, tap_time=200),
                                                                            KC.HT(KC.N, KC.RSFT, tap_time=200),
                                                                            KC.HT(KC.E, KC.RCTL, tap_time=200),
                                                                            KC.HT(KC.I, KC.RALT, tap_time=200),
                                                                            KC.HT(KC.O, KC.MEH, tap_time=200),
                                                                                                                CUT,
    TD_CURLY,    KC.Z,    KC.X,    KC.C,    KC.D,    KC.V,         KC.K,    KC.H,  KC.COMM,  KC.DOT,  KC.SLSH, PASTE,

    # Secondary Thumb
                                         xxxxxxx, xxxxxxx,      xxxxxxx, xxxxxxx,

    # Main thumb
    KC.LT(L_NUMBERS, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=200),
    KC.LT(L_CURSOR, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=200),
    KC.LT(L_WINMGT, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=200),
                                                KC.LT(L_FUNCTION1, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=200),
                                                KC.LT(L_SYMBOLS, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=200),
                                                KC.LT(L_NUMBERS, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=200),


    # Encoders
    xxxxxxx, # Click
    xxxxxxx, # CW rot
    xxxxxxx, # CCW rot
                                                                            KC.Z, # Click
                                                                            KC.A, # CW rot
                                                                            KC.B, # CCW rot
     ],

]
# fmt: on

if __name__ == "__main__":
    keyboard.go()