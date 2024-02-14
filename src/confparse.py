import yaml
from PBLogger import Logger

#TESTED
class Confparse:
    def __init__(self):
        self.SBconf = {}
        self.PMconf = {}
        self.GSconf = {}

        logpath = '../configs/PBconfig.yaml'
        self.log = Logger()
        try:
            file = open(logpath, 'r')
        except:
            self.log.werror(f"Cannot open: {logpath}")
            exit()
        self.buffer = yaml.safe_load(file)
        
    def parse(self):
        for module in self.buffer:
            for key in self.buffer.get(module):
                if module == 'sandbox':
                    self.SBconf[key] = self.buffer.get(module).get(key)
                elif module == 'proxmox':
                    self.PMconf[key] = self.buffer.get(module).get(key)
                elif module == 'guest':
                    self.GSconf[key] = self.buffer.get(module).get(key)

    def get_conf(self, conf_type, key):
        if conf_type == 'sb':
            return self.SBconf.get(key)
        elif conf_type == 'pm':
            return self.PMconf.get(key)
        elif conf_type == 'gt':
            return self.GSconf.get(key)

parcer = Confparse()
parcer.parse()
print(parcer.get_conf('pm', 'host'))
#parcer.print_()