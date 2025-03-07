import socket

# Simple Port Scanner Script
def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    if open_ports:
        print("Open ports found:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found.")

# Example usage
if __name__ == "__main__":
    target = input("Enter target IP or hostname: ")
    scan_ports(target, 20, 1024)
