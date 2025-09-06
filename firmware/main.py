from kerberos import Kerberos
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.tapdance import TapDance


# fmt: off
# ↓ EDIT CONFIG HERE ↓
oled = True           # Options: True, False
speaker = False        # Options: True, False
layers = ["Colemak DH", "Qwerty", "Desktop", "Cursor", "Symbols", "Mouse/Macros", "Functions", "Numbers"]
# ↑ EDIT CONFIG HERE ↑
# fmt: on

keyboard = Kerberos(oled, speaker, layers)

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
L_SYMBOLS = 4
L_MOUSEMACROS = 5
L_FUNCTIONS = 6
L_NUMBERS = 7

# Key aliases
xxxxxxx = KC.NO
_______ = KC.TRNS

TD_PAREN = KC.TD(KC.LPRN, KC.RPRN)
TD_BRACK = KC.TD(KC.LBRC, KC.RBRC)
TD_CURLY = KC.TD(KC.LCBR, KC.RCBR)

TD_PLMI = KC.TD(KC.PLUS, KC.MINUS)
TD_MUDI = KC.TD(KC.ASTR, KC.SLSH)

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
    KC.LT(L_NUMBERS, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=200),
    KC.LT(L_CURSOR, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=200),
    KC.LT(L_MOUSEMACROS, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=200),
                                                KC.LT(L_SYMBOLS, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=200),
                                                KC.LT(L_DESKTOP, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=200),
                                                KC.LT(L_FUNCTIONS, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=200),


    # Encoders
    xxxxxxx, # Click
    KC.LGUI(KC.RIGHT), # CW rot
    KC.LGUI(KC.LEFT), # CCW rot
                                                                            xxxxxxx, # Click
                                                                            KC.MW_DN, # CW rot
                                                                            KC.MW_UP, # CCW rot
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
    KC.LGUI(KC.ENTER),         xxxxxxx, KC.LGUI(KC.LSFT(KC.N9)), KC.LGUI(KC.LSFT(KC.N7)), KC.LGUI(KC.LSFT(KC.N7)), KC.LGUI(KC.V),                           xxxxxxx, KC.LGUI(KC.N7), KC.LGUI(KC.N8), KC.LGUI(KC.N9), xxxxxxx,  KC.LGUI(KC.DOT),
    KC.LGUI(KC.LSFT(KC.ENTER)),xxxxxxx, KC.LGUI(KC.LSFT(KC.N6)), KC.LGUI(KC.LSFT(KC.N5)), KC.LGUI(KC.LSFT(KC.N4)), KC.LGUI(KC.F),                           xxxxxxx, KC.LGUI(KC.N4), KC.LGUI(KC.N5), KC.LGUI(KC.N6), xxxxxxx,  KC.LGUI(KC.COMMA),
    xxxxxxx,                   xxxxxxx, KC.LGUI(KC.LSFT(KC.N3)), KC.LGUI(KC.LSFT(KC.N2)), KC.LGUI(KC.LSFT(KC.N1)), KC.LGUI(KC.LSFT(KC.N0)),          KC.LGUI(KC.N0), KC.LGUI(KC.N1), KC.LGUI(KC.N2), KC.LGUI(KC.N3), xxxxxxx,  KC.LGUI(KC.LSFT(KC.Q)),

    # Secondary Thumb
                                         xxxxxxx, xxxxxxx,      xxxxxxx, xxxxxxx,
    # Main thumb
                       xxxxxxx, xxxxxxx, xxxxxxx,                        xxxxxxx, xxxxxxx, xxxxxxx,
    # Encoders
    xxxxxxx, # Click
    KC.LGUI(KC.LSFT(KC.RIGHT)), # CW rot
    KC.LGUI(KC.LSFT(KC.LEFT)), # CCW rot
                                                                            KC.Z, # Click
                                                                            KC.A, # CW rot
                                                                            KC.B, # CCW rot
     ],

    # L_CURSOR = 3
    # ----------------------------------------------------------------------------------------------
    [
    # Alphanumerics
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          KC.PGUP,  KC.HOME,   KC.UP,      KC.END, KC.INS,  xxxxxxx,
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          KC.PGDN,  KC.LEFT,   KC.DOWN,  KC.RIGHT, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          KC.PAUS,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,

    # Secondary Thumb
                                         xxxxxxx, xxxxxxx,      xxxxxxx, xxxxxxx,
    # Main thumb
                       xxxxxxx, xxxxxxx, xxxxxxx,                        xxxxxxx, xxxxxxx, xxxxxxx,
    # Encoders
    xxxxxxx, # Click
    xxxxxxx, # CW rot
    xxxxxxx, # CCW rot
                                                                            xxxxxxx, # Click
                                                                            KC.LCTL(KC.PGDN), # CW rot
                                                                            KC.LCTL(KC.PGUP), # CCW rot
     ],

    # L_SYMBOLS = 4
    # ----------------------------------------------------------------------------------------------
    [
    # Alphanumerics
    xxxxxxx,    xxxxxxx,  KC.AMPR,  KC.ASTR,  xxxxxxx,  xxxxxxx,          xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,   KC.DLR,  KC.PERC,  KC.CIRC,  xxxxxxx,          xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,  KC.EXLM,    KC.AT,  KC.HASH,  xxxxxxx,          xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx,  xxxxxxx,

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
    KC.SET_SEQUENCE(5), KC.SET_SEQUENCE(4),            KC.SET_SEQUENCE(3),         KC.SET_SEQUENCE(2), KC.SET_SEQUENCE(1), KC.SET_SEQUENCE(0),             KC.MW_UP,  KC.MW_LT,   KC.MS_UP,  KC.MW_RT, xxxxxxx,  xxxxxxx,
    xxxxxxx,            xxxxxxx,                       xxxxxxx,                    xxxxxxx,            KC.PLAY_SEQUENCE(), KC.RECORD_SEQUENCE(),           KC.MW_DN,  KC.MS_LT,   KC.MS_DN,  KC.MS_RT, xxxxxxx,  xxxxxxx,
    xxxxxxx,            KC.SET_SEQUENCE_REPETITIONS(), KC.SET_SEQUENCE_INTERVAL(), xxxxxxx,            xxxxxxx,            KC.STOP_SEQUENCE(),              xxxxxxx,  xxxxxxx,    xxxxxxx,   xxxxxxx,  xxxxxxx,  xxxxxxx,

    # Secondary Thumb
                                         xxxxxxx, xxxxxxx,      xxxxxxx, xxxxxxx,
    # Main thumb
                       xxxxxxx, xxxxxxx, xxxxxxx,                        KC.MB_MMB, KC.MB_LMB, KC.MB_RMB,
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
    xxxxxxx,    xxxxxxx,    KC.F9,    KC.F8,    KC.F7,    KC.F12,         KC.F22,    KC.F17,     KC.F18,    KC.F19, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,    KC.F6,    KC.F5,    KC.F4,    KC.F11,         KC.F21,    KC.F14,     KC.F15,    KC.F16, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,    KC.F3,    KC.F2,    KC.F1,    KC.F10,         KC.F20,    KC.F11,     KC.F12,    KC.F13, xxxxxxx,  xxxxxxx,

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

    # L_NUMBERS = 7
    # ----------------------------------------------------------------------------------------------
    [
    # Alphanumerics
    COLEMAK,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          TD_PLMI,  KC.N7,   KC.N8,  KC.N9, xxxxxxx,  xxxxxxx,
    QWERTY,     xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          TD_MUDI,  KC.N4,   KC.N5,  KC.N6, xxxxxxx,  xxxxxxx,
    xxxxxxx,    xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,          KC.N0,    KC.N1,   KC.N2,  KC.N3, xxxxxxx,  xxxxxxx,

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