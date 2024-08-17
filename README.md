# MSFileInfoGenerator
MSFileInfoGenerator is a Python script that allows users to retrieve information about Microsoft DLL and EXE files from the System Explorer file database. The script prompts the user to input a file name, fetches relevant information from the web, and displays it in the terminal. It also handles common user inputs like "exit" and "quit" gracefully and supports interruption with Ctrl+C.

## Features
Fetch detailed information about Microsoft DLL and EXE files.
Gracefully handle invalid inputs and network errors.
Exit the script using "exit", "quit", or Ctrl+C.
Simple command-line interface.

## Installation
1.Clone the Repository:
  ```powershell
    git clone https://github.com/Raulisr00t/MSFileInfoGenerator.git
    cd MSFileInfoGenerator
  ```
2.Install the Required Packages:
  Install the dependencies listed in requirements.txt using pip:
  ```powershell
    pip install -r requirements.txt
  ```
3.Run the Script:
  ```powershell
    python msfileinfogenerator.py
  ```
### Usage
DLL Information: When prompted, type dll to search for a DLL file. Enter the name of the DLL (e.g., kernel32.dll), and the script will fetch and display the information.
EXE Information: When prompted, type exe to search for an EXE file. Enter the name of the EXE (e.g., cmd.exe), and the script will fetch and display the information.
Exit the Script: You can exit the script by typing "exit", "quit", or pressing Ctrl+C.

### Example
```bash
[i] What Windows File do you interested in [DLL] ? [EXE] : dll
[>>] Please Enter a Microsoft DLL: kernel32.dll
Checking URL: https://systemexplorer.net/file-database/file/kernel32-dll
Detailed information about kernel32.dll...
```
### Contributing
Contributions are welcome! Please feel free to submit a pull request or report issues.

## License
This project is licensed under the MIT License.

