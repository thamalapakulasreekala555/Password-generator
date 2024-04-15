import tkinter as tk
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    password_length = int(length_entry.get())
    generated_password = generate_password(password_length)
    
    # Update the label with the generated password
    password_label.config(text=f"Generated Password: {generated_password}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Password Generator")

# Entry field for password length
length_label = tk.Label(root, text="Enter the length of the password:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Button to generate and display password
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack()

# Label to display the generated password
password_label = tk.Label(root, text="")
password_label.pack()

# Run the Tkinter event loop
root.mainloop()