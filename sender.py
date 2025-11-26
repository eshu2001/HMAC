from hmac_sha256 import sender_process
from shared_pipe import SENDER_FILE, HMAC_FILE

key = "mysecretkey"

print("----- SENDER -----")
message = input("Enter message to send: ")

msg_hash, msg_hmac = sender_process(message, key)

print("\nSHA-256 Hash:", msg_hash)
print("Sender HMAC:", msg_hmac)

with open(SENDER_FILE, "w") as f:
    f.write(message)

with open(HMAC_FILE, "w") as f:
    f.write(msg_hmac)

print("Message sent")
