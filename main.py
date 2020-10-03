import socket
import pyfiglet
import time


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
        time.sleep(3)
        return True
    except:
        return False

print(f"[!] Scanning {target}")
for port in range(1, 100):
    print(f"Scanning port: {port}")
    if scanner(port):
        print(f"Port {port} : OPEN")