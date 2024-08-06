
# NetPortScan

NetPortScan is a multi-threaded network port scanner that allows you to scan a range of ports on a target IP address. It includes features such as delay between connection attempts, verbose mode, and the ability to save scan results to a CSV file.

## Features

- Multi-threaded port scanning
- Configurable port range
- Delay between connection attempts
- Verbose mode to show closed ports
- Save scan results to a CSV file

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sakv-dev/NetPortScan.git
    ```
2. Navigate to the project directory:
    ```bash
    cd NetPortScan
    ```

## Usage

Run the script with the following options:

```bash
python NetPortScan.py <IP_ADDRESS> [OPTIONS]
```

### Options

- `<IP_ADDRESS>`: The IP address to scan.
- `-p, --ports <PORT_RANGE>`: Port range to scan (default: 1-1024). Example: `1-100`, `20-80`, `1-33999`.
- `-v, --verbose`: Enable verbose mode to show closed ports.
- `-o, --output [<FILE>]`: Output file for scan results (default: `scan_results.csv`). If no file is specified, `scan_results.csv` will be used.
- `-t, --threads <NUMBER>`: Number of threads for scanning (default: 10).
- `-d, --delay <SECONDS>`: Delay between connection attempts in seconds (default: 0.01).

### Examples

1. Scan the default port range (1-1024) on a target IP:
    ```bash
    python netportscan.py 192.168.1.1
    ```

2. Scan a specific port range with verbose mode:
    ```bash
    python netportscan.py 192.168.1.1 -p 20-80 -v
    ```

3. Scan with a custom number of threads and delay:
    ```bash
    python netportscan.py 192.168.1.1 -t 20 -d 0.05
    ```

4. Save scan results to a custom file:
    ```bash
    python netportscan.py 192.168.1.1 -o my_scan_results.csv
    ```



## Acknowledgments

- Inspired by various open-source port scanners.
- Developed by [Stalka](https://github.com/sakv-dev).
