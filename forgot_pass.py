import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import crud
from tkinter import messagebox
import register, homepage, admin_dashboard, login

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

class ForgotPassword(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Forgot Password")
        self.geometry("1280x750")

        self.title_bar = ctk.CTkFrame(self, height=70, fg_color="#2F4D7D", corner_radius=0)
        self.title_bar.propagate(False)
        self.title_bar.pack(fill="x", side="top")

        self.title_label = ctk.CTkButton(self.title_bar, text="Rent it.", font=("Helvetica", 30, 'bold'), text_color="white", hover_color="#2F4D7D", fg_color="#2F4D7D")
        self.title_label.pack(side="left", padx=10, pady=5)

        self.menu_icon_frame = ctk.CTkFrame(self.title_bar, fg_color="#2F4D7D", width=50)
        self.menu_icon_frame.pack(side="right", padx=20)

        register_button = ctk.CTkButton(self.menu_icon_frame, text="Register", fg_color='white', text_color='#2F4D7D', width=30, hover_color='white', font=('Helvetica', 12, 'bold'), command=self.navigate_to_register)
        register_button.pack(pady=(10,5))

        self.menu_frame = ctk.CTkFrame(self.title_bar, width=100, fg_color="#2F4D7D", corner_radius=30)
        self.menu_frame.pack(side="left", fill="x", expand=True, pady=5, padx=(230, 150))

        forgot_password_frame = ctk.CTkFrame(self, fg_color='transparent', corner_radius=40, height=300)
        forgot_password_frame.pack(fill="both", padx=150, pady=50)

        left_frame = ctk.CTkFrame(forgot_password_frame, fg_color='#FDFEFF', corner_radius=30)
        left_frame.grid(row=0, column=0, sticky="nsew", pady=10)

        image = Image.open(".\\photos\\forgot.png")
        image = image.resize((550, 600), Image.Resampling.LANCZOS)
        image_tk = ImageTk.PhotoImage(image)

        image_label = ctk.CTkLabel(left_frame, image=image_tk, text="")
        image_label.pack(expand=True, pady=20)

        right_frame = ctk.CTkFrame(forgot_password_frame, corner_radius=10, fg_color="#2F4D7D", width=150)
        right_frame.propagate(False)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=(20,0), pady=10)

        title_label = ctk.CTkLabel(right_frame, text="Forgot\nYour Password?", font=("Arial", 24, "bold"), text_color="white", anchor="w", justify="left")
        title_label.pack(pady=(50, 5), padx=(5, 50))

        self.username_entry = ctk.CTkEntry(right_frame, placeholder_text="Enter Username", corner_radius=20, height=35, width=40)
        self.username_entry.pack(pady=(20, 10), fill="x", padx=(50, 90))

        self.new_password_entry = ctk.CTkEntry(right_frame, placeholder_text="New Password", show="*", corner_radius=20, height=35, width=40)
        self.new_password_entry.pack(pady=(10, 10), fill="x", padx=(50, 90))

        self.confirm_password_entry = ctk.CTkEntry(right_frame, placeholder_text="Confirm Password", show="*", corner_radius=20, height=35, width=40)
        self.confirm_password_entry.pack(pady=10, fill="x", padx=(50, 90))

        reset_password_button = ctk.CTkButton(right_frame, text="Reset Password", fg_color='white', text_color='#2F4D7D', width=50, hover_color='white', command=self.reset_password)
        reset_password_button.pack(pady=(20,5), fill="x", padx=(110,140))

        back_to_signin_label = ctk.CTkButton(right_frame, text="Back to Sign in", fg_color='transparent', text_color='white', hover_color='#2F4D7D', command=self.navigate_to_login)
        back_to_signin_label.pack(pady=(5,10), padx=(50,75))

        forgot_password_frame.grid_columnconfigure(0, weight=1)
        forgot_password_frame.grid_columnconfigure(1, weight=1)

    def navigate_to_register(self):
        self.destroy()
        app = register.Login()
        app.mainloop()

    def navigate_to_login(self):
        self.destroy()
        app = login.Login()
        app.mainloop()

    def reset_password(self):
        username = self.username_entry.get()
        if not crud.check_username_exists(username):
            messagebox.showerror("Error", "Invalid username. Please try again.")
            return

        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if new_password == confirm_password:
            crud.update_user_password(username, new_password)
            messagebox.showinfo("Success", "Password reset successfully.")
            self.navigate_to_login()
        else:
            messagebox.showerror("Error", "Passwords do not match. Please try again.")

if __name__ == "__main__":
    app = ForgotPassword()
    app.mainloop()
