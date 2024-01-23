import os
import sys
import shlex
import logging, coloredlogs
import subprocess
import platform as plat

from reloaded.farben import *
from scapy.all import *
from reloaded.kern import basis
from io import StringIO
from subprocess import Popen, PIPE, STDOUT




 
logg=logging
loggy= logg.getLogger(__name__)

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


p1=Paint()

class Main(basis.Module):
    """AutoScan 1 [param] --logging lv : auto"""

    parameters = {
        "param": ""
    }
    

    completions = list(parameters.keys())
    

    def exec(self, command_line,  argx):
        
        command_line_args = shlex.split(argx)
        process = subprocess.Popen(command_line_args, shell=True, stdout=PIPE, stderr=STDOUT)
        with process.stdout:
            for line in iter(process.stdout.readline, b''):
                # print(line.decode("latin1").strip())
                loggy.info(line.decode("latin1").strip())
        loggy.info('Subprocess: "' + command_line + '"')
        try:
            command_line_process = subprocess.Popen(
            command_line_args,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
            process_output, _ =  command_line_process.communicate()
            # self.capturedlog(process_output)
        except (OSError, subprocess.CalledProcessError) as exception:
            loggy.info('Exception occured: ' + str(exception))
            loggy.info('Subprocess failed')
            return False
        else:
           loggy.info('Subprocess finished')
        return True

    def do_run(self, argx):
        """Execute current module"""
        osx = plat.system()
        
        param = self.parameters['param']
    
        logg.basicConfig(filename='wifi.log', logger=loggy, filemode="w", level=logg.INFO)
        loggy.info("\nExecuting WiFI-scan:")
        
        if osx == "Windows":
            argx="netsh wlan show network " + param
        if osx == "Linux":
            argx="nmcli dev wifi " + param
            
            
        self.exec(command_line="", argx=argx)
        print(p1.res)
       
        



    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return f"{p1.by}" + [s[offs:] for s in self.completions if s.startswith(mline)]

    def default(self, line):
        cmd, arg, line = self.parseline(line)
        func = [getattr(self, n) for n in self.get_names() if n.startswith('do_' + cmd)]
        if func: # maybe check if exactly one or more elements, and tell the user
            func[0](arg)
        else:
            os.system(line)