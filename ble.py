import os
import time
import subprocess

def clear_terminal():
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Unix/Linux/macOS
        _ = os.system('clear')

def print_progress_bar(progress, total, color="red"):
    percent = 100 * (progress / float(total))
    bar_length = 20
    filled_length = int(bar_length * percent / 100)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f"\rProgress: [{bar}] {percent:.1f}%", end="", flush=True)

def spam_message():
    import bluetooth

# Perform Bluetooth discovery
nearby_devices = bluetooth.discover_devices(lookup_names=True)

# Print the MAC addresses of discovered devices
for addr, name in nearby_devices:
    print(f"Device Name: {name}, MAC Address: {addr}")
    
    device = input("Enter the device (MAC address): ")
    message = input("Enter the message: ")
    count = int(input("Enter the count: "))

    print("Disclaimer: This script is for educational purposes only. Use responsibly.")
    input("Press Enter to continue...")
    clear_terminal()

    print(f"Sending '{message}' to {device} {count} times...")

    for i in range(count):
        subprocess.run(["termux-bluetooth-send", f"--device='{device}'", f"--file='/storage/emulated/0/Download/{message}.txt'"])
        print_progress_bar(i + 1, count)
        time.sleep(0.5)
    
    print("\nSpamming completed!")

clear_terminal()
spam_message()
