#!/bin/sh
#
# Install script for instantbox
# Home Page: https://github.com/instantbox/instantbox
#
# Usage:
#  mkdir instantbox && cd $_
#  bash <(curl -sSL https://raw.githubusercontent.com/instantbox/instantbox/master/init.sh)"
#  docker-compose up -d
#

check_cmd() {
    command -v "$1" >/dev/null 2>&1
}

echo "Welcome to instantbox, please wait..."
echo ""

if check_cmd docker; then
    echo "docker is installed"
else
    echo "docker is not installed, please try again after it's installed"
    exit 1
fi

if check_cmd docker-compose; then
    echo "docker-compose is installed"
else
    curl -sSL https://raw.githubusercontent.com/docker/compose/master/script/run/run.sh > /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose || exit 1
fi

curl -sSLO https://raw.githubusercontent.com/instantbox/instantbox/master/docker-compose.yml

echo "Enter your IP (optional): "
read IP
echo "Choose a port (default: 8888): "
read PORT

[  -z "$IP" ] || sed -i -e "s/SERVERURL=$/SERVERURL=$IP/" docker-compose.yml
[  -z "$PORT" ] || sed -i -e "s/8888:80/$PORT:80/" docker-compose.yml

echo "You're all set! "
echo "Run 'docker-compose up -d' then go to http://${IP:-localhost}:${PORT:-8888} on your browser."
