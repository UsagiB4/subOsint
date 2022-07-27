# subOsent ![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)
_______________________
Sub OSINT aka **subOsint** is a tool that finds live subdomains from a given list. It also finds *domain-specific* **technologies** using [python-wappalizer](https://pypi.org/project/python-Wappalyzer/)

### How to use
________________________
1. First run
    
    `pip install -r requirement.txt`

2. Then put your subdomain list into the *subdomains.txt* file

3. After that run

    `python3 subosint.py`

> This will generate a ***.txt*** file called **liveDomains.txt** containing the live subdomains and other status.
