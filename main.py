import base64
import urllib.parse
import hashlib
import binascii
import html
import codecs
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Stylish Professional Banner
def display_banner():
    banner = f"""
{Fore.RED + Style.BRIGHT}█████████████████████████████████████████████████████████████████████
{Fore.RED + Style.BRIGHT}██                                                                      ██
{Fore.CYAN + Style.BRIGHT}██            {Fore.YELLOW + Style.BRIGHT}███████████{Fore.CYAN + Style.BRIGHT}      {Fore.YELLOW + Style.BRIGHT}██████████████      ██
{Fore.CYAN + Style.BRIGHT}██            {Fore.YELLOW + Style.BRIGHT}██            ██      {Fore.YELLOW + Style.BRIGHT}██        ██      ██
{Fore.CYAN + Style.BRIGHT}██            {Fore.YELLOW + Style.BRIGHT}██            ██      {Fore.YELLOW + Style.BRIGHT}██        ██      ██
{Fore.CYAN + Style.BRIGHT}██            {Fore.YELLOW + Style.BRIGHT}███████████{Fore.CYAN + Style.BRIGHT}      {Fore.YELLOW + Style.BRIGHT}██████████████      ██
{Fore.RED + Style.BRIGHT}██                                                                      ██
{Fore.RED + Style.BRIGHT}█████████████████████████████████████████████████████████████████████

{Fore.GREEN + Style.BRIGHT}             ███████╗███████╗██╗     ███████╗██╗   ██╗████████╗
{Fore.GREEN + Style.BRIGHT}             ██╔════╝██╔════╝██║     ██╔════╝██║   ██║╚══██╔══╝
{Fore.GREEN + Style.BRIGHT}             █████╗  █████╗  ██║     █████╗  ██║   ██║   ██║
{Fore.GREEN + Style.BRIGHT}             ██╔══╝  ██╔══╝  ██║     ██╔══╝  ██║   ██║   ██║
{Fore.GREEN + Style.BRIGHT}             ███████╗███████╗███████╗███████╗╚██████╔╝   ██║
{Fore.GREEN + Style.BRIGHT}             ╚══════╝╚══════╝╚══════╝╚══════╝ ╚═════╝    ╚═╝

{Fore.YELLOW + Style.BRIGHT}                 Ultimate Encode/Decode All-in-One Tool
{Fore.YELLOW + Style.BRIGHT}              Made with love by TEAM ANONYMOUS INDIA
"""
    print(banner)

# Encode/Decode Functions
class EncodeDecode:
    """A universal tool for encoding and decoding in various formats."""
    
    # Base64
    @staticmethod
    def base64_encode(data: str) -> str:
        return base64.b64encode(data.encode()).decode()

    @staticmethod
    def base64_decode(data: str) -> str:
        return base64.b64decode(data.encode()).decode()

    # URL
    @staticmethod
    def url_encode(data: str) -> str:
        return urllib.parse.quote(data)

    @staticmethod
    def url_decode(data: str) -> str:
        return urllib.parse.unquote(data)

    # HTML
    @staticmethod
    def html_encode(data: str) -> str:
        return html.escape(data)

    @staticmethod
    def html_decode(data: str) -> str:
        return html.unescape(data)

    # Hexadecimal
    @staticmethod
    def hex_encode(data: str) -> str:
        return binascii.hexlify(data.encode()).decode()

    @staticmethod
    def hex_decode(data: str) -> str:
        return binascii.unhexlify(data.encode()).decode()

    # ROT13
    @staticmethod
    def rot13_encode(data: str) -> str:
        return codecs.encode(data, 'rot_13')

    @staticmethod
    def rot13_decode(data: str) -> str:
        return codecs.decode(data, 'rot_13')

    # Binary (Base2)
    @staticmethod
    def binary_encode(data: str) -> str:
        return ' '.join(format(ord(char), '08b') for char in data)

    @staticmethod
    def binary_decode(data: str) -> str:
        return ''.join(chr(int(byte, 2)) for byte in data.split())

    # Hashing
    @staticmethod
    def md5_hash(data: str) -> str:
        return hashlib.md5(data.encode()).hexdigest()

    @staticmethod
    def sha1_hash(data: str) -> str:
        return hashlib.sha1(data.encode()).hexdigest()

    @staticmethod
    def sha256_hash(data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()

    # Base32
    @staticmethod
    def base32_encode(data: str) -> str:
        return base64.b32encode(data.encode()).decode()

    @staticmethod
    def base32_decode(data: str) -> str:
        return base64.b32decode(data.encode()).decode()

    # Base16
    @staticmethod
    def base16_encode(data: str) -> str:
        return base64.b16encode(data.encode()).decode()

    @staticmethod
    def base16_decode(data: str) -> str:
        return base64.b16decode(data.encode()).decode()

# Interactive User Menu
def user_menu():
    options = {
        "1": "Base64 Encode",
        "2": "Base64 Decode",
        "3": "URL Encode",
        "4": "URL Decode",
        "5": "HTML Encode",
        "6": "HTML Decode",
        "7": "Hexadecimal Encode",
        "8": "Hexadecimal Decode",
        "9": "ROT13 Encode",
        "10": "ROT13 Decode",
        "11": "Binary Encode",
        "12": "Binary Decode",
        "13": "MD5 Hash",
        "14": "SHA1 Hash",
        "15": "SHA256 Hash",
        "16": "Base32 Encode",
        "17": "Base32 Decode",
        "18": "Base16 Encode",
        "19": "Base16 Decode",
        "0": "Exit",
    }

    while True:
        print("\nChoose an option:")
        for key, value in options.items():
            print(f"{Fore.GREEN}{key}: {Fore.YELLOW}{value}")

        choice = input("\nEnter your choice: ")
        if choice == "0":
            print(f"{Fore.RED}Exiting... Thank you for using TEAM ANONYMOUS INDIA TOOL!")
            break

        data = input(f"{Fore.GREEN}Enter the text to process: {Fore.WHITE}")
        try:
            if choice == "1":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.base64_encode(data)}")
            elif choice == "2":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.base64_decode(data)}")
            elif choice == "3":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.url_encode(data)}")
            elif choice == "4":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.url_decode(data)}")
            elif choice == "5":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.html_encode(data)}")
            elif choice == "6":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.html_decode(data)}")
            elif choice == "7":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.hex_encode(data)}")
            elif choice == "8":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.hex_decode(data)}")
            elif choice == "9":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.rot13_encode(data)}")
            elif choice == "10":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.rot13_decode(data)}")
            elif choice == "11":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.binary_encode(data)}")
            elif choice == "12":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.binary_decode(data)}")
            elif choice == "13":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.md5_hash(data)}")
            elif choice == "14":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.sha1_hash(data)}")
            elif choice == "15":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.sha256_hash(data)}")
            elif choice == "16":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.base32_encode(data)}")
            elif choice == "17":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.base32_decode(data)}")
            elif choice == "18":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.base16_encode(data)}")
            elif choice == "19":
                print(f"{Fore.YELLOW}Result: {EncodeDecode.base16_decode(data)}")
            else:
                print(f"{Fore.RED}Invalid choice. Please try again.")
        except Exception as e:
            print(f"{Fore.RED}Error: {str(e)}")

# Main Program
if __name__ == "__main__":
    display_banner()
    user_menu()