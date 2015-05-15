
import os
import sys
import pwd


from classes.VirtualHost import VirtualHost

#import VirtualHost


class FrameworkInstaller:

    def __init__(self):
        self.VServer = VirtualHost()
        self.VServer.start()
        self.frameworkName = " "

    def mkdirFrame(self):
        print("Hello")

    #Create User
    def composer_instructions(self,group,projectname):

        #composer create-project pragmaticlinux/[dist] [dir] [branch|tag]

        os.system("create-project pragmatic/")
        os.system("useradd -m -g "+group+" -G wheel -s /bin/bash "+projectname)
        os.mkdir("/home/"+projectname+"/public_html",777)
        os.system("chmod -R 777 /home/"+projectname)

    def start(self):
        os.system("composer create-project pragmaticlinux/"+self.frameworkName+" /home/"+self.VServer.projectname+"/public_html/ dev-environment")


