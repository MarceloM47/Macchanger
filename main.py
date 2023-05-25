import subprocess

interface = str(input("[+] Enter your network card: "))
address = str(input("[+] Enter the mac address you want: "))

if(len(address) >= 17):
    pass
else:
    print("¡The mac address does not appear to be valid!")

if(len(interface) >= 3):
    pass
else:
    print("¡The interface appears to be invalid!")
 
subprocess.call(["sudo","ifconfig",interface,"down"])
subprocess.call(["sudo","ifconfig",interface,"hw","ether",address])
subprocess.call(["sudo","ifconfig",interface,"up"])
