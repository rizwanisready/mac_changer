import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i','--interface',dest='interface',help='Interface to change the Mac Address')
    parser.add_option('-m','--mac',dest='new_mac',help='New Mac Address')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please enter an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please enter a new mac, use --help for more info")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing Mac address for " + interface + " to "+ new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

def get_current_mac(interface):   
    ifconfig_result = subprocess.check_output(["ifconfig",interface])
    mac_address_search_result = re(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-]Could not found the Mac")

options=get_arguments()

current_mac=get_current_mac(options.interface)
print("Current Mac = "+ str(current_mac))

change_mac(options.interface,options.new_mac)

current_mac=get_current_mac(options.interface)
if current_mac==new_mac:
    print("[+] Current Mac successfully changed to "+ current_mac)
else:
    print("[-]Mac address did not get changed")
