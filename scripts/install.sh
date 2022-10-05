#!/bin/bash 

apt_install () {
  echo 'running apt-get update...'
  apt-get update

  echo 'installing docker dependencies...'

	if ! apt-get install ca-certificates curl gnupg lsb-release; then
    echo 'docker dependencies could not be installed.'
    echo 'Please report the issue to https://github.com/menghaoyu2002/CSC302-TeamRocket/issues with the logs file ./install_logs.txt attached'
    exit 1
  fi 

  echo 'installing docker engine'
  {
    mkdir -p /etc/apt/keyrings

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg

    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

    apt-get update
    apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
  } || {
    echo 'docker engine could not be installed.'
    echo 'Please report the issue to https://github.com/menghaoyu2002/CSC302-TeamRocket/issues with the logs file ./install_logs.txt attached'
    exit 1
  }

  echo 'installing docker desktop'
  {
    curl --create-dirs -O --output-dir ./tmp https://desktop.docker.com/linux/main/amd64/docker-desktop-4.12.0-amd64.deb
    apt-get install ./tmp/docker-desktop-4.12.0-amd64.deb
    rm -rf ./tmp
  } || {
    echo 'docker desktop could not be installed.'
    echo 'Please report the issue to https://github.com/menghaoyu2002/CSC302-TeamRocket/issues with the logs file ./install_logs.txt attached'
    exit 1
  }
}

# yum_install() {
# }


(
  if command -v apt >/dev/null; then
    echo 'installing dependencies with apt'
		apt_install
    
  elif command -v yum >/dev/null; then
      echo 'installing dependencies with yum'
      yum_install
  else
      echo 'The only package managers currently supported are apt and yum'
      echo 'Please request support for your package at https://github.com/menghaoyu2002/CSC302-TeamRocket/issues'
      exit 1
  fi
  
  echo 'docker install complete!'
) 2>&1 | tee -a install_logs.txt



