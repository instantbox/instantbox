# init.sh

check_cmd() {
    which $1 > /dev/null 2>&1
}

pretty_name=""
UPDATE=""
INSTALL=""
REMOVE=""
show_distribution() {


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

clone_html(){
    git clone https://github.com/super-inspire/super-inspire-frontend.git /var/super-inspire-frontend
    mv /var/super-inspire-frontend/build /var/build
    rm -rf /var/super-inspire-frontend
}



show_distribution
detect_pkg_tool

if [[ detect_pkg_tool == 1 ]]; then
    echo 'not support platform'
    exit 1
fi

check_cmd git || {
    $UPDATE && $INSTALL git
}

check_cmd wget || {
    $UPDATE && $INSTALL wget
}

clone_html

check_cmd docker-compose || {
    wget https://github.com/docker/compose/releases/download/1.23.2/docker-compose-Linux-x86_64
    mv docker-compose-Linux-x86_64 docker-compose && chmod +x docker-compose
    mv docker-compose /usr/bin
}


