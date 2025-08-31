#!/usr/bin/env sh

# The script will rsync the contents of the CIRCUITPY partition to the
# ./circuitpython/ subdirectory of the git repository.
if [ -d "/run/media/stratos/KERBEROS_R" ]; then 
    rsync -arv --delete --exclude-from=.rsyncignore /run/media/stratos/KERBEROS_R/ ./firmware
    exit 0
fi
echo "Error: No KERBEROS_R partition found."
