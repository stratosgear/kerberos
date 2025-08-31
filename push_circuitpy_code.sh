#!/usr/bin/env sh

# The script will rsync the contents of the circuitpython/ path with the actual mounted
# microprocessor partition
if [ -d "/run/media/stratos/KERBEROS_R" ]; then 
    echo "Pushing to KERBEROS_R"
    rsync -arv ./firmware/ /run/media/stratos/KERBEROS_R
    sudo sync
    exit 0
fi
if [ -d "/run/media/stratos/KERBEROS_L" ]; then 
    echo "Pushing to KERBEROS_L"
    rsync -arv ./firmware/ /run/media/stratos/KERBEROS_L
    sudo sync
    exit 0
fi
echo "Error: No KERBEROS_[L|R] partition found."

