
import os
import sys
import pwd
import subprocess
import socket
import fcntl
import struct
from classes.VirtualHost import VirtualHost

#import VirtualHost

class FrameworkInstaller:

    def __init__(self):
        self.VServer = VirtualHost()
        self.VServer.start()
        self.frameworkName = " "
        self.specialFramework = "laravel yii-basic yii-advanced"
        self.ip = ""
        # Text attributes
        self.ALL_OFF = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERSCORE = '\033[4m'
        self.BLINK = '\033[5m'
        self.REVERSE = '\033[7m'
        self.CONCEALED = '\033[7m'
 
        # Foreground colors
        self.FG_BLACK = '\033[30m'
        self.FG_RED = '\033[31m'
        self.FG_GREEN = '\033[32m'
        self.FG_YELLOW = '\033[33m'
        self.FG_BLUE = '\033[34m'
        self.FG_MAGENTA = '\033[35m'
        self.FG_CYAN = '\033[36m'
        self.FG_WHITE = '\033[37m'
 
        # Background colors
        self.BG_BLACK = '\033[40m'
        self.BG_RED = '\033[41m'
        self.BG_GREEN = '\033[42m'
        self.BG_YELLOW = '\033[43m'
        self.BG_BLUE = '\033[44m'
        self.BG_MAGENTA = '\033[45m'
        self.BG_CYAN = '\033[46m'
        self.BG_WHITE = '\033[47m'

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
        if self.frameworkName in self.specialFramework:
            os.system("mkdir /tmp/pragmaticLinuxCache")
            os.system("mkdir /tmp/pragmaticLinuxCache/framework")
            os.system("cp -r /home/"+self.VServer.projectname+"/ /tmp/pragmaticLinuxCache/framework/"+self.VServer.projectname)
            os.system("rm -R /home/"+self.VServer.projectname+"/")
            os.system("composer create-project pragmaticlinux/"+self.frameworkName+" /home/"+self.VServer.projectname+"/ dev-environment")
            os.system("cp -r /tmp/pragmaticLinuxCache/framework/"+self.VServer.projectname+"/ /home/"+self.VServer.projectname)
            print("Fixing permission")
            os.system("chmod -R 777 /home/"+self.VServer.projectname+"/")
            os.system("rm -R /tmp/pragmaticLinuxCache/"+self.VServer.projectname)
        else :
            os.system("composer create-project pragmaticlinux/"+self.frameworkName+" /home/"+self.VServer.projectname+"/public_html/ dev-environment")
        print(self.FG_GREEN+"Installation succesful"+self.ALL_OFF)
        self.getInterfaceNet()
        self.generate_info()


    def generate_info(self):
        print("#############################################################################")
        print("# "+self.BOLD+"Framework Installer "+self.REVERSE+"Pragmatic "+self.FG_CYAN+" Linux"+self.FG_CYAN+self.ALL_OFF+" ")
        print("# "+self.BOLD+self.FG_YELLOW+"Hostname: "+self.ALL_OFF+self.VServer.projectname)
        print("# "+self.BOLD+self.FG_YELLOW+"Home Directory: "+self.ALL_OFF+"/home/"+self.VServer.projectname)
        print("# "+self.BOLD+self.FG_YELLOW+"WWW Directory: "+self.ALL_OFF+"/home/"+self.VServer.projectname+"/public_html")
        print("# "+self.BOLD+self.FG_YELLOW+"Type: "+self.ALL_OFF+" Framework")
        print("# "+self.BOLD+self.FG_YELLOW+"User: "+self.ALL_OFF+self.VServer.projectname)
        print("#")
        print("# "+self.BOLD+self.FG_YELLOW+"FTP Server:"+self.ALL_OFF+self.ip)
        print("# "+self.BOLD+self.FG_YELLOW+"FTP Account:"+self.ALL_OFF+self.VServer.projectname)
        #Default ftp pass or custom
        if self.VServer.password == "pragmatic":
            print("# "+self.BOLD+self.FG_YELLOW+"FTP Password: "+self.ALL_OFF+"(Default password \"pragmatic\")  ")
        else :
            print("# "+self.BOLD+self.FG_YELLOW+"FTP Password: "+self.ALL_OFF+self.VServer.password)
        print("#")
        print("# "+self.BOLD+self.FG_YELLOW+"SSH Server: "+self.ALL_OFF+self.ip)
        print("# "+self.BOLD+self.FG_YELLOW+"SSH Account:"+self.ALL_OFF+self.VServer.projectname)
        #Default pass or custom
        if self.VServer.password == "pragmatic":
            print("# "+self.BOLD+self.FG_YELLOW+"FTP Password: "+self.ALL_OFF+"(Default password \"pragmatic\")  ")
        else :
            print("# "+self.BOLD+self.FG_YELLOW+"FTP Password: "+self.ALL_OFF+self.VServer.password)
        print("# ")
        print("# "+self.BOLD+self.FG_YELLOW+"MySQL Server: "+self.ALL_OFF+"localhost or"+self.ip)
        print("# "+self.BOLD+self.FG_YELLOW+"MySQL Account: "+self.ALL_OFF+" Default - root")
        print("# "+self.BOLD+self.FG_YELLOW+"MySQL Password:"+self.ALL_OFF+" Default -(pragmatic)")
        print("# This file is generated on /home/"+self.VServer.projectname+"/infoServer")
        print("#############################################################################")



        #
        # Generate ServerInfo File
        #
        serverInfo = "#############################################################################\n"
        serverInfo += "# This file is generated by PragmaticLinux Framework Installer\n"
        serverInfo += "# Framework Installer Pragmatic  Linux\n"
        serverInfo += "# Hostname: "+self.VServer.projectname+" \n"
        serverInfo += "# Home Directory: /home/"+self.VServer.projectname+"\n"
        serverInfo += "# WWW Directory: /home/"+self.VServer.projectname+"/public_html\n"
        serverInfo += "# Type: Framework\n"
        serverInfo += "# User: "+self.VServer.projectname+"\n"
        serverInfo += "#\n"
        serverInfo += "# FTP Server: "+self.ip+"\n"
        serverInfo += "# FTP Account: "+self.VServer.projectname+"  \n"
        if self.VServer.password == "pragmatic":
            serverInfo += "# FTP Password: (Default password \""+self.VServer.password+"\")  \n"
        else:
            serverInfo += "# FTP Password: "+self.VServer.password+"\n"
        #SSH Info
        serverInfo += "#\n"
        serverInfo += "# SSH Server: "+self.ip+" \n"
        serverInfo += "# SSH Account "+self.VServer.projectname+"  \n"
        if self.VServer.password == "pragmatic":
            serverInfo += "# SSH Password: No Password Defined (\"use passwd $user\")\n"
        else:
            serverInfo += "# SSH Password: "+self.VServer.password+"\n"

        serverInfo += "# \n"
        serverInfo += "# MySQL Server: localhost \n"
        serverInfo += "# MySQL Account: Default - root \n"
        serverInfo += "# MySQL Password: Default -(pragmatic)  \n"
        serverInfo += "#\n"
        serverInfo += "#############################################################################\n"
        f = open('/home/'+self.VServer.projectname+"/serverInfo", 'a')
        f.write(serverInfo)
        f.close()

    def getInterfaceNet(self):
        interface = str(subprocess.check_output("ifconfig -s -a",shell=True)).split("\\n")
        interface.pop(0)
        interface.pop(len(interface)-1)
        #interface = sot.split("\\n")
        inet = []
        iteration = 0
        #get interface and ip
        for iface in interface:
            interfaceLocal = iface.split("   ")[0].encode(encoding="UTF-8")
            inet.append(self.get_ip_address(interfaceLocal.strip()))
            iteration = iteration + 1
        #generate string with ip
        for lip in inet:
            self.ip += lip+"     "


    def get_ip_address(self,ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])

        