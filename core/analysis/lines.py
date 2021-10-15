# lines.py
# Date: 10/13/21
# Author: 0x1CA3

class GetLines(object):
    def __init__(self, target):
        self.target = target

    def getlines(self: str) -> int:
        i = 0
        filename = open(self.target, "r")
        file_data = filename.readlines()
        for line in file_data:
            i += 1
        return i