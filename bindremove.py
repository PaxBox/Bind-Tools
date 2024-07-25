import argparse, os, re
from flask import Flask

app = Flask(__name__)    
                
def get_lines(path, text):
    try:
        with open(path, 'r') as read_file:
            print(f"Reading file {path}")
            lines = read_file.readlines()
            read_file.close()
        return lines

    except FileNotFoundError:
        print(f"File '{path}' not found")



def set_lines(path, lines):
    try:
        with open(path, 'w') as write_file:
            write_file.writelines(lines)
            write_file.close()

    except FileNotFoundError:
        print(f"File '{path}' not found")



def search_for_files(path, files, text):
    for file in files:
        if file.startswith("db"):
            print(f"Found: {file}")
            file_path = os.path.join(path, file)
            lines = get_lines(file_path, text)
            
            for line in lines:
                if re.match(fr"{text}\s+", line):
                    print(f"Found:", line.strip())
                    mod_lines = [line for line in lines if text not in line]
                    set_lines(file_path, mod_lines)
                    print(f"Changed {file}")
                


def search_for_dir(path, text):
    if not os.path.exists(path):
        print(f"Cant find {path}")
        return

    if not os.path.isdir(path):
        print(f"{path} is not a directory")
        return

    print(f"Searching for 'db' files in {path}")
    for root, _, files in os.walk(path):
        search_for_files(path, files, text)
        
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask script for removing a FQDN")
    parser.add_argument("--fqdn", required=True, help="Fully Qualified Domain Name")
    parser.add_argument("--path", required=True, help="Path to dir")

    #path = os.path.join(os.path.expanduser("~"), "github", "bind-tools", "etc", "bind") #remove the first three
    
    args = parser.parse_args()
    search_for_dir(args.path, args.fqdn) #change args.path to path

    print("Processing complete!")