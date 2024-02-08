import subprocess
import optparse
import re
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
    parse_object.add_option("-m","--mac",dest="mac_address",help="new mac address")

    return parse_object.parse_args()

def change_mac_address(user_interface,user_mac):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether","ether",user_mac])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_mac(interface):

    ifconfig = subprocess.check_output("ifconfig",interface)
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("Mac changer started")
(user_input,arguments)  = get_user_input()
change_mac_address(user_input.interface,user_input.mac_address)
end_mac = control_mac(str(user_input.interface))

if end_mac == user_input.mac_address:
    print("Success!")

else:
    print("Fail!")
