from core.misc.help import *
from core.misc.clear import *
from core.misc.banner import *
from core.misc.imports import *
from core.analysis.lines import *
from core.auditr.basic_scan import *
from core.analysis.variables import *
from core.analysis.validation import *
from core.auditr.advanced_scan import *
from core.analysis.variable_usage import *

sys = __import__("sys")
from colorama import Fore
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


# Auditr
# Date: 10/13/21
# Author: 0x1CA3


class Handler(object):
    def __init__(self, option, target):
        self.option = option
        self.target = target

    @classmethod
    def help_handler(cls, option: str) -> None:
        if option == "--help": print(HelpMenu.menu())

    def handler(self: str) -> None:
        if self.option == "--basic":
            print(f"""\tLoaded File -> {self.target}
        Lines -> {GetLines(self.target).getlines()}
        Current Time: {current_time}
            """)
            BasicScan(self.target).scan()
        if self.option == "--advanced":
            print(f"""\tLoaded File -> {self.target}
        Lines -> {GetLines(self.target).getlines()}
        Current Time: {current_time}
            """)
            AdvancedScan(self.target).scan()
        if self.option == "--vars": GetVars(self.target).read_data()
        if self.option == "--vscanning":
            print(f"""\tLoaded File -> {self.target}
        Lines -> {GetLines(self.target).getlines()}
        Current Time: {current_time}
            """)
            VariableUsage(self.target).scan()
        if self.option == "--all":
            print(f"""\tLoaded File -> {self.target}
        Lines -> {GetLines(self.target).getlines()}
        Current Time: {current_time}
            """)
            BasicScan(self.target).scan()
            AdvancedScan(self.target).scan()
            VariableUsage(self.target).scan()

def main() -> None:
    if ImportCheck.check() == 1:
        sys.exit()
    print(ClearScreen.clear())
    print(DisplayBanner.banner())
    if len(sys.argv) < 3:
        print("python3 auditr.py --option <file>")
        option = sys.argv[1]
        Handler.help_handler(option)
    else:
        option = sys.argv[1]
        target = sys.argv[2]
        if ValidationCheck.check(target) == 1: sys.exit()
        if ValidationCheck.code_validation(target) == 1: sys.exit()
        Handler(option, target).handler()

if __name__ == "__main__":
    main()