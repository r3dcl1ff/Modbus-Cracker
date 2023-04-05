import os

# Define color codes
RED = "\033[1;31m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
END = "\033[0m"

print(f"{RED} ***** ModbusCracker.py ***** {END}") 

# Prompt user to enter target IP in green color
print(f"{GREEN} Enter the IP address of the target: ")
target_ip = input()

# Run modbus specific nmap scripts
nmap_output = os.popen(f"nmap --script=modbus-discover {target_ip} -p 502").read()
print(f"{RED}{nmap_output}{END}")

# Invoke metasploit and run modbus specific enumeration modules against the target
os.system(f"msfconsole -q -x 'use auxiliary/scanner/scada/modbus_banner_grabbing; set RHOSTS {target_ip}; set RPORT 502 ; run; use auxiliary/scanner/scada/modbusdetect ; set RHOSTS {target_ip}; set RPORT 502 ; set UNIT_ID 1; run; use auxiliary/scanner/scada/modbus_findunitid ;set RHOSTS {target_ip}; set RPORT 502 ; set BENICE 2 ; set UNIT_ID_FROM 1 ; set UNIT_ID_TO 25 ; run; exit;' > output.txt")

print(f"{CYAN} ***** Metasploit Enumeration Output ***** {END}")

# Print the contents of output.txt to stdout in cyan color
with open("output.txt", "r") as f:
    print(f"{CYAN}{f.read()}{END}")

print(f"{GREEN} Enumeration complete! Check output.txt for results.{END}")
