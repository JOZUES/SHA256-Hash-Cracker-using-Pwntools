
# SHA256 Hash Cracker Using Pwntools

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Pwntools](https://img.shields.io/badge/Powered%20by-pwntools-orange)](https://docs.pwntools.com/en/stable/)

A minimal and fast SHA256 hash cracker written in Python using **only** `pwntools` and `sys`. This script attempts to find a plaintext password that matches a given SHA256 hash using a wordlist file.

---

##  Features

-  **No `hashlib` used** — fully implemented with `pwntools` only
-  Real-time progress logging with `log.progress()`
-  Supports large wordlists like `rockyou.txt` (with `latin-1` encoding)
-  Simple, fast, and ideal for **CTF & educational use**

---

##  Usage

###  Prerequisites

Install `pwntools`:
```bash
pip install pwntools

python3 sha256pswd.py <sha256_hash>

python3 sha256pswd.py e99a18c428cb38d5f260853678922e03abd8334b


password_file = "/path/to/your/wordlist.txt"

exit
```
### Directory Structure

sha256-cracker/
├── crack.py          # Main script
├── gamer.txt         # Wordlist file (you provide)
└── README.md         # Project documentation
### Disclaimer
This tool is intended solely for educational and ethical hacking purposes.
Do not use it on systems or hashes that you do not own or have explicit permission to test.

### License
This project is licensed under the MIT License.
See the LICENSE file for details.

### Author
Developed by JOZUES
Feel free to fork, contribute, and star  the repo!



