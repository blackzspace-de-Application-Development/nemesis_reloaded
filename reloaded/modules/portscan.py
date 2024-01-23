import os
import sys
import socket
import logging, coloredlogs
from datetime import datetime
from reloaded.kern import basis
from reloaded.farben import  *



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


class Main(basis.Module):
    """Portscan [target] """

    parameters = {
        "target": "192.168.178.1"
    }
    
    completions = list(parameters.keys())

    def do_run(self, line):
        """Execute current module"""
        self.target = self.parameters['target']
    
    # Defining a target
        if len(sys.argv) == 2:
            self.target = socket.gethostbyname(sys.argv[1])
        else:
            loggy.info("R3704d3d > Invalid amount of Argument")
 

        loggy.info("-" * 50)
        loggy.info("Scanning Target: " + self.target)
        loggy.info("Scanning started at:" + str(datetime.now()))
        loggy.info("-" * 50)
        try:
            for port in range(1,65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
         
        # returns an error indicator
                result = s.connect_ex((self.target,port))
                if result ==0:
                        loggy.info("Port {} is open".format(port))
                s.close()
         
        except KeyboardInterrupt:
            if line == "y" or "Y":
                loggy.warning("\n Exiting Program !!!!")
                sys.exit()
            else:
                return True
        except socket.gaierror:
            loggy.warning("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()
        except socket.error:
            loggy.warning("\n Server not responding !!!!")
            sys.exit()

    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]
    
    
    def default(self, line):
        cmd, arg, line = self.parseline(line)
        func = [getattr(self, n) for n in self.get_names() if n.startswith('do_' + cmd)]
        if func: # maybe check if exactly one or more elements, and tell the user
            func[0](arg)
        else:
            if line == "!h":
                self.do_help()
            if line == "!x":
                self.do_exit()
                sys.exit()
            if line == "!w":
                if line:
                    os.system('wsl --exec whois ' + line)
            else:
                os.system(line)