import argparse, os
from ipaddress import IPv4Address
from flask import Flask
from pathlib import Path

app = Flask(__name__)

def search_for_dir(path):
    if not os.path.exists(path):
        print(f"Cant find {path}")
        return

    elif not os.path.isdir(path):
        print(f"{path} is not a directory")
        return
    else:
        return True



def process_fqdn(fqdn):
    # Extract the hostname (everything before the '.')
    parts = fqdn.split('.', 1)[1]

    # Changing the name of the file
    modified_fqdn = f"db.{parts}"

    if os.path.exists(modified_fqdn):
        print(f"File already exists: {modified_fqdn}")
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
    parser.add_argument("--path", required=True, help="Path to dir")

    #path = os.path.join(os.path.expanduser("~"), "github", "bind-tools", "etc", "bind") #remove the first three

    args = parser.parse_args()

    if search_for_dir(args.path): #change args.path to path
        modified_fqdn = process_fqdn(args.fqdn)
        
        full_path = os.path.join(args.path, args.fqdn)
        if os.path.exists(full_path):
            print(f"Found file: {args.fqdn}")
            old_path = Path(full_path)
            new_path = os.path.join(args.path, modified_fqdn)
            old_path.rename(new_path)
            print(f"Renamed {old_path} to {modified_fqdn}")
        else:
            save_to_file(f"{modified_fqdn}", "")
            print(f"Created: {modified_fqdn}")

        for ip_address in args.ip:
            modified_ip = process_ip(ip_address)
            if modified_ip:            
                save_to_file(f"{modified_ip}", "")
                print(f"Created: {modified_ip}")

    print("Processing complete!")
