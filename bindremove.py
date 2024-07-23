import argparse, os, subprocess
from flask import Flask

app = Flask(__name__)

def search_for_lines(dir, fname):
    if not os.path.exists(dir):
        print(f"Cant find {dir}")
    if not os.path.isdir(dir):
        print(f"{dir} is not a directory")
    for root, _, files in os.walk(dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            print({filename})
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask script for removing a FQDN")
    parser.add_argument("--fqdn", required=True, help="Fully Qualified Domain Name")
    dir = os.path.join(os.path.expanduser("~"), "github", "bind-tools", "etc", "bind")
    
    args = parser.parse_args()
    search_for_lines(dir, args.fqdn)

    print("Processing complete!")