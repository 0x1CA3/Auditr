re = __import__("re")
time = __import__("time")


# variables.py
# Date: 10/13/21
# Author: 0x1CA3


class GetVars(object):
    def __init__(self, target):
        self.target = target

    @classmethod
    def var_search(cls, line: str) -> None:
        commons = [
        "int",
        "char",
        "float",
        "double",
        ]
        for common in commons:
            if re.search(common, line):
                if "main(" in line: pass
                elif "()" in line: pass
                else:
                    print(f"""\t[Variable] 
        Datatype -> {common}
        Variable -> {line}""")

    def read_data(self) -> None:
        print("\t[Scanning for variables...]")
        print("\t---------------------------")
        time.sleep(3)
        filename = open(self.target, "r")
        file_data = filename.readlines()
        for line in file_data:
            GetVars.var_search(line)