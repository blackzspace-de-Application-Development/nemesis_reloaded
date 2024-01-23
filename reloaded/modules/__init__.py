import os
import pkgutil
from reloaded.farben import *



p1=Paint()


__all__ = list(module for _, module, _ in pkgutil.iter_modules([os.path.dirname(__file__)]))


def all_modules():
    """print available modules in nice way"""
    print(f"{p1.br}{'Modules':<20}\t{'Description':<20}{p1.res}")
    print(f"{p1.br}{'--'*10}\t{'--'*13}{p1.res}")
    for module in __all__:
        try:
            current_module = globals()[module].Main()
            print(f"{p1.bc}{module:<20}\t{current_module.__doc__}")
        except AttributeError:
            print(f"{p1.br}*** Module `{module}` not has `Main` class!{p1.res}")
    print("\n")
 
def module_list():
    return __all__ 


