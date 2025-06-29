# SHA256-Hash-Cracker-using-Pwntools
A minimal Python-based SHA256 hash cracker that uses only the pwntools library and sys module. It attempts to find a matching password for a given SHA256 hash by comparing it against a wordlist. Ideal for CTFs, ethical hacking practice, and understanding password hash verification workflows.
# Features:
Uses only pwntools and sys — no hashlib or external libraries.

Interactive progress output using log.progress().

Accepts SHA256 hash via command-line argument.

Wordlist-based dictionary attack with line-by-line attempts.

Latin-1 decoding support for large password dumps (e.g., rockyou.txt).

# Usage:
```bash
# Install pwntools
pip install pwntools

# Run the hash cracker
python3 sha256pswd.py <sha256_hash>


```bash
# Update wordlist path
nano crack.py

# Run the tool
python3 crack.py e99a18c428cb38d5f260853678922e03abd8334b\

sha256-cracker/
├── crack.py          # Main script
├── gamer.txt         # Wordlist file (you provide)
└── README.md         # Project documentation

