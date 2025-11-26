from shared_pipe import SENDER_FILE, MALLORY_FILE

print("----- MALLORY (ATTACKER) -----")

with open(SENDER_FILE, "r") as f:
    intercepted = f.read()

print("\nMessage Received from Sender:", intercepted)

choice = input("\nDo you want to tamper the message? (Y/N): ").strip().upper()

if choice == "Y":
    tampered = input("Enter new (tampered) message: ")
    final_msg = tampered
else:
    final_msg = intercepted

# Forward message to receiver
with open(MALLORY_FILE, "w") as f:
    f.write(final_msg)

print("\nForwarded message to Receiver...")
