# Tools: Laravel Installer
# Date:10/Nov/2014
# Author: Alban Mulaki (lithium)
# Website: 

#Library

import sys
import os
from classes.VirtualHost import VirtualHost

#import VirtualHost
VServer = VirtualHost()
VServer.start()


# if VServer.successful is False:
#     VServer.create_project()

# #Check if everything was alright
# while VServer.successful is False:
#         VServer.remove_project()
#         VServer.create_project()

# if VServer.successful == True:
#     print("Successful")

    # write application to execute "sysmtectl reload httpd.service"

