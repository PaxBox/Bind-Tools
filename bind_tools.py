import argparse, os
from ipaddress import IPv4Address
from flask import Flask

app = Flask(__name__)

def process_fqdn(fqdn):
    # Extract the hostname (everything before the first dot)
    parts = fqdn.split('.')
    hostname = parts[0]
    modified_fqdn = f"db.{hostname}"
    if os.path.exists(modified_fqdn):
        print(f"File already exists: {modified_fqdn}")
        return
    else:
        return modified_fqdn

def process_ip(ip):
    try:
        # Parse the IP address
        parsed_ip = IPv4Address(ip)
        # Remove the last octet (8 bits)
        modified_ip = f"db.{str(parsed_ip.exploded.rsplit('.', 1)[0])}"
        if os.path.exists(modified_ip):
            print(f"File already exists: {modified_ip}")
            return
        else:
            return modified_ip
    except ValueError:
        print(f"Invalid IP address: {ip}")
        return

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask script for processing FQDN and IP addresses")
    parser.add_argument("--fqdn", required=True, help="Fully Qualified Domain Name")
    parser.add_argument("--ip", nargs='+', required=True, help="One or more IP addresses")

    args = parser.parse_args()

    modified_fqdn = process_fqdn(args.fqdn)
    if modified_fqdn:
        print(f"Created FQDN: {modified_fqdn}")
        save_to_file(f"{modified_fqdn}", modified_fqdn)

    for ip_address in args.ip:
        modified_ip = process_ip(ip_address)
        if modified_ip:
            print(f"Created: {modified_ip}")
            save_to_file(f"{modified_ip}", modified_ip)

    print("Processing complete! Files saved.")
