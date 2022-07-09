import requests
import os
import tabulate
from tabulate import tabulate

domain = str(input("[+] Domain (e.g. google.com): "))
subdomain_list = str(input("[+] Path to subdomain list file: "))

if os.path.exists(subdomain_list) == False:
    print("[-] Unable to locate the file/path")

thefile = open(subdomain_list, "r")
content = thefile.read()
subdomains = content.splitlines()

http_subdomains = []
https_subdomains = []

for subdomain in subdomains:

    http_url = f"http://{subdomain}.{domain}"
    https_url = f"https://{subdomain}.{domain}"
    try:
        requests.get(http_url)
        print(f"[!] Subdomain found: {http_url}")
        http_subdomains.append(http_url)
        requests.get(https_url)
        print(f"[!] Subdomain found: {https_url}")
        https_subdomains.append(https_url)
    except requests.ConnectionError:
        pass

print("\n")

table = [[http_subdomains, https_subdomains]]

print(tabulate(table, headers=["HTTP Subdomains", "HTTPS Subdomains"]))