# Tools: Laravel Installer
# Date:10/Nov/2014
# Author: Alban Mulaki (lithium)
# Website:

file = open('/etc/hosts','a')
file.write('127.0.0.1	project	project\n')
# Virtual Host rules to write
vhr = '<VirtualHost *:80>'
vhr += '\n\tServerAdmin project'
vhr += '\n\tDocumentRoot \"/srv/http/project\"'
vhr += '\n\tServerName project'
vhr += '\n\tErrorLog \"/var/log/httpd/project-error_log\"'
vhr += '\n\tCustomLog \"/var/log/httpd/project-access_log\" common'
vhr += '\n\t\t<Directory \"/srv/http/project\">'
vhr += '\n\t\t\tOptions Indexes FollowSymLinks'
vhr += '\n\t\t\tAllowOverride None'
vhr += '\n\t\t\tRequire all granted'
vhr += '\n\t\t</Directory>'
vhr += '\n\t</VirtualHosts>'
file.close()



