import tkinter as tk
from password_checker import check_password_strength
from password_generator import generate_password
from hashing import hash_password

USERNAME = "admin"
PASSWORD = "admin123"

def login():
    if username_entry.get() == USERNAME and password_entry.get() == PASSWORD:
        open_analyzer()
    else:
        result_label.config(text="Invalid Login", fg="red")

def open_analyzer():
    win = tk.Toplevel(root)
    win.configure(bg="#111827")
    win.title("Password Strength Analyzer")
    win.geometry("350x300")

    tk.Label(
    win,
    text="Password Strength Analyzer",
    font=("Arial", 14, "bold"),
    fg="#00ffcc",
    bg="#111827"
).pack(pady=10)
    tk.Label(win, text="Enter Password:", bg="#111827", fg="#00ffcc").pack()
    entry = tk.Entry(win, show="*")
    entry.pack(pady=5)

    output = tk.Label(win, text="", justify="left", bg="#111827", fg="#00ffcc")
    output.pack(pady=10)

    def check():
        pwd = entry.get()

        result = check_password_strength(pwd)
        text = "Strength: " + result

        if result != "Strong Password":
            text += "\nSuggested: " + generate_password()

        text += "\nEncrypted: " + str(hash_password(pwd))

        output.config(text=text)

    tk.Button(win, text="Check Password", command=check).pack(pady=5)
    tk.Button(win, text="Exit", command=win.destroy).pack(pady=5)

root = tk.Tk()
root.configure(bg="#0f172a")
root.title("Password Security Application")
root.geometry("300x250")

tk.Label(
    root,
    text="Cyber Security Login",
    font=("Arial", 16, "bold"),
    fg="#00ffcc",
    bg="#0f172a"
).pack(pady=10)

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(
    root,
    text="Login",
    bg="#00ffcc",
    fg="black",
    font=("Arial", 10, "bold"),
    command=login
).pack(pady=10)

result_label = tk.Label(root, text="", bg="#0f172a", fg="#00ffcc")
result_label.pack()

root.mainloop()