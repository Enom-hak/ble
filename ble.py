import os
import time
import tkinter as tk
from tkinter import messagebox

def print_progress_bar(progress, total, color="red"):
    percent = 100 * (progress / float(total))
    progress_bar['value'] = percent
    window.update_idletasks()

def spam_message():
    device = device_entry.get()
    message = message_entry.get()
    count = int(count_entry.get())

    messagebox.showwarning("Disclaimer", "This script is for educational purposes only. Use responsibly.")
    
    messagebox.showinfo("Spamming...", f"Sending '{message}' to {device} {count} times...")

    for i in range(count):
        os.system(f"echo '{message}' | festival --tts")
        print_progress_bar(i + 1, count)
        time.sleep(0.5)  # Delay between messages
    
    messagebox.showinfo("Done", "Spamming completed!")

window = tk.Tk()
window.title("Spam Script")

tk.Label(window, text="Device:").pack()
device_entry = tk.Entry(window)
device_entry.pack()

tk.Label(window, text="Message:").pack()
message_entry = tk.Entry(window)
message_entry.pack()

tk.Label(window, text="Count:").pack()
count_entry = tk.Entry(window)
count_entry.pack()

tk.Button(window, text="Start Spamming", command=spam_message).pack()

progress_bar = tk.Progressbar(window, length=200, mode='determinate')
progress_bar.pack()

window.mainloop()
