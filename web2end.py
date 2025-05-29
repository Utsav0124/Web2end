import subprocess
import sys
import requests
from bs4 import BeautifulSoup
import socket
import os
import pyfiglet

def print_banner():
    banner = pyfiglet.figlet_format("WEB2END")
    print(banner)
    print("=== THIS TOOLS IS DEVELOP BY UTSAV SHARMA $$$  ===\n")
print (" IT IS ONLY FOR EDUCATIONAL PURPOSE ")
def run_theharvester(domain):
    print(f"\n[+] Running theHarvester on {domain} ...")
    try:
        subprocess.run(["theharvester", "-d", domain, "-b", "google"], check=True)
    except Exception as e:
        print(f"Error running theHarvester: {e}")

def run_dnsrecon(domain):
    print(f"\n[+] Running dnsrecon on {domain} ...")
    try:
        subprocess.run(["dnsrecon", "-d", domain], check=True)
    except Exception as e:
        print(f"Error running dnsrecon: {e}")

def nmap_scan(domain):
    print(f"\n[+] Running nmap scan on {domain} ...")
    try:
        subprocess.run(["nmap", "-sV", domain], check=True)
    except Exception as e:
        print(f"Error running nmap: {e}")

def brute_force_dirs(domain, wordlist_path):
    print(f"\n[+] Starting directory brute force on {domain} ...")
    try:
        with open(wordlist_path, 'r') as f:
            paths = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"Wordlist file {wordlist_path} not found.")
        return
    
    found_paths = []
    base_url = f"http://{domain}"
    for path in paths:
        url = f"{base_url}/{path}"
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(f"Found: {url} (Status: {r.status_code})")
                found_paths.append(url)
        except requests.RequestException:
            pass
    if not found_paths:
        print("No directories found from the wordlist.")
    else:
        print(f"\n[+] Brute force found {len(found_paths)} valid paths.")

def check_http_headers(domain):
    print(f"\n[+] Checking HTTP headers for {domain} ...")
    url = f"http://{domain}"
    try:
        r = requests.get(url, timeout=5)
        headers = r.headers
        print("HTTP Headers:")
        for key, value in headers.items():
            print(f"{key}: {value}")

        # Basic security header checks
        security_headers = ['Content-Security-Policy', 'X-Frame-Options', 'Strict-Transport-Security', 'X-Content-Type-Options']
        print("\nSecurity Headers Check:")
        for sh in security_headers:
            if sh in headers:
                print(f"{sh} : Present")
            else:
                print(f"{sh} : Missing")
    except requests.RequestException as e:
        print(f"Could not fetch HTTP headers: {e}")

def basic_xss_test(domain):
    print(f"\n[+] Performing a very basic XSS check on {domain} ...")
    # Warning: This is very superficial, for demonstration only!
    test_url = f"http://{domain}/?q=<script>alert(1)</script>"
    try:
        r = requests.get(test_url, timeout=5)
        if "<script>alert(1)</script>" in r.text:
            print("Potential reflected XSS vulnerability detected!")
        else:
            print("No obvious reflected XSS detected (very basic check).")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

def resolve_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"\n[+] IP address of {domain} is {ip}")
        return ip
    except socket.gaierror:
        print(f"Cannot resolve IP for domain {domain}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 web2end.py <domain> [wordlist_path]")
        sys.exit(1)

    domain = sys.argv[1]
    wordlist_path = sys.argv[2] if len(sys.argv) > 2 else "/usr/share/wordlists/dirb/common.txt"

    print_banner()
    
    resolve_ip(domain)
    run_theharvester(domain)
    run_dnsrecon(domain)
    nmap_scan(domain)
    check_http_headers(domain)
    brute_force_dirs(domain, wordlist_path)
    basic_xss_test(domain)

    print("\n=== Scan Completed ===")

if __name__ == "__main__":
    main()
