🔧 How to Use web2end in Kali Linux
Follow the steps below to install and use the web2end tool on Kali Linux.

✅ Prerequisites
Before starting, make sure your Kali Linux system is up to date:

bash
Copy
Edit
sudo apt update && sudo apt upgrade -y
Install Python and pip if not already installed:

bash
Copy
Edit
sudo apt install python3 python3-pip -y
Clone the repository:

bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/web2end.git
cd web2end
📦 Install Required Python Modules
Install the required dependencies:

bash
Copy
Edit
pip3 install -r requirements.txt
If requirements.txt is missing, use this:

bash
Copy
Edit
pip3 install requests pyfiglet socket dnspython whois
⚙️ Make the Script Executable (Optional)
bash
Copy
Edit
chmod +x web2end.py
🚀 Run the Tool
bash
Copy
Edit
python3 web2end.py
🛠 Features Included
✅ Subdomain Enumeration

✅ IP Address & Server Info Lookup

✅ Port Scanning

✅ WHOIS Lookup

✅ Website Technology Fingerprinting (if integrated with Wappalyzer APIs)

✅ DNS Recon

✅ theHarvester Integration (optional/manual)

