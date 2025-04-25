import socket
import sys
from datetime import datetime

def scan_ports(host, start_port, end_port):
    """
    Scans ports from start_port to end_port on the given host.
    """
    try:
        # Translate hostname to IPv4 address
        target_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print(f"Error: Could not resolve hostname {host}")
        return

    print(f"\nStarting scan on {host} ({target_ip})")
    print(f"Scanning ports {start_port} to {end_port}...\n")
    print("Please wait...\n")

    start_time = datetime.now()

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # 1-second timeout
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                print(f"Port {port}: CLOSED")

    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"\nScan completed in: {total_time}")

def get_user_input():
    """
    Gets and validates user input for host and port range.
    """
    print(">>> Python Port Scanner")
    print("NOTE: You may only scan 'localhost' (127.0.0.1) or 'scanme.nmap.org'")
    
    host = input("Enter the target host (127.0.0.1 or scanme.nmap.org): ").strip()
    if host not in ['127.0.0.1', 'scanme.nmap.org']:
        print("Error: Unauthorized target! You may only scan 127.0.0.1 or scanme.nmap.org.")
        sys.exit(1)

    try:
        start_port = int(input("Enter start port (0-65535): "))
        end_port = int(input("Enter end port (0-65535): "))
        if not (0 <= start_port <= 65535 and 0 <= end_port <= 65535):
            raise ValueError
        if start_port > end_port:
            raise ValueError
    except ValueError:
        print("Error: Invalid port range. Ports must be integers between 0 and 65535.")
        sys.exit(1)

    return host, start_port, end_port

if __name__ == "__main__":
    host, start_port, end_port = get_user_input()
    scan_ports(host, start_port, end_port)
