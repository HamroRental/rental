import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

# Set the appearance mode of the app
ctk.set_appearance_mode("light")  # Modes: "System" (standard), "light", "dark"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Description(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Description")
        self.geometry("1280x750")  # Adjusted to fit more content

        # Create the title bar frame
        self.title_bar = ctk.CTkFrame(self, height=100, corner_radius=0, fg_color="#2F4D7D")
        self.title_bar.pack(fill="x", side="top")

        # Create and place the title label
        self.title_label = ctk.CTkLabel(self.title_bar, text="Rent it.", font=("Helvetica", 24, 'bold'), text_color="white")
        self.title_label.pack(side="left", padx=10, pady=10)

        # Create a container frame for menu items and icons
        self.menu_icon_frame = ctk.CTkFrame(self.title_bar, fg_color="#2F4D7D")
        self.menu_icon_frame.pack(side="right", fill="x", expand=True)

        # Create a container frame for the center menu items
        self.menu_frame = ctk.CTkFrame(self.menu_icon_frame, fg_color="#2F4D7D")
        self.menu_frame.pack(side="left", pady=10, padx=420)

        # Create and place the menu items
        self.dashboard_label = ctk.CTkLabel(self.menu_frame, text="Dashboard", font=("Helvetica", 11), text_color="white")
        self.dashboard_label.pack(side="left", padx=10)

        self.categories_label = ctk.CTkLabel(self.menu_frame, text="Our Categories", font=("Helvetica", 11), text_color="white")
        self.categories_label.pack(side="left", padx=10)

        self.profile_label = ctk.CTkLabel(self.menu_frame, text="Profile", font=("Helvetica", 11), text_color="white")
        self.profile_label.pack(side="left", padx=10)

        # Load the icons
        self.bell_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\OneDrive\\Pictures\\Vector.png"))
        self.profile_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\OneDrive\\Pictures\\profile.png"))

        # Create a frame for the right-side icons
        self.icon_frame = ctk.CTkFrame(self.menu_icon_frame, fg_color="#2F4D7D")
        self.icon_frame.pack(side="right", padx=10)

        # Create and place the icon buttons
        self.bell_button = ctk.CTkButton(self.icon_frame, image=self.bell_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.bell_button.pack(side="left", padx=5)
        self.profile_button = ctk.CTkButton(self.icon_frame, image=self.profile_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.profile_button.pack(side="left", padx=5)

        # Create and place the main content
        self.main_frame = ctk.CTkScrollableFrame(self, orientation='vertical')
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Create a frame to have all images and description 
        self.all_frame = ctk.CTkFrame(self.main_frame)
        self.all_frame.pack(fill='both', expand=True, padx=220, pady=20)  # Adjusted padx to center the frame

        # Create and place the photo frame on the left side
        self.photo_frame = ctk.CTkFrame(self.all_frame, corner_radius=10, fg_color='transparent')
        self.photo_frame.pack(side='left', pady=0, padx=0)

        # Add the service placeholder image to the photo frame
        self.add_service_placeholder(self.photo_frame, "C:\\Users\\manas\\OneDrive\\Pictures\\camera.jpg")

        # Create a frame for the text content on the right side
        self.text_frame = ctk.CTkFrame(self.all_frame, fg_color='transparent')
        self.text_frame.pack(side='left', fill='both', expand=True, padx=20, pady=20)

        # Create and place the title label in the text frame
        self.title_label_main = ctk.CTkLabel(self.text_frame, text="Sony a6400 On Rent", font=("Helvetica", 30), text_color='black')
        self.title_label_main.pack(anchor='w', pady=(50, 10))  # Adjust pady to add space between title and subtitle

        # Create and place the subtitle label in the text frame
        self.subtitle_label = ctk.CTkLabel(self.text_frame, text='Rs. 1000 Per Day', font=("Helvetica", 20, 'bold'), text_color='#2F4D7D')
        self.subtitle_label.pack(anchor='w', pady=(0, 10))  # Adjust pady to add space between subtitle and the next content

        # Create and place the description text widget in the text frame
        self.description_text = tk.Text(self.text_frame, wrap="word", font=("Helvetica", 16), fg='black', bg='#E5E5E5', height=10, width=60, bd=0, padx=10, pady=10)
        self.description_text.pack(anchor='w', pady=(0, 1))
        self.description_text.insert(tk.END, "Camera Cage for Sony Alpha a6500 a6400 a6300 a6000 ILCE-6500 ILCE-6400 ILCE-6300 ILCE-6000 4K Digital Mirrorless Camera Built-in Cold Shoe, The cage features a variety of 1/4\"-20 and 3/8\"-16 threaded accessory mounting holes. At the top left of the cage is a cold shoe mount for attaching a mic or various other accessories. With the camera housed inside the cage, you can easily access the SD card, battery compartment, and all camera buttons and ports.")
        self.description_text.configure(state='disabled')  # Make the text widget read-only

        # Add buttons below the description text
        self.buttons_frame = ctk.CTkFrame(self.text_frame, fg_color="transparent")
        self.buttons_frame.pack(anchor='w', pady=0, padx=10)

        self.rent_button = ctk.CTkButton(self.buttons_frame, text="Rent Now", width=20, corner_radius=25, font=("Helvetica", 14, 'bold'), fg_color="green", hover_color='green')
        self.rent_button.pack(side="left", padx=(0, 10))

        self.wishlist_button = ctk.CTkButton(self.buttons_frame, text="Add to Wishlist", corner_radius=25, font=("Helvetica", 14, 'bold'), fg_color="#2F4D7D", hover_color="#2F4D7D")
        self.wishlist_button.pack(side="left")

    def add_service_placeholder(self, parent, image_path):
        # Load and resize the image using PIL
        image = Image.open(image_path)
        image = image.resize((360, 240), Image.LANCZOS)  # Resize to desired dimensions
        self.ctk_image = ctk.CTkImage(image, size=(300, 250))  # Create CTkImage with the resized image

        # Retain the reference to the image object
        self.service_image = self.ctk_image

        # Create and place the image label
        image_label = ctk.CTkLabel(parent, image=self.service_image, text="")
        image_label.pack(side='left', pady=(0, 10), padx=10)

if __name__ == "__main__":
    app = Description()
    app.mainloop()
