import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import crud, homepage, search, profile_1

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
        self.geometry("1280x750")  
        self.title_bar = ctk.CTkFrame(self, height=375, corner_radius=0, fg_color="#2F4D7D")
        self.title_bar.pack(fill="x", side="top")
        self.title_label = ctk.CTkLabel(self.title_bar, text="Rent it.", font=("Helvetica", 30, 'bold'), text_color="white")
        self.title_label.pack(side="left", padx = 20, pady = 20, anchor ='n')

        # Icon Frame 
        self.icon_frame = ctk.CTkFrame(self.title_bar, fg_color="#2F4D7D")
        self.icon_frame.pack(side="right", padx=10, pady=20, anchor = 'n')

        icon_size = (30, 31)  
        self.bell_image = ctk.CTkImage(light_image=Image.open(".\\photos\\Notification.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.profile_image = ctk.CTkImage(light_image=Image.open(".\\photos\\profile.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.heart_image = ctk.CTkImage(light_image=Image.open(".\\photos\\cart.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)

        # profile, cart and notification buttons 
        self.bell_button = ctk.CTkButton(self.icon_frame, image=self.bell_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.bell_button.pack(side="left", padx=1)
        self.cart_button = ctk.CTkButton(self.icon_frame, image=self.heart_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D', command = self.navigate_to_cart)
        self.cart_button.pack(side="left", padx=1)
        self.profile_button = ctk.CTkButton(self.icon_frame, image=self.profile_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D', command = self.navigate_to_profile)
        self.profile_button.pack(side="left", padx=1)

        # Main frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.pack(fill="both", expand=True)

        checkmark_image = Image.open(".\\photos\\sucess.png") 
        checkmark_image = checkmark_image.resize((150, 150))  
        checkmark_photo = ImageTk.PhotoImage(checkmark_image)

        self.checkmark_label = ctk.CTkLabel(self.main_frame, image=checkmark_photo, text="")
        self.checkmark_label.image = checkmark_photo  # Keep a reference to avoid garbage collection
        self.checkmark_label.pack(pady=(150, 10))

        self.success_label = ctk.CTkLabel(self.main_frame, text="You have Successfully Rented",
                                          font=ctk.CTkFont(size=20, weight="bold"))
        self.success_label.pack(pady=(10, 10))

        self.confirmation_label = ctk.CTkLabel(self.main_frame, text="Your rental is confirmed! We hope you enjoy your experience.\nYou can find the details of your order below.",
                                               font=ctk.CTkFont(size=14), wraplength=400, justify="center")
        self.confirmation_label.pack(pady=(10, 10))

        # Load button images
        dashboard_icon = Image.open(".\\photos\\stack.png")  
        dashboard_icon = dashboard_icon.resize((30, 30)) 
        dashboard_photo = ImageTk.PhotoImage(dashboard_icon)

        order_icon = Image.open(".\\photos\\arrowright.png")  
        order_icon = order_icon.resize((30, 30))  
        order_photo = ImageTk.PhotoImage(order_icon)

        # Buttons
        self.dashboard_button = ctk.CTkButton(self.main_frame, text=" GO TO DASHBOARD", image=dashboard_photo, compound="left",hover_color='#F2F2F2',
                                              width=200, height=40, fg_color="#F2F2F2", text_color="black", border_width=2,
                                              border_color="#1E3A8A", corner_radius=0, command = self.navigate_to_profile)
        self.dashboard_button.image = dashboard_photo  
        self.dashboard_button.pack(side="left", padx=(440, 10), pady = (20,10), anchor = 'n')

        self.order_button = ctk.CTkButton(self.main_frame, text="VIEW CART ", image=order_photo, compound="right",
                                          width=200, height=40, fg_color="#1E3A8A", text_color="white", border_width=0,
                                          hover_color="#1E3A8A", corner_radius=0, command = self.navigate_to_profile)
        self.order_button.image = order_photo 
        self.order_button.pack(side="right", padx=(10, 440), pady= (20,10), anchor ='n')

    def navigate(self):
        self.destroy()
        new_app = homepage.RentalApp()
        new_app.mainloop()

    def search(self):
        search_query = self.search_entry.get().lower()  
        search_results = crud.search_products_by_category(search_query) 

        if search_results:
            self.destroy() 
            search_app = search.RentalApp(search_query, search_results)  
            search_app.mainloop()
        else:
            self.destroy() 
            search_app = search.RentalApp(search_query, [])  
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



if __name__ == "__main__":
    app = RentalApp()
    app.mainloop()