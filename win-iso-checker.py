import os
import hashlib
import requests
import argparse

session = requests.Session()

hash_matches = 0
not_found = 0
errors = 0

def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def check_hash(hash_value):
    """Check if the hash exists in the files.rg-adguard.net database."""
    global hash_matches, not_found, errors
    data = {"search": hash_value}
    response = session.post(url="https://files.rg-adguard.net/search", data=data)
    if response.status_code == 200:
        if "such information is not found in base!!!" in response.text:
            not_found += 1
            return f"Hash: {hash_value} - Status: Not Found"
        else:
            hash_matches += 1
            return f"Hash: {hash_value} - Status: Found"  
    else: 
        errors += 1
        return f"Error while submitting the hash: {response.status_code}"

def scan_directory(directory):
    """Scan the given directory for .ISO files."""
    iso_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.iso'):
                iso_files.append(os.path.join(root, file))
    return iso_files

def main():
    parser = argparse.ArgumentParser(description="Look the SHA-256 of an image or scan a directory for ISO files and check their SHA-256 hashes with files.rg-adguard.net.")
    parser.add_argument("directory", help="The directory to scan for ISO files.")
    
    args = parser.parse_args()
    
    iso_files = scan_directory(args.directory)
    
    total_files = len(iso_files)


    for iso_file in iso_files:
        hash_value = calculate_hash(iso_file)
        result = check_hash(hash_value)
        print(f"{iso_file} ===> {result}")

    print(f"Total ISO files found: {total_files} | Valid matches: {hash_matches} | Invalid/Not Found: {not_found} | Errors: {errors}")

if __name__ == "__main__":
    main()
