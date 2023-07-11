<h1>100 MITRE ATT&CK Programming Projects for RedTeamers</h1>
<p align="center"> 
    <img src="https://cdn.infrasos.com/wp-content/uploads/2022/11/What-is-a-Red-team-in-cybersecurity.png">
</p>

This repo organizes a full list of redteam projects to help everyone into this field gain knownledge and skills in programming aimed to offensive security exercices.

I recommend you to do them on the programming language you are most comfortable with. Implementing these projects will definitely help you gain more experience and, consequently, master the language. They are divided in categories, ranging from super basic to advanced projects.

If you enjoy this list please take the time to recommend it to a friend and follow me! I will be happy with that :)  🇦🇴.

And remember: With great power comes... (we already know). 

<h3>Contributions</h3>
You can make a pull request for the "Projects" directory and name the file in 
compliance with the following convention:

```
[ID] PROJECT_NAME - <LANGUAGE> | AUTHOR
```

#### Example:

```
[91] Web Exploitation Framework - <C> | EONRaider
```
<br>
Consider to insert your notes during the development of any of those projects, to help others understand what dificultes might appear during the development. After your commit as been approved, share to your social medias and make a reference of your work so others can learn, help and use as reference.

<h2>Reconnaissance</h2>
<h4>Description</h4>
Reconnaissance consists of techniques that involve adversaries actively or passively gathering information that can be used to support targeting. Such information may include details of the victim organization, infrastructure, or staff/personnel. This information can be leveraged by the adversary to aid in other phases of the adversary lifecycle, such as using gathered information to plan and execute Initial Access, to scope and prioritize post-compromise objectives, or to drive and lead further Reconnaissance efforts.

---
ID | Title | Reference | Example
---|---|---|---
1 | Active Network and Fingerprint Scanner | Link | :x:
2 | Social media profiling and data gathering script | Link | :x:
3 | Dork based OSINT tool | Link | :x:
4 | Website vulnerability scanner | Link | :x:
5 | WHOIS | Link | :x:
6 | DNS subdomain enumeration | Link | :x:
7 | Spearphishing Service | Link | :x:
8 | Victim | Link | :x:
9 | DNS enumeration and reconnaissance tool | Link | :x:
<h5>Notable Projects</h5>

- Project A by X

---
<h2>Resource Development</h2>
<h4>Description</h4>
Resource Development consists of techniques that involve adversaries creating, purchasing, or compromising/stealing resources that can be used to support targeting. Such resources include infrastructure, accounts, or capabilities. These resources can be leveraged by the adversary to aid in other phases of the adversary lifecycle, such as using purchased domains to support Command and Control, email accounts for phishing as a part of Initial Access, or stealing code signing certificates to help with Defense Evasion.

---
ID | Title | Reference | Example
---|---|---|---
10 | Dynamic Website Phishing Tool | Link | :x:
11 | Eamil based phishing spread | Link | :x:
12 | Malware sample creation and analysis | Link | :x:
13 | Replicate a public exploit and use to create a backdoor | Link | :x:
14 | Crafting malicious documents for social engineering attacks | Link | :x:
15 | Wordpress C2 Infrastructure | Link | :x:


<h5>Notable Projects</h5>

- Project A by X

---

<h2>Initial Access</h2>
<h3>Description</h3>
Initial Access consists of techniques that use various entry vectors to gain their initial foothold within a network. Techniques used to gain a foothold include targeted spearphishing and exploiting weaknesses on public-facing web servers. Footholds gained through initial access may allow for continued access, like valid accounts and use of external remote services, or may be limited-use due to changing passwords.

---
ID | Title | Reference | Example
---|---|---|---
16 | Exploiting a vulnerable web application | Link | :x:
17 | Password spraying attack against Active Directory | Link | :x:
18 | Email spear-phishing campaign | Link | :x:
19 | Exploiting misconfigured network services | Link | :x:
20 | USB device-based attack vector development | Link | :x:
21 | Spearphishing Link | Link | :x:

<h5>Notable Projects</h5>

- Project A by X

---

<h2>Execution</h2>
<h3>Description</h3>
Execution consists of techniques that result in adversary-controlled code running on a local or remote system. Techniques that run malicious code are often paired with techniques from all other tactics to achieve broader goals, like exploring a network or stealing data. For example, an adversary might use a remote access tool to run a PowerShell script that does Remote System Discovery.

---
ID | Title | Reference | Example
---|---|---|---
22 | Remote code execution exploit development | Link | :x:
23 | Creating a backdoor using shellcode | Link | :x:
24 | Building a command-line remote administration tool | Link | :x:
25 | Malicious macro development for document-based attacks | Link | :x:
26 | Remote code execution via memory corruption vulnerability | Link | :x:
27 | Command Line Interpreter for C2 | Link | :x:
28 | Cron based execution | Link | :x:

<h5>Notable Projects</h5>

- Project A by X

---

<h2>Persistence</h2>
<h3>Description</h3>
Persistence consists of techniques that adversaries use to keep access to systems across restarts, changed credentials, and other interruptions that could cut off their access. Techniques used for persistence include any access, action, or configuration changes that let them maintain their foothold on systems, such as replacing or hijacking legitimate code or adding startup code.

---
ID | Title | Reference | Example
---|---|---|---
29 | Developing a rootkit for Windows | Link | :x:
30 | Implementing a hidden service in a web server | Link | :x:
31 | Backdooring a legitimate executable | Link | :x:
32 | Creating a scheduled task for persistent access | Link | :x:
33 | Developing a kernel-level rootkit for Linux | Link | :x:
34 | LSASS Driver | Link | :x:
35 | Shortcut modification | Link | :x:

<h5>Notable Projects</h5>

- Project A by X

---

<h2>Privilege Escalation</h2>
<h3>Description</h3>
Privilege Escalation consists of techniques that adversaries use to gain higher-level permissions on a system or network. Adversaries can often enter and explore a network with unprivileged access but require elevated permissions to follow through on their objectives. Common approaches are to take advantage of system weaknesses, misconfigurations, and vulnerabilities. Examples of elevated access include:

- SYSTEM/root level
- local administrator
- user account with admin-like access
- user accounts with access to specific system or perform specific function

These techniques often overlap with Persistence techniques, as OS features that let an adversary persist can execute in an elevated context.

---
ID | Title | Reference | Example
---|---|---|---
36 | Exploiting a local privilege escalation vulnerability | Link | :x:
37 | Password cracking using GPU acceleration | Link | :x:
38 | Windows token manipulation for privilege escalation | Link | :x:
39 | Abusing insecure service configurations | Link | :x:
40 | Exploiting misconfigured sudoers file in Linux | Link | :x:
41 | Bypass UAC | Link | :x:
42 | Startup Itens | Link | :x:

<h5>Notable Projects</h5>

- Project A by X

---

<h2>Defense Evasion</h2>
<h3>Description</h3>
Defense Evasion consists of techniques that adversaries use to avoid detection throughout their compromise. Techniques used for defense evasion include uninstalling/disabling security software or obfuscating/encrypting data and scripts. Adversaries also leverage and abuse trusted processes to hide and masquerade their malware. Other tactics’ techniques are cross-listed here when those techniques include the added benefit of subverting defenses.

---
ID | Title | Reference | Example
---|---|---|---
43 | Developing an anti-virus evasion technique | Link | :x:
44 | Bypassing application whitelisting controls | Link | :x:
45 | Building a fileless malware variant | Link | :x:
46 | Detecting and disabling security products | Link | :x:
47 | Evading network-based intrusion detection systems | Link | :x:
48 | Parent PID spoofing | Link | :x:
49 | Disable Windows Event Logging | Link | :x:
50 | HTML Smuggling | Link | :x:
51 | DLL Injection | Link | :x:
52 | Pass The Hash | Link | :x:

<h5>Notable Projects</h5>

- Project A by X

---

<h2>Credential Access</h2>
<h3>Descrition</h3>
Credential Access consists of techniques for stealing credentials like account names and passwords. Techniques used to get credentials include keylogging or credential dumping. Using legitimate credentials can give adversaries access to systems, make them harder to detect, and provide the opportunity to create more accounts to help achieve their goals.

---
ID | Title | Reference | Example
---|---|---|---
53 | Password brute-forcing tool | Link | :x:
54 | Developing a keylogger for capturing credentials | Link | :x:
55 | Creating a phishing page to harvest login credentials | Link | :x:
56 | Exploiting password reuse across different systems | Link | :x:
57 | Implementing a pass-the-hash attack technique | Link | :x:
58 | OS Credential dumping (/etc/passwd and /etc/shadow) | Link | :x:

<h5>Notable Projects</h5>

- Project A by X

---

<h2>Discovery</h2>
<h3>Description</h3>
Discovery consists of techniques an adversary may use to gain knowledge about the system and internal network. These techniques help adversaries observe the environment and orient themselves before deciding how to act. They also allow adversaries to explore what they can control and what’s around their entry point in order to discover how it could benefit their current objective. Native operating system tools are often used toward this post-compromise information-gathering objective.

---
ID | Title | Reference | Example
---|---|---|---
59 | Network service enumeration tool | Link | :x:
60 | Active Directory enumeration script | Link | :x:
61 | Automated OS and software version detection | Link | :x:
62 | File and directory enumeration on a target system | Link | :x:
63 | Extracting sensitive information from memory dumps | Link | :x:
64 | Virtualization/Sandbox detection | Link | :x:

<h5>Notable Projects</h5>

- Project A by X

---

<h2>Lateral Movement</h2>
<h3>Description</h3>
Lateral Movement consists of techniques that adversaries use to enter and control remote systems on a network. Following through on their primary objective often requires exploring the network to find their target and subsequently gaining access to it. Reaching their objective often involves pivoting through multiple systems and accounts to gain. Adversaries might install their own remote access tools to accomplish Lateral Movement or use legitimate credentials with native network and operating system tools, which may be stealthier.

---
ID | Title | Reference | Example
---|---|---|---
65 | Developing a remote desktop protocol (RDP) brute-forcer | Link | :x:
66 | Creating a malicious PowerShell script for lateral movement | Link | :x:
67 | Implementing a pass-the-ticket attack technique | Link | :x:
68 | Exploiting trust relationships between domains | Link | :x:
69 | Developing a tool for lateral movement through SMB | Link | :x:

<h5>Notable Projects</h5>

- Project A by X

---

<h2>Collection</h2>
<h3>Description</h3>
Collection consists of techniques adversaries may use to gather information and the sources information is collected from that are relevant to following through on the adversary's objectives. Frequently, the next goal after collecting data is to steal (exfiltrate) the data. Common target sources include various drive types, browsers, audio, video, and email. Common collection methods include capturing screenshots and keyboard input.

---
ID | Title | Reference | Example
---|---|---|---
70 | Keylogging and screen capturing tool | Link | :x:
71 | Developing a network packet sniffer | Link | :x:
72 | Implementing a clipboard data stealer | Link | :x:
73 | Building a tool for extracting browser history | Link | :x:
74 | Creating a memory scraper for credit card information | Link | :x:

<h5>Notable Projects</h5>

- Project A by X

---

<h2>Command and Control</h2>
<h3>Description</h3>
Command and Control consists of techniques that adversaries may use to communicate with systems under their control within a victim network. Adversaries commonly attempt to mimic normal, expected traffic to avoid detection. There are many ways an adversary can establish command and control with various levels of stealth depending on the victim’s network structure and defenses.

---
ID | Title | Reference | Example
---|---|---|---
75 | Building a custom command and control (C2) server | Link | :x:
76 | Developing a DNS-based covert channel for C2 communication | Link | :x:
77 | Implementing a reverse shell payload for C2 | Link | :x:
78 | Creating a botnet for command and control purposes | Link | :x:
79 | Developing a convert communication channel using social media platforms | Link | :x:
80 | C2 with multi-stage channels | Link | :x:

<h5>Notable Projects</h5>

- Project A by X

---
<h2>Exfiltration</h2>
<h3>Description</h3>
Exfiltration consists of techniques that adversaries may use to steal data from your network. Once they’ve collected data, adversaries often package it to avoid detection while removing it. This can include compression and encryption. Techniques for getting data out of a target network typically include transferring it over their command and control channel or an alternate channel and may also include putting size limits on the transmission.

---
ID | Title | Reference | Example
---|---|---|---
82 | Building a file transfer tool using various protocols (HTTP, FTP, etc.) | Link | :x:
83 | Developing a steganography tool for hiding data within images | Link | :x:
84 | Implementing a DNS tunneling technique for data exfiltration | Link | :x:
85 | Creating a convert channel for exfiltrating data through email | Link | :x:
86 | Building a custom exfiltration tool using ICMP or DNS | Link | :x:
87 | Exfiltration Over Symmetric Encrypted Non-C2 Protocol | Link | :x:

<h5>Notable Projects</h5>

- Project A by X

---
<h2>Impact</h2>
<h3>Description</h3>
Impact consists of techniques that adversaries use to disrupt availability or compromise integrity by manipulating business and operational processes. Techniques used for impact can include destroying or tampering with data. In some cases, business processes can look fine, but may have been altered to benefit the adversaries’ goals. These techniques might be used by adversaries to follow through on their end goal or to provide cover for a confidentiality breach.

---
ID | Title | Reference | Example
---|---|---|---
88 | Developing a ransomware variant | Link | :x:
89 | Building a destructive wiper malware | Link | :x:
90 | Creating a denial-of-service (DoS) attack tool | Link | :x:
91 | Implementing a privilege-escalation-based destructive attack | Link | :x:
92 | Internal defacement | Link | :x:
93 | Account Access Manipulation or Removal | Link | :x:
94 | Data encryption | Link | :x:
95 | Resource Hijack | Link | :x:
96 | Developing a tool for manipulating industrial control systems (ICS) | Link | :x:
97 | Developing a tool for manipulating industrial control systems (ICS) | Link | :x:
99 | Developing a tool for manipulating industrial control systems (ICS) | Link | :x:
99 | Developing a tool for manipulating industrial control systems (ICS) | Link | :x:
100 | Developing a tool for manipulating industrial control systems (ICS) | Link | :x:

<h5>Notable Projects</h5>

- Project A by X

---
### Guidelines
- If you need to test webtools, use any public vulnerable app like DVWA or DVAA
- All critical tools should be able to rollback the actions (like ransomwares)
- Make a checklist of features of any tool you developed and the resources you used to make it
### Disclaimer
All of those projects should be used inside controled enviorements, do not attemp to use any of those projects to hack, steal, destroy, evade, or any other illegal activities.

### Want to support my work?
[<a href="https://www.buymeacoffee.com/heberjuliok" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>](https://www.buymeacoffee.com/heberjuliok)

### Find me
[<a href="https://www.linkedin.com/in/h%C3%A9ber-j%C3%BAlio-496120190/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin" height="41" width="174"></a>](https://www.linkedin.com/in/h%C3%A9ber-j%C3%BAlio-496120190/)