#!/bin/bash
# Title		: pragmatic-dev.sh
# Description	: Install Frameworks for web devepolment platform
# Author	: Alban Mulaki <amulaki@pragmaticlinux.org> or <alban.mulaki@gmail.com>
# Date		: 14 April 2016
# Usage		: sh pragmatic-dev.sh or pragmatic-dev
# Copyright	: Alban Mulaki & PragmaticLinux
# Website	: www.pragmaticlinux.org
# Author Website: www.pragmaticlinux.org/AlbanMulaki
#
# @pragmaticLinux
#========================================================================================

VERSION=1.0
TYPE=standalone
EXTENSION[update]=update
EXTENSION[install]=install
EXTENSION[version]=version
EXTENSION[list]=list
#EXTENSION[-]
#EXTENSION[-]
##echo $EXTENSION[-u]
#echo ${EXTENSION[-u]}
echo " _____                                 _   _        _      _                  "
echo "|  __ \                               | | (_)      | |    (_)                 "
echo "| |__) | __ __ _  __ _ _ __ ___   __ _| |_ _  ___  | |     _ _ __  _   ___  __"
echo "|  ___/ '__/ _\` |/ _\` | '_ \` _ \ / _\` | __| |/ __| | |    | | '_ \| | | \ \/ /"
echo "| |   | | | (_| | (_| | | | | | | (_| | |_| | (__  | |____| | | | | |_| |>  < "
echo "|_|   |_|  \__,_|\__, |_| |_| |_|\__,_|\__|_|\___| |______|_|_| |_|\__,_/_/\_\\"
echo "                  __/ |                                                       "
echo "                 |___/                                                        "
echo -en "\n===================================================================================="
echo " "



create_new_project(){
	echo "write script for installing framework"
}

#Update pragmatic linux dev tools

update_pragmaticDev(){
	mkdir -p /tmp/pragmaticTools
	mkdir -p /tmp/pragmaticTools/update
	mkdir -p /tmp/pragmaticTools/restore
	git clone https://github.com/PragmaticLinux/Tools.git /tmp/pragmaticTools/update
	mv /pragmatic/* /tmp/pragmaticTools/restore
	mv /tmp/pragmaticTools/update/* /pragmatic
	echo "Updated Successfully"
}

show_version(){
	echo "show version here"
}

help_usage(){
	echo "Help usage"
}

list_framework(){
	echo "list framework supported to install"
}

for arg in "$@"
do
case $arg in
	update )
		update_pragmaticDev
	;;
	install )
		create_new_project
	;;	
	version )
		show_version
	;;
	list )
		list_framework
	;;
	*)
		help_usage
	;;
esac
done
if [ $# == 0 ]
	then
	help_usage
fi
