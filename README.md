# 🔑 BasicPortScanner
A simple and efficient **port scanner** built using Python and Nmap.  
This tool allows users to **scan active hosts** in a given IP range and detect **open ports**.

## 🚀 Features
- ✅ Scan active hosts in a given IP range.
- ✅ Perform a **quick scan** (top 1000 ports) or a **custom port range scan**.
- ✅ Displays detected open ports with associated services.
- ✅ User-friendly menu-driven interface.

## 📥 Installation

### **1️⃣ Prerequisites**
Ensure you have the following installed:
- **Python 3.6+** 👉 [Download Here](https://www.python.org/downloads/)
- **Nmap** 👉 [Download Here](https://nmap.org/download.html)
- **Python Nmap Module** (install using pip install python-nmap)

### **2️⃣ Simply Run in VS Code**
simply press the run button in vs code

OR

### **3️⃣ Clone the github repository**
git clone https://github.com/brgv0815/BasicPortScanner.git

### ** Sample output**

[Note: this is just a sample output to understand what type of output the code should be producing. please dont use the same input datas as used below!]

🔑 Basic Port Scanner
Developer: Bhargav Mistry

🔽 Main Menu:
1️⃣ Start a New Scan
2️⃣ Exit Program

🌐 Enter the IP range to scan (e.g., 192.168.1.0/24 or 192.168.1.1-100): 192.168.1.0/24

🔍 Scanning 192.168.1.0/24 for active hosts...

✅ Host 192.168.1.1 is active.
✅ Host 192.168.1.5 is active.

🔽 Choose a port scanning option:
1️⃣ Quick Scan (Top 1000 Ports)
2️⃣ Custom Port Range
3️⃣ Back to Main Menu

🔍 Scanning 192.168.1.5 for open ports in range 1-1000...

✅ Open Ports on 192.168.1.5:
  🔹 Port: 22, Service: ssh
  🔹 Port: 80, Service: http


