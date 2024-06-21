# Cyber Security Tools

This project contains a collection of simple cyber security tools including a port scanner, file hashing tool, and basic vulnerability scanner. 

## Tools Included

1. **Port Scanner**: Scans for open ports on a given IP address.
2. **Hashing Tool**: Generates and compares hashes of files.
3. **Basic Vulnerability Scanner**: Checks for common vulnerabilities in a web application.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/cyber-security-tools.git
    cd cyber-security-tools
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Port Scanner

```python
from port_scanner import port_scanner

ip = "192.168.1.1"
ports = [21, 22, 80, 443]
port_scanner(ip, ports)
