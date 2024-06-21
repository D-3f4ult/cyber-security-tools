import logging
from port_scanner import port_scanner
from hashing_tool import hash_file, compare_hash
from vulnerability_scanner import basic_vulnerability_scan

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    setup_logging()
    
    # Example usage of port scanner
    ip = "192.168.1.1"
    ports = [21, 22, 80, 443]
    logging.info("Starting port scan...")
    port_scanner(ip, ports)
    
    # Example usage of hashing tool
    file_path = "example.txt"
    expected_hash = "expectedhashvalue"
    logging.info("Comparing file hash...")
    match = compare_hash(file_path, expected_hash)
    logging.info(f"File hash matches: {match}")
    
    # Example usage of basic vulnerability scanner
    url = "http://example.com"
    logging.info("Starting vulnerability scan...")
    basic_vulnerability_scan(url)
