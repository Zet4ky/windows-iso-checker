# windows-iso-checker
A python script to check the integrity of all the windows images under a directory using https://files.rg-adguard.net to determine if they are valid or not.

The script will output the status of each hash checked, indicating whether it was found in the files.rg-adguard.net database or not. At the end of the scan, it will provide a summary of the total number of ìmages found, valid hashes, not found or invalid hashes, and number of errors encountered while requesting the hash.

## Requirements

- Python 3.10 or higher
- `requests` library (can be installed via pip)

## Installation

1. Install python for your system from https://www.python.org/downloads/
2. Clone the repository or download the script.
3. Install requests lib with `pip install requests`)
4. run the script with `python checker.py [directory]`

## Usage

```powershell
python checker.py "D:\WindowsImages"
```
