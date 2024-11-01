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

def scan_devices():
    print("Scanning for nearby Bluetooth devices...")
    result = subprocess.run(["termux-bluetooth-scan"], capture_output=True, text=True)
    devices = []

    for line in result.stdout.splitlines():
        if "Address" in line:
            address = line.split(": ")[1]
        elif "Name" in line:
            name = line.split(": ")[1]
            devices.append((name, address))
    
    if not devices:
        print("No devices found.")
        return None

    print("\nFound devices:")
    for i, (name, address) in enumerate(devices, start=1):
        print(f"{i}. {name} - {address}")
    
    while True:
        try:
            choice = int(input("Select a device by number: "))
            if 1 <= choice <= len(devices):
                return devices[choice - 1][1]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")

def spam_message():
    device = scan_devices()
    if not device:
        print("No device selected. Exiting.")
        return

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
