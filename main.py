import socket
import pyfiglet
import time

class portScan:
    def __init__(self):
        print("[!] INITIALIZING PORT SCANNER [!]")
        time.sleep(3)

    def banner(self):
        self.banner = pyfiglet.figlet_format("PORT SCANNER")
        print(self.banner)

    def target(self):
        self.target = input("Input target: ")
        self.target = socket.gethostbyname(self.target)
        self.ports = input("Enter no of ports: ")

        print(self.target)
        print(self.ports)

    def scanner():
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.


if __name__ == "__main__":
    scan = portScan()
    scan.banner()
    scan.target()