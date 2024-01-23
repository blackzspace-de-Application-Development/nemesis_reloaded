import platform
import importlib.util
import sys
import subprocess
import coloredlogs, logging
import colorama
from colorama import *
from time import sleep
from reloaded.farben import *



p1=Paint()

logg=logging
loggy = logg.getLogger(__name__)

fieldstyle = {'asctime': {'color': 'green'},
              'levelname': {'bold': True, 'color': 'black'},
              'filename':{'color':'cyan'},
              'funcName':{'color':'blue'}}
                                   
levelstyles = {'critical': {'bold': True, 'color': 'red'},
               'debug': {'color': 'green'}, 
               'error': {'color': 'red'}, 
               'info': {'color':'blue'},
               'warning': {'color': 'yellow'}}

coloredlogs.install(level=logg.INFO,
                    logger=loggy,
                    fmt='%(asctime)s [%(levelname)s] - %(message)s',
                    datefmt='%H:%M:%S',
                    field_styles=fieldstyle,
                    level_styles=levelstyles)  

def check_dependencies():
    colorama.init()
    
    
    """Check system befor starting core"""
    modules = [
        'scapy',
        'requests',
        'colorama',
        'dnslib',
        'coloredlogs'
    ]

    not_installed_modules = []

    for module in modules:
        spec = importlib.util.find_spec(module)
        if spec is None:
            loggy.warning(f" Console > [-] WARNING : `{module}` library not installed.")  
            not_installed_modules.append(module)

    if not_installed_modules:
        install_string = ""
        for module in not_installed_modules:
            install_string += f"{p1.bm} {module} "

        install_command = f"{p1.br} python -m pip install {install_string}"
        
        if install_string in sys.modules == True:
        
            loggy.debug("Console > [+] Use below command for installing missing libraries.")
            loggy.debug(f"Console > [+] {install_command}")
            loggy.debug("Console > Do you want to auto-install? (y/n)")
        
            x = input(p1.br + "R3704d3d > ")
        
            if x == "y" or "Y":
                p = subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
    install_string])
                p.communicate()[0]

            if x == "n" or "N":
                loggy.info(f" {p1.bw} Console > Do you want to try 2 continue with missing dependencies?(y/n)")
                a = input(p1.bg + "Decision: ")
                if a == "y" or "Y":
                    return True
                if a == "n" or "N":
                    sys.exit()
        else:
            loggy.warning("Console > " + install_string + " isnt a pip-package.")        
        
    else:
        loggy.info("Console > Modules are all installed.")
        loggy.info("Console > initializing....")
    
        return True
  