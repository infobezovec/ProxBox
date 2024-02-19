import sys


class NetCapper:
    def __init__(self, interface="eth0", filename="captured.pcap"):
        self.filename = filename

    def make_filter(self, rule_list):
        rule = ''
        for proto in rule_list:
            rule += ' or ' + proto 
        return rule

    def write_to_log(self, packet):
        wrpcap(self.filename, packet, append=True)


    def packet_callback(self, packet):
        print(packet)
        self.write_to_log(packet)

    def start_sniffing(self, filter):
        sniff(filter=filter, prn=self.packet_callback)

def print_help():
    print("""
EXAMPLE: PowerPointAddition.exe 10.0.10.1 434 UDP Ethernet0
        
arg 1 - Server IP
arg 2 - Server PORT
arg 3 - TCP or UDP 
arg 4 - Network interface
        """)



def main():
    if len(sys.argv) < 4: 
        print_help()
        exit()
        
    from scapy.all import sniff, wrpcap
    capper = NetCapper(sys.argv[1], sys.argv[2], sys.argv[3])
    capper.start_sniffing(sys.argv[4])

if __name__ == "__main__":
    main()