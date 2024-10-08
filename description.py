import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageOps
import crud 
import search
import homepage, profile_1, payment 

ctk.set_appearance_mode("light") 
ctk.set_default_color_theme("dark-blue")  

class Description(ctk.CTk):
    def __init__(self, product_id, product_name, price, product_description, image_path, category, images):
        super().__init__()
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.category = category
        self.image_path = image_path

        self.title("Description")
        self.geometry("1280x750")  

        # Title Bar Frame 
        self.title_bar = ctk.CTkFrame(self, height=100, fg_color="#2F4D7D", corner_radius=0)
        self.title_bar.pack(fill="x", side="top")
        self.title_label = ctk.CTkButton(self.title_bar, text="Rent it.", font=("Helvetica", 30, 'bold'), text_color="white", hover_color="#2F4D7D", fg_color = "#2F4D7D", command = self.navigate)
        self.title_label.pack(side="left", padx=10, pady=5)

        # Menu Frame 
        self.menu_icon_frame = ctk.CTkFrame(self.title_bar, fg_color="#2F4D7D", width=50)  
        self.menu_icon_frame.pack(side="right", padx=20)
        self.menu_frame = ctk.CTkFrame(self.title_bar, width = 100, fg_color="#2F4D7D")
        self.menu_frame.pack(side="left", fill="x", expand=True, pady=5, padx=(230, 150))  

        # Search Bar
        self.search_frame = ctk.CTkFrame(self.menu_frame, width=500, fg_color="#2F4D7D")
        self.search_frame.pack(pady=20, padx=10, fill ='x', expand=True)  
        self.glass_image = ctk.CTkImage(light_image=Image.open(".\\photos\\white-glass.png"))

        self.search_container = ctk.CTkFrame(self.search_frame, fg_color="#6883AE", width=250, corner_radius=5)
        self.search_container.pack(fill = 'x', expand=True, padx=10, pady=5)

        self.search_entry_frame = ctk.CTkFrame(self.search_container, fg_color="#6883AE", width=70, corner_radius=5)
        self.search_entry_frame.pack(fill="x", padx=(1,0), pady=0)

        self.search_entry = ctk.CTkEntry(self.search_entry_frame, placeholder_text="Rooms, Vehicles, Equipment, Clothes", height=27, border_width=0, corner_radius=0)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(0,2))
        self.search_button = ctk.CTkButton(self.search_entry_frame, image=self.glass_image, text="", width=70, height=26, fg_color="#6883AE", hover_color="#6883AE",corner_radius=0, command= self.search)
        self.search_button.pack(side="right", fill = "x", padx=(2.5,0))

        # Images at the side of the top bar 
        icon_size = (30, 30)  
        self.bell_image = ctk.CTkImage(light_image=Image.open(".\\photos\\Notification.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.profile_image = ctk.CTkImage(light_image=Image.open(".\\photos\\profile.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.heart_image = ctk.CTkImage(light_image=Image.open(".\\photos\\cart.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)

        # profile, cart and notification 
        self.bell_button = ctk.CTkButton(self.menu_icon_frame, image=self.bell_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.bell_button.pack(side="left", padx=1)
        self.heart_button = ctk.CTkButton(self.menu_icon_frame, image=self.heart_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D', command=self.navigate_to_cart)
        self.heart_button.pack(side="left", padx=1)
        self.profile_button = ctk.CTkButton(self.menu_icon_frame, image=self.profile_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D', command = self.navigate_to_profile)
        self.profile_button.pack(side="left", padx=1)

        # Main Frame 
        self.main_frame = ctk.CTkScrollableFrame(self, orientation='vertical', fg_color='transparent')
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Frame for holding both image and decription frame 
        self.all_frame = ctk.CTkFrame(self.main_frame, corner_radius=30, width=400, fg_color='transparent')
        self.all_frame.pack(fill='both', expand=True, padx=(30,50), pady=20)  

        # Photo Frame 
        self.photo_frame = ctk.CTkFrame(self.all_frame, corner_radius=10, fg_color='transparent')
        self.photo_frame.pack(side='left', pady=10, padx=(20,5))
        self.add_service_placeholder(self.photo_frame, image_path, images)

        # Text frame 
        self.text_frame = ctk.CTkFrame(self.all_frame, fg_color='white', width = 400, height = 400,corner_radius=15)
        self.text_frame.pack(side='left', fill='both', expand=True, padx=(5,10), pady=10)

        self.title_label_main = ctk.CTkLabel(self.text_frame, text=product_name, font=("Helvetica", 30), text_color='black')
        self.title_label_main.pack(anchor='w', padx = (30,10),pady=(50, 20))  # Adjust pady to add space between title and subtitle

        self.description_text = tk.Text(self.text_frame, wrap="word", font=("Helvetica", 16), fg='#808080', bg='white',
                                        height=10, width=100, bd=0, padx=20, pady=10)
        self.description_text.pack(anchor='w', padx = (30,10),pady=(0, 1))

        if isinstance(product_description, str):
            self.description_text.insert('1.0', product_description)
        else:
            self.description_text.insert('1.0', "No description available.")
        self.description_text.configure(state='disabled')

        self.buttons_frame = ctk.CTkFrame(self.text_frame, fg_color="transparent",width = 100)
        self.buttons_frame.pack(anchor='w', pady=20, padx=10, side = 'bottom')
        price = price
        price_frame = ctk.CTkFrame(self.buttons_frame, fg_color="transparent")
        price_frame.pack(side="left", padx=(30, 20), pady=(30,10))

        self.price_label = ctk.CTkLabel(price_frame, text=f'Rs. {price}', font=("Inter", 30, 'bold'), text_color="black")
        self.price_label.pack(side="left")

        self.day_label = ctk.CTkLabel(price_frame, text=' / Day', font=("Inter", 30), text_color='#2F4D7D')
        self.day_label.pack(side="left")

        self.rent_button = ctk.CTkButton(self.buttons_frame, text="Rent Now", corner_radius=5, font=("Helvetica", 15, 'bold'), fg_color="#2F4D7D", hover_color='#2F4D7D', width = 20, height = 35, command = self.navigate_to_payment)
        self.rent_button.pack(side="left", padx=(100, 0), pady=(15,0))

        self.add_to_cart = ctk.CTkButton(self.buttons_frame, text="Add to cart", corner_radius=5, font=("Helvetica", 15, 'bold'), fg_color="green", hover_color='green', width = 20, height =35, command = self.add_to_cart)
        self.add_to_cart.pack(side="left", padx=(10, 0), pady=(15,0))

        # Recomended Frame 
        self.recommended_label = ctk.CTkLabel(self.main_frame, text="Recommended for you", font=("Helvetica", 30), text_color="black")
        self.recommended_label.pack(anchor="w", pady=(80,10), padx= 60)  

        search_results = crud.search_products_by_category(category)  

        if search_results:
            row_frame = None
            products_in_row = 0

            for i,(product_name, price, image_path) in enumerate(search_results):

                if product_name == crud.get_product_name(product_id):
                    continue

                if products_in_row == 0:
                    row_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
                    row_frame.pack(fill="x", padx=(40,10), pady=30)

                self.show_recommended(row_frame, product_name, f"Rs.{price} Per Day", image_path)
                products_in_row += 1

                if products_in_row >= 4:
                    products_in_row = 0

    def add_service_placeholder(self, parent, image_path, images):
        image = Image.open(image_path)
        image = image.resize((370, 300), Image.Resampling.LANCZOS)  

        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle([0, 0, image.size[0], image.size[1]], radius=10, fill=255)

        rounded_image = ImageOps.fit(image, mask.size, centering=(1, 1))
        rounded_image.putalpha(mask)

        self.ctk_image = ctk.CTkImage(rounded_image, size=(370, 300))  
        self.service_image = self.ctk_image

        image_label = ctk.CTkLabel(parent, image=self.service_image, text="")
        image_label.pack(side='top', pady=(0, 10), padx=10)

    
        for img_path in images:
            small_image = Image.open(img_path)
            small_image = small_image.resize((115, 102), Image.Resampling.LANCZOS)

            small_ctk_image = ctk.CTkImage(small_image, size=(115, 90))

            small_image_label = ctk.CTkLabel(parent, image=small_ctk_image, text="")
            small_image_label.pack(side='left', pady=(10, 10), padx=5)

    def show_recommended(self, parent, title, price, image_path):
        formatted_path = image_path.replace("\\", "/")

        # Image 
        image = Image.open(image_path)
        image.resize((180, 120),Image.Resampling.LANCZOS)  
        self.ctk_image = ctk.CTkImage(image, size=(250, 230))  

        # Service frame for both image and text 
        service_frame = ctk.CTkFrame(parent, width=130, height=130, corner_radius=10, fg_color="white")
        service_frame.pack(padx=15, pady=10, side="left")

        image_label = ctk.CTkLabel(service_frame, image=self.ctk_image, text="")
        image_label.pack(pady=0.5)

        title_button = ctk.CTkButton(service_frame, text=title, text_color="black", font=("Helvetica", 18, 'bold'), fg_color="transparent", hover_color="white", command=lambda: self.button_clicked(crud.get_product_id_by_image(formatted_path)))
        title_button.pack(side="top", pady=5)

        price_label = ctk.CTkLabel(service_frame, text=price, font=("Helvetica", 12, 'bold'), text_color='#2F4D7D')
        price_label.pack()


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

    # Adding search functionality 
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

    def add_to_cart(self):
        crud.add_cart(self.product_id, self.product_name, self.price, self.category, self.image_path)
        tick_image_pil = Image.open(".\\photos\\green-tick.png").convert("RGBA")
        tick_image = ctk.CTkImage(tick_image_pil, size=(30, 30))  

        # Update the button text to "Added" and change the color to lightest green
        self.add_to_cart.configure(
            text="Added",
            image=tick_image,
            fg_color="#F2F2F2",
            command=lambda: None,
            text_color="green",
            hover_color="#F2F2F2"
        )


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

    def navigate_to_payment(self):
        crud.add_purchase(self.product_id, self.product_name, self.price, self.category, 'unchecked', self.image_path)
        if crud.check_product_in_cart(self.product_id) == True:
            crud.delete_cart(self.product_id)
        self.destroy()
        payment_app = payment.RentalApp()
        payment_app.mainloop()

    def notification(self):
        notifications = [
            {"title": "Item Available for Rent", 
            "message": "Sony a6400 is now available for rent. Click here to book it before it's gone!"
            }
        ]
        
        popup = tk.Toplevel(self)
        popup.overrideredirect(True)
        popup.geometry("320x400") 
        popup.configure(bg="white")

        # Notification header frame 
        header_frame = ctk.CTkFrame(popup, height=40, corner_radius=0, fg_color="white")
        header_frame.pack(padx=10, pady=(10, 0), fill="x", expand=False)

        header_label = ctk.CTkLabel(header_frame, text="Notifications", font=("Helvetica", 14), text_color="#2F4D7D")
        header_label.pack(side="left", padx=(10, 0), pady=5)

        # Content Frame 
        content_frame = ctk.CTkFrame(popup, corner_radius=0, fg_color="white")
        content_frame.pack(padx=10, pady=10, fill="both", expand=True)

        for notification in notifications:
            title_label = ctk.CTkLabel(content_frame, text=notification["title"], font=("Helvetica", 12, "bold"), text_color="black", anchor="w", justify="left")
            title_label.pack(anchor="w", padx=(10, 0), pady=(5, 0), fill="x")
            
            message_label = ctk.CTkLabel(content_frame, text=notification["message"], font=("Helvetica", 12), text_color="gray", wraplength=280, anchor="w", justify="left")
            message_label.pack(anchor="w", padx=(10, 0), pady=(0, 10), fill="x")

        # Position of notifcation window 
        x = self.bell_button.winfo_rootx() - 50  # Offset to center the popup under the button
        y = self.bell_button.winfo_rooty() + self.bell_button.winfo_height() + 10  # Offset to place it below the button

        # Adjust the x position to add a gap on the right side
        x = x - 20  # Adjust this value to increase or decrease the gap

        popup.geometry(f"+{x}+{y}")

    def navigate_to_cart(self):
        self.destroy()
        profile_app = profile_1.RentalApp()
        profile_app.create_dashboard()
        profile_app.on_click(profile_app.cart_button, profile_app.cart_hover_image, profile_app.create_cart)
        profile_app.mainloop()


if __name__ == "__main__":
    no_image = ".\\photos\\no-image.png"
    app = Description(product_id ='1d9ec61f-cc76-440c-bf35-250a9b74d779',product_name="Alpha 7 IV", price="3000", product_description="A high-quality mirrorless camera designed for professionals. aksldfjlk dasflkjalskd fl sfakjasdf flaklfsa djlkfdd alkfdasj lsdfka fsd lasdkf j lsdaf  kfsad l sdfakjasdfl sdalf lasfd jasdl; f", image_path=".\\photos\\camera.jpg", category = "accesories", images = [no_image, no_image, no_image])
    app.mainloop()
