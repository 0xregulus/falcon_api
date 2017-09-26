#!/usr/bin/env bash
export APP_ENV="dev"

function start () {
    source .venv/bin/activate
    gunicorn -b 127.0.0.1:5000 --reload app.main:application
}

function stop () {
    ps -ef | grep gunicorn | awk '{print $2}' | xargs kill -9
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        start
        ;;
    *)
    echo "Usage: run.sh {start|stop|restart}"
    exit 1
esac
