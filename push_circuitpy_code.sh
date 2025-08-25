#!/usr/bin/env sh

# The script will rsync the contents of the circuitpython/ path with the actual moubted
# microprocessor partition
rsync -arv ./circuitpython/ /run/media/stratos/CIRCUITPY
