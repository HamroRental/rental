import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import crud, homepage, search

# Set the appearance mode of the app
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

class RentalApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rent it.")
        self.geometry("1280x750")

        # Track the active button
        self.active_button = None

        # Create the title bar frame
        self.title_bar = ctk.CTkFrame(self, height=100, fg_color="#2F4D7D", corner_radius=0)
        self.title_bar.pack(fill="x", side="top")

        self.title_button = ctk.CTkButton(self.title_bar, text="Rent it.", font=("Helvetica", 30, 'bold'), text_color="white", hover_color="#2F4D7D", fg_color="#2F4D7D", command=self.navigate)
        self.title_button.pack(side="left", padx=10, pady=5)

        self.menu_icon_frame = ctk.CTkFrame(self.title_bar, fg_color="#2F4D7D", width=50)
        self.menu_icon_frame.pack(side="right", padx=20)

        self.menu_frame = ctk.CTkFrame(self.title_bar, width=100, fg_color="#2F4D7D")
        self.menu_frame.pack(side="left", fill="x", expand=True, pady=5, padx=(230, 150))

        self.search_frame = ctk.CTkFrame(self.menu_frame, width=500, fg_color="#2F4D7D")
        self.search_frame.pack(pady=20, padx=10, fill='x', expand=True)

        self.glass_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\photos\\white-glass.png"))

        self.search_container = ctk.CTkFrame(self.search_frame, fg_color="#6883AE", width=250, corner_radius=0)
        self.search_container.pack(fill='x', expand=True, padx=10, pady=5)

        self.search_entry_frame = ctk.CTkFrame(self.search_container, fg_color="#6883AE", width=70)
        self.search_entry_frame.pack(fill="x", padx=(1, 0), pady=0)

        self.search_entry = ctk.CTkEntry(self.search_entry_frame, placeholder_text="Rooms, Vehicles, Equipment, Clothes", height=27, border_width=0, corner_radius=0)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(0, 2))

        self.search_button = ctk.CTkButton(self.search_entry_frame, image=self.glass_image, text="", width=70, height=26, fg_color="#6883AE", hover_color="#6883AE", corner_radius=0, command=self.search)
        self.search_button.pack(side="right", fill="x", padx=(2.5, 0))

        icon_size = (30, 30)
        self.bell_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\photos\\Notification.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.profile_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\photos\\profile.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.heart_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\photos\\cart.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)

        self.bell_button = ctk.CTkButton(self.menu_icon_frame, image=self.bell_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.bell_button.pack(side="left", padx=1)
        self.heart_button = ctk.CTkButton(self.menu_icon_frame, image=self.heart_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.heart_button.pack(side="left", padx=1)
        self.profile_button = ctk.CTkButton(self.menu_icon_frame, image=self.profile_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.profile_button.pack(side="left", padx=1)

        self.main_frame = ctk.CTkScrollableFrame(self, orientation='vertical', bg_color='transparent')
        self.main_frame.pack(fill="both", expand=True, padx=(20, 10), pady=20, side="right")

        self.side_frame = ctk.CTkFrame(self, width=300, corner_radius=10, bg_color="transparent", fg_color='transparent')
        self.side_frame.pack(fill='y', side='left', padx=(20, 0), pady=20)

        self.home_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\photos\\home.png"), size=(20, 20))
        self.home_hover_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\photos\\home1.png"), size=(20, 20))
        self.cart_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\photos\\cart2.png"), size=(20, 20))
        self.cart_hover_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\photos\\cart2.png"), size=(20, 20))
        self.settings_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\photos\\wheel.png"), size=(20, 20))
        self.logout_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\photos\\logout.png"), size=(20, 20))

        self.dashboard_button = ctk.CTkButton(
            self.side_frame,
            text="Dashboard",
            image=self.home_image,
            compound="left",
            text_color='#97A8C3',
            font=("Helvetica", 12, 'bold'),
            fg_color='#F2F2F2',
            height=50,
            width=180,
            anchor='w',
            command=lambda: self.on_click(self.dashboard_button, self.home_hover_image, self.create_dashboard)
        )
        self.dashboard_button.pack(anchor="w", padx=(20, 30), pady=(20, 2))

        self.dashboard_button.bind("<Enter>", lambda e: self.on_enter(self.dashboard_button, self.home_hover_image))
        self.dashboard_button.bind("<Leave>", lambda e: self.on_leave(self.dashboard_button, self.home_image))

        self.cart_button = ctk.CTkButton(
            self.side_frame,
            text="My Cart",
            image=self.cart_image,
            compound="left",
            text_color='#97A8C3',
            font=("Helvetica", 12, 'bold'),
            fg_color='#F2F2F2',
            hover_color='#2F4D7D',
            height=50,
            width=180,
            anchor='w',
            command=lambda: self.on_click(self.cart_button, self.cart_hover_image, self.create_cart)
        )
        self.cart_button.pack(anchor="w", padx=(20, 30), pady=(2, 5))

        self.cart_button.bind("<Enter>", lambda e: self.on_enter(self.cart_button, self.cart_hover_image))
        self.cart_button.bind("<Leave>", lambda e: self.on_leave(self.cart_button, self.cart_image))

        self.logout_button = ctk.CTkButton(
            self.side_frame,
            text="Log out",
            image=self.logout_image,
            compound="left",
            text_color='#97A8C3',
            font=("Helvetica", 12, 'bold'),
            fg_color='#F2F2F2',
            hover_color='#2F4D7D',
            height=50,
            width=180,
            anchor='w',
            command=lambda: self.on_click(self.logout_button, self.logout_image)
        )
        self.logout_button.pack(anchor="w", padx=(20, 30), pady=(5, 0), side = 'bottom')

        self.settings_button = ctk.CTkButton(
            self.side_frame,
            text="Settings",
            image=self.settings_image,
            compound="left",
            text_color='#97A8C3',
            font=("Helvetica", 12, 'bold'),
            fg_color='#F2F2F2',
            hover_color='#2F4D7D',
            height=50,
            width=180,
            anchor='w',
            command=lambda: self.on_click(self.settings_button, self.settings_image, self.create_settings)
        )
        self.settings_button.pack(anchor="w", padx=(20, 30), pady=(20, 0), side='bottom')

    def on_enter(self, button, hover_image):
        if self.active_button != button:
            button.configure(image=hover_image, text_color="white", fg_color='#2F4D7D')

    def on_leave(self, button, image):
        if self.active_button != button:
            button.configure(image=image, text_color='#97A8C3', fg_color='#F2F2F2')

    def on_click(self, button, hover_image, callback=None):
        if self.active_button:
            self.active_button.configure(fg_color='#F2F2F2', text_color='#97A8C3')
            self.active_button.bind("<Enter>", lambda e: self.on_enter(self.active_button, hover_image))
            self.active_button.bind("<Leave>", lambda e: self.on_leave(self.active_button, hover_image))

        self.active_button = button
        self.active_button.configure(fg_color="#2F4D7D", text_color="white")
        self.active_button.unbind("<Enter>")
        self.active_button.unbind("<Leave>")

        if callback:
            callback()

    def create_dashboard(self):
        # Clear the current contents of the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create the dashboard layout in the main frame
        title_label = ctk.CTkLabel(self.main_frame, text="Dashboard", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=10)

        # Additional content can be added here
        # For example, you can add buttons, labels, etc., to the main_frame
        # that matches your second screenshot design

    def create_cart(self):
        # Clear the current contents of the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create the dashboard layout in the main frame
        title_label = ctk.CTkLabel(self.main_frame, text="My cart", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=10)

        # Additional content can be added here
        # For example, you can add buttons, labels, etc., to the main_frame
        # that matches your second screenshot design

    def create_settings(self):
        # Clear the current contents of the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create the dashboard layout in the main frame
        title_label = ctk.CTkLabel(self.main_frame, text="Settings", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=10)

        # Additional content can be added here
        # For example, you can add buttons, labels, etc., to the main_frame
        # that matches your second screenshot design

    def navigate(self):
        print("Button clicked!")

    def search(self):
        search_term = self.search_entry.get()
        print(f"Searching for {search_term}...")

# Run the application
if __name__ == "__main__":
    app = RentalApp()
    app.mainloop()
