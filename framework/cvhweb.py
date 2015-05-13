# Tools: Laravel Installer
# Date:10/Nov/2014
# Author: Alban Mulaki (lithium)
# Website: 

#Library
import os
import sys
import pwd

#Environment Variables
#successful = False
#projectname = None

class VirtualServer:
    successful = False
    projectname = " "
    def create_project(self):
        self.projectname = input('Project Name: ')
        group = "projectdev"

    #Creating User  
        try:
            pwd.getpwnam(self.projectname)
        except KeyError:
            print("User Created")
            os.system("useradd -m -g "+group+" -G wheel -s /bin/bash "+self.projectname)
            os.mkdir("/home/"+self.projectname+"/public_html",777)
            os.system("chmod -R 777 /home/"+self.projectname)

    # #Make directory
    # os.mkdir('/srv/http/'+this.projectname,777)

    # Hostname create
        file = open('/etc/hosts','a')
        file.write('#ProjectName - '+self.projectname+' \n127.0.0.1    '+self.projectname+'    '+self.projectname+'\n')
        file.close()

        
    # Virtual Host rules to write
        vhr = '\n\n<VirtualHost *:80>'
        vhr += '\n\tServerAdmin '+self.projectname
        vhr += '\n\tDocumentRoot \"/home/'+self.projectname+'/public_html\"'
        vhr += '\n\tServerName '+self.projectname
        vhr += '\n\tErrorLog \"/var/log/httpd/'+self.projectname+'-error_log\"'
        vhr += '\n\tCustomLog \"/var/log/httpd/'+self.projectname+'-access_log\" common'
        vhr += '\n\t<Directory \"/home/'+self.projectname+'/public_html\">'
        vhr += '\n\t\tOptions Indexes FollowSymLinks'
        vhr += '\n\t\tAllowOverride All'
        vhr += '\n\t\tRequire all granted'
        vhr += '\n\t</Directory>'
        vhr += '\n</VirtualHost>'

        vhost = open('/etc/httpd/conf/extra/httpd-vhosts.conf','a')
        vhost.write(vhr)
        vhost.close()

    # write application to execute "sysmtectl restart httpd.service"
        os.system("systemctl restart httpd.service")
        self.successful = True


    def remove_project(self):
        os.system("userdel -r "+self.projectname)
        print(self.projectname)



VServer = VirtualServer()
VServer.create_project()
if VServer.successful is False:
    VServer.create_project()

#Check if everything was alright
while VServer.successful is False:
        VServer.remove_project()
        VServer.create_project()

if VServer.successful == True:
    print("Successful")

    # write application to execute "sysmtectl reload httpd.service"

