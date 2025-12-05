import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Centralized Tabs with Rounded Buttons")
root.geometry("400x300")

# Create a style to customize the look
style = ttk.Style(root)

# Apply the 'clam' theme for a modern look
style.theme_use('clam')

# Style for rounded buttons
style.configure("RoundedButton.TButton",
                padding=6,
                relief="flat",
                background="#4CAF50",
                foreground="white",
                font=("Arial", 12, "bold"),
                borderwidth=0)
style.map("RoundedButton.TButton",
          background=[("active", "#45A049")])

# Create a Notebook widget (tabs)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Create frames for each tab
user_tab = ttk.Frame(notebook)
moderator_tab = ttk.Frame(notebook)

# Add frames to the notebook
notebook.add(user_tab, text="User")
notebook.add(moderator_tab, text="Moderator")

# Center layout for User tab
user_login_btn = ttk.Button(user_tab, text="Login", style="RoundedButton.TButton")
user_signup_btn = ttk.Button(user_tab, text="Signup", style="RoundedButton.TButton")

user_login_btn.pack(pady=10)
user_signup_btn.pack(pady=10)

# Center layout for Moderator tab
moderator_login_btn = ttk.Button(moderator_tab, text="Login", style="RoundedButton.TButton")
moderator_login_btn.pack(pady=10)

# Run the application
root.mainloop()
