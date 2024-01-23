import platform as plat
import os
import time
import logging, coloredlogs
from scapy.all import *
from reloaded.kern import basis
from reloaded.farben import*
from reloaded.kern.dienste.check import Check
from socket import *

startTime = time.time()


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

logg.basicConfig(filename='portscan.log', filemode="w", level=logg.INFO)


class Main(basis.Module):
    """IPCONFIG [para] """

    parameters = {
        "param": ""
    }
    completions = list(parameters.keys())

    def do_run(self, line):
        """Execute current module"""
        
        param = self.parameters['param']
        target = input('Enter the host to be scanned: ')
        t_IP = gethostbyname(target)
        loggy.info('Starting scan on host: ', t_IP)
   
        for i in range(50, 500):
            s = socket(AF_INET, SOCK_STREAM)
      
            conn = s.connect_ex((t_IP, i))
            if(conn == 0) :
                loggy.info('Port %d: OPEN' % (i,))
            s.close()
            
        loggy.info('Time taken:', time.time() - startTime)


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


