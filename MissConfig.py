import sys #Handling Exceptions and Errors
import socket
import argparse
from datetime import datetime

print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~ ██████   ██████  ███                               █████████                         ██████   ███          ~
~░░██████ ██████  ░░░                               ███░░░░░███                       ███░░███ ░░░           ~
~ ░███░█████░███  ████   █████   █████             ███     ░░░   ██████  ████████    ░███ ░░░  ████   ███████~
~ ░███░░███ ░███ ░░███  ███░░   ███░░   ██████████░███          ███░░███░░███░░███  ███████   ░░███  ███░░███~
~ ░███ ░░░  ░███  ░███ ░░█████ ░░█████ ░░░░░░░░░░ ░███         ░███ ░███ ░███ ░███ ░░░███░     ░███ ░███ ░███~
~ ░███      ░███  ░███  ░░░░███ ░░░░███           ░░███     ███░███ ░███ ░███ ░███   ░███      ░███ ░███ ░███~
~ █████     █████ █████ ██████  ██████             ░░█████████ ░░██████  ████ █████  █████     █████░░███████~
~░░░░░     ░░░░░ ░░░░░ ░░░░░░  ░░░░░░               ░░░░░░░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░     ░░░░░  ░░░░░███~
~                                                                                                    ███ ░███~
~                                                                                                   ░░██████ ~
~  By Hamish Drummond                                                                                ░░░░░░  ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
StartTime = datetime.now()
print(f"Scan Start Time is {StartTime}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print('''

''')
#-------------------------------#
#ARGPARSE
parser = argparse.ArgumentParser()
#I'm keeping things simple for now, splitting ports and targets into 2 excl
target_group = parser.add_mutually_exclusive_group(required=True)
target_group.add_argument("-t", "--target", help="Target IP Address")
target_group.add_argument("-tr", "--targetrange", help="Target IP Address range")
target_group.add_argument("-tf", "--targetfile", help="File containing target IP addresses (.txt)")

# Mutually exclusive group for port options (optional in this example)
port_group = parser.add_mutually_exclusive_group()
port_group.add_argument("-p", "--port", help="Port Number to scan")
port_group.add_argument("-pr", "--Portrange", help="Range of Ports to scan")

args = parser.parse_args()
#--------------------------------#
# Access target arguments
if args.target:
    target = args.target
    print(f"Scanning single target: {target}")
elif args.targetrange:
    target_range = args.targetrange
    print(f"Scanning target range: {target_range}")
elif args.targetfile:
    target_file = args.targetfile
    print(f"Scanning targets from file: {target_file}")

# Access port arguments
if args.port:
    port = int(args.port)
    print(f"Scanning specific port: {port}")
elif args.portrange:
    port_range = args.portrange
    print(f"Scanning port range: {port_range}")
else:
    print("No port specified, will scan default range (1-1024)")

