import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import crud, homepage, search, profile_1, submission

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

        self.title("Rent it.")
        self.geometry("1280x750")  # Adjusted to fit more content

        # Create the title bar frame
        self.title_bar = ctk.CTkFrame(self, height=375, corner_radius=0, fg_color="#2F4D7D")
        self.title_bar.pack(fill="x", side="top")

        # Create and place the title label
        self.title_label = ctk.CTkButton(self.title_bar, text="Rent it.", font=("Helvetica", 30, 'bold'), text_color="white", hover_color="#2F4D7D", fg_color = "#2F4D7D", command = self.navigate)
        self.title_label.pack(side="left", padx=10, pady=5)

        # Create a container frame for the menu icons
        self.icon_frame = ctk.CTkFrame(self.title_bar, fg_color="#2F4D7D")
        self.icon_frame.pack(side="right", padx=10, pady=20, anchor = 'n')

        # Load the icons with increased size
        icon_size = (30, 30)  # Adjust the size as needed
        self.bell_image = ctk.CTkImage(light_image=Image.open(".\\photos\\Notification.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.profile_image = ctk.CTkImage(light_image=Image.open(".\\photos\\profile.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.heart_image = ctk.CTkImage(light_image=Image.open(".\\photos\\cart.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)

        # Create and place the icon buttons with adjusted width and height
        self.bell_button = ctk.CTkButton(self.icon_frame, image=self.bell_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.bell_button.pack(side="left", padx=1)
        self.cart_button = ctk.CTkButton(self.icon_frame, image=self.heart_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D', command = self.navigate_to_cart)
        self.cart_button.pack(side="left", padx=1)
        self.profile_button = ctk.CTkButton(self.icon_frame, image=self.profile_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D', command = self.navigate_to_profile)
        self.profile_button.pack(side="left", padx=1)

        self.main_frame = ctk.CTkScrollableFrame(self, orientation='vertical', bg_color='transparent')
        self.main_frame.pack(fill="both", expand=True, padx=0, pady=1, side="right")

       # Adding a billing frame
        self.billing_frame = ctk.CTkFrame(self.main_frame, fg_color='#F2F2F2', width=400, height=150)
        self.billing_frame.pack_propagate(False)
        self.billing_frame.pack(side='top', ipadx=150, ipady=30, padx=20, pady=30)  # Explicitly set the size in pack


        # Billing Info Label
        billing_info_label = ctk.CTkLabel(self.billing_frame, text="Billing Info", font=("Arial", 20, "bold"))
        billing_info_label.grid(row=0, column=0, columnspan=2, sticky="w", padx=(40, 10), pady=(30, 0))

        # Subtext Label
        subtext_label = ctk.CTkLabel(self.billing_frame, text="Please enter your billing info", font=("Arial", 12), text_color="#90A3BF")
        subtext_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=(40, 10), pady=(0, 20))

        # Name Label and Entry
        name_label = ctk.CTkLabel(self.billing_frame, text="Name", font=("Arial", 14, 'bold'))
        name_label.grid(row=2, column=0, sticky="w", padx=(45, 10), pady=(0, 5))

        name_entry = ctk.CTkEntry(self.billing_frame, placeholder_text="   Your name", width=300, border_color='#D3D3D3', fg_color="#D3D3D3", height = 45, text_color="#90A3BF")
        name_entry.grid(row=3, column=0, sticky="w", padx=(40, 10), pady=(0, 30))

        # Phone Number Label and Entry
        phone_label = ctk.CTkLabel(self.billing_frame, text="Phone Number", font=("Arial", 14, 'bold'))
        phone_label.grid(row=2, column=1, sticky="w", padx=(45, 10), pady=(0, 5))

        phone_entry = ctk.CTkEntry(self.billing_frame, placeholder_text="   Phone number", width=300, border_color='#D3D3D3', fg_color="#D3D3D3", height = 45)
        phone_entry.grid(row=3, column=1, sticky="w", padx=(40, 10), pady=(0, 30))

        # Address Label and Entry
        address_label = ctk.CTkLabel(self.billing_frame, text="Address", font=("Arial", 14, 'bold'))
        address_label.grid(row=4, column=0, sticky="w", padx=(45, 10), pady=(0, 10))

        address_entry = ctk.CTkEntry(self.billing_frame, placeholder_text="   Address", width=300, border_color='#D3D3D3', fg_color="#D3D3D3", height = 45)
        address_entry.grid(row=5, column=0, sticky="w", padx=(40, 10), pady=(0, 20))

        # Town / City Label and Entry
        city_label = ctk.CTkLabel(self.billing_frame, text="Town / City", font=("Arial", 14, 'bold'))
        city_label.grid(row=4, column=1, sticky="w", padx=(40, 10), pady=(0, 10))

        city_entry = ctk.CTkEntry(self.billing_frame, placeholder_text="   Town or city", width=300, border_color='#D3D3D3', fg_color="#D3D3D3", height = 45)
        city_entry.grid(row=5, column=1, sticky="w", padx=(40, 10), pady=(0, 20))

        # Step Label (e.g., Step 1 of 4)
        step_label = ctk.CTkLabel(self.billing_frame, text="        Step 1 of 4", font=("Arial", 12, 'bold'), fg_color='#F2F2F2', text_color="#90A3BF")
        step_label.grid(row=0, column=1, sticky="e", padx=(40, 10), pady=(30, 5))

        # Adding a rent-info frame
        self.rent_info = ctk.CTkFrame(self.main_frame, fg_color='#F2F2F2', width=400, height=150)
        self.rent_info.pack_propagate(False)
        self.rent_info.pack(side='top', ipadx=150, ipady=40, padx=20, pady=30)  # Explicitly set the size in pack


        # Billing Info Label
        rent_info_label = ctk.CTkLabel(self.rent_info, text="Rent Info", font=("Arial", 20, "bold"))
        rent_info_label.grid(row=0, column=0, columnspan=2, sticky="w", padx=(40, 10), pady=(40, 0))

        # Subtext Label
        subtext_label = ctk.CTkLabel(self.rent_info, text="Please select your rental date", font=("Arial", 12), text_color="#90A3BF")
        subtext_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=(40, 10), pady=(0, 20))

        # Pickup Label
        pickup_label = ctk.CTkLabel(self.rent_info, text="Pick-Up", font=("Arial", 16, 'bold'), text_color="green")
        pickup_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=(40, 10), pady=(0, 10))

        # Location Label and Entry
        location_label = ctk.CTkLabel(self.rent_info, text="Location", font=("Arial", 14, 'bold'))
        location_label.grid(row=3, column=0, sticky="w", padx=(45, 10), pady=(0, 5))

        location_label = ctk.CTkEntry(self.rent_info, placeholder_text="   Enter your city", width=300, border_color='#D3D3D3', fg_color="#D3D3D3", height = 45, text_color="#90A3BF")
        location_label.grid(row=4, column=0, sticky="w", padx=(40, 10), pady=(0, 30))

        # Date Label and Entry
        date_label = ctk.CTkLabel(self.rent_info, text="Date", font=("Arial", 14, 'bold'))
        date_label.grid(row=3, column=1, sticky="w", padx=(45, 10), pady=(0, 5))

        date_entry = ctk.CTkEntry(self.rent_info, placeholder_text="   Enter Date", width=300, border_color='#D3D3D3', fg_color="#D3D3D3", height = 45)
        date_entry.grid(row=4, column=1, sticky="w", padx=(40, 10), pady=(0, 30))

        # Time Label and Entry
        time_label = ctk.CTkLabel(self.rent_info, text="Time", font=("Arial", 14, 'bold'))
        time_label.grid(row=5, column=0, sticky="w", padx=(45, 10), pady=(0, 10))

        time_label = ctk.CTkEntry(self.rent_info, placeholder_text="   Enter your time", width=300, border_color='#D3D3D3', fg_color="#D3D3D3", height = 45)
        time_label.grid(row=6, column=0, sticky="w", padx=(40, 10), pady=(0, 20))

        # Pickup Label
        dropoff_label = ctk.CTkLabel(self.rent_info, text="Drop-Off", font=("Arial", 16, 'bold'), text_color="red")
        dropoff_label.grid(row=7, column=0, columnspan=2, sticky="w", padx=(45, 10), pady=(30, 10))

        # Location Label and Entry
        location_label1 = ctk.CTkLabel(self.rent_info, text="Location", font=("Arial", 14, 'bold'))
        location_label1.grid(row=8, column=0, sticky="w", padx=(45, 10), pady=(0, 5))

        location_label1 = ctk.CTkEntry(self.rent_info, placeholder_text="   Enter your city", width=300, border_color='#D3D3D3', fg_color="#D3D3D3", height = 45, text_color="#90A3BF")
        location_label1.grid(row=9, column=0, sticky="w", padx=(40, 10), pady=(0, 30))

        # Date Label and Entry
        date_label1 = ctk.CTkLabel(self.rent_info, text="Date", font=("Arial", 14, 'bold'))
        date_label1.grid(row=8, column=1, sticky="w", padx=(45, 10), pady=(0, 5))

        date_entry1 = ctk.CTkEntry(self.rent_info, placeholder_text="   Enter Date", width=300, border_color='#D3D3D3', fg_color="#D3D3D3", height = 45)
        date_entry1.grid(row=9, column=1, sticky="w", padx=(40, 10), pady=(0, 30))

        # Time Label and Entry
        time_label1 = ctk.CTkLabel(self.rent_info, text="Time", font=("Arial", 14, 'bold'))
        time_label1.grid(row=10, column=0, sticky="w", padx=(45, 10), pady=(0, 10))

        time_label1 = ctk.CTkEntry(self.rent_info, placeholder_text="   Enter your time", width=300, border_color='#D3D3D3', fg_color="#D3D3D3", height = 45)
        time_label1.grid(row=11, column=0, sticky="w", padx=(40, 10), pady=(0, 10))

        # Step Label (e.g., Step 1 of 4)
        step_label = ctk.CTkLabel(self.rent_info, text="        Step 2 of 4", font=("Arial", 12, 'bold'), fg_color='#F2F2F2', text_color="#90A3BF")
        step_label.grid(row=0, column=1, sticky="e", padx=(40, 10), pady=(40, 5))

        # Adding a rent-info frame
        self.payment_info = ctk.CTkFrame(self.main_frame, fg_color='transparent', width=400, height=150)
        self.payment_info.pack_propagate(False)
        self.payment_info.pack(side='top', ipadx=100, ipady=40, padx=(5,20), pady=(30,1))  # Explicitly set the size in pack
        

        # Title and subtitle within payment_info frame
        title = ctk.CTkLabel(self.payment_info, text="Payment Method", font=("Helvetica", 24, "bold"))
        subtitle = ctk.CTkLabel(self.payment_info, text="Please enter your payment method", font=("Helvetica", 12), text_color="#90A3BF")

        title.grid(row=0, column=0, padx=10, pady=(20, 5), sticky="w")
        subtitle.grid(row=1, column=0, padx=10, pady=(0, 20), sticky="w")

        # Step Label (e.g., Step 1 of 4)
        step_label = ctk.CTkLabel(self.payment_info, text="        Step 3 of 4", font=("Arial", 12, 'bold'), fg_color='transparent', text_color="#90A3BF")
        step_label.grid(row=0, column=1, sticky="e", padx=(50, 10), pady=(40, 5))

        # Radio button frames
        self.radio_var = ctk.StringVar(value="Credit Card")

        self.credit_card_frame = self.create_radio_frame("Credit Card", "Credit Card", row=2, image_path=".\\photos\\Visa.png", size = (45,20))
        self.esewa_frame = self.create_radio_frame("Esewa", "Esewa", row=3, image_path=".\\photos\\esewa.png")
        self.khalti_frame = self.create_radio_frame("Khalti", "Khalti", row=4, image_path=".\\photos\\khalti.png", size = (60,30))
        self.cod_frame = self.create_radio_frame("COD", "COD", row=5, image_path=".\\photos\\cod.png", size=(35,30))

        # Initially expand the Credit Card frame to show the labels and entries
        self.expand_frame()

        # Adding a confirmation frame
        self.confirmation_frame = ctk.CTkFrame(self.main_frame, fg_color='transparent', width=600, height=150)
        self.confirmation_frame.pack_propagate(False)
        self.confirmation_frame.pack(side='top', ipadx=150, ipady=30, padx=10, pady=(1,10), anchor='n')  # Explicitly set the size in pack

        # Title and subtitle within confirmation_frame
        title = ctk.CTkLabel(self.confirmation_frame, text="Confirmation", font=("Helvetica", 24, "bold"))
        subtitle = ctk.CTkLabel(self.confirmation_frame, text="We are getting to the end. Just a few clicks and your rental is ready!", font=("Helvetica", 12), text_color="#90A3BF")

        title.grid(row=0, column=0, padx=30, pady=(20, 0), sticky="w")
        subtitle.grid(row=1, column=0, padx=30, pady=(0, 20), sticky="w")

        # Step Label (e.g., Step 4 of 4)
        step_label = ctk.CTkLabel(self.confirmation_frame, text="        Step 4 of 4", font=("Arial", 12, 'bold'), fg_color='transparent', text_color="#90A3BF")
        step_label.grid(row=0, column=1, sticky="e", padx=(50, 10), pady=(40, 5))

        # Adding a checkbox frame within confirmation_frame
        checkbox_frame = ctk.CTkFrame(self.confirmation_frame, fg_color='#F2F2F2', width=350, height=40)
        checkbox_frame.pack_propagate(False)
        checkbox_frame.grid(row=2, column=0, columnspan=2, padx=30, pady=(5, 0), sticky="w")

        # Checkbox and text beside it
        checkbox_var = ctk.BooleanVar()  # Variable to hold the state of the checkbox
        checkbox = ctk.CTkCheckBox(checkbox_frame, text="", variable=checkbox_var, width = 10)
        checkbox.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="w")

        checkbox_text = ctk.CTkLabel(checkbox_frame, text="I agree to the terms and conditions.", font=("Helvetica", 12), text_color="#000000")
        checkbox_text.grid(row=0, column=1, padx=(0, 450), pady=10, sticky="w")

        rent_now_button = ctk.CTkButton(self.main_frame, text = 'Rent now', text_color='white', font=("Helvetica", 12, 'bold'), fg_color='#2F4D7D', hover_color="#2F4D7D", width =100, height = 40, command = self.navigate_to_submission)
        rent_now_button.pack(side = 'bottom', anchor = 'n', pady = 20, padx= (500,10))

        

    def create_radio_frame(self, label_text, value, row, image_path, size=(40,20)):
        # Frame for radio button
        frame = ctk.CTkFrame(self.payment_info, height=100, width=700, corner_radius=10, fg_color='#F2F2F2')
        frame.grid_propagate(False)
        frame.grid(row=row, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)

        # Configure grid columns
        frame.grid_columnconfigure(0, weight=1)  # Allow the first column to expand
        frame.grid_columnconfigure(1, weight=0)  # Fixed width for the second column (for image)

        # Radio button and label
        radio_btn = ctk.CTkRadioButton(frame, text=label_text, variable=self.radio_var, value=value, command=self.expand_frame)
        radio_btn.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # Loading and displaying the icon
        icon_image = ctk.CTkImage(Image.open(image_path), size=size)
        icon_label = ctk.CTkLabel(frame, image=icon_image, text="")
        icon_label.grid(row=0, column=1, padx=(10, 10), pady=10, sticky='e')  # Align to the right side

        # Credit Card specific content
        if value == "Credit Card":
            self.add_credit_card_fields(frame)

        # Esewa and Khalti specific content
        if value in "Esewa":
            button = ctk.CTkButton(frame, text=f"Connect Your {label_text}", fg_color='#4D9638', hover_color='#4D9638')
            button.grid(row=1, column=0, padx=(250,200), pady=10, sticky="nsew")
            button.grid_remove()  # Hide button initially
            frame.button = button
        elif value in "Khalti":
            button = ctk.CTkButton(frame, text=f"Connect Your {label_text}", fg_color="#4A2574", hover_color="#4A2574")
            button.grid(row=1, column=0, padx=(250,200), pady=10, sticky="nsew", columnspan = 2)
            button.grid_remove()  # Hide button initially
            frame.button = button


        return frame

    
    def add_credit_card_fields(self, frame):
        # Labels and entries for credit card information
        card_number_label = ctk.CTkLabel(frame, text="Card Number")
        card_number_entry = ctk.CTkEntry(frame, placeholder_text="Card number", width = 300, border_color='#D3D3D3', fg_color="#D3D3D3", height = 45)

        expiry_date_label = ctk.CTkLabel(frame, text="Expiration Date")
        expiry_date_entry = ctk.CTkEntry(frame, placeholder_text="DD/MM/YY", width = 300, border_color='#D3D3D3', fg_color="#D3D3D3", height = 45)

        card_holder_label = ctk.CTkLabel(frame, text="Card Holder")
        card_holder_entry = ctk.CTkEntry(frame, placeholder_text="Card holder", width = 300, border_color='#D3D3D3', fg_color="#D3D3D3", height = 45)

        cvc_label = ctk.CTkLabel(frame, text="CVC")
        cvc_entry = ctk.CTkEntry(frame, placeholder_text="CVC", width = 300, border_color='#D3D3D3', fg_color="#D3D3D3", height = 45)

        card_number_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        card_number_entry.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="ew")

        expiry_date_label.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="w")
        expiry_date_entry.grid(row=2, column=1, padx=10, pady=(0, 10), sticky="ew")

        card_holder_label.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")
        card_holder_entry.grid(row=4, column=0, padx=10, pady=(0, 10), sticky="ew")

        cvc_label.grid(row=3, column=1, padx=10, pady=(10, 0), sticky="w")
        cvc_entry.grid(row=4, column=1, padx=10, pady=(0, 10), sticky="ew")

        # Make sure the entries expand with the frame
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

    def expand_frame(self):
        # Collapse all frames first
        for frame in [self.credit_card_frame, self.esewa_frame, self.khalti_frame, self.cod_frame]:
            frame.configure(height=50)
            if hasattr(frame, 'expanding_content'):
                frame.expanding_content.grid_remove()
            if hasattr(frame, 'button'):
                frame.button.grid_remove()

        # Expand the selected frame
        selected_frame = {
            "Credit Card": self.credit_card_frame,
            "Esewa": self.esewa_frame,
            "Khalti": self.khalti_frame,
            "COD": self.cod_frame
        }[self.radio_var.get()]

        if self.radio_var.get() == "Credit Card":
            selected_frame.configure(height=270)
        elif self.radio_var.get() in ["Esewa", "Khalti"]:
            selected_frame.configure(height=100)
            selected_frame.button.grid()


    def navigate(self):
        self.destroy()
        new_app = homepage.RentalApp()
        new_app.mainloop()

    def navigate_to_submission(self):
        self.destroy()
        submission_app = submission.RentalApp()
        submission_app.mainloop()

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



# Run the application
if __name__ == "__main__":
    app = RentalApp()
    app.mainloop()



