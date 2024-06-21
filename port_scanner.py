import socket
import logging

def port_scanner(ip, ports):
    logging.info(f"Scanning {ip} for open ports...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                logging.info(f"Port {port} is open")
            else:
                logging.info(f"Port {port} is closed")
            sock.close()
        except Exception as e:
            logging.error(f"Error scanning port {port}: {e}")
