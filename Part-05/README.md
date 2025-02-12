# Task: Using NMap to Perform Various Scans

## Objective  
- Detect open ports  
- Perform OS fingerprinting  
- Conduct ping scans  
- Execute TCP port scans  
- Execute UDP port scans  
- Additional advanced scans and options

## Understanding Network Tools  
- **NMap (Network Mapper):** A powerful open-source tool used for network discovery and security auditing

## Prerequisites  
- **NMap Download Link:** [NMap Official Website](https://nmap.org/)  
- **Operating System:** Windows

## Step-by-Step Guide

  
### 1. Download and Install NMap  
- Visit the [NMap Official Website](https://nmap.org/).  
- Download the Windows installer.  
- Follow the installation instructions to install NMap on your system.  
  
### 2. Open Command Prompt  
- Press `Win + R`, type `cmd`, and press `Enter` to open the Command Prompt.

### 3. Basic NMap Commands

#### a. Detect Open Ports
```
nmap -p 1-65535 <target_ip>
nmap -p 1-65535 192.168.1.1
```
Explanation: Scans all ports (1-65535) on the target IP to detect open ports.

#### b. OS Fingerprinting
```
nmap -O <target_ip>
nmap -O 192.168.1.1
```
Explanation: Attempts to determine the operating system of the target.

#### c. Ping Scan
```
nmap -sn <target_ip>
nmap -sn 192.168.1.1
```
Explanation: Performs a ping scan to check if the target is up without doing a port scan.

#### d. TCP Port Scan
```
nmap -sT <target_ip>
nmap -sT 192.168.1.1
```
Explanation: Performs a TCP connect scan to detect open TCP ports.

#### e. UDP Port Scan
```
nmap -sU <target_ip>
nmap -sU 192.168.1.1
```
Explanation: Performs a UDP scan to detect open UDP ports.

### Advanced NMap Scans and Options

#### f. Service Version Detection
```
nmap -sV <target_ip>
nmap -sV 192.168.1.1
```
Explanation: Detects the version of services running on open ports.
#### g. Aggressive Scan
```
nmap -A <target_ip>
nmap -A 192.168.1.1
```
Explanation: Performs an aggressive scan that includes OS detection, version detection, script scanning, and traceroute.
#### h. Scan Multiple Targets
```
nmap <target_ip1> <target_ip2> <target_ip3>
nmap 192.168.1.1 192.168.1.2 192.168.1.3
```
Explanation: Scans multiple targets in a single command.
#### i. Scan a Range of IPs
```
nmap <target_ip_range>
nmap 192.168.1.1-254
```
Explanation: Scans a range of IP addresses.
#### j. Scan a Subnet
```
nmap <target_subnet>
nmap 192.168.1.0/24
```
Explanation: Scans all IP addresses in a subnet.
#### k. Save Scan Results to a File
```
nmap -oN output.txt <target_ip>
nmap -oN output.txt 192.168.1.1
```
Explanation: Saves the scan results to a file in normal format.
#### l. Save Scan Results in XML Format
```
nmap -oX output.xml <target_ip>
nmap -oX output.xml 192.168.1.1
```
Explanation: Saves the scan results to a file in XML format.

## Summary

    - NMap: A versatile tool for network scanning and security auditing.
    - Scans Covered:
        - Open Ports Detection
        - OS Fingerprinting
        - Ping Scan
        - TCP Port Scan
        - UDP Port Scan
        - Service Version Detection
        - Aggressive Scan
        - Scanning Multiple Targets
        - Scanning IP Ranges and Subnets
        - Saving Scan Results to Files
    - Download and Install: NMap Official Website (https://nmap.org/)
    - Operating System: Windows