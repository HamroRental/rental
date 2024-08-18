import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw
import crud, homepage, search
import tkinter as tk
from tkinter import ttk, font , Canvas, filedialog
from random import randint

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

        self.glass_image = ctk.CTkImage(light_image=Image.open(".\\photos\\white-glass.png"))

        self.search_container = ctk.CTkFrame(self.search_frame, fg_color="#6883AE", width=250, corner_radius=0)
        self.search_container.pack(fill='x', expand=True, padx=10, pady=5)

        self.search_entry_frame = ctk.CTkFrame(self.search_container, fg_color="#6883AE", width=70)
        self.search_entry_frame.pack(fill="x", padx=(1, 0), pady=0)

        self.search_entry = ctk.CTkEntry(self.search_entry_frame, placeholder_text="Rooms, Vehicles, Equipment, Clothes", height=27, border_width=0, corner_radius=0)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(0, 2))

        self.search_button = ctk.CTkButton(self.search_entry_frame, image=self.glass_image, text="", width=70, height=26, fg_color="#6883AE", hover_color="#6883AE", corner_radius=0, command=self.search)
        self.search_button.pack(side="right", fill="x", padx=(2.5, 0))

        icon_size = (30, 30)
        self.bell_image = ctk.CTkImage(light_image=Image.open(".\\photos\\Notification.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.profile_image = ctk.CTkImage(light_image=Image.open(".\\photos\\profile.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.heart_image = ctk.CTkImage(light_image=Image.open(".\\photos\\cart.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)

        self.bell_button = ctk.CTkButton(self.menu_icon_frame, image=self.bell_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.bell_button.pack(side="left", padx=1)
        self.heart_button = ctk.CTkButton(self.menu_icon_frame, image=self.heart_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.heart_button.pack(side="left", padx=1)
        self.profile_button = ctk.CTkButton(self.menu_icon_frame, image=self.profile_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.profile_button.pack(side="left", padx=1)

        self.main_frame = ctk.CTkScrollableFrame(self, orientation='vertical', bg_color='transparent')
        self.main_frame.pack(fill="both", expand=True, padx=(20, 10), pady=1, side="right")

        self.side_frame = ctk.CTkFrame(self, width=300, corner_radius=10, bg_color="transparent", fg_color='transparent')
        self.side_frame.pack(fill='y', side='left', padx=(20, 0), pady=10)

        # Sample data list
        image_path = '.\\photos\\no-profile.png'
        data = [
            {
                'name': 'Kantoor Nepal',
                'email': 'kantoornepal@gmail.com',
                'location': 'Kathmandu',
                'phone': '98073939012',
                'member_since': '2024-01-09'
            }
        ]

        # Add content from data to the side frame
        for item in data:
            # Profile image
            profile_img = Image.open(image_path)
            profile_img = profile_img.resize((100, 100), Image.Resampling.LANCZOS)
            profile_img = ImageTk.PhotoImage(profile_img)

            # Profile image canvas
            canvas = Canvas(self.side_frame, width=120, height=120, bg="#f2f2f2", highlightthickness=0)
            canvas.pack(pady=20)
            canvas.create_oval(10, 10, 110, 110, outline="#2F4D7D", width=4)
            canvas.create_image(60, 60, image=profile_img)
            canvas.image = profile_img

            # Name
            name_label = ctk.CTkLabel(self.side_frame, text=item['name'], font=("Helvetica", 20, 'bold'))
            name_label.pack(pady=(10, 0))

            # Member since
            member_label = ctk.CTkLabel(self.side_frame, text=f"Member Since {item['member_since']}", font=("Helvetica", 12))
            member_label.pack(pady=(5, 15))

            # Email
            email_image = ctk.CTkImage(light_image=Image.open(".\\photos\\email.png").resize((15, 15), Image.Resampling.LANCZOS))
            email_label = ctk.CTkLabel(self.side_frame, text=item['email'], image=email_image, compound="left")
            email_label.pack(anchor="w", padx=20)

            # Location
            location_image = ctk.CTkImage(light_image=Image.open(".\\photos\\location.png").resize((15, 15), Image.Resampling.LANCZOS))
            location_label = ctk.CTkLabel(self.side_frame, text=item['location'], image=location_image, compound="left")
            location_label.pack(anchor="w", padx=20, pady=(5, 0))

            # Phone
            phone_image = ctk.CTkImage(light_image=Image.open(".\\photos\\phone.png").resize((15, 15), Image.Resampling.LANCZOS))
            phone_label = ctk.CTkLabel(self.side_frame, text=item['phone'], image=phone_image, compound="left")
            phone_label.pack(anchor="w", padx=20, pady=(5, 0))
        
    def navigate(self):
        self.destroy()
        new_app = homepage.RentalApp()
        new_app.mainloop()

    # Adding search functionality 
    def search(self):
        search_query = self.search_entry.get().lower()  # Get the search input and convert it to lowercase
        search_results = crud.search_products_by_category(search_query)  # Query the database

        if search_results:
            self.destroy()  # Close the current window
            search_app = search.RentalApp(search_query, search_results)  # Pass search query and results to the search app
            search_app.mainloop()
        else:
            self.destroy()  # Close the current window
            search_app = search.RentalApp(search_query, [])  # Create a new instance with an empty search result
            search_app.label = ctk.CTkLabel(search_app.main_frame, text=f"No results found for category: {search_query}", font=("Helvetica", 18, 'bold'))
            search_app.label.pack(anchor="n", pady=(40, 20))
            search_app.mainloop()

# Run the application
if __name__ == "__main__":
    app = RentalApp()
    app.mainloop()
