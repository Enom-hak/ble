import os
import sys
import time

def print_disclaimer():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;31;40mDisclaimer: This script is for educational purposes only. Use responsibly.\033[0;37;40m")

def print_progress_bar(progress, total, color="\033[1;31;40m"):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(color + f"\r|{bar}| {percent:.2f}%", end="\r")
    if progress == total:
        print("\033[0;37;40m")  # Reset color

def spam_message(device, message, count):
    print_disclaimer()
    print(f"Sending '{message}' to {device} {count} times...")
    for i in range(count):
        os.system(f"echo '{message}' | festival --tts")
        print_progress_bar(i + 1, count)
        time.sleep(0.5)  # Delay between messages

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 spam_script.py <device> <message> <count>")
        sys.exit(1)

    device = sys.argv[1]
    message = sys.argv[2]
    count = int(sys.argv[3])

    spam_message(device, message, count)
