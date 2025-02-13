import tkinter as tk
from tkinter import messagebox
import cv2

def decrypt():
    # Get the passcode from the user
    pas = pass_entry.get()

    if not pas:
        messagebox.showerror("Input Error", "Passcode is required!")
        return

    with open("password.txt", "r") as f:
        password = f.read().strip()  # Read the stored password

    # Check passcode
    if password != pas:
        messagebox.showerror("Authentication Failed", "Incorrect passcode!")
        return

    img = cv2.imread("encryptedImage.png")  # Load the encrypted image

    with open("msg_length.txt", "r") as f:
        msg_length = int(f.read().strip())  # Read message length

    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    message = ""
    n, m, z = 0, 0, 0

    # Decrypt the message
    for i in range(msg_length):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    messagebox.showinfo("Decrypted Message", f"Decrypted message: {message}")


# Create the main window
root = tk.Tk()
root.title("Decryption")

# Create labels and entries
pass_label = tk.Label(root, text="Enter passcode:")
pass_label.pack(pady=5)

pass_entry = tk.Entry(root, width=40, show="*")
pass_entry.pack(pady=5)

# Create a decrypt button
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack(pady=10)

# Run the GUI
root.mainloop()
