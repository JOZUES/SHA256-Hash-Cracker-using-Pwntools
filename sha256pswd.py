import sys
from pwn import log
from pwnlib.util.fiddling import sha256sumhex

if len(sys.argv) != 2:
    print("Invalid argument!")
    print(">> {} <sha256sum>".format(sys.argv[0]))
    exit()

wanted_hash = sys.argv[1]
password_file = "/path/to/the/game/gamer.txt"  # Change this to your wordlist path
attempts = 0

with log.progress(f"Attempting to crack: {wanted_hash}") as p:
    try:
        with open(password_file, "r", encoding="latin-1") as password_list:
            for password in password_list:
                password = password.strip()
                hashed = sha256sumhex(password.encode("latin-1"))

                p.status(f"[{attempts}] {password} → {hashed}")

                if hashed == wanted_hash:
                    p.success(f"Password found after {attempts} attempts: '{password}'")
                    exit()

                attempts += 1

            p.failure(f"Password not found after {attempts} attempts.")
    except FileNotFoundError:
        print(f"[!] File not found: {password_file}")
