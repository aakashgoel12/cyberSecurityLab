# Introduction to Network Reconnaissance Tools

## Objective:
- Understand the use of network reconnaissance tools like WHOIS, DIG, Traceroute, and NSLookup to gather network and domain registrar details.

## Materials Needed:
- Kali Linux (Oracle Virtual Box + Kali Linux)
- Reference: Kali Linux VirtualBox Import (https://www.kali.org/docs/virtualization/import-premade-virtualbox/)


1. Introduction to Network Reconnaissance

Today, we are going to dive into the fascinating world of network reconnaissance. This is a crucial aspect of cybersecurity, especially in the context of smart manufacturing environments like PLC and SCADA systems. Let's start by understanding what network reconnaissance is and why it is so important.

- What is Network Reconnaissance?

Network reconnaissance is the process of gathering information about a network, its devices, and its services. This information can include details about the network's topology, the devices connected to it, the services running on those devices, and any potential vulnerabilities that might exist. Essentially, it's like mapping out the landscape of a network to understand its structure and identify any weak points.

- Why is Network Reconnaissance Important in Cybersecurity?

In cybersecurity, knowledge is power. The more you know about your network, the better you can protect it. Network reconnaissance allows security professionals to:

* Identify Vulnerabilities: By understanding the network's structure and the devices connected to it, you can identify potential vulnerabilities that could be exploited by attackers.
* Monitor Network Activity: Regular reconnaissance helps in monitoring network activity and detecting any unusual behavior that might indicate a security breach.
* Plan Defenses: With detailed knowledge of the network, you can plan and implement more effective security measures to protect against potential threats.

For smart manufacturing environments, where systems like PLCs and SCADA are critical, understanding the network is essential to ensure the integrity and availability of manufacturing processes.


2. How Hackers Use Network Reconnaissance Tools

Now, let's talk about how hackers use network reconnaissance tools. Hackers use these tools to gather as much information as possible about a target network before launching an attack. This process is often referred to as 'footprinting' or 'information gathering.' Here are some common steps hackers take during network reconnaissance:

* Domain Information Gathering: Hackers use tools like WHOIS to gather information about the domain, such as the domain registrar, contact information, and registration dates. This can help them identify potential targets within the organization.
* DNS Information Gathering: Tools like DIG and NSLookup are used to query DNS servers and gather information about the domain's DNS records. This can reveal details about the network's structure and the services running on it.
* Network Path Analysis: Traceroute is used to map out the path that data takes from the hacker's machine to the target network. This can help identify potential points of interception or attack.
* Service Enumeration: By identifying the services running on the network, hackers can look for known vulnerabilities in those services and plan their attack accordingly.

Understanding these tools and techniques is crucial for defending against cyber-attacks. By knowing how hackers think and operate, you can better anticipate their moves and design more robust security measures.

3. Commands

- WHOIS Command

WHOIS is a query and response protocol that is widely used for querying databases that store the registered users or assignees of an Internet resource, such as a domain name, an IP address block, or an autonomous system.

You can try below command on, https://whois.domaintools.com/,https://viewdns.info/.
```
whois bits-pilani.ac.in
```

* Registry Domain ID: D10794-IN, This is a unique identifier for the domain in the registry.
* Registrar URL: http://www.ernet.in, The URL of the registrar's website.
* Updated Date: 2021-02-03T04:46:04Z, The date and time when the domain information was last updated.
* Creation Date: 2003-02-28T05:00:00Z, The date and time when the domain was originally registered.
* Registry Expiry Date: 2028-02-28T05:00:00Z, The date and time when the domain registration will expire if not renewed.
* Registrar IANA ID: 800068, The unique identifier for the registrar assigned by the Internet Assigned Numbers Authority (IANA).
* Domain Status: ok http://www.icann.org/epp#OK, The current status of the domain. "OK" indicates that the domain is active and there are no issues.
* Registrant Organization: Birla Institute Of Technology & Science
* Registrant Country: IN
* 3 Name Server The DNS servers that are authoritative for the domain. These servers translate the domain name into an IP address.
* DNSSEC: unsigned, Indicates whether the domain is using DNS Security Extensions (DNSSEC). "Unsigned" means it is not using DNSSEC.

**Summary of whois output**
* The domain bits-pilani.ac.in is registered to the Birla Institute Of Technology & Science.
* The domain was created on February 28, 2003, and is set to expire on February 28, 2028.
* The domain is managed by the registrar ERNET India.
* Most of the registrant, admin, and tech contact information is redacted for privacy.
* The domain uses three name servers: ns1.bits-pilani.ac.in, ns2.bits-pilani.ac.in, and ns3.bits-pilani.ac.in.
* The domain is not using DNSSEC.

This information helps in understanding the ownership, registration details, and technical setup of the domain, which can be useful for both network administrators and potential attackers.

- DIG Command

DIG (Domain Information Groper) is a network administration command-line tool for querying Domain Name System (DNS) name servers.

https://toolbox.googleapps.com/apps/dig/#A/

```
dig bits-pilani.ac.in  
```

* The domain www.bits-pilani.ac.in has an A record that maps to the IP address 141.148.211.159. Understanding the IP address mapping can help in identifying potential security issues. For example, if the IP address changes unexpectedly, it could indicate a DNS hijacking attack.
* The TTL value indicates that this DNS information will be cached for approximately 6 hours before it needs to be refreshed.
* Scenario: You notice that the website www.bits-pilani.ac.in is not accessible. By using the DIG command, you find that the domain resolves to the IP address 141.148.211.159. You can then: Ping the IP Address: Check if the server is reachable by pinging the IP address. ping 141.148.211.159.

- Traceroute Command

Task: Run the Traceroute command on a different domain and analyze the output.

Open Command Prompt and run
```
tracert bits-pilani.ac.in
```

The tracert command in Windows is used to trace the path that packets take from your computer to a destination host. It helps in identifying the route and measuring transit delays of packets across an IP network.

* Tracing route to bits-pilani.ac.in [141.148.211.159] over a maximum of 30 hops:  This indicates that the tracert command is tracing the route to the domain bits-pilani.ac.in with the IP address 141.148.211.159. The command will attempt to trace up to 30 hops (intermediate devices like routers) to reach the destination.
* 1 <1 ms <1 ms <1 ms gsa-476b0d53-7866000000.internal.cloudapp.net [10.20.254.5]: The first hop is a device with the hostname gsa-476b0d53-7866000000.internal.cloudapp.net and the IP address 10.20.254.5. The response time is less than 1 millisecond, indicating it is very close to your location, likely within the same local network or data center.
* For hops 2 through 30, the requests timed out. This means that the tracert command did not receive a response from these intermediate devices. This could be due to several reasons: The devices are configured to not respond to ICMP (Internet Control Message Protocol) requests. There are firewalls or security policies in place that block ICMP traffic.

- NSLookup Command

Task: Run the NSLookup command on a different domain and analyze the output.

Open Command Prompt and run
```
nslookup bits-pilani.ac.in
```

* The domain bits-pilani.ac.in resolves to the IP address 141.148.211.159.
* The DNS query was resolved by a DNS server with the IP address 10.20.254.4, which is a private IP address within your local network.
* The response is a non-authoritative answer, meaning it was obtained from a cached record rather than directly from the authoritative DNS server for the domain.


**Summary and Conclusions**

- Summary:
* Network reconnaissance is the process of gathering information about a network, its devices, and its services.
* It is crucial for identifying vulnerabilities, monitoring network activity, and planning defenses.
* Hackers use reconnaissance tools like WHOIS, DIG, Traceroute, and NSLookup to gather information about a target network before launching an attack.
* Understanding these tools and techniques is essential for defending against cyber-attacks.

- From a Hacker's Perspective:
* Hackers use network reconnaissance to gather as much information as possible about a target network.
* They use tools like WHOIS to gather domain information, DIG and NSLookup to query DNS records, and Traceroute to map the network path.
* This information helps them identify potential vulnerabilities and plan their attacks.

- From a Network Maintenance Perspective:
* Network administrators use reconnaissance tools to understand the network's structure and identify potential vulnerabilities.
* Regular reconnaissance helps in monitoring network activity and detecting any unusual behavior that might indicate a security breach.
* By understanding the network, administrators can plan and implement more effective security measures to protect against potential threats.

- Basic Conclusions:
* Network reconnaissance is a fundamental aspect of cybersecurity, providing valuable insights into the network's structure and potential vulnerabilities.
* Both hackers and network administrators use reconnaissance tools, but for different purposes. Hackers use them to plan attacks, while administrators use them to defend against attacks.
* Understanding how these tools work and how to interpret their output is crucial for maintaining the security and integrity of smart manufacturing environments.

By mastering these tools and techniques, you can better protect your network and anticipate potential threats, ensuring the security and availability of your smart manufacturing systems.