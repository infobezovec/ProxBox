import warnings
from termcolor import colored
from proxmoxer import ProxmoxAPI
import time

warnings.filterwarnings('ignore')





class sandbox:
    def __init__(self):
        self.proxmox = ProxmoxAPI(proxmox_server, user=proxmox_user, password=proxmox_passwd, verify_ssl=False, service='PVE')
        self.node = node
    
    def get_vm_state(self, vm_id):
        vm = self.proxmox.nodes(self.node).qemu(vm_id).status.current.get()
        print(vm['status']) 


    def start_vm(self, vm_id):
        print(self.node)
        self.proxmox.nodes('sandbox').qemu(vm_id).status.start.post()


    def stop_vm(self, vm_id):
        self.proxmox.nodes(self.node).qemu(vm_id).status.stop.post()

    def vm_from_template(self, template):
        pass


    def get_all_vm_state(self):
        for node in self.proxmox.nodes.get():
            
            for vm in self.proxmox.nodes(node['node']).qemu.get():
                print(colored(vm['vmid'], 'blue'), vm['name'], colored(vm['status'], 'green') if vm['status'] == 'running' else colored(vm['status'], 'red'))
                config = self.proxmox.nodes(node['node']).qemu(vm['vmid']).config().get()
                #network_interfaces = self.proxmox.nodes('sandbox').network.get()

                #i = 0
                #while i < len(network_interfaces):  
                #    try:
                #        print (config['net' + str(i)])
                #    except:
                #        break
                #    i += 1

    def change_net_settings(self,proxmox, node, vm_id, iface):
    vm = proxmox.nodes(node).qemu.get(vm_id)
    interface_id = vm['networks'][iface]['interface']
    network_settings = {
        'model': 'virtio',  # Модель сетевого интерфейса
        'bridge': 'vmbr0',  # Имя моста, к которому подключен интерфейс
        'tag': 10,  # VLAN-тег (если требуется)
        'firewall': '1',  # Включение/выключение фаервола (1 - включено, 0 - выключено)
    }
    proxmox.nodes(node).qemu(vm_id).network(interface_id).put(**network_settings)



def main():
    object = sandbox()
    #object.get_all_vm_state()
    object.get_vm_state(103)
    object.stop_vm(103)
    time.sleep(1)
    object.get_vm_state(103)


    

if __name__ == '__main__':
    main()