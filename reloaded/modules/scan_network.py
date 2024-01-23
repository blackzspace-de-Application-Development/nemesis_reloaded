from reloaded.kern import *
from scapy.all import *
from reloaded.kern import basis
from reloaded.farben import *
from reloaded.kern.dienste import Check



conf.verb = 0

p1=Paint()
chk=Check()

loggy = logging.getLogger(__name__)


class Main(basis.Module):
    """Scan IP range for new devices || [ip] [prefix] [opt][0]=enable logging [1]to disable """

    parameters = {
        "ip": "192.168.1.1",
        "prefix": "/24"
    
    }
    
    
    completions = list(parameters.keys())

    def do_run(self, line):
        """Execute current module"""
        

        opt = self.parameters['opt']

        arp = scapy.ARP(pdst=self.parameters['ip'] + "/24")
        ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp
        result = srp(packet, timeout=5)[0]
        print(f"{p1.br}{'IP':<16}\t {'MAC':^15}{p1.res}")
        for _, received in result:
            print(f"{p1.bg}{received.psrc:<20} {received.hwsrc:^18}{p1.res}")

    def complete_set(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]

    def default(self, line):
        cmd, arg, line = self.parseline(line)
        func = [getattr(self, n) for n in self.get_names() if n.startswith('do_' + cmd)]
        if func: 
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