import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import crud, homepage, profile_1

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
        self.title_button = ctk.CTkButton(self.title_bar, text="Rent it.", font=("Helvetica", 30, 'bold'), text_color="white", hover_color="#2F4D7D", fg_color = "#2F4D7D", command = self.navigate)
        self.title_button.pack(side="left", padx=10, pady=5)

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
        self.glass_image = ctk.CTkImage(light_image=Image.open(".\\photos\\white-glass.png"))

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
        self.bell_image = ctk.CTkImage(light_image=Image.open(".\\photos\\Notification.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.profile_image = ctk.CTkImage(light_image=Image.open(".\\photos\\profile.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.heart_image = ctk.CTkImage(light_image=Image.open(".\\photos\\cart.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)

        # Create and place the icon buttons with adjusted width and height
        self.bell_button = ctk.CTkButton(self.menu_icon_frame, image=self.bell_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.bell_button.pack(side="left", padx=1)
        self.heart_button = ctk.CTkButton(self.menu_icon_frame, image=self.heart_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.heart_button.pack(side="left", padx=1)
        self.profile_button = ctk.CTkButton(self.menu_icon_frame, image=self.profile_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D', command = self.navigate_to_profile)
        self.profile_button.pack(side="left", padx=1)

        
        # Create and place the main content
        self.main_frame = ctk.CTkScrollableFrame(self, orientation='vertical', fg_color='transparent')
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20, side="right")

        # Create the side filter frame
        self.side_frame = ctk.CTkFrame(self, width=300, corner_radius=10, bg_color="white", fg_color='white')
        self.side_frame.pack(fill='y', side='left', padx=(0, 0), pady=5)


        # Add filter options to the side frame
        self.filter_label = ctk.CTkLabel(self.side_frame, text="Filters Options", font=("Helvetica", 16, 'bold'))
        self.filter_label.pack(anchor="w", padx=30, pady=(10, 20))

        self.sort_by_label = ctk.CTkLabel(self.side_frame, text="Sort by:", font=("Helvetica", 14))
        self.sort_by_label.pack(anchor="w", padx=42, pady=10)

        self.search_results = search_results or []

        self.sort_var = tk.StringVar(value="Relevance")
        self.relevance_radio = ctk.CTkRadioButton(self.side_frame, text="Relevance", variable=self.sort_var, value="Relevance")
        self.relevance_radio.pack(anchor="w", padx=40, pady=5)

        self.high_low_radio = ctk.CTkRadioButton(self.side_frame, text="Price (High - Low)", variable=self.sort_var, value="Price (High - Low)")
        self.high_low_radio.pack(anchor="w", padx=40, pady=5)

        self.low_high_radio = ctk.CTkRadioButton(self.side_frame, text="Price (Low - High)", variable=self.sort_var, value="Price (Low - High)")
        self.low_high_radio.pack(anchor="w", padx=40, pady=5)


        # Bind the radio buttons to the update_sorting method
        self.relevance_radio.configure(command=self.update_sorting)
        self.high_low_radio.configure(command=self.update_sorting)
        self.low_high_radio.configure(command=self.update_sorting)


        # Adding a title label for the search results
        if search_query:
            if type(search_query) == int:
                self.title_label_main = ctk.CTkLabel(self.main_frame, text=f"{search_query} Results Found", font=("Helvetica", 18, 'bold'))
                self.title_label_main.pack(anchor = 'w', padx = 30, pady=(20, 30))
            else:
                self.title_label_main = ctk.CTkLabel(self.main_frame, text=f"Search results for: {search_query}", font=("Helvetica", 18, 'bold'))
                self.title_label_main.pack(anchor = 'w', padx = 40, pady=(20, 30))

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
        image_path = crud.get_product_image(product_id) or ".\\photos\\no-image.png"
        category = crud.get_category(product_id)
        images = crud.get_product_images(product_id)
        # Initialize and open the new page with these details
        import description
        self.destroy()
        new_page = description.Description(product_id,product_name, price, product_description, image_path, category, images)
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
        title_button = ctk.CTkButton(service_frame, text=title, text_color="black", font=("Helvetica", 18, 'bold'), fg_color="transparent", hover_color="white", command=lambda: self.button_clicked(crud.get_product_id_by_image(formatted_path)))
        title_button.pack(side="top", pady=5)

        price_label = ctk.CTkLabel(service_frame, text=price, font=("Helvetica", 12, 'bold'), text_color='#2F4D7D')
        price_label.pack()

    def search(self):
        search_query = self.search_entry.get().lower()  # Get the search input and convert it to lowercase
        self.search_results = crud.search_products_by_category(search_query)  # Query the database

        # Initially display the search results without any sorting
        self.display_results(search_query, self.search_results)

    def update_sorting(self):
        # Ensure search_results exists
        if not self.search_results:
            print("No search results to sort.")
            return

        # Determine sorting order based on the selected radio button
        sort_option = self.sort_var.get()
        if sort_option == "Price (Low - High)":
            self.search_results.sort(key=lambda x: x[1])  # Sort by price (ascending)
        elif sort_option == "Price (High - Low)":
            self.search_results.sort(key=lambda x: x[1], reverse=True)  # Sort by price (descending)

        # Clear and redisplay sorted results
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        row_frame = None
        products_in_row = 0

        for i, (product_name, price, image) in enumerate(self.search_results):
            if products_in_row == 0:
                row_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
                row_frame.pack(fill="x", padx=20, pady=10)

            self.add_service_placeholder(row_frame, product_name, f"Rs.{price} Per Day", image)
            products_in_row += 1

            if products_in_row >= 3:
                products_in_row = 0


    def display_results(self, search_query, search_results):
        # Clear existing search results
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Add a title label for the search results (if a search query was provided)
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
            no_results_label = ctk.CTkLabel(self.main_frame, text="No results found.", font=("Helvetica", 18, 'bold'))
            no_results_label.pack(anchor="n", pady=(40, 20))


    def navigate(self):
        self.destroy()
        new_app = homepage.RentalApp()
        new_app.mainloop()

    def navigate_to_profile(self):
        self.destroy()
        profile_app = profile_1.RentalApp()
        profile_app.create_dashboard()
        profile_app.on_click(profile_app.dashboard_button, profile_app.home_hover_image, profile_app.create_dashboard)
        profile_app.mainloop()

    def notification(self):
        # Example data array for notifications
        notifications = [
            {"title": "Item Available for Rent", 
            "message": "Sony a6400 is now available for rent. Click here to book it before it's gone!"
            }
        ]
        
        # Create a small window below the bell_button
        popup = tk.Toplevel(self)
        
        # Remove window decorations for a cleaner popup look
        popup.overrideredirect(True)
        
        # Set the size of the popup window
        popup.geometry("320x400")  # Adjust the size as needed

        # Set the background color of the popup window
        popup.configure(bg="white")

        # Frame for the Notification header
        header_frame = ctk.CTkFrame(popup, height=40, corner_radius=0, fg_color="white")
        header_frame.pack(padx=10, pady=(10, 0), fill="x", expand=False)

        # Label for "Notifications"
        header_label = ctk.CTkLabel(header_frame, text="Notifications", font=("Helvetica", 14), text_color="#2F4D7D")
        header_label.pack(side="left", padx=(10, 0), pady=5)

        # Frame for Notification content
        content_frame = ctk.CTkFrame(popup, corner_radius=0, fg_color="white")
        content_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Display notifications from the data array
        for notification in notifications:
            # Title Label
            title_label = ctk.CTkLabel(content_frame, text=notification["title"], font=("Helvetica", 12, "bold"), text_color="black", anchor="w", justify="left")
            title_label.pack(anchor="w", padx=(10, 0), pady=(5, 0), fill="x")
            
            # Message Label
            message_label = ctk.CTkLabel(content_frame, text=notification["message"], font=("Helvetica", 12), text_color="gray", wraplength=280, anchor="w", justify="left")
            message_label.pack(anchor="w", padx=(10, 0), pady=(0, 10), fill="x")

        # Calculate the position of the popup relative to the bell_button
        x = self.bell_button.winfo_rootx() - 50  # Offset to center the popup under the button
        y = self.bell_button.winfo_rooty() + self.bell_button.winfo_height() + 10  # Offset to place it below the button

        # Adjust the x position to add a gap on the right side
        x = x - 20  # Adjust this value to increase or decrease the gap

        popup.geometry(f"+{x}+{y}")

        # Optional: Auto-close the popup after a certain time (e.g., 3 seconds)
        # popup.after(5000, popup.destroy)


        
if __name__ == "__main__":
    app = RentalApp()
    app.mainloop()
