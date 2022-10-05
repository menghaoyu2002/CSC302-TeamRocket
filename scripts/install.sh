#!/bin/bash 

echo_report_error_message() {
    echo 'Please report the issue to https://github.com/menghaoyu2002/CSC302-TeamRocket/issues with the logs file ./install_logs.txt attached'
    exit 1
}

apt_install () {
  echo 'running apt-get update...'
  apt-get update

  echo 'installing docker dependencies...'

	if ! apt-get install ca-certificates curl gnupg lsb-release; then
    echo 'docker dependencies could not be installed.'
    echo_report_error_message
  fi 

  echo 'installing docker engine'
  {
    mkdir -p /etc/apt/keyrings

    curl -fsSL $GPG_LINK | gpg --dearmor -o /etc/apt/keyrings/docker.gpg

    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] $REPO_LINK \
    $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

    apt-get update
    apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
  } || {
    echo 'docker engine could not be installed.'
    echo_report_error_message
  }
}

dnf_install() {
  echo 'installing docker engine'
  {
    dnf -y install dnf-plugins-core
    dnf config-manager --add-repo $REPO_LINK
    dnf install docker-ce docker-ce-cli containerd.io docker-compose-plugin 
  } || {
    echo 'docker engine could not be installed'
    echo_report_error_message
  }
}

yum_install() {
  echo 'installing docker engine'
  {
    yum install -y yum-utils
    yum-config-manager --add-repo $REPO_LINK
    yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin
  } || {
    echo 'docker engine could not be installed'
    echo_report_error_message
  }
}

# install docker
install() {
  if command -v apt >/dev/null; then
    echo 'installing dependencies with apt'
    apt_install
  elif command -v dnf >/dev/null; then
    echo 'installing dependencies with dnf'
    dnf_install
  elif command -v yum >/dev/null; then
    echo 'installing dependencies with yum'
    yum_install
  else
    echo 'The only package managers currently supported are apt, dnf, and yum.'
    echo 'Please request support for your package manager at https://github.com/menghaoyu2002/CSC302-TeamRocket/issues'
    exit 1
  fi
}

(
  # check which version of linux
  # source https://unix.stackexchange.com/questions/6345/how-can-i-get-distribution-name-and-version-number-in-a-simple-shell-script
  if [ -f /etc/os-release ]; then
      . /etc/os-release
      OS=$NAME
  elif type lsb_release >/dev/null 2>&1; then
      OS=$(lsb_release -si)
  elif [ -f /etc/lsb-release ]; then
      . /etc/lsb-release
      OS=$DISTRIB_ID
  elif [ -f /etc/debian_version ]; then
      OS=Debian
  else
    echo 'Your version of linux could not be identified'
    echo_report_error_message
  fi

  # truncate the OS to the first word
  OS=$(echo $OS | awk '{print $1;}')

  # handle which download urls to use based on distro
  if [[ "$OS" == "Ubuntu" ]]; then
    GPG_LINK="https://download.docker.com/linux/ubuntu/gpg"
    REPO_LINK="https://download.docker.com/linux/ubuntu"
    install
  elif [[ "$OS" == "Debian" ]]; then 
    GPG_LINK="https://download.docker.com/linux/debian/gpg"
    REPO_LINK="https://download.docker.com/linux/debian"
    install
  elif [[ "$OS" == "Fedora" ]]; then
    REPO_LINK="https://download.docker.com/linux/fedora/docker-ce.repo"
    install
  elif [[ "$OS" == "CentOS"]]; then 
    REPO_LINK="https://download.docker.com/linux/centos/docker-ce.repo"
    install
  else 
      echo 'Your version of linux is not yet supported.'
      echo 'Please manually install docker from https://docs.docker.com/desktop/install/linux-install/' 
      exit 1
  fi

  echo 'docker install complete!'

  echo 'starting docker...'
  {
    systemctl start docker
  } || {
    echo 'Docker could not be started.'
    echo_report_error_message
  }
  echo 'docker has been started.'

  echo 'verifying docker installation...' 
  {
    docker run hello-world
  } || {
    echo 'Docker installation was unsucessful.'
    echo_report_error_message
  }

  echo 'docker has been installed.'
) 2>&1 | tee -a install_logs.txt



