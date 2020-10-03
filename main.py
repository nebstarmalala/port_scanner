import socket
import pyfiglet
import time

open_ports = []

def banner():
    print("[!] INITIALIZING PORT SCANNER [!]")
    time.sleep(3)
    banner = pyfiglet.figlet_format("PORT SCANNER")
    print(banner)

banner()

try:
    target = input("Input target: ")
    target = socket.gethostbyname(target)
except:
    print("[*] Unable to get target")

def scanner(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        time.sleep(1)
        return True
    except:
        return False

print(f"[!] Scanning {target}")
for port in range(1, 100):
    print(f"Scanning port: {port}")
    if scanner(port):
        print(f"Port {port} : OPEN")
        open_ports.append(port)

def conclu():
    print("\n================ OPEN PORTS ================")
    for port in open_ports:
        print(port+"\n")

conclu()