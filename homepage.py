import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import search
import crud, profile_1




# Set the appearance mode of the app
ctk.set_appearance_mode("light")  # Modes: "System" (standard), "light", "dark"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class RentalApp(ctk.CTk):
    def __init__(self):
        super().__init__()
 
        self.title("Rent it.")
        self.geometry("1280x750")  # Adjusted to fit more content

        # Create the title bar frame
        self.title_bar = ctk.CTkFrame(self, height=375, corner_radius=0, fg_color="#2F4D7D")
        self.title_bar.pack(fill="x", side="top")

        # Create and place the title label
        self.title_label = ctk.CTkLabel(self.title_bar, text="Rent it.", font=("Helvetica", 30, 'bold'), text_color="white")
        self.title_label.pack(side="left", padx = 20, pady = 20, anchor ='n')

        # Create a container frame for the menu icons
        self.icon_frame = ctk.CTkFrame(self.title_bar, fg_color="#2F4D7D")
        self.icon_frame.pack(side="right", padx=10, pady=20, anchor = 'n')

        # Load the icons with increased size
        icon_size = (40, 40)  # Adjust the size as needed
        self.bell_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\photos\\Notification.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.profile_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\photos\\profile.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.heart_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\photos\\cart.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)

        # Create and place the icon buttons with adjusted width and height
        self.bell_button = ctk.CTkButton(self.icon_frame, image=self.bell_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.bell_button.pack(side="left", padx=1)
        self.cart_button = ctk.CTkButton(self.icon_frame, image=self.heart_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D', command = self.navigate_to_cart)
        self.cart_button.pack(side="left", padx=1)
        self.profile_button = ctk.CTkButton(self.icon_frame, image=self.profile_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D', command = self.navigate_to_profile)
        self.profile_button.pack(side="left", padx=1)


        # Create and place the title label in the main content
        self.title_label_main = ctk.CTkLabel(self.title_bar, text="Rent anything, anywhere", font=("Inter", 40, 'bold'), text_color='white')
        self.title_label_main.pack(pady=(100,2), padx =(100,50))

        # Create the search bar frame
        self.search_frame = ctk.CTkFrame(self.title_bar, width = 500, fg_color="#2F4D7D")
        self.search_frame.pack(pady=(20,70), padx=(100,50), fill = 'x')

        # Create the search entry with the search button and magnifying glass icon
        self.search_container = ctk.CTkFrame(self.search_frame, fg_color="#FFFFFF", width = 500, corner_radius=0)
        self.search_container.pack(pady=10, padx=30, fill="x", expand=True)

        self.search_entry_frame = ctk.CTkFrame(self.search_container, fg_color="#FFFFFF", width = 500)
        self.search_entry_frame.pack(fill="x", expand=True, padx=10, pady=5)

        # Load the magnifying glass image
        self.glass_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\photos\\glass.png"))

        # Create and place the magnifying glass label inside the search entry
        self.glass_label = ctk.CTkLabel(self.search_entry_frame, image=self.glass_image, text="", width=25, height=20, fg_color="#FFFFFF")
        self.glass_label.pack(side="left", padx=10)

        # Create and place the search entry
        self.search_entry = ctk.CTkEntry(self.search_entry_frame, placeholder_text="Rooms, Vehicles, Equipment, Clothes", height=25, border_width=0)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=5)

        # Create and place the search button inside the search entry
        self.search_button = ctk.CTkButton(self.search_entry_frame, text="Search", width=70, height=25,fg_color="#2F4D7D", corner_radius=0, command=self.search)
        self.search_button.pack(side="right", padx=10)

        # Create and place the main content
        self.main_frame = ctk.CTkScrollableFrame(self, orientation='vertical', fg_color='transparent')
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Create and place the category frame
        self.category_label = ctk.CTkLabel(self.main_frame, text="Explore Our Categories", font=("Helvetica", 18, 'bold'), text_color="#2F4D7D")
        self.category_label.pack(anchor="w", pady=(30,5), padx= 40)  # anchor="w" aligns it to the left


        self.category_frame = ctk.CTkFrame(self.main_frame, corner_radius=10, fg_color='transparent')
        self.category_frame.pack(pady=10, padx=20, fill="x")

        # Initialize the category_images list
        self.category_images = []

        #add palceholders for Explore Our Categories 
        self.create_category_placeholder(self.category_frame, "Luxury","C:\\Users\\manas\\Documents\\rental\\photos\\luxury.jpg")
        self.create_category_placeholder(self.category_frame, "Shoes", "C:\\Users\\manas\\Documents\\rental\\photos\\shoes.jpeg")
        self.create_category_placeholder(self.category_frame, "Cars", "C:\\Users\\manas\\Documents\\rental\\photos\\car.jpg")
        self.create_category_placeholder(self.category_frame, "Room", "C:\\Users\\manas\\Documents\\rental\\photos\\rent.png")

        # Add trending services section
        self.trending_label = ctk.CTkLabel(self.main_frame, text="Trending Services", font=("Helvetica", 18, 'bold'), text_color="#2F4D7D")
        self.trending_label.pack(anchor="w", pady=(70,5), padx=40)

        self.trending_frame = ctk.CTkFrame(self.main_frame, corner_radius=10, fg_color='transparent')
        self.trending_frame.pack(pady=10, padx=20, fill="x")

        #add placeholders for Trending services 
        self.add_service_placeholder(self.trending_frame, "Kurtha Set", "Rs.200 Per Day", "C:\\Users\\manas\\Documents\\rental\\photos\\kurtha.png")
        self.add_service_placeholder(self.trending_frame, "2BHK Flat", "Rs.400 Per Day", "C:\\Users\\manas\\Documents\\rental\\photos\\flat.png")
        self.add_service_placeholder(self.trending_frame, "Sony a6400 ","Rs.1000 Per Day", "C:\\Users\\manas\\Documents\\rental\\photos\\camera.jpg")
        self.add_service_placeholder(self.trending_frame, "3BHK Apartment","Rs.500 Per Day", "C:\\Users\\manas\\Documents\\rental\\photos\\flat1.jpg")


        # Add recommended for you section
        self.recommended_label = ctk.CTkLabel(self.main_frame, text="Recommended for you", font=("Helvetica", 18, 'bold'), text_color="#2F4D7D")
        self.recommended_label.pack(anchor="w", pady=(70,5), padx= 40)

        self.recommended_frame = ctk.CTkFrame(self.main_frame, corner_radius=10, fg_color='transparent')
        self.recommended_frame.pack(pady=10, padx=20, fill="x")

        # Add placeholders for recommended services
        self.add_service_placeholder(self.recommended_frame, "It Ends with us", "Rs.10 Per Day", "C:\\Users\\manas\\Documents\\rental\\photos\\book.jpg")
        self.add_service_placeholder(self.recommended_frame, "Daura Suruwal On Rent", "Rs.200 Per Day", "C:\\Users\\manas\\Documents\\rental\\photos\\daura.jpg")
        self.add_service_placeholder(self.recommended_frame, "Nike Dunk High", "Rs.100 Per Day", "C:\\Users\\manas\\Documents\\rental\\photos\\nike.jpg")
        self.add_service_placeholder(self.recommended_frame, "Red Comodo On Rent", "Rs.10,000 Per Day", "C:\\Users\\manas\\Documents\\rental\\photos\\bigcamera.jpg")

    
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
        image_button = ctk.CTkButton(frame, image=self.ctk_image, text="", fg_color='transparent', hover_color='#F2F2F2', command=lambda: self.search(text))
        image_button.pack(pady=10)

        # Place the text below the image
        label_text = ctk.CTkLabel(frame, text=text, text_color="black")
        label_text.pack(side="bottom", pady=5)



    def add_service_placeholder(self, parent, title, price, image_path):

        # formatting the image_path as in the database # Replace single backslashes with double backslashes
        formatted_path = image_path.replace("\\", "/")

        # Load and resize the image using PIL
        image = Image.open(image_path)
        image = image.resize((180, 120), Image.Resampling.LANCZOS)  # Resize to desired dimensions
        self.ctk_image = ctk.CTkImage(image, size=(250, 230))  # Create CTkImage with the resized image

        # Create the frame for the image and text
        service_frame = ctk.CTkFrame(parent, width=200, height=200, corner_radius=10, fg_color="white")
        service_frame.pack(padx=10, pady=10, side="left")

        # Create and place the image label
        image_label = ctk.CTkLabel(service_frame, image=self.ctk_image, text="")
        image_label.pack(pady=0.5)

        # Create and place the text button 
        title_button = ctk.CTkButton(service_frame, text=title, text_color="black", font=("Helvetica", 18, 'bold'), fg_color="transparent", hover_color="white", command=lambda: self.button_clicked(crud.get_product_id_by_image(formatted_path)))
        title_button.pack(side="top", pady=(5,1), anchor = 'w')

        price_label = ctk.CTkLabel(service_frame, text=price, font=("Helvetica", 12, 'bold'), text_color='#2F4D7D')
        price_label.pack(side = 'left', padx = 22.5)

    def search(self, category=None):
        if category:
            search_query = category.lower()
        else:
            search_query = self.search_entry.get().lower()  # Get the search input and convert it to lowercase

        search_results = crud.search_products_by_category(search_query)  # Query the database

        if search_results:
            if category:
                search_query = len(search_results)
                self.destroy()  # Close the current window
                search_app = search.RentalApp(search_query, search_results)  # Pass search query and results to the search app
                search_app.mainloop()

            self.destroy()  # Close the current window
            search_app = search.RentalApp(search_query, search_results)  # Pass search query and results to the search app
            search_app.mainloop()
        else:
            self.destroy()  # Close the current window
            search_app = search.RentalApp(search_query, [])  # Create a new instance with an empty search result
            search_app.label = ctk.CTkLabel(search_app.main_frame, text=f"No results found for category: {search_query}", font=("Helvetica", 18, 'bold'))
            search_app.label.pack(anchor="n", pady=(40, 20))
            search_app.mainloop()

            
    def open_link(self, title):
        print(f"Opening details for: {title}")

    def button_clicked(self, product_id):
        product_name = crud.get_product_name(product_id)
        price = crud.get_price(product_id)
        product_description = crud.get_description(product_id)
        image_path = crud.get_product_image(product_id) or "C:\\Users\\manas\\Documents\\rental\\photos\\no-image.png"
        category = crud.get_category(product_id)
        images = crud.get_product_images(product_id)
        # Initialize and open the new page with these details
        import description
        self.destroy()
        new_page = description.Description(product_id,product_name, price, product_description, image_path, category, images)
        new_page.mainloop()

    def navigate_to_profile(self):
        self.destroy()
        profile_app = profile_1.RentalApp()
        profile_app.create_dashboard()
        profile_app.on_click(profile_app.dashboard_button, profile_app.home_hover_image, profile_app.create_dashboard)
        profile_app.mainloop()

    def navigate_to_cart(self):
        self.destroy()
        profile_app = profile_1.RentalApp()
        profile_app.create_dashboard()
        profile_app.on_click(profile_app.cart_button, profile_app.cart_hover_image, profile_app.create_cart)
        profile_app.mainloop()


if __name__ == "__main__":
    app = RentalApp()
    app.mainloop()
