import tkinter as tk

class VotingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Blockchain Voting System")
        self.geometry("400x300")

        self.login_frame = LoginFrame(self)
        self.vote_frame = VoteFrame(self)
        self.result_frame = ResultFrame(self)

        self.login_frame.pack()
        self.current_frame = self.login_frame

    def show_login(self):
        self.current_frame.pack_forget()
        self.login_frame.pack()
        self.current_frame = self.login_frame

    def show_vote(self):
        self.current_frame.pack_forget()
        self.vote_frame.pack()
        self.current_frame = self.vote_frame

    def show_result(self):
        self.current_frame.pack_forget()
        self.result_frame.pack()
        self.current_frame = self.result_frame

class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Add login UI components here

class VoteFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Add voting UI components here

class ResultFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Add result UI components here

if __name__ == "__main__":
    app = VotingApp()
    app.mainloop()
