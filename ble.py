import os
import time
import subprocess

def clear_terminal():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar_length = 20
    filled_length = int(bar_length * percent / 100)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f"\rProgress: [{bar}] {percent:.1f}%", end="", flush=True)

def scan_devices():
    print("Retrieving paired Bluetooth devices...")
    try:
        result = subprocess.run(["termux-bluetooth-list"], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving devices: {e}")
        return None

    devices = []
    for line in result.stdout.splitlines():
        if "Address" in line:
            address = line.split(": ")[1].strip()
        elif "Name" in line:
            name = line.split(": ")[1].strip()
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

    message = input("Enter the message (filename): ")
    count = int(input("Enter the count: "))

    print("Disclaimer: This script is for educational purposes only. Use responsibly.")
    input("Press Enter to continue...")
    clear_terminal()

    print(f"Sending '{message}' to {device} {count} times...")

    for i in range(count):
        try:
            subprocess.run(["termux-bluetooth-send", "--device", device, "--file", f"/storage/emulated/0/Download/{message}.txt"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error sending message: {e}")
            break
        print_progress_bar(i + 1, count)
        time.sleep(0.5)

    print("\nSpamming completed!")

clear_terminal()
spam_message()
