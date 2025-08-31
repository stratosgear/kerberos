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
L_COLEMAK = 0
L_QWERTY = 1
L_DESKTOP = 2
L_CURSOR = 3
L_NUMSYMS = 4
L_MOUSEMACROS = 5
L_FUNCTIONS = 6
L_KERBEROSSYS = 7

# Key aliases
xxxxxxx = KC.NO
_______ = KC.TRNS

TD_PAREN = KC.TD(KC.LPRN, KC.RPRN)
TD_BRACK = KC.TD(KC.LBRC, KC.RBRC)
TD_CURLY = KC.TD(KC.LCBR, KC.RCBR)

COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)
CUT = KC.LCTL(KC.X)

COLEMAK = KC.DF(L_COLEMAK)
QWERTY = KC.DF(L_QWERTY)

# Keymap
# fmt: off
keyboard.keymap = [

    # L_Colemak: 0
    # ----------------------------------------------------------------------------------------------
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
    KC.LT(L_KERBEROSSYS, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=200),
    KC.LT(L_CURSOR, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=200),
    KC.LT(L_MOUSEMACROS, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=200),
                                                KC.LT(L_NUMSYMS, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=200),
                                                KC.LT(L_DESKTOP, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=200),
                                                KC.LT(L_FUNCTIONS, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=200),


    # Encoders
    xxxxxxx, # Click
    xxxxxxx, # CW rot
    xxxxxxx, # CCW rot
                                                                            KC.Z, # Click
                                                                            KC.A, # CW rot
                                                                            KC.B, # CCW rot
     ],

    # L_QWERTY: 1
    # TODO: Update from colemak
    # ----------------------------------------------------------------------------------------------
    [
    # Alphanumerics
    TD_PAREN,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,         KC.Y,    KC.U,     KC.I,    KC.O,   KC.P,  COPY,
    TD_BRACK,
                 KC.HT(KC.A, KC.MEH, tap_time=200),
                 KC.HT(KC.S, KC.LALT, tap_time=200),
                 KC.HT(KC.D, KC.LCTL, tap_time=200),
                 KC.HT(KC.F, KC.LSFT, tap_time=200),
                 KC.HT(KC.G, KC.LGUI, tap_time=200),
                                                                            KC.HT(KC.H, KC.RGUI, tap_time=200),
                                                                            KC.HT(KC.J, KC.RSFT, tap_time=200),
                                                                            KC.HT(KC.K, KC.RCTL, tap_time=200),
                                                                            KC.HT(KC.L, KC.RALT, tap_time=200),
                                                                            KC.HT(KC.QUOTE, KC.MEH, tap_time=200),
                                                                                                                CUT,
    TD_CURLY,    KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,         KC.N,    KC.M,  KC.COMM,  KC.DOT,  KC.SLSH, PASTE,

    # Secondary Thumb
                                         xxxxxxx, xxxxxxx,      xxxxxxx, xxxxxxx,
    # Main thumb
                 _______, _______, _______,                      _______, _______, _______,
    # Encoders
    xxxxxxx, # Click
    xxxxxxx, # CW rot
    xxxxxxx, # CCW rot
                                                                            KC.Z, # Click
                                                                            KC.A, # CW rot
                                                                            KC.B, # CCW rot
     ],

    # L_DESKTOP = 2
    # ----------------------------------------------------------------------------------------------
    [
    # Alphanumerics
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,

    # Secondary Thumb
                                         xxxxxxx, xxxxxxx,      xxxxxxx, xxxxxxx,
    # Main thumb
                       xxxxxxx, xxxxxxx, xxxxxxx,                        xxxxxxx, xxxxxxx, xxxxxxx,
    # Encoders
    xxxxxxx, # Click
    xxxxxxx, # CW rot
    xxxxxxx, # CCW rot
                                                                            KC.Z, # Click
                                                                            KC.A, # CW rot
                                                                            KC.B, # CCW rot
     ],

    # L_CURSOR = 3
    # ----------------------------------------------------------------------------------------------
    [
    # Alphanumerics
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,

    # Secondary Thumb
                                         xxxxxxx, xxxxxxx,      xxxxxxx, xxxxxxx,
    # Main thumb
                       xxxxxxx, xxxxxxx, xxxxxxx,                        xxxxxxx, xxxxxxx, xxxxxxx,
    # Encoders
    xxxxxxx, # Click
    xxxxxxx, # CW rot
    xxxxxxx, # CCW rot
                                                                            KC.Z, # Click
                                                                            KC.A, # CW rot
                                                                            KC.B, # CCW rot
     ],

    # L_NUMSYMS = 4
    # ----------------------------------------------------------------------------------------------
    [
    # Alphanumerics
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,

    # Secondary Thumb
                                         xxxxxxx, xxxxxxx,      xxxxxxx, xxxxxxx,
    # Main thumb
                       xxxxxxx, xxxxxxx, xxxxxxx,                        xxxxxxx, xxxxxxx, xxxxxxx,
    # Encoders
    xxxxxxx, # Click
    xxxxxxx, # CW rot
    xxxxxxx, # CCW rot
                                                                            KC.Z, # Click
                                                                            KC.A, # CW rot
                                                                            KC.B, # CCW rot
     ],

    # L_MOUSEMACROS = 5
    # ----------------------------------------------------------------------------------------------
    [
    # Alphanumerics
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,           xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,           xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,           xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,

    # Secondary Thumb
                                         xxxxxxx, xxxxxxx,      xxxxxxx, xxxxxxx,
    # Main thumb
                       xxxxxxx, xxxxxxx, xxxxxxx,                        xxxxxxx, xxxxxxx, xxxxxxx,
    # Encoders
    xxxxxxx, # Click
    xxxxxxx, # CW rot
    xxxxxxx, # CCW rot
                                                                            KC.Z, # Click
                                                                            KC.A, # CW rot
                                                                            KC.B, # CCW rot
     ],

    # L_FUNCTIONS = 6
    # ----------------------------------------------------------------------------------------------
    [
    # Alphanumerics
    xxxxxxx,    xxxxxxx,    KC.F19,    KC.F18,    KC.F17,    KC.F22,         KC.F12,    KC.F7,     KC.F8,    KC.F9, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,    KC.F16,    KC.F15,    KC.F14,    KC.F21,         KC.F11,    KC.F4,     KC.F5,    KC.F6, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,    KC.F13,    KC.F12,    KC.F11,    KC.F22,         KC.F10,    KC.F1,     KC.F2,    KC.F3, xxxxxxx,  xxxxxxx,

    # Secondary Thumb
                                         xxxxxxx, xxxxxxx,      xxxxxxx, xxxxxxx,
    # Main thumb
                       xxxxxxx, xxxxxxx, xxxxxxx,                        xxxxxxx, xxxxxxx, xxxxxxx,
    # Encoders
    xxxxxxx, # Click
    xxxxxxx, # CW rot
    xxxxxxx, # CCW rot
                                                                            KC.Z, # Click
                                                                            KC.A, # CW rot
                                                                            KC.B, # CCW rot
     ],

    # L_KERBEROSSYS = 7
    # ----------------------------------------------------------------------------------------------
    [
    # Alphanumerics
    COLEMAK,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,
    QWERTY,     xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,

    # Secondary Thumb
                                         xxxxxxx, xxxxxxx,      xxxxxxx, xxxxxxx,
    # Main thumb
                       xxxxxxx, xxxxxxx, xxxxxxx,                        xxxxxxx, xxxxxxx, xxxxxxx,
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