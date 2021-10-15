from colorama import Fore


# banner.py
# Date: 10/13/21
# Author: 0x1CA3


class DisplayBanner(object):
    @classmethod
    def banner(cls) -> str:
        ascii_banner = f"""
        {Fore.YELLOW} _______           __ __ __         {Fore.RESET}
        {Fore.YELLOW}|   _   |.--.--.--|  |__|  |_.----. {Fore.RESET}
        {Fore.YELLOW}|       ||  |  |  _  |  |   _|   _| {Fore.RESET}
        {Fore.YELLOW}|___|___||_____|_____|__|____|__|   {Fore.RESET}                       
        {Fore.YELLOW}[Made by: https://github.com/0x1CA3]{Fore.RESET}
        """
        return ascii_banner