# clear.py
# Date: 10/13/21
# Author: 0x1CA3

class ClearScreen(object):
    @classmethod
    def clear(cls) -> str:
        return "\033[H\033[2J"