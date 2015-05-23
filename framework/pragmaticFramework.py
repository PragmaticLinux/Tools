# Tools: Laravel Installer
# Date:15/May/2015
# Author: Alban Mulaki (lithium)
# Website: 

#Library
import sys
from classes.FrameworkInstaller import FrameworkInstaller
if len(sys.argv) > 1:
    print("Installing "+sys.argv[1])
    framework = sys.argv[1]
else:
    framework = input('Framework Name: ')

FInstaller = FrameworkInstaller()
FInstaller.frameworkName = framework
FInstaller.start()
input(FInstaller.FG_GREEN+"Installation Completed 100% --> Successful  (Press Enter to exit)")