import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP8,  # column
    source=board.GP21,  # row
    midi=False,
    storage=False,
    usb_id={'manufacturer': 'Stratosgear Industries', 'product': 'Kerberos'},
)