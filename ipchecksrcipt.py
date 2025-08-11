import socket
import concurrent.futures
import time
from datetime import datetime
import os
import subprocess

# Function to ping an IP address
def ping_ip(ip_address):
    print(f"Pinging IP: {ip_address}...")
    try:
        response = subprocess.run(
            ["ping", "-n", "1", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if response.returncode == 0:
            print(f"{ip_address} is reachable.")
            return ip_address
        else:
            print(f"{ip_address} is not reachable.")
            return None
    except Exception as e:
        print(f"Error pinging {ip_address}: {e}")
        return None

# Function to check if a port is open
def check_port(ip_address, port):
    print(f"Checking port {port} on {ip_address}...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout reduced to 1 second for quicker response
        result = sock.connect_ex((ip_address, port))
        sock.close()
        if result == 0:
            print(f"Port {port} is open on {ip_address}.")
            return port  # Return the port if it's open
        else:
            print(f"Port {port} is closed on {ip_address}.")
            return None  # Return None if the port is not open
    except (socket.timeout, socket.error) as e:
        print(f"Error checking port {port}: {e}")
        return None

# Read and validate the ports from the text file
def read_ports(file_path):
    print(f"Reading ports from {file_path}...")
    try:
        with open(file_path, "r") as file:
            ports = file.read().split(',')
        
        # Strip whitespace, filter out empty ports, and convert to integers
        valid_ports = []
        for port in ports:
            port = port.strip()  # Strip any leading/trailing spaces
            if port.isdigit():  # Check if the port is a valid number
                valid_ports.append(int(port))
            else:
                print(f"Skipping invalid port: {port}")

        print(f"Ports read: {valid_ports}")
        return valid_ports
    except Exception as e:
        print(f"Error reading ports file: {e}")
        return []

# Function to check ports using multithreading
def check_ports_multithreaded(ip_address, ports):
    open_ports = []
    print(f"Starting multithreaded port checks for IP: {ip_address}...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2048) as executor:
        futures = {executor.submit(check_port, ip_address, port): port for port in ports}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result is not None:
                open_ports.append(result)
    
    print(f"Completed port checks for {ip_address}. Found open ports: {open_ports}")
    return open_ports

# Function to read the list of IP addresses from the file
def read_ip_addresses(file_path):
    print(f"Reading IP addresses from {file_path}...")
    try:
        with open(file_path, "r") as file:
            ip_addresses = file.read().splitlines()  # Read file line by line
        return [ip.strip() for ip in ip_addresses if ip.strip()]
    except Exception as e:
        print(f"Error reading IP addresses file: {e}")
        return []

# Main function
def main():
    ip_addresses = read_ip_addresses("ip_addrs.txt")
    if not ip_addresses:
        print("No IP addresses to check.")
        return

    ports = read_ports("ports.txt")
    if not ports:
        print("No ports to check.")
        return

    # Loop through each IP address
    for ip_address in ip_addresses:
        # Ping the IP address first
        reachable_ip = ping_ip(ip_address)
        if reachable_ip:
            # If the IP is reachable, check its ports
            open_ports = check_ports_multithreaded(reachable_ip, ports)
            if open_ports:
                print(f"Open ports for {reachable_ip}: {open_ports}")
                # Wait for user input "asd" before continuing
                input("Type 'asd' to continue to the next IP address: ")
            else:
                print(f"No open ports found for {reachable_ip}.")
        
        else:
            print(f"Skipping {ip_address} as it is not reachable.")

if __name__ == "__main__":
    main()
