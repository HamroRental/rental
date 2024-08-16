import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import crud, homepage, search

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

        # Create the title bar frame
        self.title_bar = ctk.CTkFrame(self, height=100, fg_color="#2F4D7D", corner_radius=0)
        self.title_bar.pack(fill="x", side="top")

        self.title_button = ctk.CTkButton(self.title_bar, text="Rent it.", font=("Helvetica", 30, 'bold'), text_color="white", hover_color="#2F4D7D", fg_color="#2F4D7D", command=self.navigate)
        self.title_button.pack(side="left", padx=10, pady=5)

        self.menu_icon_frame = ctk.CTkFrame(self.title_bar, fg_color="#2F4D7D", width=50)
        self.menu_icon_frame.pack(side="right", padx=20)

        self.menu_frame = ctk.CTkFrame(self.title_bar, width=100, fg_color="#2F4D7D")
        self.menu_frame.pack(side="left", fill="x", expand=True, pady=5, padx=(230, 150))

        self.search_frame = ctk.CTkFrame(self.menu_frame, width=500, fg_color="#2F4D7D")
        self.search_frame.pack(pady=20, padx=10, fill='x', expand=True)

        self.glass_image = ctk.CTkImage(light_image=Image.open(".\\photos\\white-glass.png"))

        self.search_container = ctk.CTkFrame(self.search_frame, fg_color="#6883AE", width=250, corner_radius=0)
        self.search_container.pack(fill='x', expand=True, padx=10, pady=5)

        self.search_entry_frame = ctk.CTkFrame(self.search_container, fg_color="#6883AE", width=70)
        self.search_entry_frame.pack(fill="x", padx=(1, 0), pady=0)

        self.search_entry = ctk.CTkEntry(self.search_entry_frame, placeholder_text="Rooms, Vehicles, Equipment, Clothes", height=27, border_width=0, corner_radius=0)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(0, 2))

        self.search_button = ctk.CTkButton(self.search_entry_frame, image=self.glass_image, text="", width=70, height=26, fg_color="#6883AE", hover_color="#6883AE", corner_radius=0, command=self.search)
        self.search_button.pack(side="right", fill="x", padx=(2.5, 0))

        icon_size = (30, 30)
        self.bell_image = ctk.CTkImage(light_image=Image.open(".\\photos\\Notification.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.profile_image = ctk.CTkImage(light_image=Image.open(".\\photos\\profile.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)
        self.heart_image = ctk.CTkImage(light_image=Image.open(".\\photos\\cart.png").resize(icon_size, Image.Resampling.LANCZOS), size=icon_size)

        self.bell_button = ctk.CTkButton(self.menu_icon_frame, image=self.bell_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.bell_button.pack(side="left", padx=1)
        self.heart_button = ctk.CTkButton(self.menu_icon_frame, image=self.heart_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.heart_button.pack(side="left", padx=1)
        self.profile_button = ctk.CTkButton(self.menu_icon_frame, image=self.profile_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D')
        self.profile_button.pack(side="left", padx=1)

        self.main_frame = ctk.CTkScrollableFrame(self, orientation='vertical', bg_color='transparent')
        self.main_frame.pack(fill="both", expand=True, padx=(20, 10), pady=1, side="right")

        self.side_frame = ctk.CTkFrame(self, width=300, corner_radius=10, bg_color="transparent", fg_color='transparent')
        self.side_frame.pack(fill='y', side='left', padx=(20, 0), pady=10)

        self.home_image = ctk.CTkImage(light_image=Image.open(".\\photos\\home.png"), size=(20, 20))
        self.home_hover_image = ctk.CTkImage(light_image=Image.open(".\\photos\\home1.png"), size=(20, 20))
        self.shopping_image = ctk.CTkImage(light_image=Image.open(".\\photos\\shopping.png"), size=(20, 20))
        self.shopping_hover_image = ctk.CTkImage(light_image=Image.open(".\\photos\\shopping1.png"), size=(20, 20))
        self.manage_image = ctk.CTkImage(light_image=Image.open(".\\photos\\manage.png"), size=(20, 20))
        self.manage_hover_image = ctk.CTkImage(light_image=Image.open(".\\photos\\manage1.png"), size=(20, 20))
        self.finance_image = ctk.CTkImage(light_image=Image.open(".\\photos\\finance.png"), size=(20, 20))
        self.finance_hover_image = ctk.CTkImage(light_image=Image.open(".\\photos\\finance1.png"), size=(20, 20))
        self.settings_image = ctk.CTkImage(light_image=Image.open(".\\photos\\wheel.png"), size=(20, 20))
        self.settings_hover_image = ctk.CTkImage(light_image=Image.open(".\\photos\\setting1.png"), size=(20, 20))
        self.logout_image = ctk.CTkImage(light_image=Image.open(".\\photos\\logout.png"), size=(20, 20))
        self.logout_hover_image = ctk.CTkImage(light_image=Image.open(".\\photos\\logout1.png"), size=(20, 20))

        self.dashboard_button = ctk.CTkButton(
            self.side_frame,
            text="Dashboard",
            image=self.home_image,
            compound="left",
            text_color='#97A8C3',
            font=("Helvetica", 12, 'bold'),
            fg_color='#F2F2F2',
            height=50,
            width=180,
            anchor='w',
            command=lambda: self.on_click(self.dashboard_button, self.home_hover_image, self.create_dashboard)
        )
        self.dashboard_button.pack(anchor="w", padx=(20, 30), pady=(30, 2))

        self.dashboard_button.bind("<Enter>", lambda e: self.on_enter(self.dashboard_button, self.home_hover_image))
        self.dashboard_button.bind("<Leave>", lambda e: self.on_leave(self.dashboard_button, self.home_image))

        self.add_product_button = ctk.CTkButton(
            self.side_frame,
            text="Add Product",
            image=self.shopping_image,
            compound="left",
            text_color='#97A8C3',
            font=("Helvetica", 12, 'bold'),
            fg_color='#F2F2F2',
            hover_color='#2F4D7D',
            height=50,
            width=180,
            anchor='w',
            command=lambda: self.on_click(self.add_product_button, self.shopping_hover_image, self.create_add_product)
        )
        self.add_product_button.pack(anchor="w", padx=(20, 30), pady=(2, 5))

        self.add_product_button.bind("<Enter>", lambda e: self.on_enter(self.add_product_button, self.shopping_hover_image))
        self.add_product_button.bind("<Leave>", lambda e: self.on_leave(self.add_product_button, self.shopping_image))

        self.manage_product_button = ctk.CTkButton(
            self.side_frame,
            text="Manage Product",
            image=self.manage_image,
            compound="left",
            text_color='#97A8C3',
            font=("Helvetica", 12, 'bold'),
            fg_color='#F2F2F2',
            hover_color='#2F4D7D',
            height=50,
            width=180,
            anchor='w',
            command=lambda: self.on_click(self.manage_product_button, self.manage_hover_image, self.create_manage_product)
        )
        self.manage_product_button.pack(anchor="w", padx=(20, 30), pady=(2, 5))

        self.manage_product_button.bind("<Enter>", lambda e: self.on_enter(self.manage_product_button, self.manage_hover_image))
        self.manage_product_button.bind("<Leave>", lambda e: self.on_leave(self.manage_product_button, self.manage_image))

        self.finance_button = ctk.CTkButton(
            self.side_frame,
            text="Finance",
            image=self.finance_image,
            compound="left",
            text_color='#97A8C3',
            font=("Helvetica", 12, 'bold'),
            fg_color='#F2F2F2',
            hover_color='#2F4D7D',
            height=50,
            width=180,
            anchor='w',
            command=lambda: self.on_click(self.finance_button, self.finance_hover_image, self.create_finance)
        )
        self.finance_button.pack(anchor="w", padx=(20, 30), pady=(2, 5))

        self.finance_button.bind("<Enter>", lambda e: self.on_enter(self.finance_button, self.finance_hover_image))
        self.finance_button.bind("<Leave>", lambda e: self.on_leave(self.finance_button, self.finance_image))

        self.logout_button = ctk.CTkButton(
            self.side_frame,
            text="Log out",
            image=self.logout_image,
            compound="left",
            text_color='#97A8C3',
            font=("Helvetica", 12, 'bold'),
            fg_color='#F2F2F2',
            hover_color='#8B0000',
            height=50,
            width=180,
            anchor='w',
            command=lambda: self.on_click(self.logout_button, self.logout_image)
        )
        self.logout_button.pack(anchor="w", padx=(20, 30), pady=(5, 0), side = 'bottom')

        self.logout_button.bind("<Enter>", lambda e: self.on_enter(self.logout_button, self.logout_hover_image))
        self.logout_button.bind("<Leave>", lambda e: self.on_leave(self.logout_button, self.logout_image))


        self.settings_button = ctk.CTkButton(
            self.side_frame,
            text="Settings",
            image=self.settings_image,
            compound="left",
            text_color='#97A8C3',
            font=("Helvetica", 12, 'bold'),
            fg_color='#F2F2F2',
            hover_color='#2F4D7D',
            height=50,
            width=180,
            anchor='w',
            command=lambda: self.on_click(self.settings_button, self.settings_image, self.create_settings)
        )
        self.settings_button.pack(anchor="w", padx=(20, 30), pady=(20, 0), side='bottom')
        self.settings_button.bind("<Enter>", lambda e: self.on_enter(self.settings_button, self.settings_hover_image))
        self.settings_button.bind("<Leave>", lambda e: self.on_leave(self.settings_button, self.settings_image))


    def on_enter(self, button, hover_image):
        if self.active_button != button:
            if button == self.logout_button:
                button.configure(image=hover_image, text_color="white", fg_color='#8B0000')  # Red hover color
            else:
                button.configure(image=hover_image, text_color="white", fg_color='#2F4D7D')  # Default hover color

    def on_leave(self, button, image):
        if self.active_button != button:
            button.configure(image=image, text_color='#97A8C3', fg_color='#F2F2F2')

    def on_click(self, button, hover_image, callback=None):
        if self.active_button:
            # Reset the previously active button
            self.active_button.configure(image=self.get_default_image(self.active_button), text_color='#97A8C3', fg_color='#F2F2F2')
            self.active_button.bind("<Enter>", lambda e: self.on_enter(self.active_button, hover_image))
            self.active_button.bind("<Leave>", lambda e: self.on_leave(self.active_button, hover_image))

        # Set the new active button
        self.active_button = button

        if button == self.logout_button:
            self.active_button.configure(fg_color="#8B0000", text_color="white")  # Red color on click
        else:
            self.active_button.configure(fg_color="#2F4D7D", text_color="white")

        # Unbind hover events for the active button
        self.active_button.unbind("<Enter>")
        self.active_button.unbind("<Leave>")

        if callback:
            callback()

    def get_default_image(self, button):
        # Return the default image for the button
        if button == self.dashboard_button:
            return self.home_image
        elif button == self.add_product_button:
            return self.shopping_image
        elif button == self.logout_button:
            return self.logout_image
        elif button == self.settings_button:
            return self.settings_image
        elif button == self.manage_product_button:
            return self.manage_image
        elif button == self.finance_button:
            return self.finance_image
        return None
    
    
    def create_dashboard(self):
        # Clear the current contents of the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Configure grid columns to push the button to the right
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_columnconfigure(3, weight=1)
        self.main_frame.grid_columnconfigure(4, weight=1)

        # Welcome Label
        welcome_label = ctk.CTkLabel(self.main_frame, text="Welcome, User", font=("Arial", 16, 'bold'))
        welcome_label.grid(row=0, column=0, padx=40, pady=(30, 10), sticky="w")

        # Add Product Button
        add_product_button = ctk.CTkButton(self.main_frame, text="+ Add Product", fg_color="#2F4D7D", font=("Arial", 12, 'bold'), width = 25, height = 35)
        add_product_button.grid(row=0, column=4, padx=30, pady=(30, 20), sticky="n")

        # Revenue Card
        revenue_card = ctk.CTkFrame(self.main_frame, width=150, height=150, fg_color="white")
        revenue_card.pack_propagate(False)
        revenue_card.grid(row=1, column=0, padx=(30, 10), pady=(5, 10), columnspan=2, sticky="nsew")

        # Load and resize the image
        image = Image.open(".\\photos\\revenue.png")
        image = image.resize((60, 60), Image.Resampling.LANCZOS)  # Increase size to 80x80 pixels

        # Convert to Tkinter Image
        image_tk = ImageTk.PhotoImage(image)

        # Place the image inside a label using Tkinter's Label widget
        image_label = ctk.CTkLabel(revenue_card, image=image_tk, text = "")
        image_label.image = image_tk  # Keep a reference to the image to prevent garbage collection
        image_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")

        # Revenue Label
        revenue_label = ctk.CTkLabel(revenue_card, text="Total Revenue", font=("Arial", 14))
        revenue_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        # Revenue Value and Change
        revenue_value = ctk.CTkLabel(revenue_card, text="Rs.7,500", font=("Arial", 24, "bold"))
        revenue_value.grid(row=2, column=0, padx=20, sticky="w")

        # Rent Card
        rent_card = ctk.CTkFrame(self.main_frame, width=100, height=150, fg_color='white')
        rent_card.pack_propagate(False)
        rent_card.grid(row=1, column=2, padx=(30, 70), pady=(5,10), columnspan = 3, sticky = 'nsew')

        # Load and resize the image
        image = Image.open(".\\photos\\renting.png")
        image = image.resize((60, 60), Image.Resampling.LANCZOS)  # Increase size to 80x80 pixels

        # Convert to Tkinter Image
        image_tk = ImageTk.PhotoImage(image)

        # Place the image inside a label using Tkinter's Label widget
        image_label = ctk.CTkLabel(rent_card, image=image_tk, text = "")
        image_label.image = image_tk  # Keep a reference to the image to prevent garbage collection
        image_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")

        rent_label = ctk.CTkLabel(rent_card, text="Total Rent", font=("Arial", 14))
        rent_label.grid(row=1, column=0, padx = 20, pady =5, sticky = "w")

        rent_value = ctk.CTkLabel(rent_card, text="3,500", font=("Arial", 24, "bold"))
        rent_value.grid(row=2, column =0, padx =20, pady=(1,5),sticky = 'nw')

        # Product ID Card
        product_id_card = ctk.CTkFrame(self.main_frame, width=170, height=150, fg_color='white')
        product_id_card.pack_propagate(False)
        product_id_card.grid(row=2, column=0, padx=(30,10), pady=10, columnspan = 2, sticky = 'nswe')
        
        # Load and resize the image
        image = Image.open(".\\photos\\product_id.png")
        image = image.resize((60, 60), Image.Resampling.LANCZOS)  # Increase size to 80x80 pixels

        # Convert to Tkinter Image
        image_tk = ImageTk.PhotoImage(image)

        # Place the image inside a label using Tkinter's Label widget
        image_label = ctk.CTkLabel(product_id_card, image=image_tk, text = "")
        image_label.image = image_tk  # Keep a reference to the image to prevent garbage collection
        image_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        product_id_label = ctk.CTkLabel(product_id_card, text="Product Id", font=("Arial", 14))
        product_id_label.grid(row= 1, column =0, sticky = 'w', padx =20)

        product_id_value = ctk.CTkLabel(product_id_card, text="10", font=("Arial", 24, "bold"))
        product_id_value.grid(row=2, column = 0, sticky = 'w', padx = 20)

        # Balance Card
        balance_card = ctk.CTkFrame(self.main_frame, width=100, height=150, fg_color="white")
        balance_card.pack_propagate(False)
        balance_card.grid(row=2, column=2, padx=(30,70), pady=10, columnspan = 3, sticky = 'nswe')

        # Load and resize the image
        image = Image.open(".\\photos\\wallet.png")
        image = image.resize((60, 60), Image.Resampling.LANCZOS)  # Increase size to 80x80 pixels

        # Convert to Tkinter Image
        image_tk = ImageTk.PhotoImage(image)

        # Place the image inside a label using Tkinter's Label widget
        image_label = ctk.CTkLabel(balance_card, image=image_tk, text = "")
        image_label.image = image_tk  # Keep a reference to the image to prevent garbage collection
        image_label.grid(row=0, column=0, padx=20, pady=(10, 5), sticky="w")

        balance_label = ctk.CTkLabel(balance_card, text="Balance", font=("Arial", 14))
        balance_label.grid(row=1, column= 0, padx =20, pady = 5, sticky = 'w')

        balance_value = ctk.CTkLabel(balance_card, text="Rs.2,500", font=("Arial", 24, "bold"))
        balance_value.grid(row=2, column =0, padx = 20, pady = (0, 15), sticky = 'w')
        

    def create_row(self, parent, label_text, value_text, image_path):
        # Creating a frame for each row
        row_frame = ctk.CTkFrame(parent, fg_color='#F2F2F2')
        row_frame.pack(fill='x', pady=(10,5), padx=10)  # Adjusted padding and placement

        # Loading and displaying the icon
        icon_image = ctk.CTkImage(Image.open(image_path), size=(30, 30))
        icon_label = ctk.CTkLabel(row_frame, image=icon_image, text="")
        icon_label.grid(row=0, column=0, padx=(7, 5))

        # Adding the label
        text_label = ctk.CTkLabel(row_frame, text=label_text, font=("Helvetica", 14))
        text_label.grid(row=0, column=1, padx=(0, 20))

        # Adding the value on the right
        value_label = ctk.CTkLabel(row_frame, text=value_text, font=("Helvetica", 14))
        value_label.grid(row=0, column=2, padx=(140, 10), sticky="e")


        
    def create_address_row(self, parent, label_text, value_text, image_path):
        # Creating a frame for each row
        row_frame = ctk.CTkFrame(parent, fg_color='#F2F2F2')
        row_frame.pack(fill='x', pady=(10, 5), padx=10)  # Adjusted padding and placement

        # Loading and displaying the icon
        icon_image = ctk.CTkImage(Image.open(image_path), size=(35, 35))
        icon_label = ctk.CTkLabel(row_frame, image=icon_image, text="")
        icon_label.grid(row=0, column=0, padx=(10, 10), rowspan = 2, sticky = 'n')

        # Adding the label, aligned to the center of the icon
        text_label = ctk.CTkLabel(row_frame, text=label_text, font=("Helvetica", 14, 'bold'))
        text_label.grid(row=0, column=1, padx=(0, 10), sticky='w')

        # Adding the value below the label for a wrapped layout
        value_label = ctk.CTkLabel(row_frame, text=value_text, font=("Helvetica", 14), wraplength=250, anchor="w")
        value_label.grid(row=0, column=2, padx=(10, 20), sticky='w', columnspan=2)
        



            

    def create_add_product(self):
        # Clear the current contents of the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create the dashboard layout in the main frame
        list_frame = ctk.CTkFrame(self.main_frame, fg_color='#F2F2F2', bg_color='#F2F2F2', width=400, height=50 )
        list_frame.pack(side='top', fill='both', padx=50, pady=30)

        # adding check box in the list frame at the left side 
        select_box = ctk.CTkCheckBox(
            list_frame, 
            fg_color='#D3D3D3', 
            bg_color='#F2F2F2', 
            border_color='#D3D3D3', 
            text ='', 
            hover_color='#D3D3D3',
            checkmark_color='black',
            checkbox_height=17,
            checkbox_width=16,
            width = 10
            )
        select_box.pack(side='left', padx=(10,0), pady=10, anchor ='w')

        select_label = ctk.CTkLabel(list_frame, text ='select all items', text_color='gray')
        select_label.pack(side = 'left', padx = (0,30), fill = 'x')
        
        # Adding delete button 
        delete_button = ctk.CTkButton(
            list_frame,
            text="Delete",
            font=("Helvetica", 15),
            text_color="red",
            fg_color='transparent',
            bg_color='transparent',
            hover_color='#F2F2F2',
        )
        delete_button.pack(pady=10, side='right', padx=(30, 10), anchor='e')


    def create_manage_product(self):
        # Clear the current contents of the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create the dashboard layout in the main frame
        list_frame = ctk.CTkFrame(self.main_frame, fg_color='#F2F2F2', bg_color='#F2F2F2', width=400, height=50 )
        list_frame.pack(side='top', fill='both', padx=50, pady=30)

        # adding check box in the list frame at the left side 
        select_box = ctk.CTkCheckBox(
            list_frame, 
            fg_color='#D3D3D3', 
            bg_color='#F2F2F2', 
            border_color='#D3D3D3', 
            text ='', 
            hover_color='#D3D3D3',
            checkmark_color='black',
            checkbox_height=17,
            checkbox_width=16,
            width = 10
            )
        select_box.pack(side='left', padx=(10,0), pady=10, anchor ='w')

        select_label = ctk.CTkLabel(list_frame, text ='select all items', text_color='gray')
        select_label.pack(side = 'left', padx = (0,30), fill = 'x')
        
        # Adding delete button 
        delete_button = ctk.CTkButton(
            list_frame,
            text="Delete",
            font=("Helvetica", 15),
            text_color="red",
            fg_color='transparent',
            bg_color='transparent',
            hover_color='#F2F2F2',
        )
        delete_button.pack(pady=10, side='right', padx=(30, 10), anchor='e')


    def create_finance(self):
        # Clear the current contents of the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Configure grid columns to push the button to the right
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_columnconfigure(3, weight=1)
        self.main_frame.grid_columnconfigure(4, weight=1)

        # Welcome Label
        welcome_label = ctk.CTkLabel(self.main_frame, text="Welcome, User", font=("Arial", 16, 'bold'))
        welcome_label.grid(row=0, column=0, padx=40, pady=(30, 10), sticky="w")

        # Add Product Button
        add_product_button = ctk.CTkButton(self.main_frame, text="+ Add Product", fg_color="#2F4D7D", font=("Arial", 12, 'bold'), width = 25, height = 35)
        add_product_button.grid(row=0, column=4, padx=30, pady=(30, 20), sticky="n")

        # Revenue Card
        revenue_card = ctk.CTkFrame(self.main_frame, width=150, height=150, fg_color="white")
        revenue_card.pack_propagate(False)
        revenue_card.grid(row=1, column=0, padx=(30, 40), pady=(5, 10), columnspan=2, sticky="nsew")

        # Load and resize the image
        image = Image.open(".\\photos\\revenue.png")
        image = image.resize((60, 60), Image.Resampling.LANCZOS)  # Increase size to 80x80 pixels

        # Convert to Tkinter Image
        image_tk = ImageTk.PhotoImage(image)

        # Place the image inside a label using Tkinter's Label widget
        image_label = ctk.CTkLabel(revenue_card, image=image_tk, text = "")
        image_label.image = image_tk  # Keep a reference to the image to prevent garbage collection
        image_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")

        # Revenue Label
        revenue_label = ctk.CTkLabel(revenue_card, text="Total Revenue", font=("Arial", 14))
        revenue_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        # Revenue Value and Change
        revenue_value = ctk.CTkLabel(revenue_card, text="Rs.7,500", font=("Arial", 24, "bold"))
        revenue_value.grid(row=2, column=0, padx=20, sticky="w")

        # Balance Card
        balance_card = ctk.CTkFrame(self.main_frame, width=100, height=150, fg_color="white")
        balance_card.pack_propagate(False)
        balance_card.grid(row=1, column=2, padx=(10,50), pady=(5,10), columnspan = 3, sticky = 'nswe')

        # Load and resize the image
        image = Image.open(".\\photos\\wallet.png")
        image = image.resize((60, 60), Image.Resampling.LANCZOS)  # Increase size to 80x80 pixels

        # Convert to Tkinter Image
        image_tk = ImageTk.PhotoImage(image)

        # Place the image inside a label using Tkinter's Label widget
        image_label = ctk.CTkLabel(balance_card, image=image_tk, text = "")
        image_label.image = image_tk  # Keep a reference to the image to prevent garbage collection
        image_label.grid(row=0, column=0, padx=20, pady=(10, 5), sticky="w")

        balance_label = ctk.CTkLabel(balance_card, text="Balance", font=("Arial", 14))
        balance_label.grid(row=1, column= 0, padx =20, pady = 5, sticky = 'w')

        balance_value = ctk.CTkLabel(balance_card, text="Rs.2,500", font=("Arial", 24, "bold"))
        balance_value.grid(row=2, column =0, padx = 20, pady = (0, 15), sticky = 'w')

        
    def create_settings(self):
        # Clear the current contents of the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create the title label
        title_label = ctk.CTkLabel(self.main_frame, text="Settings", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=20, side='top', padx=60, anchor='w')

        # Create the 'Update Password' frame
        update_frame = ctk.CTkFrame(self.main_frame, fg_color='#F2F2F2', height=800, width=800, corner_radius=0)
        update_frame.pack_propagate(False)
        update_frame.pack(pady=(10, 5), padx=60, side='top', anchor='w')

        update_label = ctk.CTkLabel(update_frame, text="Update Password", font=("Helvetica", 20, "bold"))
        update_label.pack(pady=(20,10), padx=20, anchor='w')

        current_password_entry = ctk.CTkEntry(update_frame, placeholder_text="Current Password", fg_color="#F2F2F2", border_color='gray')
        current_password_entry.pack(pady=5, padx=20, fill='x')

        new_password_entry = ctk.CTkEntry(update_frame, placeholder_text="New Password")
        new_password_entry.pack(pady=5, padx=20, fill='x')

        confirm_password_entry = ctk.CTkEntry(update_frame, placeholder_text="Confirm Password")
        confirm_password_entry.pack(pady=5, padx=20, fill='x')

        button_frame = ctk.CTkFrame(update_frame, fg_color='#F2F2F2')
        button_frame.pack(pady=10, padx=20, fill='x', side='bottom', anchor='e')

        cancel_button = ctk.CTkButton(button_frame, text="Cancel", fg_color="#E0E0E0", hover_color='#E0E0E0', text_color="black")
        cancel_button.pack(side='left', padx=5)

        save_button = ctk.CTkButton(button_frame, text="Save Changes", fg_color="#1E3A8A")
        save_button.pack(side='left', padx=5)

        # Create the 'Delete Account' frame
        delete_account_frame = ctk.CTkFrame(self.main_frame, fg_color='#F2F2F2', height=150, width=800, corner_radius=0)
        delete_account_frame.pack_propagate(False)
        delete_account_frame.pack(pady=10, padx=60, side='top', anchor='w')

        delete_label = ctk.CTkLabel(delete_account_frame, text="Delete Account", font=("Helvetica", 20, "bold"))
        delete_label.pack(pady=(20,10), padx=20, anchor='w')

        warning_label = ctk.CTkLabel(delete_account_frame, text="Deleting your account is permanent and cannot be reversed.", font=("Helvetica", 14))
        warning_label.pack(pady=5, padx=20, anchor='w')

        delete_button = ctk.CTkButton(delete_account_frame, text="Delete Account", fg_color="#B91C1C")
        delete_button.pack(pady=10, padx=20, anchor='w')




        
    def navigate(self):
        self.destroy()
        new_app = homepage.RentalApp()
        new_app.mainloop()

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

# Run the application
if __name__ == "__main__":
    app = RentalApp()
    app.mainloop()
