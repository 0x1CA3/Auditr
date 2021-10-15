re = __import__("re")
time = __import__("time")
from colorama import Fore


# basic_scan.py
# Date: 10/14/21
# Author: 0x1CA3


class BasicScan(object):
    def __init__(self, target):
        self.target = target
    
    database = {
        "fgets(": "gets(",
        "strncat(": "strcat(",
        "strncmp(": "strcmp(",
        "strncpy(": "strcpy(",
        "memset_s(": "memset(",
        "vsnprintf(": "vsprintf(",
        "sscanf_s(": "scanf(",
        "sscanf_s(": "sscanf(",
        "_snscanf_s(": "snscanf(",
        "strlen_s(": "strlen(",
        "fread(": "read("
    }

    descriptions = {
        "fgets(": "Buffer Overflow Vulnerability",
        "strncat(": "Vulnerable Function",
        "strncmp(": "Possible Timing Attack Vulnerability",
        "strncpy(": "Vulnerable Function",
        "memset_s(": "Vulnerable Function",
        "vsnprintf(": "Vulnerable Function",
        "sscanf_s(": "CWE-119: Improper Restriction of Operations within the Bounds of a Memory Buffer",
        "sscanf_s(": "CWE-119: Improper Restriction of Operations within the Bounds of a Memory Buffer",
        "_snscanf_s(": "Vulnerable Function",
        "strlen_s(": "Vulnerable Function",
        "fread(": "Vulnerable Function"
    }

    @classmethod
    def search(cls, i: int, line: str, database=database, descriptions=descriptions) -> None:
        for key in database:
            if key not in line:
                if database[key] in line:
                    print(f"\t{Fore.RED}{descriptions[key]} | Line {i} -> {Fore.GREEN}{line}", end='')

    def scan(self: str) -> None:
        i = 0
        print("\t[Scanning for vulnerabilties...]")
        print("\t--------------------------------")
        time.sleep(3)
        filename = open(self.target, "r")
        file_data = filename.readlines()
        for line in file_data:
            i += 1
            BasicScan.search(i, line)