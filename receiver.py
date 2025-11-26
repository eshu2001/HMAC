from hmac_sha256 import hmac_hash
from shared_pipe import MALLORY_FILE, HMAC_FILE

key = "mysecretkey"

print("----- RECEIVER -----")

with open(MALLORY_FILE, "r") as f:
    received_msg = f.read()

print("\nMessage Received:", received_msg)


with open(HMAC_FILE, "r") as f:
    sender_hmac = f.read()


computed_hmac = hmac_hash(key.encode(), received_msg.encode()).hex()

print("Receiver Computed HMAC:", computed_hmac)

if computed_hmac == sender_hmac:
    print("\nMatch? True")
    print("Message from sender ✔️")
else:
    print("\nMatch? False")
    print("❌ Message was TAMPERED")
