# help.py
# Date: 10/13/21
# Author: 0x1CA3

class HelpMenu(object):
    @classmethod
    def menu(cls) -> str:
        helpmenu = """
        --help             Shows the available options.
        --all              Scans for everything, including possibly misused variables and functions.
        --vars             Scans for defined variables.
        --basic            Scans for common & basic vulnerabilties.
        --advanced         Scans for more advanced vulnerabilties.
        --vscanning        Scans for variables that are possibly being used in a vulnerable way.
        """
        return helpmenu