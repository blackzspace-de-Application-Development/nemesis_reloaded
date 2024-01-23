from __future__ import print_function
import colorama
from colorama import * 
# import medusa.kern.dienste.version



class Paint:
    def __init__(self):
        self.br=Back.BLACK + Fore.RED
        self.bc=Back.BLACK + Fore.CYAN
        self.by=Back.BLACK + Fore.YELLOW
        self.bb=Back.BLACK + Fore.BLUE
        self.bg=Back.BLACK + Fore.GREEN
        self.bm=Back.BLACK + Fore.MAGENTA
        self.bw=Back.BLACK + Fore.WHITE
        
        self.wr=Back.WHITE + Fore.RED
        self.wc=Back.WHITE + Fore.CYAN
        self.wy=Back.WHITE + Fore.YELLOW
        self.wb=Back.WHITE + Fore.BLACK
        self.wg=Back.WHITE + Fore.BLUE
        self.wm=Back.WHITE + Fore.MAGENTA
        self.wbl=Back.WHITE + Fore.BLACK
        
        self.b1="BLACK"
        self.b2=f"WHITE"
        self.b3=f"RED"
        self.b3=f"CYAN"
        self.b3=f"YELLOW"
        self.b3=f"BLUE"
        self.b3=f"MAGENTA"
        self.b3=f"GREEN"
        
        self.b=f"Back."
        self.f=f" Fore."
        
        self.res=Back.RESET + Fore.RESET
        
p=(print)

        
# 'p1=Paint()
        
# p=(print)
# text="Sinnvollertext"'
# # p(f"{p1.b} + {p1.b1} + {p1.f} + {p1.b3} + text")
        
# 'p(p1.wr + text)
#         '