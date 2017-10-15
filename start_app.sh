#!/bin/bash

function check_error() {
  local dir=$1
  for file in `ls $dir | awk '{print $1}'`; do
    local error=`grep error $dir$file`
    if [[ ! -z $error ]]; then
      echo "[!]$file error"
    fi
  done
}

supervisorctl stop all &&
pgrep supervisord| xargs kill -9 ;
rm -rf log/* &&
supervisord -c supervisord.conf &&
sleep 3 &&
check_error log/ &&
supervisorctl status
