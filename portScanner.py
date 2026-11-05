import socket
import sys
from concurrent.futures import ThreadPoolExecutor


usage = "Usage: python portScanner.py <target_host> <start_port> <end_port>"

if len(sys.argv) != 4:
    print(usage)
    sys.exit(1)

target_host = sys.argv[1].strip()
if not target_host:
    print("Target IP address or hostname cannot be empty.")
    sys.exit(1)

try:
    target_ip = socket.gethostbyname(target_host)
except socket.gaierror:
    print(f"Name resolution error: could not resolve {target_host}")
    sys.exit(1)

try:
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
except ValueError:
    print("Ports must be integers.")
    sys.exit(1)

if not (1 <= start_port <= end_port <= 65535):
    print("Ports must satisfy 1 <= start_port <= end_port <= 65535.")
    sys.exit(1)


def scan_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(2)
        try:
            sock.connect((target_ip, port))
            return port, "open"
        except ConnectionRefusedError:
            return port, "closed"
        except socket.timeout:
            return port, "no response (possibly filtered or unreachable)"
        except OSError:
            return port, "no response (possibly filtered or unreachable)"


with ThreadPoolExecutor(max_workers=100) as executor:
    for port, status in executor.map(scan_port, range(start_port, end_port + 1)):
        print(f"Port {port}: {status}")
