re = __import__("re")
from colorama import Fore


# variable_usage.py
# Date: 10/14/21
# Author: 0x1CA3


var_list = []

class VariableUsage(object):
    def __init__(self, target):
        self.target = target

    @classmethod
    def var_usage_check(cls, i: int, line:str) -> None:
        func_list = [
            "gets(",
            "read(",
            "strcat(",
            "strcpy(",
            "strcmp(",
            "system("
        ]
        if "fgets" in line and "sizeof" not in line:
            print(f"\t{Fore.RED}Warning: Possible Variable Misusage | Line {i} -> {Fore.GREEN}{line}", end='')
        for func in func_list:
            if func in line:
                for var in var_list:
                    if var in line:
                        pass
                    else:
                        print(f"\t{Fore.RED}Warning: Possible Variable Misusage | Line {i} -> {Fore.GREEN}{line}", end='')
                        break

    @classmethod
    def var_usage(cls, targ: str) -> None:
        i = 0
        filename = open(targ, "r")
        file_data = filename.readlines()
        for line in file_data:
            i += 1
            VariableUsage.var_usage_check(i, line)

    @classmethod
    def var_scan(cls, line: str) -> None:
        illegals = ["int", "char", "float", "double"]
        trimming = ["[", "]", ";", "=", "{", "}", "(", ")", " "]
        for illegal in illegals:
            if illegal in line:
                new = re.sub("1|2|3|4|5|6|7|8|9|0", "", line)
                for trim in trimming:
                    new = new.replace(trim, "")
                for illegal in illegals:
                    new = new.replace(illegal, "")
                var_list.append(new)

    def scan(self) -> None:
        filename = open(self.target, "r")
        file_data = filename.readlines()
        for line in file_data:
            VariableUsage.var_scan(line)
        targ = self.target
        VariableUsage.var_usage(targ)