# Task: Using NMap to Perform Various Scans

## Objective:
    - Detect open ports
    - Perform OS fingerprinting
    - Conduct ping scans
    - Execute TCP port scans
    - Execute UDP port scans

## Understanding Network Tools:
    - NMap (Network Mapper): A powerful open-source tool used for network discovery and security auditing.

## Prerequisites:
    - NMap Download Link: NMap Official Website (https://nmap.org/download.html#windows)
    - Operating System: Windows

## Step-by-Step Guide

1. Download and Install NMap
    - Visit the NMap Official Website (https://nmap.org/)
    - Download the Windows installer.
    - Follow the installation instructions to install NMap on your system.

2. Open Command Prompt
   - Press Win + R, type cmd, and press Enter to open the Command Prompt.

3. Basic NMap Commands
    - Detect Open Ports
       ```nmap -p 1-65535 <target_ip>```
        Explanation: Scans all ports (1-65535) on the target IP to detect open ports.
    - OS Fingerprinting
      ```nmap -O <target_ip>```
        Explanation: Attempts to determine the operating system of the target.
    - Ping Scan
      ```nmap -sn <target_ip>```
        Explanation: Performs a ping scan to check if the target is up without doing a port scan.
    - TCP Port Scan
      ```nmap -sT <target_ip>```
        Explanation: Performs a TCP connect scan to detect open TCP ports.
    - UDP Port Scan
        ```nmap -sU <target_ip>```
        Explanation: Performs a UDP scan to detect open UDP ports.

## Example Usage

    - Detect Open Ports:
        ```nmap -p 1-65535 192.168.1.1```
        Scans all ports on the target IP 192.168.1.1.
    - OS Fingerprinting:
        ```nmap -O 192.168.1.1```
        Attempts to determine the operating system of the target IP 192.168.1.1.
    - Ping Scan:
        ```nmap -sn 192.168.1.1```
        Checks if the target IP 192.168.1.1 is up without scanning ports.
    - TCP Port Scan:
        ```nmap -sT 192.168.1.1```
        Performs a TCP connect scan on the target IP 192.168.1.1.
    - UDP Port Scan:
        ```nmap -sU 192.168.1.1```
        Performs a UDP scan on the target IP 192.168.1.1.

## Summary

    - NMap: A versatile tool for network scanning and security auditing.
    - Scans Covered:
        - Open Ports Detection
        - OS Fingerprinting
        - Ping Scan
        - TCP Port Scan
        - UDP Port Scan
    - Download and Install: NMap Official Website (https://nmap.org/)
    - Operating System: Windows

By following this guide, students will be able to perform various types of scans using NMap and understand the purpose and output of each scan type. This will help them gain practical experience in network reconnaissance and security auditing.