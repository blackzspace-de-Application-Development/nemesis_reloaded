#!/usr/bin/python3
# check dependencies before start
from .kern.dienste import check_dependencies
check_dependencies()


import platform as plat
import cmd
import os
import sys
import coloredlogs, logging
import colorama

from .modules import *
from .modules import module_list, all_modules

from .farben import *
from .kern.dienste import logo




completions = module_list() 

p1=Paint()


 




loggy = logging.getLogger(__name__)

fieldstyle = {'asctime': {'color': 'green'},
              'levelname': {'bold': True, 'color': 'black'},
              'filename':{'color':'cyan'},
              'funcName':{'color':'blue'}}
                                   
levelstyles = {'critical': {'bold': True, 'color': 'red'},
               'debug': {'color': 'blue'}, 
               'error': {'color': 'red'}, 
               'info': {'color':'cyan'},
               'warning': {'color': 'yellow'}}

coloredlogs.install(level=logging.INFO,
                    logger=loggy,
                    fmt='%(asctime)s [%(levelname)s] - %(message)s',
                    datefmt='%H:%M:%S',
                    field_styles=fieldstyle,
                    level_styles=levelstyles)      
        
print(Back.BLACK + "")        
class Main(cmd.Cmd):
    """ Commands: use, show, exit, help"""
    
    intro = logo()

    prompt = p1.bg + 'R3704d3d > '
    doc_header = 'Commands'
    undoc_header = 'Undocumented Commands'
    
    def do_use(self, line):
        """Select module for modules"""
        if line in module_list():
            module = globals()[line]
            if hasattr(module, 'Main'):
                module = module.Main()
                module.prompt = f"{p1.bg}R3704d3d > {line} > "
                module.cmdloop()
            else:
                 loggy.warning("*** Module `{module}` not has `Main` class!")
        else:
            loggy.warn(f"*** Module {line} not found!")
        


    def do_show(self, line):
        """Show available modules"""
        all_modules()
    

    def do_exit(self, line):
        """Exit"""
        return True

    def complete_use(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in completions if s.startswith(mline)]
    
    def default(self, line):
        cmd, arg, line = self.parseline(line)
        func = [getattr(self, n) for n in self.get_names() if n.startswith('do_' + cmd)]
        if func: # maybe check if exactly one or more elements, and tell the user
            func[0](arg)
        else:
            os.system(line)
   


                

def start_reloaded():
    try:
        Main().cmdloop()
    except KeyboardInterrupt:
        x = input("Do your really want to exit?(Yy/Nn)")
        if  x == "n" or "N":
            return True
        if x == "y" or "Y":
            print(p1.by + "\nBye!")
            sys.exit()
        

if __name__ == '__main__':
    start_reloaded()
