
#                                                                Lecture = 1                           
# -------------------------------------------------------------------------
# import subprocess
# subprocess.call("ifconfig",shell=True)

#                                                                  Lecture = 2
# ________________________________________________________________________________________

# import subprocess

# subprocess.call("ifconfig eth0 down",shell=True)
# subprocess.call("ifconfig eth0 hw ether 00:44:33:22:11:55",shell=True)
# subprocess.call("ifconfig eth0 up",shell=True)


#                                                                  004 Variables & Strings
# _____________________________________________________________________________________________


# interface = "eth0"
# new_mac  = "00:55:11:22:44:66"

# print("[+] changing mac address for " + interface, "to " + new_mac)



#                                                                  005 Using Variables in MAC Changer


# interface = "eth0"
# new_mac = "11:22:33:44:55:66"
# print("[+] changing " + interface + " to " + new_mac)


# import subprocess
# subprocess.call(" ifconfig " + interface + " down ", shell=True)
# subprocess.call(" ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call(" ifconfig " + interface + " up ", shell=True)



#                                                                 006 Getting Input From The User

# interface = input("enter the interface name > ")
# new_mac = input("enter the new mac address > ")
# print("[+] changing " + interface + " to " + new_mac)


# import subprocess
# subprocess.call(" ifconfig " + interface + " down ", shell=True)
# subprocess.call(" ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call(" ifconfig " + interface + " up ", shell=True)



#                                                                 007 Handling User Input (this is more secure)

# interface = input("enter the interface name > ")
# new_mac = input("enter the new mac address > ")
# print("[+] changing " + interface + " to " + new_mac)

# import subprocess
# subprocess.call(["ifconfig", interface, "down"])
# subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
# subprocess.call(["ifconfig", interface, "up"])


#                                                                 008 Handling Command-line Arguments


# import subprocess
# import optparse                #parser function we can use for display help like nmap -h 

# parser = optparse.OptionParser()                                
# parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's mac address")
# parser.parse_args()

# interface = input("enter the interface name > ")
# new_mac = input("enter the new mac address > ")
# print("[+] changing " + interface + " to " + new_mac)

# subprocess.call(["ifconfig", interface, "down"])
# subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
# subprocess.call(["ifconfig", interface, "up"])



#                                                           009 Initialising Variables Based on Command-line Arguments



# import subprocess
# import argparse                                   #  it's same like optparse but now optparse don't support python 3 

# parser = argparse.ArgumentParser(description="Change MAC address of a network interface")
# parser.add_argument("-i", "--interface", dest="interface", required=True, help="Interface to change its MAC address")
# parser.add_argument("-m", "--mac", dest="new_mac", required=True, help="New MAC address")

# args = parser.parse_args()

# interface = args.interface
# new_mac = args.new_mac

# print(f"[+] Changing MAC address of {interface} to {new_mac}")

# subprocess.call(["ifconfig", interface, "down"])
# subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
# subprocess.call(["ifconfig", interface, "up"])


#                                                        010 Python Functions


# import subprocess
# import argparse

# def change_mac(interface, new_mac):
#     print(f"+ changing mac address for {interface} to {new_mac}")
#     subprocess.call(["ifconfig", interface, "down"])
#     subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#     subprocess.call(["ifconfig", interface, "up"])

# parser = argparse.ArgumentParser()
# parser.add_argument("-i", "--interface", help="Interface to change mac address", required=True)
# parser.add_argument("-m", "--mac", help="New MAC address", required=True)

# args = parser.parse_args()

# change_mac(args.interface, args.mac)



#                                                      011 Returning Values From Functions

# import subprocess
# import argparse

# def get_arguments():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-i", "--interface", help="Interface to change mac address", required=True)
#     parser.add_argument("-m", "--mac", help="New MAC address", required=True)
#     return parser.parse_args()


# def change_mac(interface, new_mac):
#     print(f"+ changing mac address for {interface} to {new_mac}")
#     subprocess.call(["ifconfig", interface, "down"])
#     subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#     subprocess.call(["ifconfig", interface, "up"])


# args = get_arguments()
# change_mac(args.interface, args.mac)


#                                                    012 Decision Making in Python


# import subprocess
# import argparse

# def get_arguments():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-i", "--interface", help="Interface to change mac address", required=True)
#     parser.add_argument("-m", "--mac", help="New MAC address", required=True)
#     args = parser.parse_args()
#     if not args.interface:
#         parser.error("[-] Please specify an interface or use --help for more info.")
#     elif not args.mac:
#         parser.error("[-] Please specify a new mac or use --help for more info.")
#     return args


# def change_mac(interface, new_mac):
#     print(f"+ changing mac address for {interface} to {new_mac}")
#     subprocess.call(["ifconfig", interface, "down"])
#     subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#     subprocess.call(["ifconfig", interface, "up"])


# args = get_arguments()
# change_mac(args.interface, args.mac)


