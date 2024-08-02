import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw


# Set the appearance mode of the app
ctk.set_appearance_mode("light")  # Modes: "System" (standard), "light", "dark"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class RentalApp(ctk.CTk):
    def __init__(self):
        super().__init__()
 
        self.title("Rent it.")
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
        self.bell_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\Vector.png"))
        self.profile_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\profile.png"))

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

        # Create and place the title label in the main content
        self.title_label_main = ctk.CTkLabel(self.main_frame, text="Rent anything, anywhere", font=("Helvetica", 24, 'bold'), text_color='#2F4D7D')
        self.title_label_main.pack(pady=20)

        # Create the search bar frame
        self.search_frame = ctk.CTkFrame(self.main_frame, corner_radius=10, fg_color="#e0e0e0")
        self.search_frame.pack(pady=10, padx=20, fill="x")

        # Create the search entry with the search button and magnifying glass icon
        self.search_container = ctk.CTkFrame(self.search_frame, fg_color="#FFFFFF", corner_radius=30)
        self.search_container.pack(pady=10, padx=10, fill="x", expand=True)

        self.search_entry_frame = ctk.CTkFrame(self.search_container, fg_color="#FFFFFF")
        self.search_entry_frame.pack(fill="x", expand=True, padx=10, pady=5)

        # Load the magnifying glass image
        self.glass_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\glass.png"))

        # Create and place the magnifying glass label inside the search entry
        self.glass_label = ctk.CTkLabel(self.search_entry_frame, image=self.glass_image, text="", width=25, height=20, fg_color="#FFFFFF")
        self.glass_label.pack(side="left", padx=10)

        # Create and place the search entry
        self.search_entry = ctk.CTkEntry(self.search_entry_frame, placeholder_text="Rooms, Vehicles, Equipment, Clothes", height=25, corner_radius=15, border_width=0)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=5)

        # Create and place the search button inside the search entry
        self.search_button = ctk.CTkButton(self.search_entry_frame, text="Search", width=70, height=25, corner_radius=15, fg_color="#2F4D7D", command=self.search)
        self.search_button.pack(side="right", padx=10)

        # Create and place the category frame
        self.category_label = ctk.CTkLabel(self.main_frame, text="Explore Our Categories", font=("Helvetica", 18, 'bold'), text_color="#2F4D7D")
        self.category_label.pack(anchor="w", pady=(50,5), padx= 40)  # anchor="w" aligns it to the left

        self.category_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.category_frame.pack(pady=10, padx=20, fill="x")

        # Initialize the category_images list
        self.category_images = []

        #add palceholders for Explore Our Categories 
        self.create_category_placeholder(self.category_frame, "Luxury","C:\\Users\\manas\\Documents\\rental\\luxury.jpg")
        self.create_category_placeholder(self.category_frame, "shoes", "C:\\Users\\manas\\Documents\\rental\\shoes.jpeg")
        self.create_category_placeholder(self.category_frame, "Cars", "C:\\Users\\manas\\Documents\\rental\\car.jpg")
        self.create_category_placeholder(self.category_frame, "Room", "C:\\Users\\manas\\Documents\\rental\\rent.png")

        # Add trending services section
        self.trending_label = ctk.CTkLabel(self.main_frame, text="Trending Services", font=("Helvetica", 18, 'bold'), text_color="#2F4D7D")
        self.trending_label.pack(anchor="w", pady=(70,5), padx=40)

        self.trending_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.trending_frame.pack(pady=10, padx=20, fill="x")

        #add placeholders for Trending services 
        self.add_service_placeholder(self.trending_frame, "Kurtha Set", "New Collection", "Rs.200 Per Day", "C:\\Users\\manas\\Documents\\rental\\kurtha.png")
        self.add_service_placeholder(self.trending_frame, "2BHK Flat", "New Collection", "Rs.200 Per Day", "C:\\Users\\manas\\Documents\\rental\\flat.png")
        self.add_service_placeholder(self.trending_frame, "Sony a6400 ", "Camera Zone", "Rs.1000 Per Day", "C:\\Users\\manas\\Documents\\rental\\camera.jpg")
        self.add_service_placeholder(self.trending_frame, "3BHK Apartment", "New Collection", "Rs.200 Per Day", "C:\\Users\\manas\\Documents\\rental\\flat1.jpg")


        # Add recommended for you section
        self.recommended_label = ctk.CTkLabel(self.main_frame, text="Recommended for you", font=("Helvetica", 18, 'bold'), text_color="#2F4D7D")
        self.recommended_label.pack(anchor="w", pady=(70,5), padx= 40)

        self.recommended_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.recommended_frame.pack(pady=10, padx=20, fill="x")

        # Add placeholders for recommended services
        self.add_service_placeholder(self.recommended_frame, "It Ends with us", "Books Mandala", "Rs.10 Per Day", "C:\\Users\\manas\\Documents\\rental\\book.jpg")
        self.add_service_placeholder(self.recommended_frame, "Daura Suruwal On Rent", "Kapda Pasal", "Rs.200 Per Day", "C:\\Users\\manas\\Documents\\rental\\daura.jpg")
        self.add_service_placeholder(self.recommended_frame, "Nike Dunk High", "Shoes Hub", "Rs.100 Per Day", "C:\\Users\\manas\\Documents\\rental\\nike.jpg")
        self.add_service_placeholder(self.recommended_frame, "Red Comodo On Rent", "Filmy World", "Rs.10,000 Per Day", "C:\\Users\\manas\\Documents\\rental\\bigcamera.jpg")

    
    def create_category_placeholder(self, parent, text, image_path):
        frame = ctk.CTkFrame(parent, width=253, height=258, corner_radius=10, fg_color='transparent')
        frame.pack(side="left", padx=10, pady=10)
        
        # Load and place the image
        image = Image.open(image_path)
        image = image.resize((250, 250), Image.Resampling.LANCZOS)

        # Create a circular mask
        mask = Image.new('L', (250, 250), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 250, 250), fill=255)

        # Apply the mask to the image
        image = image.convert("RGBA")
        image.putalpha(mask)

        self.ctk_image = ctk.CTkImage(image, size = (260, 200))  
        self.category_images.append(self.ctk_image)  # Keep a reference to the image

        # Create and place the label with the image
        image_button = ctk.CTkButton(frame, image=self.ctk_image, text="", fg_color='transparent', hover_color='#E5E5E5')
        image_button.pack(pady=10)

        # Place the text below the image
        label_text = ctk.CTkLabel(frame, text=text, text_color="black")
        label_text.pack(side="bottom", pady=5)


    def add_service_placeholder(self, parent, title, subtitle, price, image_path):
        # Load and resize the image using PIL
        image = Image.open(image_path)
        image = image.resize((180, 120), Image.Resampling.LANCZOS)  # Resize to desired dimensions
        self.ctk_image = ctk.CTkImage(image, size=(250, 230))  # Create CTkImage with the resized image

        # Create the frame for the image and text
        service_frame = ctk.CTkFrame(parent, width=200, height=200, corner_radius=10)
        service_frame.pack(padx=10, pady=10, side="left")

        # Create and place the image label
        image_label = ctk.CTkLabel(service_frame, image=self.ctk_image, text="")
        image_label.pack(pady=10)

        # Create and place the text button 
        title_button = ctk.CTkButton(service_frame, text=title, text_color="black", font=("Helvetica", 18, 'bold'), fg_color="transparent", hover_color="#D9D9D9", command=self.button_clicked)
        title_button.pack(side="top", pady=5)

        subtitle_label = ctk.CTkLabel(service_frame, text=subtitle, font=("Helvetica", 12))
        subtitle_label.pack()

        price_label = ctk.CTkLabel(service_frame, text=price, font=("Helvetica", 12, 'bold'), text_color='#2F4D7D')
        price_label.pack()

    def search(self):
        # Define the search functionality
        print(f"Searching for: {self.search_entry.get()}")

    def open_link(self, title):
        print(f"Opening details for: {title}")

    def button_clicked(self):
        print('button clicked')
        import description
        new_page = description.Description()
        new_page.mainloop()

if __name__ == "__main__":
    app = RentalApp()
    app.mainloop()
