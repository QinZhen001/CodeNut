#!/bin/bash

# java
<<<<<<< HEAD
apt-get install -y openjdk-7-jdk

# ruby
apt-get install -y ruby-full
=======
apt-get install openjdk-8-jdk -y

# ruby
apt-get install ruby-full -y
>>>>>>> refs/remotes/origin/all

# mono
PREFIX=$@
if [ -z $PREFIX  ]; then
      PREFIX="/usr/local"
  fi

  # Ensure you have write permissions to PREFIX
  mkdir $PREFIX
  chown -R `whoami` $PREFIX

  # Ensure that all required packages are installed.
  apt-get install -y wget git autoconf libtool automake build-essential mono-devel gettext cmake

  PATH=$PREFIX/bin:$PATH
  git clone https://github.com/mono/mono.git
  cd mono
  ./autogen.sh --prefix=$PREFIX
  make
  make install

# go
# https://www.golangtc.com/download
nohup wget https://www.golangtc.com/static/go/1.9/go1.9.linux-amd64.tar.gz && 
tar -C /usr/local/share/ -xzf go1.9.linux-amd64.tar.gz && 
ln -s /usr/local/share/go/bin/go /usr/bin/go &
