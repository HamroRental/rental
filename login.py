import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageOps
import crud 
from tkinter import messagebox
import register, homepage, admin_dashboard

# Set the appearance mode of the app
ctk.set_appearance_mode("light")  # Modes: "System" (standard), "light", "dark"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Login(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry("1280x750")  # Adjusted to fit more content

        # Create the title bar frame
        self.title_bar = ctk.CTkFrame(self, height=70, fg_color="#2F4D7D", corner_radius=0)
        self.title_bar.propagate(False)
        self.title_bar.pack(fill="x", side="top")

        # Create and place the title label
        self.title_label = ctk.CTkButton(self.title_bar, text="Rent it.", font=("Helvetica", 30, 'bold'), text_color="white", hover_color="#2F4D7D", fg_color = "#2F4D7D")
        self.title_label.pack(side="left", padx=10, pady=5)

        # Create a container frame for menu items and icons
        self.menu_icon_frame = ctk.CTkFrame(self.title_bar, fg_color="#2F4D7D", width=50)  # Reduce the width of this frame
        self.menu_icon_frame.pack(side="right", padx=20)

        # Login Button
        register_button = ctk.CTkButton(self.menu_icon_frame, text="Register", fg_color='white', text_color='#2F4D7D', width =30, hover_color='white', font = ('Helvetica', 12, 'bold'), command = self.navigate_to_register)
        register_button.pack(pady=(10,5))


        # Adjust padding in the menu frame to allow more space for the search bar
        self.menu_frame = ctk.CTkFrame(self.title_bar, width = 100, fg_color="#2F4D7D", corner_radius=30)
        self.menu_frame.pack(side="left", fill="x", expand=True, pady=5, padx=(230, 150))  # Reduce padding to allow more space

        # Main Frame
        login_frame = ctk.CTkFrame(self, fg_color='transparent', corner_radius=40, height = 300)
        login_frame.pack(fill="both", padx = 150, pady =50)

        # Left Frame (Image)
        left_frame = ctk.CTkFrame(login_frame, fg_color='#FDFEFF', corner_radius=30)
        left_frame.grid(row=0, column=0, sticky="nsew", pady = 10)

        # Load and display the image
        image = Image.open(".\\photos\\login.png")  # Replace with your image path
        image = image.resize((400, 600), Image.Resampling.LANCZOS)  # Adjust size as needed
        image_tk = ImageTk.PhotoImage(image)

        image_label = ctk.CTkLabel(left_frame, image=image_tk, text="")
        image_label.pack(expand=True, pady = 20)

        # Right Frame (Details)
        right_frame = ctk.CTkFrame(login_frame, corner_radius=10, fg_color="#2F4D7D", width = 150)
        right_frame.propagate(False)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=(20,0), pady=10)

        # Title and Subtitle
        title_label = ctk.CTkLabel(right_frame, text="Welcome", font=("Arial", 24, "bold"), text_color="white")
        title_label.pack(pady=(50, 5))

        subtitle_label = ctk.CTkLabel(right_frame, text="Login to your account to continue", font=("Arial", 14), text_color='white')
        subtitle_label.pack(pady=(5, 20))

        Username_label = ctk.CTkLabel(right_frame,text="Sign in to your account", font=("Arial", 14), text_color='white')
        Username_label.pack(pady = (10,5), fill ='x', padx = (20,170))

        # Username Entry
        self.username_entry = ctk.CTkEntry(right_frame, placeholder_text="Username", corner_radius=20, height =35, width = 40)
        self.username_entry.pack(pady=10, fill="x", padx = (50,100))

        # Password Entry
        self.password_entry = ctk.CTkEntry(right_frame, placeholder_text="Password", show="*", corner_radius=20, height =35, width = 40)
        self.password_entry.pack(pady=10, fill="x", padx = (50,100))

        # Forgot Password Label
        forgot_password_label = ctk.CTkLabel(right_frame, text="forget password?", font=("Arial", 12), fg_color=None, text_color='white')
        forgot_password_label.pack(pady=(5,10), padx = (90,5))

        # Login Button
        login_button = ctk.CTkButton(right_frame, text="Login", fg_color='white', text_color='#2F4D7D', width =10, hover_color='white', command=self.check)
        login_button.pack(pady=(10,5), fill="x", padx = (140,180))

        # Configure grid for responsiveness
        login_frame.grid_columnconfigure(0, weight=1)
        login_frame.grid_columnconfigure(1, weight=1)

    def navigate_to_register(self):
        self.destroy()
        app = register.Login()
        app.mainloop()

    def check(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        valid, role = crud.check_user_credentials(username, password)
        
        if valid:
            if role =='provider':
                self.destroy()
                app= admin_dashboard.RentalApp()
                app.mainloop()
            else:
                self.destroy()
                app = homepage.RentalApp()
                app.mainloop()

        else:
            # Show error message
            messagebox.showerror("Login Error", "Invalid username or password. Please try again.")

if __name__ == "__main__":
    app = Login()
    app.mainloop()
