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

VERSION_NUM=1.0
TYPE=standalone

UPDATE="update"
INSTALL="install"
VERSION="version"
LIST="list"

echo "   _____                                 _   _        _      _                  "
echo "  |  __ \                               | | (_)      | |    (_)                 "
echo "  | |__) | __ __ _  __ _ _ __ ___   __ _| |_ _  ___  | |     _ _ __  _   ___  __"
echo "  |  ___/ '__/ _\` |/ _\` | '_ \` _ \ / _\` | __| |/ __| | |    | | '_ \| | | \ \/ /"
echo "  | |   | | | (_| | (_| | | | | | | (_| | |_| | (__  | |____| | | | | |_| |>  < "
echo "  |_|   |_|  \__,_|\__, |_| |_| |_|\__,_|\__|_|\___| |______|_|_| |_|\__,_/_/\_\\"
echo "                    __/ |                                                       "
echo "                   |___/                                                        "
echo "===================================================================================="
echo " "



create_new_project(){
	python ./framework/pragmaticFramework.py $1
}

###################################
#Update pragmatic linux dev tools #
###################################
update_pragmaticDev(){
	mkdir -p /tmp/pragmaticTools
	mkdir -p /tmp/pragmaticTools/update
	mkdir -p /tmp/pragmaticTools/restore
	git clone https://github.com/PragmaticLinux/Tools.git /tmp/pragmaticTools/update
	mv /pragmatic/* /tmp/pragmaticTools/restore
	mv /tmp/pragmaticTools/update/* /pragmatic
	cp /tmp/pragmaticTools/update/pragmatic-dev.sh /usr/bin/pragmatic-dev
	rm -R /tmp/pragmaticTools/update/*
	echo "Updated Successfully"
}




show_version(){
	echo "Pragmatic Dev Tools Version: $VERSION_NUM"
}


##########################
# Help message and usage #
##########################
help_usage(){
	echo "  Usage: pragmatic-dev [options] [framework]"
	echo ""
	echo "  Examples:\n"
	echo "   pragmatic-dev  install laravel	  --->  # Install new framework laravel "
	echo "   pragmatic-dev  update		  --->  # Update PragmaticDev Tools"
	echo ""
	echo "  Where [options] is one of:"
	echo "     version              #Shows the version info and details about PragmaticDev Tools"
	echo "     update               #Update PragmaticDev Tools itself"
	echo "     install [framework]  #Install framework"
	echo "     list                 #List all framework supported by pragmaitc-dev"
}


###################
# List framework  #
###################
list_framework(){
        echo "   ember          # Ember Javascript Framework"
	echo "   laravel        # Laravel php Framework"
	echo "   skeleton       # Skeleton css html Framework"
	echo "   99lime         # 99lime kickstarter HTML CSS Framework"
	echo "   bootstrap      # Bootstrap Css HTML Framework"
	echo "   foundation-css # Foundation Css HTML Framework"
	echo "   angularjs      # AngularJS Javascript Framework"
	echo "   codeigniter    # Codeigniter PHP Framework"
	echo "   yii-basic      # Yii Basic PHP Framework"
	echo "   backbone       # Backbone Javascript Framework"
}

for arg in "$@"
do
case $arg in
	$UPDATE )
		update_pragmaticDev
	;;
	$INSTALL )
		create_new_project $2
	;;	
	$VERSION )
		show_version
	;;
	$LIST )
		list_framework
	;;
	*)
		help_usage
	;;
esac
done

if [  $# = 0 ]
	then
	help_usage
fi
