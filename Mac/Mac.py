## Mac File
## This file is used to implement code used to run scripts for Mac
## Codes implemented here, will run before the script starts running.

import os
from Mac import Core
from Mac import FileSystem

def Mac():
    ## NOTE: You can use this function
    ## To load information before the app starts running

    ## Lets run the SplashScreen
    from Mac import SplashScreen

    ## Lets check system requirements
    from ErrorReport import SystemRequirements
    
    ## Start App for Mac
    from Mac import MacApp
