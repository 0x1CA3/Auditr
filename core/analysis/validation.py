# validation.py
# Date: 10/13/21
# Author: 0x1CA3

class ValidationCheck(object):
    @classmethod
    def check(cls, filename: str) -> int:
        if ".c" not in filename:
            print("Make sure your file has a '.c' extension!")
            return 1

    @classmethod
    def code_validation(cls, filename: str) -> int:
        i = 0
        target = open(filename, "r")
        file_data = target.readlines()
        for line in file_data:
            if "#include" in line: i += 1
        if i != 0: 
            pass
        else:
            print("""C file validation check failed!
Error: Missing Includes
            """)
            return 1