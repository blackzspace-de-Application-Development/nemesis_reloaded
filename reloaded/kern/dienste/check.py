import platform
import coloredlogs, logging
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

coloredlogs.install(level=logg.DEBUG,
                    logger=loggy,
                    fmt='%(asctime)s [%(levelname)s] - %(message)s',
                    datefmt='%H:%M:%S',
                    field_styles=fieldstyle,
                    level_styles=levelstyles)      
        
        



class Check:
    def __init__(self):
        self.osxy = platform.system()
        
        if self.osxy == "Windows":
            loggy.debug("Detected OS: " + self.osxy)
            loggy.info("OS supported")
            return None
        if self.osxy == "Linux":
            loggy.debug("Detected OS: " + self.osxy)
            loggy.info("OS supported")
            return None
