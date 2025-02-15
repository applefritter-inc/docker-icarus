#!/bin/sh
set -e

cleanup() {
    echo "intercepted SIGINT or SIGTERM. shutting down server"
    pkill -P $$ || true
    exit 0
}
trap cleanup SIGTERM SIGINT

restart_process() {
    while true; do
        "$@"
        echo "$@ crashed, restarting..."
        sleep 1
    done
}

cd /icarus-server/httpmitm/dmbackend
restart_process bash start_server.sh &
SERVER_PID=$!

cd ..
restart_process node proxy.js &
PROXY_PID=$!

wait $SERVER_PID $PROXY_PID
