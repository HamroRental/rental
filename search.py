import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import crud

# Set the appearance mode of the app
ctk.set_appearance_mode("light")  # Modes: "System" (standard), "light", "dark"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class RentalApp(ctk.CTk):
    def __init__(self, search_query = None, search_results =None):
        super().__init__()

        self.title("Rent it.")
        self.geometry("1280x750")  # Adjusted to fit more content

        # Create the title bar frame
        self.title_bar = ctk.CTkFrame(self, height=100, fg_color="#2F4D7D", corner_radius=0)
        self.title_bar.pack(fill="x", side="top")

        # Create and place the title label
        self.title_label = ctk.CTkLabel(self.title_bar, text="Rent it.", font=("Helvetica", 30, 'bold'), text_color="white")
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
        self.search_container = ctk.CTkFrame(self.search_frame, fg_color="#6883AE", width=250, corner_radius=0)
        self.search_container.pack(fill = 'x', expand=True, padx=10, pady=5)

        self.search_entry_frame = ctk.CTkFrame(self.search_container, fg_color="#6883AE", width=70)
        self.search_entry_frame.pack(fill="x", padx=(1,0), pady=0)

        # Create and place the search entry
        self.search_entry = ctk.CTkEntry(self.search_entry_frame, placeholder_text="Rooms, Vehicles, Equipment, Clothes", height=27, border_width=0, corner_radius=0)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(0,2))

        # Create and place the search button inside the search entry
        self.search_button = ctk.CTkButton(self.search_entry_frame, image=self.glass_image, text="", width=70, height=26, fg_color="#6883AE", hover_color="#6883AE",corner_radius=0, command=self.search)
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
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20, side="right")

        # Create the side filter frame
        self.side_frame = ctk.CTkFrame(self, width=300, corner_radius=10, bg_color="#e0e0e0")
        self.side_frame.pack(fill='y', side='left', padx=(20, 0), pady=20)


        # Add filter options to the side frame
        self.filter_label = ctk.CTkLabel(self.side_frame, text="Filters Options", font=("Helvetica", 16, 'bold'))
        self.filter_label.pack(anchor="w", padx=10, pady=(10, 20))

        self.sort_by_label = ctk.CTkLabel(self.side_frame, text="Sort by:", font=("Helvetica", 14))
        self.sort_by_label.pack(anchor="w", padx=20)

        self.sort_var = tk.StringVar(value="Relevance")
        self.relevance_radio = ctk.CTkRadioButton(self.side_frame, text="Relevance", variable=self.sort_var, value="Relevance")
        self.relevance_radio.pack(anchor="w", padx=40, pady=5)

        self.high_low_radio = ctk.CTkRadioButton(self.side_frame, text="Price (High - Low)", variable=self.sort_var, value="Price (High - Low)")
        self.high_low_radio.pack(anchor="w", padx=40, pady=5)

        self.low_high_radio = ctk.CTkRadioButton(self.side_frame, text="Price (Low - High)", variable=self.sort_var, value="Price (Low - High)")
        self.low_high_radio.pack(anchor="w", padx=40, pady=5)

        self.best_match_radio = ctk.CTkRadioButton(self.side_frame, text="Best Match", variable=self.sort_var, value="Best Match")
        self.best_match_radio.pack(anchor="w", padx=40, pady=5)

        # Adding a title label for the search results
        if search_query:
            self.title_label_main = ctk.CTkLabel(self.main_frame, text=f"Search results for: {search_query}", font=("Helvetica", 18, 'bold'))
            self.title_label_main.pack(anchor = 'w', padx = 20, pady=(20, 30))

        # Displaying the search results
        if search_results:
            row_frame = None
            products_in_row = 0

            for i,(product_name, price, image_path) in enumerate(search_results):
                if products_in_row == 0:
                    # Create a new row frame when starting a new row
                    row_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
                    row_frame.pack(fill="x", padx=20, pady=10)

                self.add_service_placeholder(row_frame, product_name, f"Rs.{price} Per Day", image_path)

                products_in_row += 1

                # Reset after adding 3 products in a row
                if products_in_row >= 3:
                    products_in_row = 0

    def button_clicked(self, product_id):
        product_name = crud.get_product_name(product_id)
        price = crud.get_price(product_id)
        product_description = crud.get_description(product_id)
        image_path = crud.get_product_image(product_id) or "C:\\Users\\manas\\Documents\\rental\\no-image.png"

        # Initialize and open the new page with these details
        import description
        self.destroy()
        new_page = description.Description(product_name, price, product_description, image_path)
        new_page.mainloop()
                
    def add_service_placeholder(self, parent, title, price, image_path):

        # formatting the image as in the database # Replace single backslashes with double backslashes
        formatted_path = image_path.replace("\\", "/")

        # Load and resize the image using PIL
        image = Image.open(image_path)
        image.resize((180, 120),Image.Resampling.LANCZOS)  # Resize to desired dimensions
        self.ctk_image = ctk.CTkImage(image, size=(250, 230))  # Create CTkImage with the resized image

        # Create the frame for the image and text
        service_frame = ctk.CTkFrame(parent, width=200, height=200, corner_radius=10, fg_color="white")
        service_frame.pack(padx=20, pady=10, side="left")

        # Create and place the image label
        image_label = ctk.CTkLabel(service_frame, image=self.ctk_image, text="")
        image_label.pack(pady=0.5)

        # Create and place the text button
        title_button = ctk.CTkButton(service_frame, text=title, text_color="black", font=("Helvetica", 18, 'bold'), fg_color="transparent", hover_color="#D9D9D9", command=lambda: self.button_clicked(crud.get_product_id_by_image(formatted_path)))
        title_button.pack(side="top", pady=5)

        price_label = ctk.CTkLabel(service_frame, text=price, font=("Helvetica", 12, 'bold'), text_color='#2F4D7D')
        price_label.pack()

    # Adding search functionality 
    def search(self):
        search_query = self.search_entry.get().lower()  # Get the search input and convert it to lowercase
        search_results = crud.search_products_by_category(search_query)  # Query the database

        # Clear existing search results
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Add a title label for the search results
        if search_query:
            title_label_main = ctk.CTkLabel(self.main_frame, text=f"Search results for: {search_query}", font=("Helvetica", 18, 'bold'))
            title_label_main.pack(anchor='w', padx=20, pady=(20, 30))

        # Display the search results
        if search_results:
            row_frame = None
            products_in_row = 0

            for i, (product_name, price, image) in enumerate(search_results):
                if products_in_row == 0:
                    # Create a new row frame when starting a new row
                    row_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
                    row_frame.pack(fill="x", padx=20, pady=10)

                self.add_service_placeholder(row_frame, product_name, f"Rs.{price} Per Day", image)

                products_in_row += 1

                # Reset after adding 3 products in a row
                if products_in_row >= 3:
                    products_in_row = 0

        else:
            no_results_label = ctk.CTkLabel(self.main_frame, text=f"No results found for category: {search_query}", font=("Helvetica", 18, 'bold'))
            no_results_label.pack(anchor="n", pady=(40, 20))

        
if __name__ == "__main__":
    app = RentalApp()
    app.mainloop()
