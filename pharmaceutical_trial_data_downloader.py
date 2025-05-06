import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def download_files():
    date = date_entry.get()
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        status_label.config(text="❌ Invalid date format. Use YYYY-MM-DD.")
        return

    status_label.config(text="🔄 Downloading and validating files...")
    # Simulated process
    root.after(2000, lambda: status_label.config(text=f"✅ Files for {date} processed successfully."))

# Create main window
root = tk.Tk()
root.title("Pharmaceutical Trial Data Downloader")
root.geometry("400x200")
root.resizable(False, False)

# Date entry
tk.Label(root, text="Enter Date (YYYY-MM-DD):").pack(pady=10)
date_entry = tk.Entry(root, width=25)
date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))
date_entry.pack()

# Download button
tk.Button(root, text="Download", command=download_files).pack(pady=10)

# Status label
status_label = tk.Label(root, text="", fg="blue")
status_label.pack(pady=10)

# Run GUI
root.mainloop()
