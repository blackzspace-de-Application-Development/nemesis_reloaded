import cmd
import sys
from reloaded.modules import all_modules, module_list
from reloaded.farben import *

p1=Paint()
completions = [
    'target',
    'ip',
    'gateway',
    'mac',
    'iface',
    'gateway_mac',
    'target_mac'
]

class Module(cmd.Cmd):
    parameters = {}
   


    def do_run(self):
        """Execute current module"""
        pass

    def do_back(self, *args):
        """go back one level"""
        return True

    def do_exit(self, line):
        """exit websploit"""
        sys.exit(0)

    def do_set(self, line):
        """set options"""
        try:
            key, value = line.split(' ')
            print(key, value)
            self.parameters.update({key: value})
        except KeyError:
             print(f"{p1.br}*** Unknown Option! option not has value!{p1.res}")
        except ValueError:
            print(f"{p1.bm}*** Option not has value!{p1.res}")
            print(f"{p1.bg}*** Example : set host 127.0.0.1{p1.res}")
     
    def do_options(self, line):
        """Show options of current module"""
        print("\n")
        print(f"{p1.bm}{'Option':20}\t{'Value':20}{p1.res}")
        print(f"{p1.by}{'--'*8:<20}\t{'--'*8:<20}{p1.res}")
        for k,v in self.parameters.items():
            print(f"{p1.bg}{k:20}\t{v:20}{p1.res}")
        print("\n")

    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]
