import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Positioned Notebook in Tkinter")
root.geometry("400x300")

# Create a Notebook widget (tab widget)
notebook = ttk.Notebook(root)

# Set geometry with place() to specify coordinates and size
notebook.place(x=70, y=70, width=261, height=191)

# Create frames for each tab
user_tab = ttk.Frame(notebook)
moderator_tab = ttk.Frame(notebook)

# Add frames to the notebook
notebook.add(user_tab, text="User")
notebook.add(moderator_tab, text="Moderator")

# Add buttons to User tab
user_login_btn = ttk.Button(user_tab, text="Login")
user_signup_btn = ttk.Button(user_tab, text="Signup")

# Center buttons in User tab
user_login_btn.pack(pady=10)
user_signup_btn.pack(pady=10)

# Add button to Moderator tab
moderator_login_btn = ttk.Button(moderator_tab, text="Login")
moderator_login_btn.pack(pady=10)

# Run the application
root.mainloop()
