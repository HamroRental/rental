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
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20, side="right")

        # Create the side filter frame
        self.side_frame = ctk.CTkFrame(self, width=300, corner_radius=10, bg_color="#e0e0e0")
        self.side_frame.pack(fill='y', side='left', padx=(20, 0), pady=20)

        #Adding search bar 
         # Create the search bar frame
        self.search_frame = ctk.CTkFrame(self.main_frame, corner_radius=10, fg_color="#E5E5E5")
        self.search_frame.pack(pady=10, padx=20, fill="x")

        # Create the search entry with the search button and magnifying glass icon
        self.search_container = ctk.CTkFrame(self.search_frame, fg_color="#FFFFFF", corner_radius=30)
        self.search_container.pack(pady=10, padx=30, side = 'left')

        self.search_entry_frame = ctk.CTkFrame(self.search_container, fg_color="#FFFFFF")
        self.search_entry_frame.pack(fill="x", expand=True, padx=10, pady=5)

        # Load the magnifying glass image
        self.glass_image = ctk.CTkImage(light_image=Image.open("C:\\Users\\manas\\Documents\\rental\\glass.png"))

        # Create and place the magnifying glass label inside the search entry
        self.glass_label = ctk.CTkLabel(self.search_entry_frame, image=self.glass_image, text="", width=25, height=20, fg_color="#FFFFFF")
        self.glass_label.pack(side="left", padx=10)

        # Create and place the search entry
        self.search_entry = ctk.CTkEntry(self.search_entry_frame, placeholder_text="Search something here", height=25, corner_radius=15, border_width=0)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=5)

       



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

        
if __name__ == "__main__":
    app = RentalApp()
    app.mainloop()
