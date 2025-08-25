#!/usr/bin/env sh

# This ought to be run from the location where the git repository resides.
# The script will rsync the contents of the CIRCUITPY partition to the
# circuitpython/ subdirectory of the git repository.
rsync -arv --delete --exclude-from=.rsyncignore /run/media/stratos/CIRCUITPY/ /projects/stratosgear/diy_keyboards/kerberos/circuitpython
