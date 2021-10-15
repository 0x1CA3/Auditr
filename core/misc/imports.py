subprocess = __import__("subprocess")


# imports.py
# Date: 10/13/21
# Author: 0x1CA3


class ImportCheck(object):
    @classmethod
    def check(cls) -> int:
        try: 
            from colorama import Fore
        except: 
            command = subprocess.Popen(["pip3", "install", "colorama"], stdout=subprocess.PIPE).communicate()[0]
            if "Requirement already satisfied" in str(command): 
                return 0
            else: 
                print("Installed missing modules, please run Auditr again.")
                return 1