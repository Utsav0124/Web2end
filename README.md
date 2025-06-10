# 🌐 WEB2END - Website Reconnaissance Tool

**WEB2END** is a powerful, cross-platform website reconnaissance and vulnerability scanning tool written in Python. Built for cybersecurity students and professionals, it automates various techniques to gather intelligence about websites.

> ✅ Compatible with **Kali Linux** and **Windows**

---

## 🚀 Features

- Subdomain Enumeration
- IP Address & Port Scanner
- DNS Records Lookup
- WHOIS Info Fetcher
- Server Header Detection
- Technology Detection (Wappalyzer-ready)
- Optional Integration: `theHarvester`, `dnsrecon`

---

## 🛠 Installation on Kali Linux

### 1. COMMANDS 

```bash
sudo apt update && sudo apt upgrade -y

sudo apt install python3 python3-pip -y

git clone 
cd web2end

pip3 install requests pyfiglet socket dnspython whois

TO MAKE SCRIPT EXCUTEABLE TYPE THIS
chmod +x web2end.py

USAGE :- python3 web2end.py ENTER TARGET WEBSITE DOMAIN 



