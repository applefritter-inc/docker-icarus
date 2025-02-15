#!/bin/bash
echo "$@"
SCRIPTDIR=$(readlink -f "$(dirname "$0")")
echo "Script directory: $SCRIPTDIR"
pushd "${SCRIPTDIR}" || exit
echo "now in scriptdir"
echo "${SCRIPTDIR}/server.py"
python3 "$SCRIPTDIR"/server.py 