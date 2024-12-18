import requests
from bs4 import BeautifulSoup
import re
def check_sql_injection(url):
    sql_payloads = ["' OR '1'='1", "'; DROP TABLE users; --", "admin'--"]
    for payload in sql_payloads:
        new_url = f"{url}?id={payload}"
        response = requests.get(new_url)
        if "error" in response.text.lower():
            print(f"SQL Injection vulnerability found at {new_url}")
        else:
            print(f"No SQL Injection vulnerability found at {new_url}")
def check_xss(url):
    xss_payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"]
    for payload in xss_payloads:
        new_url = f"{url}?q={payload}"
        response = requests.get(new_url)
        if payload in response.text:
            print(f"XSS vulnerability found at {new_url}")
        else:
            print(f"No XSS vulnerability found at {new_url}")
def crawl_urls(base_url):
    urls = [base_url]
    visited = set(urls)
    while urls:
        url = urls.pop(0)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('/'):
                href = base_url + href
            if href not in visited:
                visited.add(href)
                urls.append(href)
    return visited
def run_scanner(base_url):
    print(f"Starting scan on {base_url}")
    urls = crawl_urls(base_url)
    for url in urls:
        print(f"Scanning {url}")
        check_sql_injection(url)
        check_xss(url)
    print("Scan completed.")

if __name__ == "__main__":
    base_url = "https://google.com"  # Replace with your target URL
    run_scanner(base_url)
import requests
from bs4 import BeautifulSoup
import re
import sqlite3
import threading
#database
def run_scanner(base_url):
    setup_database()
    print(f"Starting scan on {base_url}")
    urls = crawl_urls(base_url)
    threads = []
    for url in urls:
        print(f"Scanning {url}")
        t1 = threading.Thread(target=check_sql_injection, args=(url,))
        t2 = threading.Thread(target=check_xss, args=(url,))
        threads.append(t1)
        threads.append(t2)
        t1.start()
        t2.start()
    for t in threads:
        t.join()
    print("Scan completed.")

if __name__ == "__main__":
    base_url = "http://google.com"  # Replace with your target URL
    run_scanner(base_url)
import nmap

def setup_nmap():
    nmScan = nmap.PortScanner()
    return nmScan
def scan_ports(nmScan, ip_address, port_range):
    nmScan.scan(ip_address, port_range)
    for host in nmScan.all_hosts():
        print(f"Host: {host} ({ip_address})")
        for proto in nmScan[host].all_protocols():
            print(f"Protocol: {proto}")
            lport = nmScan[host][proto].keys()
            for port in lport:
                print(f"port: {port} state: {nmScan[host][proto][port]['state']}")
def run_scanner(base_url):
    setup_database()
    nmScan = setup_nmap()
    print(f"Starting scan on {base_url}")
    urls = crawl_urls(base_url)
    for url in urls:
        print(f"Scanning {url}")
        check_sql_injection(url)
        check_xss(url)
        scan_ports(nmScan, url, "1-1024")  # Example port range
    print("Scan completed.")

if __name__ == "__main__":
    base_url = "http://google.com"  # Replace with your target URL
    run_scanner(base_url)
import requests
from bs4 import BeautifulSoup
import re
import sqlite3
import threading
import nmap
import tkinter as tk
from tkinter import ttk, messagebox
def setup_database():
    conn = sqlite3.connect('vulnerability_scanner.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY,
            url TEXT,
            vulnerability TEXT,
            details TEXT
        )
    ''')
    conn.commit()
    conn.close()

def store_result(url, vulnerability, details):
    conn = sqlite3.connect('vulnerability_scanner.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO results (url, vulnerability, details)
        VALUES (?, ?, ?)
    ''', (url, vulnerability, details))
    conn.commit()
    conn.close()
def check_sql_injection(url):
    sql_payloads = ["' OR '1'='1", "'; DROP TABLE users; --", "admin'--"]
    for payload in sql_payloads:
        new_url = f"{url}?id={payload}"
        response = requests.get(new_url)
        if "error" in response.text.lower():
            print(f"SQL Injection vulnerability found at {new_url}")
            store_result(new_url, "SQL Injection", payload)
        else:
            print(f"No SQL Injection vulnerability found at {new_url}")

def check_xss(url):
    xss_payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"]
    for payload in xss_payloads:
        new_url = f"{url}?q={payload}"
        response = requests.get(new_url)
        if payload in response.text:
            print(f"XSS vulnerability found at {new_url}")
            store_result(new_url, "XSS", payload)
        else:
            print(f"No XSS vulnerability found at {new_url}")

def crawl_urls(base_url):
    urls = [base_url]
    visited = set(urls)
    while urls:
        url = urls.pop(0)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('/'):
                href = base_url + href
            if href not in visited:
                visited.add(href)
                urls.append(href)
    return visited
def setup_nmap():
    nmScan = nmap.PortScanner()
    return nmScan

def scan_ports(nmScan, ip_address, port_range):
    nmScan.scan(ip_address, port_range)
    for host in nmScan.all_hosts():
        print(f"Host: {host} ({ip_address})")
        for proto in nmScan[host].all_protocols():
            print(f"Protocol: {proto}")
            lport = nmScan[host][proto].keys()
            for port in lport:
                print(f"port: {port} state: {nmScan[host][proto][port]['state']}")
def run_scanner(base_url):
    setup_database()
    nmScan = setup_nmap()
    print(f"Starting scan on {base_url}")
    urls = crawl_urls(base_url)
    threads = []
    for url in urls:
        print(f"Scanning {url}")
        t1 = threading.Thread(target=check_sql_injection, args=(url,))
        t2 = threading.Thread(target=check_xss, args=(url,))
        t3 = threading.Thread(target=scan_ports, args=(nmScan, url, "1-1024"))
        threads.append(t1)
        threads.append(t2)
        threads.append(t3)
        t1.start()
        t2.start()
        t3.start()
    for t in threads:
        t.join()
    print("Scan completed.")
def start_scan():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return
    run_scanner(url)
    messagebox.showinfo("Scan Completed", "Vulnerability scan completed.")

# Tkinter GUI setup
root = tk.Tk()
root.title("Vulnerability Scanner")
root.geometry("400x300")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Enter URL:").grid(row=0, column=0, pady=10)
url_entry = ttk.Entry(frame, width=40)
url_entry.grid(row=0, column=1, pady=10)

scan_button = ttk.Button(frame, text="Start Scan", command=start_scan)
scan_button.grid(row=1, column=0, columnspan=2, pady=20)

root.mainloop()
