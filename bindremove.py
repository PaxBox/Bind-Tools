import argparse, os, subprocess
from flask import Flask

app = Flask(__name__)

def search_for_lines(dir, fname):
    try:
        # Use subprocess to execute the 'cd' command
        subprocess.run(f'cd {dir}', shell=True, check=True)
        print(f"Successfully navigated to {dir}!")
    except subprocess.CalledProcessError:
        print(f"Error: Could not navigate to {dir}. Check if the directory exists.")
        return
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask script for removing a FQDN")
    parser.add_argument("--fqdn", required=True, help="Fully Qualified Domain Name")
    dir = "~/github/bind-tools"
    
    args = parser.parse_args()
    search_for_lines(dir, args.fqdn)

    print("Processing complete!")