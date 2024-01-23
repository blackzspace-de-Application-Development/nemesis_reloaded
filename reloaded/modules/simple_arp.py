import scapy.all as scapy
import os
import sys
import logging, coloredlogs
from reloaded.farben import*
from reloaded.kern import basis

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
    """Another arp-wifi scan"""
    parameters = {
        "ip": "192.168.178.1",
        "prefix": "/24",
        "opt": "opt"
    }
    
    def do_run(self, line):
        """ Executes module []"""
        self.ip=self.parameters['ip']
        self.prefix=self.parameters['prefix']
        opt = self.parameters['opt']
        
        if opt == "0":
            logg.basicConfig(filename='simple_arp.log', logger=loggy, level=logg.INFO)
            return 
        if opt == "1":
            return 
        
        request = scapy.ARP() 
        request.pdst = self.ip + self.prefix#'192.168.0.1/24'
        broadcast = scapy.Ether() 
        broadcast.dst = 'ff:ff:ff:ff:ff:ff'
        request_broadcast = broadcast / request 
        clients = scapy.srp(request_broadcast, timeout = 10,verbose = 1)[0] 
        for element in clients: 
            print(element[1].psrc + "      " + element[1].hwsrc) 

            loggy.info(element[1].psrc + "      " + element[1].hwsrc) 
            

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
            os.system(line)