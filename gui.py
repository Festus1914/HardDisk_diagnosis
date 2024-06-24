import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import json
from diagnostics import diagnose_harddisk

def display_diagnosis():
    try:
        diagnosis = diagnose_harddisk()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, json.dumps(diagnosis, indent=4))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("Hard Disk Health Diagnostics")

# Define colors and font
bg_color = "#f0f0f0"
fg_color = "#333333"
font = ("Helvetica", 10)

# Main frame
main_frame = tk.Frame(root, bg=bg_color)
main_frame.pack(padx=20, pady=20)

# Header label
header_label = tk.Label(main_frame, text="Hard Disk Health Diagnostics", font=("Helvetica", 16, "bold"), bg=bg_color, fg=fg_color)
header_label.pack(pady=(0, 10))

# Run button
btn = tk.Button(main_frame, text="Run Diagnostics", command=display_diagnosis, font=font, bg="#4caf50", fg="white")
btn.pack(pady=(0, 10))

# Result text area
result_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=100, height=30, font=font)
result_text.pack(pady=(0, 10))

# Status bar
status_bar = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W, font=font)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
