#!/bin/bash

#Author: Alban Mulaki
# 09/September/ 2014

case $1 in
"apache" )
#Check Apache Status
retval=$(systemctl status httpd.service)
if [[ $retval == *"Loaded: not-found (Reason: No such file or directory)"* ]] ;
then
  echo "[ Not Installed ]";
fi
if [[ $retval == *"Active: inactive"* ]] ;
then
  echo "[ Not Running ]";
fi
if [[ $retval == *"Active: active (running)"* ]] ;
then
  echo "[ Running ]";
fi
;;
"mysql" )
#Check Apache Status
retval=$(systemctl status mysqld.service)
if [[ $retval == *"Loaded: not-found (Reason: No such file or directory)"* ]] ;
then
  echo "[ Not Installed ]";
fi
if [[ $retval == *"Active: inactive"* ]] ;
then
  echo "[ Not Running ]";
fi
if [[ $retval == *"Active: active (running)"* ]] ;
then
  echo "[ Running ]";
fi
;;
"sshd" )
#Check Apache Status
retval=$(systemctl status sshd.service)
if [[ $retval == *"Loaded: not-found (Reason: No such file or directory)"* ]] ;
then
  echo "[ Not Installed ]";
fi
if [[ $retval == *"Active: inactive"* ]] ;
then
  echo "[ Not Running ]";
fi
if [[ $retval == *"Active: active (running)"* ]] ;
then
  echo "[ Running ]";
fi
;;
"ftp" )
#Check Apache Status
retval=$(systemctl status vsftpd.service)
if [[ $retval == *"Loaded: not-found (Reason: No such file or directory)"* ]] ;
then
  echo "[ Not Installed ]";
fi
if [[ $retval == *"Active: inactive"* ]] ;
then
  echo "[ Not Running ]";
fi
if [[ $retval == *"Active: active (running)"* ]] ;
then
  echo "[ Running ]";
fi
;;
esac