#!/bin/bash

LSB_ID=

INSTALL=
REMOVE=
UPDATE=

PKG_LIBEV="libev-dev"
PKG_SSL="libssl-dev"

show_distribution() {
    local pretty_name=""

    if [ -f /etc/os-release ];
    then
        . /etc/os-release
        pretty_name="$PRETTY_NAME"

        LSB_ID="$(echo "$ID" | tr '[:upper:]' '[:lower:]')"

    elif [ -f /etc/redhat-release ];
    then
        pretty_name=$(cat /etc/redhat-release)
        LSB_ID="$(echo "$pretty_name" | tr '[:upper:]' '[:lower:]')"
        echo "$LSB_ID" | grep centos > /dev/null && LSB_ID=centos
    fi

    LSB_ID=$(echo "$LSB_ID" | tr '[:upper:]' '[:lower:]')

    echo "Platform: $pretty_name"
}

check_cmd() {
    which $1 > /dev/null 2>&1
}

detect_pkg_tool() {
    check_cmd apt && {
        UPDATE="apt update -q"
        INSTALL="apt install -y"
        REMOVE="apt remove -y"
        return 0
    }

    check_cmd apt-get && {
        UPDATE="apt-get update -q"
        INSTALL="apt-get install -y"
        REMOVE="apt-get remove -y"
        return 0
    }

    check_cmd yum && {
        UPDATE="yum update -yq"
        INSTALL="yum install -y"
        REMOVE="yum "
        PKG_LIBEV="libev-devel"
        PKG_SSL="openssl-devel"
        return 0
    }

    check_cmd pacman && {
        UPDATE="pacman -Sy --noprogressbar"
        INSTALL="pacman -S --noconfirm --noprogressbar"
        REMOVE="pacman -R --noconfirm --noprogressbar"
        PKG_LIBEV="libev"
        PKG_SSL="openssl"
        return 0
    }

    return 1
}

check_tool() {
    local tool=$1

    check_cmd $tool || $INSTALL $tool
}

show_distribution

detect_pkg_tool || {
    echo "Your platform is not supported by this installer script."
    exit 1
}

#$UPDATE

[ "$LSB_ID" = "centos" ] && $INSTALL epel-release

check_tool pkg-config
check_tool gcc
check_tool make
check_tool cmake
check_tool git

$INSTALL $PKG_LIBEV
$INSTALL $PKG_SSL

rm -rf /tmp/rtty-build
mkdir /tmp/rtty-build
pushd /tmp/rtty-build

git clone https://github.com/zhaojh329/libuwsc.git || {
    echo "Clone libuwsc failed"
    exit 1
}

sleep 2

git clone https://github.com/zhaojh329/rtty.git || {
    echo "Clone rtty failed"
    exit 1
}

# libuwsc
rm -f /usr/local/lib/libuwsc.*
cd libuwsc && cmake . && make install && cd -
[ $? -eq 0 ] || exit 1

# rtty
cd rtty && cmake . && make install
[ $? -eq 0 ] || exit 1

popd
rm -rf /tmp/rtty-build

ldconfig

case "$LSB_ID" in
    centos|arch)
        echo "/usr/local/lib" > /etc/ld.so.conf.d/rtty
        ldconfig -f /etc/ld.so.conf.d/rtty
    ;;
esac

rtty -V

