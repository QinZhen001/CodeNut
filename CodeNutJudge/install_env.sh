#!/bin/bash

function java() {
  apt-get install openjdk-8-jdk -y || apt-get install -y openjdk-7-jdk
}

function ruby() {
  apt-get install ruby-full -y
}

function mono() {
  apt-get install --yes mono-complete
  : ' # below treat as comments
  PREFIX=$@
  if [ -z $PREFIX  ]; then
    PREFIX="/usr/local"
  fi

  # Ensure you have write permissions to PREFIX
  sudo mkdir $PREFIX
  sudo chown -R `whoami` $PREFIX

  # Ensure that all required packages are installed.
  sudo apt-get install -y git autoconf libtool automake build-essential mono-devel gettext cmake

  PATH=$PREFIX/bin:$PATH
  git clone https://github.com/mono/mono.git
  cd mono
  ./autogen.sh --prefix=$PREFIX
  make
  make install
  '
}


function go() {
  # https://www.golangtc.com/download
  #nohup wget https://www.golangtc.com/static/go/1.9/go1.9.linux-amd64.tar.gz &&
  #tar -C /usr/local/share/ -xzf go1.9.linux-amd64.tar.gz &&
  #ln -s /usr/local/share/go/bin/go /usr/bin/go &
  sudo apt-get install -y golang
}

function nodejs() {
  # https://nodejs.org/en/download/
  apt-get install --yes nodejs
  return
}



function main() {
  env=('java' 'ruby' 'mono' 'go' 'nodejs')
  for e in ${env[*]}; do
    if [[ -z `which $e` ]]; then eval $e; fi
  done
}

main
