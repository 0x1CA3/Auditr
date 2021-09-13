try:
    import sys
    import platform
    import subprocess
    from time import sleep
    from colorama import Fore
    from datetime import datetime
except:
    print("Please make sure to install the required modules before running!")

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
clear_screen = lambda: subprocess.call("clear" if "Linux" in platform.platform() else "cls", shell=True)


# Auditr
# Date: 09/13/21
# Author: 0x1CA3


banner = f"""
        {Fore.YELLOW} _______           __ __ __         {Fore.RESET}
        {Fore.YELLOW}|   _   |.--.--.--|  |__|  |_.----. {Fore.RESET}
        {Fore.YELLOW}|       ||  |  |  _  |  |   _|   _| {Fore.RESET}
        {Fore.YELLOW}|___|___||_____|_____|__|____|__|   {Fore.RESET}                       
        {Fore.YELLOW}[Made by: https://github.com/0x1CA3]{Fore.RESET}
"""

class Auditr:
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

    extra = {
        "system(": "Possible Arbitrary Command Execution Vulnerability",
        "getpw(": "Buffer Overflow Vulnerability",
        "execlp(": "CWE-114: Process Control",
        "execvp(": "CWE-114: Process Control"
    }

    def analysis(line, scan_num, database=database, extra=extra):
        for key in database:
            if key not in line:
                if database[key] in line:
                    print(f"        {Fore.RED}Vulnerable Function | Line {scan_num} -> {Fore.GREEN}{line}", end="")

        for key in extra:
            if key in line:
                print(f"        {Fore.RED}{extra[key]} | Line {scan_num} -> {Fore.GREEN}{line}", end="")

    def scan_file(self):
        scan_num = 0
        targ_file = open(self.target, "r")
        targ_data = targ_file.readlines()
        for line in targ_data:
            scan_num += 1
            Auditr.analysis(line, scan_num)

    def file_validation(self):
        if ".c" not in self.target:
            print("Error! Make sure your file is a '.c' file!")
            sys.exit()
        clear_screen()
        print(f"""
        {banner}
        [Auditr]
        Loaded File -> {self.target}
        Current Time: {current_time}""")
        sleep(3)
        print("\n        [Scanning for vulnerablities...]")
        Auditr.scan_file(self)

def main() -> None:
    print(banner)
    if len(sys.argv) < 2:
        print(f"{Fore.GREEN}Usage: python3 auditr.py <file>{Fore.RESET}")
        sys.exit()
    target = sys.argv[1]
    Auditr(target).file_validation()

if __name__ == "__main__":
    main()