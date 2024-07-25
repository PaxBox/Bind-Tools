import argparse, os, subprocess
from flask import Flask

app = Flask(__name__)

def search_for_lines(dir, fname):
    if not os.path.exists(dir):
        print(f"Cant find {dir}")
        return

    if not os.path.isdir(dir):
        print(f"{dir} is not a directory")
        return

    for root, _, files in os.walk(dir):
        for file in files:
            if file.startswith("db"):
                rfile = os.path.join(dir, file)
                try:
                    print("hallo")
                    with open(rfile, 'r') as read_file:
                        lines = read_file.readlines()
                        print(lines)
                        read_file.close()

                    mod_lines = [line for line in lines if fname not in line]

                    with open(rfile, 'w') as write_file:
                        write_file.writelines(mod_lines)
                        print(mod_lines)
                        write_file.close()

                except FileNotFoundError:
                    print(f"File '{file}' not found")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask script for removing a FQDN")
    parser.add_argument("--fqdn", required=True, help="Fully Qualified Domain Name")

    dir = os.path.join(os.path.expanduser("~"), "github", "bind-tools", "etc", "bind") #remove the first three
    
    args = parser.parse_args()
    search_for_lines(dir, args.fqdn)

    print("Processing complete!")