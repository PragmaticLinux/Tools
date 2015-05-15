
import os
import sys
import pwd


class VirtualHost:
    successful = False
    projectname = " "

    def prt(self):
        print("Hello")

    #Create User
    def create_user(self,group,projectname):
        os.system("useradd -m -g "+group+" -G wheel -s /bin/bash "+projectname)
        os.mkdir("/home/"+projectname+"/public_html",777)
        os.system("chmod -R 777 /home/"+projectname)

    #Create Virtualhost
    def create_virtualhost(self,projectname):

        # Hostname create
        file = open('/etc/hosts','a')
        file.write('#ProjectName - '+self.projectname+' \n127.0.0.1    '+self.projectname+'    '+self.projectname+'\n')
        file.close()
        # Configure VirtualHost
        vhr = '\n\n<VirtualHost *:80>'
        vhr += '\n\tServerAdmin '+projectname
        vhr += '\n\tDocumentRoot \"/home/'+projectname+'/public_html\"'
        vhr += '\n\tServerName '+projectname
        vhr += '\n\tErrorLog \"/var/log/httpd/'+projectname+'-error_log\"'
        vhr += '\n\tCustomLog \"/var/log/httpd/'+projectname+'-access_log\" common'
        vhr += '\n\t<Directory \"/home/'+projectname+'/public_html\">'
        vhr += '\n\t\tOptions Indexes FollowSymLinks'
        vhr += '\n\t\tAllowOverride All'
        vhr += '\n\t\tRequire all granted'
        vhr += '\n\t</Directory>'
        vhr += '\n</VirtualHost>'
        vhost = open('/etc/httpd/conf/extra/httpd-vhosts.conf','a')
        vhost.write(vhr)
        vhost.close()

    #Create Project
    def create_project(self):
        self.projectname = input('Project Name: ')
        group = "projectdev"

        #Creating User  
        try:
            pwd.getpwnam(self.projectname)
        except KeyError:
            print("User Created")
            self.create_user(group,self.projectname)

        
        # Virtual Host rules to write
        self.create_virtualhost(self.projectname)

        # write application to execute "sysmtectl restart httpd.service"
        os.system("systemctl restart httpd.service")
        self.successful = True

    def remove_project(self):
        os.system("userdel -r "+self.projectname)
        print(self.projectname)
    def start(self):
        self.create_project()
        if self.successful is False:
            self.create_project()
        while self.successful is False:
            self.remove_project()
            self.create_project()

        if self.successful is True:
            print("Successful")

