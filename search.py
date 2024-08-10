import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

# Set the appearance mode of the app
ctk.set_appearance_mode("light")  # Modes: "System" (standard), "light", "dark"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class RentalApp(ctk.CTk):
    def __init__(self, search_query = None, search_results =None):
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
        self.bell_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\Notification.png"))
        self.profile_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\profile.png"))
        self.settings_image = ctk.CTkImage(light_image = Image.open("C:\\Users\\manas\\Documents\\rental\\Settings.png"))

        # Create a frame for the right-side icons
        self.icon_frame = ctk.CTkFrame(self.menu_icon_frame, fg_color="#2F4D7D")
        self.icon_frame.pack(side="right", padx=1)

        # Create and place the icon buttons
        self.bell_button = ctk.CTkButton(self.icon_frame, image=self.bell_image, text="", width=35, height=35, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.bell_button.pack(side="left", padx=3)
        self.settings_image = ctk.CTkButton(self.icon_frame, image=self.settings_image, text= '', width = 35, height =35, fg_color = "#2F4D7D", hover_color = "#2F4D7D")
        self.settings_image.pack(side ='left', padx=3)
        self.profile_button = ctk.CTkButton(self.icon_frame, image=self.profile_image, text="", width=35, height=35, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.profile_button.pack(side="left", padx=3)

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
            self.title_label_main.pack(anchor = 'w', padx = 1, pady=(20, 10))

        # Displaying the search results
        if search_results:
            for product_name, price, image in search_results:
                self.add_service_placeholder(self.main_frame, product_name, f"Rs.{price} Per Day", image)

    def button_clicked(self):
        print('button clicked')
        import description
        new_page = description.Description()
        new_page.mainloop()

                
    def add_service_placeholder(self, parent, title, price, image):
        # Load and resize the image using PIL
        image = Image.open(image)
        image.resize((180, 120),Image.Resampling.LANCZOS)  # Resize to desired dimensions
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

        price_label = ctk.CTkLabel(service_frame, text=price, font=("Helvetica", 12, 'bold'), text_color='#2F4D7D')
        price_label.pack()

        
if __name__ == "__main__":
    app = RentalApp()
    app.mainloop()
