import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import crud
import login

ctk.set_appearance_mode("light")  
ctk.set_default_color_theme("dark-blue")  

class Login(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry("1280x750")  

        # Title Bar Frame 
        self.title_bar = ctk.CTkFrame(self, height=70, fg_color="#2F4D7D", corner_radius=0)
        self.title_bar.propagate(False)
        self.title_bar.pack(fill="x", side="top")
        self.title_label = ctk.CTkButton(self.title_bar, text="Rent it.", font=("Helvetica", 30, 'bold'), text_color="white", hover_color="#2F4D7D", fg_color="#2F4D7D")
        self.title_label.pack(side="left", padx=10, pady=5)

        # Menu Frame  
        self.menu_icon_frame = ctk.CTkFrame(self.title_bar, fg_color="#2F4D7D", width=50)  
        self.menu_icon_frame.pack(side="right", padx=20)

        login_button = ctk.CTkButton(self.menu_icon_frame, text="  login   ", fg_color='white', text_color='#2F4D7D', width=40, hover_color='white', font=('Helvetica', 12, 'bold'), command=self.navigate_to_login)
        login_button.pack(pady=(10, 5))

        self.menu_frame = ctk.CTkFrame(self.title_bar, width=100, fg_color="#2F4D7D", corner_radius=30)
        self.menu_frame.pack(side="left", fill="x", expand=True, pady=5, padx=(230, 150)) 

        # Main Frame
        login_frame = ctk.CTkFrame(self, fg_color='transparent', corner_radius=40, height=800)
        login_frame.propagate(False)
        login_frame.pack(fill="both", padx=150, pady=50, expand=True)

        # Left Frame (Image)
        left_frame = ctk.CTkFrame(login_frame, fg_color='#FDFEFF', corner_radius=30, height=800)
        left_frame.grid(row=0, column=0, sticky="nsew", pady=10, rowspan=2)

        # Loading Image
        image = Image.open(".\\photos\\signup.png")  
        image = image.resize((500, 500), Image.Resampling.LANCZOS)  
        image_tk = ImageTk.PhotoImage(image)

        image_label = ctk.CTkLabel(left_frame, image=image_tk, text="")
        image_label.pack(expand=True, pady=20)

        # Right Frame (Details)
        self.right_frame = ctk.CTkFrame(login_frame, corner_radius=10, fg_color="#2F4D7D", width=150, height=800)
        self.right_frame.propagate(False)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=(20, 0), pady=10, rowspan=2)

        # Title and Subtitle
        title_label = ctk.CTkLabel(self.right_frame, text="Sign Up", font=("Arial", 24, "bold"), text_color="white")
        title_label.pack(pady=(40, 5))

        subtitle_label = ctk.CTkLabel(self.right_frame, text="Create account to continue", font=("Arial", 14), text_color='white')
        subtitle_label.pack(pady=(5, 10))

        # All entries and buttons 
        self.username_entry = ctk.CTkEntry(self.right_frame, placeholder_text="Username", corner_radius=20, height=35, width=40)
        username_label = ctk.CTkLabel(self.right_frame, text="Full Name", font=("Arial", 14), text_color='white')
        username_label.pack(pady=(5, 0), fill='x', padx=(10, 240))
        self.username_entry.pack(pady=(1, 5), fill="x", padx=(60, 90))

        self.email_entry = ctk.CTkEntry(self.right_frame, placeholder_text="Email", corner_radius=20, height=35, width=40)
        email_label = ctk.CTkLabel(self.right_frame, text="Email", font=("Arial", 14), text_color='white')
        email_label.pack(pady=(5, 1), fill='x', padx=(10, 260))
        self.email_entry.pack(pady=(1, 5), fill="x", padx=(60, 90))

        self.phone_entry = ctk.CTkEntry(self.right_frame, placeholder_text="Phone", corner_radius=20, height=35, width=40)
        phone_label = ctk.CTkLabel(self.right_frame, text="Phone", font=("Arial", 14), text_color='white')
        phone_label.pack(pady=(10, 0), fill='x', padx=(10, 260))
        self.phone_entry.pack(pady=(5, 10), fill="x", padx=(60, 90))

        self.password_entry = ctk.CTkEntry(self.right_frame, placeholder_text="Set password", show="*", corner_radius=20, height=35, width=40)
        password_label = ctk.CTkLabel(self.right_frame, text="Set Password", font=("Arial", 14), text_color='white')
        password_label.pack(pady=(10, 0), fill='x', padx=(30, 230))
        self.password_entry.pack(pady=(5, 1), fill="x", padx=(60, 90))

        register_button = ctk.CTkButton(self.right_frame, text="Register", font=("Arial", 14, "bold"), fg_color="white", text_color="#2F4D7D", hover_color="lightgray", corner_radius=20, command=self.on_register_click)
        register_button.pack(side="bottom", pady=(10, 20), padx=(10, 70))

        # Radio Buttons 
        radio_frame = ctk.CTkFrame(self.right_frame, fg_color='transparent', height=10)
        radio_frame.pack(side="bottom", anchor="sw", pady=(1, 10), padx=65)

        self.radio_var = tk.StringVar(value="user")  

        radio_button1 = ctk.CTkRadioButton(radio_frame, text="User", variable=self.radio_var, value="user", text_color='white', border_color='gray')
        radio_button1.pack(side="left", padx=5)

        radio_button2 = ctk.CTkRadioButton(radio_frame, text="Provider", variable=self.radio_var, value="provider", text_color='white', border_color='gray')
        radio_button2.pack(side="left", padx=5)

        login_frame.grid_columnconfigure(0, weight=1)
        login_frame.grid_columnconfigure(1, weight=1)

        login_frame.grid_rowconfigure(0, weight=1)
        login_frame.grid_rowconfigure(1, weight=1)
        login_frame.grid_rowconfigure(3, weight=1)
        login_frame.grid_rowconfigure(4, weight=1)
        login_frame.grid_rowconfigure(5, weight=1)

    def navigate_to_login(self):
        self.destroy()
        app = login.Login()
        app.mainloop()

    def on_register_click(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        password = self.password_entry.get()
        user_type = self.radio_var.get()

        if not username or not email or not phone or not password:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        if user_type not in ["user", "provider"]:
            messagebox.showerror("Input Error", "Please select a user type.")
            return
        
        if crud.check_username_exists(username):
            messagebox.showerror('Already have  an account', 'Username already exists')
            return 

        self.add_profile(username, email, phone, password, user_type)

    def add_profile(self, fullname, email, phone, password, user_type):
        print(f"Full Name: {fullname}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Password: {password}")
        print(f"User Type: {user_type}")
        crud.add_user(user_type, fullname,fullname,email,password,phone)
        messagebox.showinfo('sucess','you have sucessfully created your account')
        self.navigate_to_login()
        
        

if __name__ == "__main__":
    app = Login()
    app.mainloop()
