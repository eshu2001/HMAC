🚀 Project Overview

This project demonstrates how HMAC ensures message integrity and authenticity between a Sender and Receiver, even when an attacker (Mallory) intercepts the message.

The implementation includes:

Pure Python SHA-256 implementation

HMAC construction using ipad (0x36) and opad (0x5C)

Sender → Mallory → Receiver communication flow

Integrity verification using shared secret key

Tampering detection using computed HMAC comparison
----------------------------------------------------------------------------------------------------------------

📂 Project Structure

Src/
 Src/
 ├── code/
 │    ├── hmac_sha256.py
 │    ├── sender.py
 │    ├── receiver.py
 │    ├── mallory.py
 │    └── shared_pipe.py
 ├── logs/
 │    ├── sender_hmac.txt
 │    ├── sender_to_mallory.txt
 │    └── mallory_to_receiver.txt
 └── PPT/
      └── HMAC_Presentation.pptx


📌 HMAC-SHA256 From Scratch — Secure Message Authentication System

A complete from-scratch implementation of:

✔ SHA-256 hashing
✔ HMAC (Hash-based Message Authentication Code)
✔ Message integrity verification
✔ Demonstration of sender, attacker (Mallory), and receiver workflow

This project shows how secure message authentication works without using any external cryptographic libraries - everything is implemented manually using Python.
-----------------------------------------------------------------------------------------------------------------------

🧠 Core Features
🔐 1. SHA-256 From Scratch

Implements message padding

64-round compression function

32-bit word operations

Right rotation, bitwise operations

Follows FIPS-180-4 structure

🔑 2. HMAC-SHA256 Implementation

Block size = 64 bytes

Key normalization (shortened or padded)

ipad = 0x36, opad = 0x5C

HMAC = SHA256(opad || SHA256(ipad || message))

📬 3. Three-Party Message Flow
| Party        | Role                             |
| ------------ | -------------------------------- |
| **Sender**   | Creates message + HMAC           |
| **Mallory**  | Intercepts & optionally tampers  |
| **Receiver** | Computes HMAC & checks integrity |


🔍 4. Message Tampering Detection

Receiver recomputes HMAC → if mismatch → message was modified.
------------------------------------------------------------------------------------------------------------------------

🛠 How It Works
Sender --(Message + HMAC)--> Mallory --(Message*)--> Receiver

Steps:

1. Sender

Inputs a message

Computes:

SHA-256(message)

HMAC(key, message)

Writes data to shared files

2. Mallory (Attacker)

Reads message

Optionally modifies it

Forwards it to Receiver

3. Receiver

Reads message and sender’s HMAC

Computes its own HMAC

Compares → Match = Authentic / No Match = Tampered
----------------------------------------------------------------------------------------------------------------
▶️ Running the Application

Run each script in separate terminals:

Terminal 1 — Sender
py sender.py
Enter a message → it generates hash + HMAC.

Terminal 2 — Mallory
py mallory.py
You can tamper with the message.

Terminal 3 — Receiver
py receiver.py
Receiver verifies:

Computed HMAC

Sender’s HMAC

Reports True/False
----------------------------------------------------------------------------------------------------------------
📘 Source Code Summary
🔹 hmac_sha256.py

Contains your full implementation:

sha256() — hashing function

right_rotate() — rotates 32-bit words

hmac_hash() — HMAC construction

sender_process() — used by sender.py

🔹 sender.py

Takes user input

Computes SHA-256 + HMAC

Stores message & HMAC in shared files

🔹 mallory.py

Acts as an attacker

Intercepts original message

Allows tampering

Forwards final message

🔹 receiver.py

Reads tampered/original message

Computes HMAC

Compares with sender’s HMAC

Detects tampering
--------------------------------------------------------------------------------------------------------
🔐 Security Properties Achieved

✔ Integrity — receiver detects modified messages
✔ Authentication — only sender with key can generate valid HMAC
✔ Keyed Hashing — prevents brute-force hash forgery
-----------------------------------------------------------------------------------------------------------
🧩 Why This Project Matters

This project helps you understand:

How real systems like TLS, JWT, AWS Signature V4, OAuth, API authentication use HMAC

Why raw hashing cannot authenticate messages

How an attacker fails to forge the correct HMAC

It is a perfect demonstration for networking, security, or cryptography assignments.

