import socket
import subprocess
import requests
import re

def banner():
    print(r"""
 __      __      _              _____                         
 \ \    / /__ _ (_) ___  _ __  |  ___|__  _ __ __ _ _ __ ___  
  \ \/\/ / _ \ '__|/ _ \| '_ \ | |_ / _ \| '__/ _` | '_ ` _ \ 
   \_/\_/\___/_|  \___/| .__/ |_| | (_) | | | (_| | | | | | |
                      |_|     \____\___/|_|  \__,_|_| |_| |_|

        VulnScan - IP, Port, Server & Vulnerability Scanner
        Author: YourName | Kali Linux Compatible
    """)

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] IP Address: {ip}")
        return ip
    except socket.gaierror:
        print("[-] Could not resolve domain.")
        return None

def scan_ports(ip):
    print(f"[+] Scanning common ports on {ip} using nmap...")
    result = subprocess.getoutput(f"nmap -sS -T4 -F {ip}")
    print(result)

def get_server_info(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        server = response.headers.get('Server', 'Unknown')
        print(f"[+] Web Server: {server}")
        return server
    except:
        print("[-] Could not retrieve server information.")
        return "Unknown"

def run_whatweb(domain):
    print(f"[+] Running WhatWeb on {domain}...")
    result = subprocess.getoutput(f"whatweb -v {domain}")
    print(result)
    return result

def run_vuln_scan(ip):
    print(f"[+] Running vulnerability scan using nmap NSE scripts on {ip}...")
    result = subprocess.getoutput(f"nmap -sV --script=vuln {ip}")
    print(result)
    return result

def search_exploits(tech_string):
    print("[+] Searching for known exploits using searchsploit...")
    matches = re.findall(r"\b\w+\b", tech_string)
    for term in set(matches):
        output = subprocess.getoutput(f"searchsploit {term}")
        if "Exploits" in output:
            print(f"\n[Exploit Results for: {term}]\n{output}")

def main():
    banner()
    domain = input("Enter domain (e.g. example.com): ").strip()
    ip = get_ip(domain)
    if not ip:
        return

    scan_ports(ip)
    get_server_info(domain)
    web_info = run_whatweb(domain)
    run_vuln_scan(ip)
    search_exploits(web_info)

if __name__ == "__main__":
    main()
