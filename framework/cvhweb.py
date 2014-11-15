# Tools: Laravel Installer
# Date:10/Nov/2014
# Author: Alban Mulaki (lithium)
# Website: 


import os
import sys
#automatic = sys.argv[1]
#print(arg)
projectname = input('Project Name: ')
sts = os.path.isdir("/srv/http/"+projectname)
if sts == 1:
  print("Directory with name "+projectname)
else:
  print('OK Continue Program'+projectname)

#Make directory
os.mkdir('/srv/http/'+projectname,777)

# Hostname create
file = open('/etc/hosts','a')
file.write('#Project name - '+projectname+' \n127.0.0.1	'+projectname+'	'+projectname+'\n')
file.close()

	
# Virtual Host rules to write
vhr = '\n\n<VirtualHost *:80>'
vhr += '\n\tServerAdmin '+projectname
vhr += '\n\tDocumentRoot \"/srv/http/'+projectname+'\"'
vhr += '\n\tServerName '+projectname
vhr += '\n\tErrorLog \"/var/log/httpd/'+projectname+'-error_log\"'
vhr += '\n\tCustomLog \"/var/log/httpd/'+projectname+'-access_log\" common'
vhr += '\n\t<Directory \"/srv/http/'+projectname+'\">'
vhr += '\n\t\tOptions Indexes FollowSymLinks'
vhr += '\n\t\tAllowOverride All'
vhr += '\n\t\tRequire all granted'
vhr += '\n\t</Directory>'
vhr += '\n</VirtualHost>'

vhost = open('/etc/httpd/conf/extra/httpd-vhosts.conf','a')
vhost.write(vhr)
vhost.close()

# write application to execute "sysmtectl restart httpd.service"
# write application to execute "sysmtectl reload httpd.service"

