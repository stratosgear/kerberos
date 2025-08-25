#!/usr/bin/env sh

# The script will rsync the contents of the CIRCUITPY partition to the
# ./circuitpython/ subdirectory of the git repository.
rsync -arv --delete --exclude-from=.rsyncignore /run/media/stratos/CIRCUITPY/ ./circuitpython
