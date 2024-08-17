import requests
from bs4 import BeautifulSoup
import sys
from colorama import Style, Fore
import signal

url_db = "https://systemexplorer.net/file-database/file/"

# Function to handle the user's choice of file type (DLL or EXE)
def get_file_info(file_type):
    while True:
        file_name = str(input(Fore.LIGHTBLUE_EX + f"[>>] Please Enter a Microsoft {file_type.upper()}: " + Style.RESET_ALL)).strip()
        
        if not file_name:
            continue
        
        if f".{file_type}" in file_name.lower():
            file_name = file_name.split(f".{file_type}")[0]
        
        elif file_name.lower() in ["exit", "quit"]:
            return
        
        full_url = f"{url_db}{file_name}-{file_type.lower()}"
        print(Fore.RED + "Checking URL:", full_url + Style.RESET_ALL)

        try:
            response = requests.get(url=full_url, allow_redirects=False)
        except requests.RequestException as e:
            print(Fore.RED + f"Request failed: {e}" + Style.RESET_ALL)
            continue

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find('div', class_='fileDescription' if file_type == 'dll' else 'article')
            
            if content:
                print(Fore.CYAN + content.get_text().strip() + Style.RESET_ALL)
            else:
                print(Fore.BLACK + "Content not found." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Failed to retrieve the content, status code:", response.status_code, Style.RESET_ALL)

def signal_handler(sig, frame):
    print(Fore.YELLOW + "\nGOODBYE!" + Style.RESET_ALL)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Main loop to select DLL or EXE
while True:
    choice = str(input(Fore.RED + "[i] What Windows File do you interested in [DLL] ? [EXE] : " + Style.RESET_ALL)).strip().lower()

    if choice == "dll":
        get_file_info("dll")
    elif choice == "exe":
        get_file_info("exe")
    elif choice in ["exit", "quit"]:
        print(Fore.YELLOW + "GOODBYE!" + Style.RESET_ALL)
        break
    else:
        print(Fore.YELLOW + "Invalid choice. Please select either 'DLL' or 'EXE'." + Style.RESET_ALL)
