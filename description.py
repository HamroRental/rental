import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import crud 
import search
import homepage

# Set the appearance mode of the app
ctk.set_appearance_mode("light")  # Modes: "System" (standard), "light", "dark"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Description(ctk.CTk):
    def __init__(self,product_name, price, product_description, image_path):
        super().__init__()

        self.title("Description")
        self.geometry("1280x750")  # Adjusted to fit more content

        # Create the title bar frame
        self.title_bar = ctk.CTkFrame(self, height=100, fg_color="#2F4D7D", corner_radius=0)
        self.title_bar.pack(fill="x", side="top")

        # Create and place the title label
        self.title_label = ctk.CTkButton(self.title_bar, text="Rent it.", font=("Helvetica", 30, 'bold'), text_color="white", hover_color="#2F4D7D", fg_color = "#2F4D7D", command = self.navigate)
        self.title_label.pack(side="left", padx=10, pady=5)

        # Create a container frame for menu items and icons
        self.menu_icon_frame = ctk.CTkFrame(self.title_bar, fg_color="#2F4D7D", width=50)  # Reduce the width of this frame
        self.menu_icon_frame.pack(side="right", padx=20)

        # Adjust padding in the menu frame to allow more space for the search bar
        self.menu_frame = ctk.CTkFrame(self.title_bar, width = 100, fg_color="#2F4D7D")
        self.menu_frame.pack(side="left", fill="x", expand=True, pady=5, padx=(230, 150))  # Reduce padding to allow more space

        # Create the search bar frame
        self.search_frame = ctk.CTkFrame(self.menu_frame, width=500, fg_color="#2F4D7D")
        self.search_frame.pack(pady=20, padx=10, fill ='x', expand=True)  # Allow the search frame to take up more space

        # Load the magnifying glass image
        self.glass_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\white-glass.png"))

        # Create the search entry with the search button and magnifying glass icon
        self.search_container = ctk.CTkFrame(self.search_frame, fg_color="#6883AE", width=250, corner_radius=5)
        self.search_container.pack(fill = 'x', expand=True, padx=10, pady=5)

        self.search_entry_frame = ctk.CTkFrame(self.search_container, fg_color="#6883AE", width=70, corner_radius=5)
        self.search_entry_frame.pack(fill="x", padx=(1,0), pady=0)

        # Create and place the search entry
        self.search_entry = ctk.CTkEntry(self.search_entry_frame, placeholder_text="Rooms, Vehicles, Equipment, Clothes", height=27, border_width=0, corner_radius=0)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(0,2))

        # Create and place the search button inside the search entry
        self.search_button = ctk.CTkButton(self.search_entry_frame, image=self.glass_image, text="", width=70, height=26, fg_color="#6883AE", hover_color="#6883AE",corner_radius=0, command= self.search)
        self.search_button.pack(side="right", fill = "x", padx=(2.5,0))


        
        # Load the icons with increased size
        icon_size = (30, 30)  # Adjust the size as needed
        self.bell_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\Notification.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.profile_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\profile.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.heart_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\cart.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)

        # Create and place the icon buttons with adjusted width and height
        self.bell_button = ctk.CTkButton(self.menu_icon_frame, image=self.bell_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.bell_button.pack(side="left", padx=1)
        self.heart_button = ctk.CTkButton(self.menu_icon_frame, image=self.heart_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.heart_button.pack(side="left", padx=1)
        self.profile_button = ctk.CTkButton(self.menu_icon_frame, image=self.profile_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.profile_button.pack(side="left", padx=1)

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
        self.add_service_placeholder(self.photo_frame, image_path)

        # Create a frame for the text content on the right side
        self.text_frame = ctk.CTkFrame(self.all_frame, fg_color='transparent')
        self.text_frame.pack(side='left', fill='both', expand=True, padx=20, pady=20)

        # Create and place the title label in the text frame
        self.title_label_main = ctk.CTkLabel(self.text_frame, text=product_name, font=("Helvetica", 30), text_color='black')
        self.title_label_main.pack(anchor='w', pady=(50, 10))  # Adjust pady to add space between title and subtitle

        # Create and place the subtitle label in the text frame
        price = price
        self.subtitle_label = ctk.CTkLabel(self.text_frame, text=f'Rs. {price} Per Day', font=("Helvetica", 20, 'bold'), text_color='#2F4D7D')
        self.subtitle_label.pack(anchor='w', pady=(0, 10))  # Adjust pady to add space between subtitle and the next content

        # Create and place the description text widget in the text frame
        self.description_text = tk.Text(self.text_frame, wrap="word", font=("Helvetica", 16), fg='black', bg='#E5E5E5', height=10, width=60, bd=0, padx=10, pady=10)
        self.description_text.pack(anchor='w', pady=(0, 1))
        self.description_text.insert('1.0', product_description)
        self.description_text.configure(state='disabled')  # Make the text widget read-only

        # Add buttons below the description text
        self.buttons_frame = ctk.CTkFrame(self.text_frame, fg_color="transparent")
        self.buttons_frame.pack(anchor='w', pady=0, padx=10)

        self.rent_button = ctk.CTkButton(self.buttons_frame, text="Rent Now", width=20, corner_radius=25, font=("Helvetica", 14, 'bold'), fg_color="green", hover_color='green')
        self.rent_button.pack(side="left", padx=(0, 10))

        self.wishlist_button = ctk.CTkButton(self.buttons_frame, text="Add to Wishlist", corner_radius=25, font=("Helvetica", 14, 'bold'), fg_color="#2F4D7D", hover_color="#2F4D7D")
        self.wishlist_button.pack(side="left")

    def add_service_placeholder(self,parent,image_path):
        # Load and resize the image using PIL
        image = Image.open(image_path)
        image = image.resize((360, 240), Image.LANCZOS)  # Resize to desired dimensions
        self.ctk_image = ctk.CTkImage(image, size=(300, 250))  # Create CTkImage with the resized image

        # Retain the reference to the image object
        self.service_image = self.ctk_image

        # Create and place the image label
        image_label = ctk.CTkLabel(parent, image=self.service_image, text="")
        image_label.pack(side='left', pady=(0, 10), padx=10)

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

    def navigate(self):
        self.destroy()
        new_app = homepage.RentalApp()
        new_app.mainloop()



if __name__ == "__main__":
    app = Description(product_name="Alpha 7 IV", price="3000", product_description="A high-quality mirrorless camera designed for professionals.", image_path="C:\\Users\\manas\\Documents\\rental\\camera.jpg")
    app.mainloop()
