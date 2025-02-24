import nmap  # Import the Nmap module for network scanning
import re    # Import regex module for input validation

# ASCII Art Banner displaying Key with "PORT SCANNER" inside
def print_banner():
    print("""
           _________
         /  ______  \   
         | /      \  |
         | |       | |
 ________| |_______| |________      
|                             |
|          Basic Port         |
|           Scanner           |
|            _____            |
|           //   \\\           |
|           \\\   //           |
|            || ||            |
|            ||_||            |
|                             |
|         DEVELOPER:          |
|       Bhargav Mistry        |  
|_____________________________|
          """)

def is_valid_ip_range(ip_range):
    """
    Validate the entered IP range format.
    
    Accepts formats like:
    - Subnet notation: 192.168.1.0/24
    - Range notation: 192.168.1.1-100

    Returns:
        True if the format is valid, otherwise False.
    """
    ip_pattern = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(/\d{1,2})?|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}-\d{1,3})$"
    return bool(re.match(ip_pattern, ip_range))

def scan_active_hosts(ip_range):
    """
    Scan the given IP range to detect active hosts.

    Uses an Nmap ping scan (-sn) to check which hosts are online.

    Args:
        ip_range (str): The IP range/subnet to scan.

    Returns:
        list: A list of active hosts (IP addresses).
    """
    nm = nmap.PortScanner()
    print(f"\n🔍 Scanning {ip_range} for active hosts...\n")

    # Perform an Nmap ping scan (-sn) to detect active hosts
    nm.scan(hosts=ip_range, arguments="-sn")

    active_hosts = []
    for host in nm.all_hosts():
        if nm[host].state() == "up":
            active_hosts.append(host)
            print(f"✅ Host {host} is active.")

    # Notify if no active hosts were found
    if not active_hosts:
        print("\n⚠️ No active hosts found.")
    
    return active_hosts

def scan_ports(host, port_range):
    """
    Scan a specific host for open ports within the specified range.

    Args:
        host (str): The IP address of the target host.
        port_range (str): The range of ports to scan (e.g., "1-1000" or "22,80,443").
    """
    nm = nmap.PortScanner()
    print(f"\n🔍 Scanning {host} for open ports in range {port_range}...\n")

    # Perform an Nmap port scan with the given range
    nm.scan(hosts=host, arguments=f"-p {port_range} --open")

    # Check if the host has any open ports
    if host not in nm.all_hosts():
        print(f"⚠️ {host} has no open ports.")
        return

    open_ports = []
    for proto in nm[host].all_protocols():
        ports = nm[host][proto].keys()
        for port in ports:
            service = nm[host][proto][port]['name']
            open_ports.append((port, service))

    # Display results based on open ports
    if open_ports:
        print(f"\n✅ Open Ports on {host}:")
        for port, service in open_ports:
            print(f"  🔹 Port: {port}, Service: {service}")
    else:
        print(f"⚠️ No open ports found on {host}.")

if __name__ == "__main__":
    print_banner()  # Display banner at the start of the program
    
    while True:  # Main program loop to allow repeated scans
        while True:  # Loop to handle user input for menu selection
            print("\n🔽 Main Menu:")
            print("1️⃣  Start a New Scan")
            print("2️⃣  Exit Program")

            main_choice = input("Enter your choice (1 or 2): ").strip()

            # Ensure valid input (1 or 2)
            if main_choice in ["1", "2"]:
                break
            else:
                print("❌ Invalid choice! Please enter **1** to start a scan or **2** to exit.")

        if main_choice == "2":
            print("\n🚪 Exiting program. Goodbye!")
            break  # Exit the main loop and terminate the script

        while True:  # Loop to ensure a valid IP range is entered
            ip_range = input("\n🌐 Enter the IP range to scan (e.g., 192.168.1.0/24 or 192.168.1.1-100): ").strip()

            # Validate the IP range input
            if is_valid_ip_range(ip_range):
                break
            else:
                print("❌ Invalid IP range format! Please enter a valid subnet (e.g., 192.168.1.0/24) or range (e.g., 192.168.1.1-100).")

        # Scan for active hosts
        active_hosts = scan_active_hosts(ip_range)

        # If no active hosts found, return to the main menu
        if not active_hosts:
            continue  

        while True:  # Loop for selecting port scan options
            print("\n🔽 Choose a port scanning option:")
            print("1️⃣  Quick Scan (Scans top 1000 ports)")
            print("2️⃣  Custom Port Range")
            print("3️⃣  Back to Main Menu")

            choice = input("Enter your choice (1-3): ").strip()

            # Assign port range based on user choice
            if choice == "1":
                port_range = "1-1000"  # Default quick scan (Top 1000 ports)
            elif choice == "2":
                port_range = input("Enter the port range (e.g., 20-1000 or 80,443,8080): ").strip()
            elif choice == "3":
                break  # Return to the main menu
            else:
                print("❌ Invalid choice. Please select again.")
                continue  

            # Perform port scanning on all active hosts
            for host in active_hosts:
                scan_ports(host, port_range)
