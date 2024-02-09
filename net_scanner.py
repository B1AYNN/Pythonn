import scapy
import scapy.all as scapy
import optparse
#1) arp yarat
#2) broadcast
#3)respons
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress",dest="ip_address",help="Enter Ip Address")

    (user_input,arguments) = parse_object.parse_args()

    if not user_input.ip_address:
        print("Please enter an IP")
    return user_input
def scan_net(ip):
    arp_request_packet = scapy.ARP(pdst="10.0.2.1/24") #burda basqa ip addressde ola biler
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet/arp_request_packet
    (answered_list, unanswered_list) = scapy.srp(combined_packet,timeout=1)
    answered_list.summary()


user_ip_address = get_user_input()
scan_net(user_ip_address)
