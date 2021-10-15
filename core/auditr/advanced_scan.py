time = __import__("time")
from colorama import Fore


# advanced_scan.py
# Date: 10/14/21
# Author: 0x1CA3


class AdvancedScan(object):
    def __init__(self, target):
        self.target = target
    
    database = {
        "system(": "Possible Arbitrary Command Execution Vulnerability",
        "getpw(": "Buffer Overflow Vulnerability",
        "execlp(": "CWE-114: Process Control",
        "execvp(": "CWE-114: Process Control"
    }

    @classmethod
    def search(cls, i: int, line: str, database=database) -> None:
        for key in database:
                if key in line:
                    print(f"\t{Fore.RED}{database[key]} | Line {i} -> {Fore.GREEN}{line}", end='')

    def scan(self: str) -> None:
        i = 0
        print("\t[Scanning for vulnerabilties...]")
        print("\t--------------------------------")
        time.sleep(3)
        filename = open(self.target, "r")
        file_data = filename.readlines()
        for line in file_data:
            i += 1
            AdvancedScan.search(i, line)