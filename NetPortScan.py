import socket
import subprocess
import sys
from datetime import datetime, timedelta
import argparse
import time
import csv
import threading

# Clear the screen
subprocess.call('clear', shell=True)

print("*********************** NetPortScan ***********************")
print("*********************** By Stalka *************************")
print("Github : https://github.com/sakv-dev")
print()

# Argument parser for command-line options
parser = argparse.ArgumentParser(description='Network port scanner')
parser.add_argument('ip', help='IP address to scan')
parser.add_argument('-p', '--ports', type=str, help='Port range to scan (e.g., 1-1024)', default='1-1024')
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
parser.add_argument('-o', '--output', type=str, nargs='?', const='scan_results.csv', help='Output file for scan results (default: scan_results.csv)')
parser.add_argument('-t', '--threads', type=int, help='Number of threads for scanning', default=10)
parser.add_argument('-d', '--delay', type=float, help='Delay between connection attempts in seconds', default=0.01)
args = parser.parse_args()

remoteServerIP = args.ip
port_range = args.ports
verbose = args.verbose
output_file = args.output if args.output else 'scan_results.csv'
num_threads = args.threads
delay = args.delay

# Convert port range to a list of integers
port_min, port_max = map(int, port_range.split('-'))
ports = list(range(port_min, port_max + 1))

print(f"[+] Starting port scan on {remoteServerIP}")

# Start the timer
t1 = datetime.now()
last_timer_update = t1

results = []
lock = threading.Lock()

def scan_port(port):
    global last_timer_update
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((remoteServerIP, port))
        with lock:
            if result == 0:
                try:
                    service = socket.getservbyport(port, 'tcp')
                except:
                    service = 'Unknown'
                print(f"[+] Port {port}: Open (Service: {service})")
                results.append({'Port': port, 'Status': 'Open', 'Service': service})
            elif verbose:
                print(f"[-] Port {port}: Closed")
                results.append({'Port': port, 'Status': 'Closed', 'Service': 'N/A'})
        sock.close()
        time.sleep(delay)
    except Exception as e:
        with lock:
            print(f"ERROR: {e}")

def threader():
    global last_timer_update
    while ports:
        port = ports.pop(0)
        scan_port(port)
        current_time = datetime.now()
        with lock:
            if (current_time - last_timer_update) >= timedelta(seconds=10):
                elapsed_time = current_time - t1
                print(f"[+] Elapsed time: {str(elapsed_time).split('.')[0]}")  # Format HH:MM:SS
                last_timer_update = current_time

threads = []

for _ in range(num_threads):
    thread = threading.Thread(target=threader)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# Stop the timer
t2 = datetime.now()
total_time = t2 - t1

print(f"[+] Scan completed in {str(total_time).split('.')[0]}")  # Format HH:MM:SS

if output_file:
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Port', 'Status', 'Service']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    print(f"[+] Scan results saved in {output_file}")
