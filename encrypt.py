import tkinter as tk
from tkinter import messagebox
import cv2
import os

# Function to encrypt the message
def encrypt():
    msg = message_entry.get()
    password = pass_entry.get()

    if not msg or not password:
        messagebox.showerror("Input Error", "Message and password are required!")
        return

    img = cv2.imread("mypic.png")

    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    m, n, z = 0, 0, 0
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite("encryptedImage.png", img)
    os.system("start encryptedImage.png")

    with open("password.txt", "w") as f:
        f.write(password)

    with open("msg_length.txt", "w") as f:
        f.write(str(len(msg)))

    messagebox.showinfo("Success", "Message encrypted successfully!")


# Create the main window
root = tk.Tk()
root.title("Encryption")
root.geometry("400x300")
root.config(bg="#f2f2f2")  # Light grey background

# Header label
header_label = tk.Label(root, text="Message Encryption", font=("Helvetica", 16, "bold"), bg="#f2f2f2", fg="#333")
header_label.pack(pady=20)

# Message input label
message_label = tk.Label(root, text="Enter secret message:", font=("Arial", 12), bg="#f2f2f2", fg="#555")
message_label.pack(pady=5)

# Message input entry
message_entry = tk.Entry(root, width=40, font=("Arial", 12), bd=2, relief="solid", borderwidth=2)
message_entry.pack(pady=5)

# Passcode input label
pass_label = tk.Label(root, text="Enter passcode:", font=("Arial", 12), bg="#f2f2f2", fg="#555")
pass_label.pack(pady=5)

# Passcode input entry
pass_entry = tk.Entry(root, width=40, font=("Arial", 12), bd=2, relief="solid", borderwidth=2, show="*")
pass_entry.pack(pady=5)

# Encrypt button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="solid", width=20)
encrypt_button.pack(pady=20)

# Run the GUI
root.mainloop()
