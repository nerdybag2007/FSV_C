import random
import time
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"

clear()

print("Initializing Quantum Neural Network...")
time.sleep(1)

for i in range(101):
    print(f"\rLoading AI Core: {i}%", end="")
    time.sleep(0.03)

print("\n")
time.sleep(1)

targets = [
    "NASA Database",
    "Military Satellite",
    "Encrypted Mainframe",
    "Quantum Server",
    "Government Records"
]

target = random.choice(targets)

print(f"Target Locked: {target}")
time.sleep(1)

print("\nDecrypting Security Layers...\n")

for _ in range(50):
    line = "".join(random.choice(chars) for _ in range(60))
    print(line)
    time.sleep(0.03)

print("\nPassword Hash Located\n")
time.sleep(1)

password = "".join(random.choice(chars) for _ in range(12))

guess = ["_"] * len(password)

for i in range(len(password)):
    for _ in range(10):
        guess[i] = random.choice(chars)
        print("\rCracking: " + "".join(guess), end="")
        time.sleep(0.05)

    guess[i] = password[i]

print("\n")
print(f"\nPassword Cracked: {password}")
time.sleep(1)

print("\nAccess Level: ROOT")
time.sleep(1)

print("Bypassing Firewall...")
time.sleep(2)

print("\nACCESS GRANTED")
print("WELCOME ADMIN")