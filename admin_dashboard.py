import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw
import crud, homepage, search, login, admin_profile
import tkinter as tk
from tkinter import ttk, font , Canvas, filedialog, messagebox
from random import randint

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

class RentalApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rent it.")
        self.geometry("1280x750")

        self.active_button = None

        # Title Bar Frame 
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
        self.profile_button = ctk.CTkButton(self.menu_icon_frame, image=self.profile_image, text="", width=40, height=40, fg_color="#2F4D7D", hover_color='#2F4D7D', command = self.navigate_to_admin_profile)
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
            command=lambda: self.on_click(self.logout_button, self.logout_image, self.logout)
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

        data = crud.get_admin_rental1()
        print(data)

        # the tuple that get_admin_rental provides is (product_name,product_id, category, price,status, created_at, image) so writing down their index
        price_index = 3
        status_index = 4

        def to_numeric(value):
            return float(value)  

        self.total_revenue = sum(to_numeric(item[price_index]) for item in data)
        self.total_rent = len(data)
        self.product_count = self.total_rent
        self.total_balance = sum(to_numeric(item[price_index]) for item in data if item[status_index] == 'settled')

    def on_enter(self, button, hover_image):
        if self.active_button != button:
            if button == self.logout_button:
                button.configure(image=hover_image, text_color="white", fg_color='#8B0000')  
            else:
                button.configure(image=hover_image, text_color="white", fg_color='#2F4D7D')  

    def on_leave(self, button, image):
        if self.active_button != button:
            button.configure(image=image, text_color='#97A8C3', fg_color='#F2F2F2')

    def on_click(self, button, hover_image, callback=None):
        if self.active_button:
            self.active_button.configure(image=self.get_default_image(self.active_button), text_color='#97A8C3', fg_color='#F2F2F2')
            self.active_button.bind("<Enter>", lambda e: self.on_enter(self.active_button, hover_image))
            self.active_button.bind("<Leave>", lambda e: self.on_leave(self.active_button, hover_image))

        self.active_button = button

        if button == self.logout_button:
            self.active_button.configure(fg_color="#8B0000", text_color="white")  
        else:
            self.active_button.configure(fg_color="#2F4D7D", text_color="white")

        self.active_button.unbind("<Enter>")
        self.active_button.unbind("<Leave>")

        if callback:
            callback()

    def get_default_image(self, button):
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
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_columnconfigure(3, weight=1)
        self.main_frame.grid_columnconfigure(4, weight=1)

        welcome_label = ctk.CTkLabel(self.main_frame, text="Welcome, User", font=("Arial", 16, 'bold'))
        welcome_label.grid(row=0, column=0, padx=40, pady=(30, 10), sticky="w")

        # Refresh the total revenue, rent, product count, and balance from the database
        self.total_revenue = crud.total_revenue()
        self.total_rent = crud.count_products()
        self.product_count = crud.count_products()
        self.total_balance = crud.total()

        # Add Product Button
        add_product_button = ctk.CTkButton(self.main_frame, text="+ Add Product", fg_color="#2F4D7D", font=("Arial", 12, 'bold'), width = 25, height = 35)
        add_product_button.grid(row=0, column=4, padx=30, pady=(30, 20), sticky="n")

        # The four cards 
        # Revenue Card 
        revenue_card = ctk.CTkFrame(self.main_frame, width=150, height=150, fg_color="#F2F2F2", bg_color='#F2F2F2')
        revenue_card.pack_propagate(False)
        revenue_card.grid(row=1, column=0, padx=(30, 10), pady=(5, 10), columnspan=2, sticky="nsew")

        image = Image.open(".\\photos\\revenue.png")
        image = image.resize((60, 60), Image.Resampling.LANCZOS)  

        image_tk = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(revenue_card, image=image_tk, text = "")
        image_label.image = image_tk  # Keeping a reference to the image to prevent garbage collection
        image_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")

        revenue_label = ctk.CTkLabel(revenue_card, text="Total Revenue", font=("Arial", 14))
        revenue_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        revenue_value = ctk.CTkLabel(revenue_card, text=f"Rs.{self.total_revenue}", font=("Arial", 24, "bold"))
        revenue_value.grid(row=2, column=0, padx=20, sticky="w")

        # Rent Card
        rent_card = ctk.CTkFrame(self.main_frame, width=100, height=150, fg_color='#F2F2F2')
        rent_card.pack_propagate(False)
        rent_card.grid(row=1, column=2, padx=(30, 70), pady=(5,10), columnspan = 3, sticky = 'nsew')

        image = Image.open(".\\photos\\renting.png")
        image = image.resize((60, 60), Image.Resampling.LANCZOS)  
        image_tk = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(rent_card, image=image_tk, text = "")
        image_label.image = image_tk  # Keep a reference to the image to prevent garbage collection
        image_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")

        rent_label = ctk.CTkLabel(rent_card, text="Total Rent", font=("Arial", 14))
        rent_label.grid(row=1, column=0, padx = 20, pady =5, sticky = "w")

        rent_value = ctk.CTkLabel(rent_card, text=self.total_rent, font=("Arial", 24, "bold"))
        rent_value.grid(row=2, column =0, padx =(30,20), pady=(1,5),sticky = 'nw')

        # Product ID Card
        product_id_card = ctk.CTkFrame(self.main_frame, width=170, height=150, fg_color='#F2F2F2')
        product_id_card.pack_propagate(False)
        product_id_card.grid(row=2, column=0, padx=(30,10), pady=10, columnspan = 2, sticky = 'nswe')
        
        image = Image.open(".\\photos\\product_id.png")
        image = image.resize((60, 60), Image.Resampling.LANCZOS)  
        image_tk = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(product_id_card, image=image_tk, text = "")
        image_label.image = image_tk  # Keep a reference to the image to prevent garbage collection
        image_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        product_id_label = ctk.CTkLabel(product_id_card, text="Product Id", font=("Arial", 14))
        product_id_label.grid(row= 1, column =0, sticky = 'w', padx =20)

        product_id_value = ctk.CTkLabel(product_id_card, text=self.product_count, font=("Arial", 24, "bold"))
        product_id_value.grid(row=2, column = 0, sticky = 'w', padx = (30,10))

        # Balance Card
        balance_card = ctk.CTkFrame(self.main_frame, width=100, height=150, fg_color="#F2F2F2")
        balance_card.pack_propagate(False)
        balance_card.grid(row=2, column=2, padx=(30,70), pady=10, columnspan = 3, sticky = 'nswe')

        image = Image.open(".\\photos\\wallet.png")
        image = image.resize((60, 60), Image.Resampling.LANCZOS)  
        image_tk = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(balance_card, image=image_tk, text = "")
        image_label.image = image_tk  # Keep a reference to the image to prevent garbage collection
        image_label.grid(row=0, column=0, padx=20, pady=(10, 5), sticky="w")

        balance_label = ctk.CTkLabel(balance_card, text="Balance", font=("Arial", 14))
        balance_label.grid(row=1, column= 0, padx =20, pady = 5, sticky = 'w')

        balance_value = ctk.CTkLabel(balance_card, text=f"Rs. {self.total_balance}", font=("Arial", 24, "bold"))
        balance_value.grid(row=2, column =0, padx = 20, pady = (0, 15), sticky = 'w')

        # Table Frame 
        table_frame = ttk.Frame(self.main_frame)
        table_frame.grid(row=4, column=0, columnspan=5, padx=(50, 100), pady=(40, 20), sticky="nsew")
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_columnconfigure(1, weight=1)
        table_frame.grid_columnconfigure(2, weight=1)
        table_frame.grid_columnconfigure(3, weight=1)

        # Define the column names
        columns = ['Product', 'Price', 'Category', 'status']

        for i in range(len(columns)):  
            table_frame.grid_columnconfigure(i, weight=1)
        table_frame.grid_rowconfigure(0, weight=1)  
        table_frame.grid_rowconfigure(1, weight=1)  

        data = crud.get_admin_rental()
        print(data)
        item_count = len(data)
        if item_count > 0:
            item_count_text = f"{item_count} Products"
            item_count_fg_color = 'green'
            item_count_bg_color = '#D1FAE5'  
        else:
            item_count_text = "0 Products"
            item_count_fg_color = 'darkgrey'
            item_count_bg_color = '#F0F1F3'  

        # Recent Frame to hold label and button 
        recent_frame = tk.Frame(table_frame, bg='#F2F2F2')
        recent_frame.grid(row=0, column=0, columnspan=len(columns), padx=15, pady=10, sticky="w")
        recent_label = tk.Label(recent_frame, text="Recent Rentals", bg='#F2F2F2', font=('Arial', 16, 'bold'))
        recent_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        recent_button = ctk.CTkButton(recent_frame, text=item_count_text, 
                                    fg_color=item_count_bg_color, 
                                    hover_color='#C3F9D8',  
                                    text_color=item_count_fg_color,
                                    font=('Arial', 12, 'bold'), 
                                    width=80, 
                                    height=30,
                                    border_width=0)

        recent_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Canvas for rounded header 
        header_canvas = tk.Canvas(table_frame, height=30, bg='#F7F8FA', bd=0, highlightthickness=0)
        header_canvas.grid(row=1, column=0, columnspan=len(columns), padx=10, pady=5, sticky="nsew")
        self.create_rounded_rectangle(header_canvas, 0, 0, 700, 30, radius=10, fill='#F7F8FA', outline='#F0F1F3')

        # Create the header row with column names
        for col, column_name in enumerate(columns):
            col_label = ttk.Label(table_frame, text=column_name, font=('Arial', 13, 'bold'), background='#F7F8FA', foreground='#6B7280', anchor='w')
            col_label.grid(row=1, column=col, padx=15, pady=(5, 20), sticky="nsew")

        for row, record in enumerate(data, start=2):  
            for col, value in enumerate(record[:4]):
                if col == 0: 
                    cell_frame = ttk.Frame(table_frame)
                    cell_frame.grid(row=row, column=col, padx=15, pady=10, sticky="w")
                    img_path = record[4]  
                    img = Image.open(img_path)
                    img = img.resize((60, 60), Image.Resampling.LANCZOS)  
                    img_tk = ImageTk.PhotoImage(img)

                    img_label = tk.Label(cell_frame, image=img_tk, bg='#E5E7EB')
                    img_label.image = img_tk  # Keep a reference to prevent garbage collection
                    img_label.grid(row=0, column=0, padx=(0, 10), pady=0)

                    cell_label = ttk.Label(cell_frame, text=value, font=('Arial', 12), foreground='#111827', anchor='w')
                    cell_label.grid(row=0, column=1, sticky="w")

                elif col == 3:  #status column
                    if 'settled' == value.lower():
                        status_color = 'green'
                        status_bg = '#D1FAE5'  
                    else:
                        status_color = 'red'
                        status_bg = '#FFEDD5'  

                    status_label = tk.Label(
                        table_frame,
                        text=value,
                        font=('Arial', 12, 'bold'),
                        foreground=status_color,
                        background=status_bg,
                        anchor='center', 
                        justify='center' 
                    )
                    
                    status_label.grid(row=row, column=col, padx=15, pady=10, sticky="nw")


                else:  
                    cell_label = ttk.Label(table_frame, text=value, font=('Arial', 12), foreground='#111827', anchor='w')
                    cell_label.grid(row=row, column=col, padx=15, pady=5, sticky="nsew")

        table_frame.grid_rowconfigure(len(data) + 2, weight=1)

        self.main_frame.grid_rowconfigure(2, weight=1)

               

    def create_row(self, parent, label_text, value_text, image_path):
        row_frame = ctk.CTkFrame(parent, fg_color='#F2F2F2')
        row_frame.pack(fill='x', pady=(10,5), padx=10)  

        icon_image = ctk.CTkImage(Image.open(image_path), size=(30, 30))
        icon_label = ctk.CTkLabel(row_frame, image=icon_image, text="")
        icon_label.grid(row=0, column=0, padx=(7, 5))

        text_label = ctk.CTkLabel(row_frame, text=label_text, font=("Helvetica", 14))
        text_label.grid(row=0, column=1, padx=(0, 20))

        value_label = ctk.CTkLabel(row_frame, text=value_text, font=("Helvetica", 14))
        value_label.grid(row=0, column=2, padx=(140, 10), sticky="e")


        
    def create_address_row(self, parent, label_text, value_text, image_path):
        row_frame = ctk.CTkFrame(parent, fg_color='#F2F2F2')
        row_frame.pack(fill='x', pady=(10, 5), padx=10)  

        icon_image = ctk.CTkImage(Image.open(image_path), size=(35, 35))
        icon_label = ctk.CTkLabel(row_frame, image=icon_image, text="")
        icon_label.grid(row=0, column=0, padx=(10, 10), rowspan = 2, sticky = 'n')

        text_label = ctk.CTkLabel(row_frame, text=label_text, font=("Helvetica", 14, 'bold'))
        text_label.grid(row=0, column=1, padx=(0, 10), sticky='w')

        value_label = ctk.CTkLabel(row_frame, text=value_text, font=("Helvetica", 14), wraplength=250, anchor="w")
        value_label.grid(row=0, column=2, padx=(10, 20), sticky='w', columnspan=2)
        

    def create_add_product(self):
        global product_name_entry
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Main Frame 
        main_container = ctk.CTkFrame(self.main_frame, fg_color='#e5e5e5', bg_color='#F2F2F2', width=800)
        main_container.pack(side='top', fill='both', padx=50, pady=30)

        # Top Frame for Save Button and Product Details Header
        top_frame = ctk.CTkFrame(main_container, fg_color='#e5e5e5', bg_color='#F2F2F2', width=800)
        top_frame.pack(side='top', fill='x', padx=10, pady=(10, 0))

        save_image = Image.open(".\\photos\\save.png")
        save_image_resized = save_image.resize((14, 14))  
        save_image_ctk = ctk.CTkImage(save_image_resized)

        save_button = ctk.CTkButton(top_frame, 
                                    text="Save Product", 
                                    font=("Helvetica", 12, 'bold'), 
                                    fg_color='#2F4D7D',  
                                    hover_color='#1E3A5C',
                                    text_color='#FFFFFF',
                                    corner_radius=10, 
                                    image=save_image_ctk, 
                                    height = 30,
                                    width= 30,
                                    compound="left", 
                                    command = self.save_product)
        save_button.pack(side='right', padx=10, pady=10)

        # Product Details Header
        product_details_label = ctk.CTkLabel(top_frame, text="Product Details", font=("Helvetica", 20, 'bold'))
        product_details_label.pack(side='left', padx=10, pady=10)

        # General Information Frame and Entries 
        general_info_frame = ctk.CTkFrame(main_container, fg_color='#F2F2F2', bg_color='#F2F2F2', width=800, height = 330, corner_radius=30)
        general_info_frame.propagate(False)
        general_info_frame.pack(side='top', fill='x', padx=10, pady=10)

        general_info_label = ctk.CTkLabel(general_info_frame, text="General Information", font=("Helvetica", 16, 'bold'))
        general_info_label.pack(side='top', anchor='w', padx=10, pady=(10, 0))

        product_name_label = ctk.CTkLabel(general_info_frame, text="Product Name", font=("Helvetica", 14))
        product_name_label.pack(side='top', anchor='w', padx=20, pady=(10, 0))

        self.product_name_entry = ctk.CTkEntry(general_info_frame, width=750, fg_color="#D3D3D3", border_color='#D3D3D3', height = 40)
        self.product_name_entry.pack(side='top', padx=20, pady=5, anchor='w')

        description_label = ctk.CTkLabel(general_info_frame, text="Description", font=("Helvetica", 14))
        description_label.pack(side='top', anchor='w', padx=20, pady=(10, 0))

        self.description_entry = ctk.CTkEntry(general_info_frame, width=750, height=150, fg_color="#D3D3D3", border_color='#D3D3D3')
        self.description_entry.pack(side='top', padx=20, pady=(5, 15), anchor='w')

        # Media Frame
        media_frame = ctk.CTkFrame(main_container, fg_color='#F2F2F2', bg_color='#F2F2F2', width=800)
        media_frame.pack(side='top', fill='x', padx=10, pady=10)

        media_label = ctk.CTkLabel(media_frame, text="Media", font=("Helvetica", 16, 'bold'))
        media_label.pack(side='top', anchor='w', padx=20, pady=(10, 0))

        add_image_frame = ctk.CTkFrame(media_frame, fg_color='#D3D3D3', width=750, height=100)
        add_image_frame.propagate(False)
        add_image_frame.pack(side='top', padx=20, pady=(5,10), anchor='w')

        add_image_label = ctk.CTkLabel(add_image_frame, text="Drag and drop image here, or click add image",
                                    font=("Helvetica", 12), text_color='gray')
        add_image_label.pack(side='top', pady=10, anchor='center')

        def add_image():
            self.image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
            if self.image_path:
                add_image_label.configure(text=self.image_path)
                self.selected_image_path = self.image_path

        add_image_button = ctk.CTkButton(add_image_frame, text="Add Image", font=("Helvetica", 14),corner_radius=10,
                                        bg_color='#2F4D7D', fg_color='#2F4D7D', command=add_image)
        add_image_button.pack(side='top', pady=10, anchor='center')

        # Additional Information Frame
        additional_info_frame = ctk.CTkFrame(main_container, fg_color='#F2F2F2', bg_color='#F2F2F2', width=800)
        additional_info_frame.pack(side='top', fill='x', padx=10, pady=10)

        additional_info_label = ctk.CTkLabel(additional_info_frame, text="Pricing", font=("Helvetica", 16, 'bold'))
        additional_info_label.pack(side='top', anchor='w', padx=10, pady=(10, 0))

        price_label = ctk.CTkLabel(additional_info_frame, text="Base Price", font=("Helvetica", 14))
        price_label.pack(side='top', anchor='w', padx=20, pady=(10, 0))

        self.price_entry = ctk.CTkEntry(additional_info_frame, width=750, fg_color="#D3D3D3", border_color='#D3D3D3')
        self.price_entry.pack(side='top', padx=20, pady=5, anchor='w')

        category_label = ctk.CTkLabel(additional_info_frame, text="Category", font=("Helvetica", 14))
        category_label.pack(side='top', anchor='w', padx=20, pady=(10, 0))

        self.category_entry = ctk.CTkEntry(additional_info_frame, width=750, fg_color="#D3D3D3", border_color='#D3D3D3')
        self.category_entry.pack(side='top', padx=20, pady=(5,15), anchor='w')



    def create_manage_product(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        header_frame = ctk.CTkFrame(self.main_frame, fg_color='transparent', height=50, corner_radius=10)
        header_frame.grid(row=0, column=0, columnspan=5, padx=20, pady=10, sticky="nsew", ipadx=500)

        product_label = ctk.CTkLabel(header_frame, text="Product", font=("Helvetica", 18, "bold"))
        product_label.grid(row=0, column=0, padx=(20, 10), sticky="w")

        add_product_button = ctk.CTkButton(header_frame, text="+ Add Product", text_color="white", 
                                        fg_color="#2F4D7D", hover_color="#2F4D7D", command=self.create_add_product,
                                        font=("Helvetica", 15))
        add_product_button.grid(row=0, column=4, padx=(50, 2), pady=5, sticky="e")

        search_frame = ctk.CTkFrame(self.main_frame, fg_color='transparent', corner_radius=8)
        search_frame.grid(row=1, column=0, columnspan=5, padx=20, pady=(15, 10), sticky="ew", ipadx=200)

        search_icon = ctk.CTkLabel(search_frame, text="🔍", text_color="gray", width=10)
        search_icon.grid(row=0, column=0, padx=(10, 5), pady=5, sticky="w")

        search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search product...", width=200, border_width=0)
        search_entry.grid(row=0, column=1, padx=(5, 10), pady=5, sticky="w")

        list_frame = ctk.CTkFrame(self.main_frame, fg_color='#e5e5e5', bg_color='#e5e5e5') 
        list_frame.grid(row=2, column=0, columnspan=5, padx=(30,20), pady=(10, 20), sticky="nsew")

        select_all_var = tk.IntVar()

        def toggle_all():
            select_all = select_all_var.get() == 1
            for checkbox in checkboxes:
                checkbox.set(1) if select_all else checkbox.set(0)

        top_checkbox = ctk.CTkCheckBox(
            list_frame,
            variable=select_all_var,
            fg_color='#D3D3D3',
            bg_color='#e5e5e5',
            border_color='#D3D3D3',
            text='Select All',
            hover_color='#D3D3D3',
            checkmark_color='black',
            checkbox_height=17,
            checkbox_width=16,
            width=10,
            command=toggle_all
        )
        top_checkbox.grid(row=0, column=0, padx=(10, 0), pady=10, sticky='w')

        delete_button = ctk.CTkButton(
            list_frame,
            text="Delete",
            font=("Helvetica", 15),
            text_color="red",
            fg_color='transparent',
            bg_color='transparent',
            hover_color='#e5e5e5',
            command=lambda: delete_selected()
        )
        delete_button.grid(row=0, column=4, padx=(0, 10), pady=10, sticky='e')

        checkboxes = []
        product_frames = []
        order_ids = []  

        data = crud.get_admin_rental()

        if not data:
            no_product_frame = ctk.CTkFrame(self.main_frame, fg_color='transparent')
            no_product_frame.grid(row=2, column=0, columnspan=5, padx=(10,20), pady=30, sticky="nsew")

            no_product_img = Image.open(".\\photos\\no-product.png")
            no_product_img = no_product_img.resize((250, 250), Image.Resampling.LANCZOS)
            no_product_photo = ImageTk.PhotoImage(no_product_img)

            no_product_label = ctk.CTkLabel(no_product_frame, image=no_product_photo, text="")
            no_product_label.image = no_product_photo
            no_product_label.grid(row=0, column=0, padx=10, pady=10)

            no_product_title = ctk.CTkLabel(no_product_frame, text='No Products   ', font=("Helvetica", 16))
            no_product_title.grid(row=1, column=0, padx=10, pady=10)
        else:
            for idx, record in enumerate(data):
                product_frame = ctk.CTkFrame(list_frame, fg_color='#F2F2F3', border_width=1, border_color='#F2F2F3', corner_radius=10, width=300)
                product_frame.propagate(False)
                product_frame.grid(row=idx+1, column=0, columnspan=5, padx=20, pady=10, sticky='nsew', ipadx=400)

                select_var = tk.IntVar()
                checkbox = ctk.CTkCheckBox(
                    product_frame,
                    variable=select_var,
                    fg_color='#D3D3D3',
                    bg_color='#F2F2F3',
                    border_color='#D3D3D3',
                    text='',
                    hover_color='#D3D3D3',
                    checkmark_color='black',
                    checkbox_height=17,
                    checkbox_width=16,
                    width=10
                )
                checkbox.grid(row=0, column=0, padx=10, pady=10, sticky='w')

                checkboxes.append(select_var)
                product_frames.append(product_frame)
                order_ids.append(record[-1])  

                img_path = record[4]
                img = Image.open(img_path)
                img = img.resize((60, 60), Image.Resampling.LANCZOS)
                img_tk = ImageTk.PhotoImage(img)

                img_label = ctk.CTkLabel(product_frame, image=img_tk, fg_color='white', text='')
                img_label.image = img_tk
                img_label.grid(row=0, column=1, padx=10, pady=10)

                details_frame = ctk.CTkFrame(product_frame, fg_color='#F2F2F3')
                details_frame.grid(row=0, column=2, padx=10, pady=10, sticky='w')

                product_name = ctk.CTkLabel(details_frame, text=record[0], font=("Helvetica", 14, "bold"))
                product_name.grid(row=0, column=0, sticky='w')

                product_details = ctk.CTkLabel(details_frame, text=f"Rs {record[1]}", font=("Helvetica", 12))
                product_details.grid(row=1, column=0, sticky='w')

                status_color = 'red' if 'unsettled' == record[3].lower() else 'green'
                status_bg = '#FFEDD5' if 'unsettled' == record[3].lower() else '#D1FAE5'

                status_label = ctk.CTkLabel(
                    product_frame,
                    text=record[3],
                    font=("Helvetica", 12, "bold"),
                    fg_color=status_bg,
                    text_color=status_color,
                    corner_radius=8,
                    width=80
                )
                status_label.grid(row=0, column=4, padx=10, pady=10, sticky='e')

        def delete_selected():
            for frame, checkbox, order_id in zip(product_frames, checkboxes, order_ids):
                if checkbox.get() == 1:
                    frame.destroy()
                    crud.delete_admin_cart(order_id)  

        self.main_frame.grid_rowconfigure(2, weight=1)






    def create_finance(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_columnconfigure(3, weight=1)
        self.main_frame.grid_columnconfigure(4, weight=1)

        welcome_label = ctk.CTkLabel(self.main_frame, text="Welcome, User", font=("Arial", 16, 'bold'))
        welcome_label.grid(row=0, column=0, padx=40, pady=(40, 10), sticky="w")

        add_product_button = ctk.CTkButton(self.main_frame, text="+ Add Product", fg_color="#2F4D7D", font=("Arial", 12, 'bold'), width=25, height=35, command = self.create_add_product)
        add_product_button.grid(row=0, column=4, padx=30, pady=(30, 20), sticky="n")
        self.total_revenue = crud.total_revenue()
        self.total_balance = crud.total()
        
        # Two cards 
        # Revenue Card
        revenue_card = ctk.CTkFrame(self.main_frame, width=150, height=150, fg_color="#F2F2F2", bg_color="#F2F2F2")
        revenue_card.pack_propagate(False)
        revenue_card.grid(row=1, column=0, padx=(30, 5), pady=(5, 10), columnspan=2, sticky="nsew")

        image = Image.open(".\\photos\\revenue.png")
        image = image.resize((60, 60), Image.Resampling.LANCZOS)
        image_tk = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(revenue_card, image=image_tk, text="")
        image_label.image = image_tk  # Keep a reference to the image to prevent garbage collection
        image_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")

        revenue_label = ctk.CTkLabel(revenue_card, text="Total Revenue", font=("Arial", 14))
        revenue_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")
        revenue_value = ctk.CTkLabel(revenue_card, text=f"Rs. {self.total_revenue}", font=("Arial", 24, "bold"))
        revenue_value.grid(row=2, column=0, padx=20, sticky="w")

        # Balance Card
        balance_card = ctk.CTkFrame(self.main_frame, width=100, height=150, fg_color="#F2F2F2", bg_color="#F2F2F2")
        balance_card.pack_propagate(False)
        balance_card.grid(row=1, column=2, padx=(40,100), pady=(5,10), columnspan=3, sticky="nswe")

        image = Image.open(".\\photos\\wallet.png")
        image = image.resize((60, 60), Image.Resampling.LANCZOS)
        image_tk = ImageTk.PhotoImage(image)

        image_label = ctk.CTkLabel(balance_card, image=image_tk, text="")
        image_label.image = image_tk  # Keep a reference to the image to prevent garbage collection
        image_label.grid(row=0, column=0, padx=20, pady=(10, 5), sticky="w")

        balance_label = ctk.CTkLabel(balance_card, text="Balance", font=("Arial", 14))
        balance_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        balance_value = ctk.CTkLabel(balance_card, text=f"Rs. {self.total_balance}", font=("Arial", 24, "bold"))
        balance_value.grid(row=2, column=0, padx=20, pady=(0, 15), sticky="w")

        # Table Frame
        table_frame = ttk.Frame(self.main_frame)
        table_frame.grid(row=2, column=0, columnspan=5, padx=(40, 150), pady=(40, 20), sticky="nsew", rowspan=5, ipady=50)
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_columnconfigure(1, weight=1)
        table_frame.grid_columnconfigure(2, weight=1)
        table_frame.grid_columnconfigure(3, weight=1)
        table_frame.grid_columnconfigure(4, weight=1)
        table_frame.grid_columnconfigure(5, weight=1)  

        columns = ['Product', 'Id', 'Category', 'Price', 'Status', 'Added']

        header_canvas = tk.Canvas(table_frame, height=30, bg='#F7F8FA', bd=0, highlightthickness=0)
        header_canvas.grid(row=0, column=0, columnspan=len(columns), padx=10, pady=5, sticky="nsew")
        self.create_rounded_rectangle(header_canvas, 0, 0, 700, 30, radius=10, fill='#F7F8FA', outline='#F0F1F3')

        for col, column_name in enumerate(columns):
            col_label = ttk.Label(table_frame, text=column_name, font=('Arial', 13, 'bold'), background='#F7F8FA', foreground='#6B7280', anchor='w')
            col_label.grid(row=0, column=col, padx=15, pady=10, sticky="nsew")

        data = crud.get_admin_rental1()

        for row, record in enumerate(data, start=1):
            for col, value in enumerate(record[:6]):
                if col == 0:  
                    cell_frame = ttk.Frame(table_frame)
                    cell_frame.grid(row=row, column=col, padx=15, pady=10, sticky="w")
                    
                    img_path = record[6]  
                    img = Image.open(img_path)
                    img = img.resize((60, 60), Image.Resampling.LANCZOS) 
                    img_tk = ImageTk.PhotoImage(img)

                    img_label = tk.Label(cell_frame, image=img_tk, bg='#E5E7EB')
                    img_label.image = img_tk  # Keep a reference to prevent garbage collection
                    img_label.grid(row=0, column=0, padx=(0, 10), pady=0)
                    
                    cell_label = ttk.Label(cell_frame, text=value, font=('Arial', 12), foreground='#111827', anchor='w')
                    cell_label.grid(row=0, column=1, sticky="w")
                
                elif col == 4:  
                    status_color = 'red' if value == 'unsettled' else 'green'
                    status_bg = '#FFEDD5' if value == 'unsettled' else '#D1FAE5'
                    
                    status_label = tk.Label(table_frame, text=value, font=('Arial', 12), fg=status_color, anchor='w',
                                            bg=status_bg, padx=15, pady=5)
                    status_label.grid(row=row, column=col, padx=15, pady=10, sticky="w")

                
                else:
                    cell_label = ttk.Label(table_frame, text=value, font=('Arial', 12), foreground='#111827', anchor='w')
                    cell_label.grid(row=row, column=col, padx=15, pady=10, sticky="w")

    
    def create_rounded_rectangle(self, canvas, x1, y1, x2, y2, radius=30, **kwargs):
        """Draws a rounded rectangle on the canvas."""
        points = [x1 + radius, y1,
                x1 + radius, y1,
                x2 - radius, y1,
                x2 - radius, y1,
                x2, y1,
                x2, y1 + radius,
                x2, y1 + radius,
                x2, y2 - radius,
                x2, y2 - radius,
                x2, y2,
                x2 - radius, y2,
                x2 - radius, y2,
                x1 + radius, y2,
                x1 + radius, y2,
                x1, y2,
                x1, y2 - radius,
                x1, y2 - radius,
                x1, y1 + radius,
                x1, y1 + radius,
                x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)



        
    
    def create_settings(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        title_label = ctk.CTkLabel(self.main_frame, text="Settings", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=20, side='top', padx=60, anchor='w')

        # Top frame that holds Customer and Address sections
        top_frame = ctk.CTkFrame(self.main_frame, fg_color='#F2F2F2', height=250, corner_radius=0)
        top_frame.pack_propagate(False)
        top_frame.pack(pady=(10, 5), padx=60, fill='x', side='top', anchor='w')

        # Create the 'Customer' frame
        customer_frame = ctk.CTkFrame(top_frame, fg_color='#F2F2F2', height=250, width=380, corner_radius=0)
        customer_frame.pack_propagate(False)
        customer_frame.pack(padx=(0, 10), side='left', anchor='w')

        customer_label = ctk.CTkLabel(customer_frame, text="Customer", font=("Helvetica", 16, "bold"))
        customer_label.pack(pady=(20, 10), padx=20, anchor='w')

        self.name_entry1 = ctk.CTkEntry(customer_frame, placeholder_text="Username", fg_color="#D3D3D3", border_color='#D3D3D3')
        self.name_entry1.pack(pady=5, padx=20, fill='x')

        self.email_entry1 = ctk.CTkEntry(customer_frame, placeholder_text="Email Address", fg_color='#D3D3D3', border_color='#D3D3D3')
        self.email_entry1.pack(pady=5, padx=20, fill='x')

        self.phone_entry1 = ctk.CTkEntry(customer_frame, placeholder_text="Phone Number", fg_color='#D3D3D3', border_color='#D3D3D3')
        self.phone_entry1.pack(pady=5, padx=20, fill='x')

        customer_button_frame = ctk.CTkFrame(customer_frame, fg_color='#F2F2F2')
        customer_button_frame.pack(pady=10, padx=20, fill='x', side='bottom', anchor='e')

        cancel_button = ctk.CTkButton(customer_button_frame, text="Cancel", fg_color="#E0E0E0", hover_color='#E0E0E0', text_color="black", command=lambda: self.clear_entries(customer_frame))
        cancel_button.pack(side='left', padx=5)

        save_button = ctk.CTkButton(customer_button_frame, text="Save Changes", fg_color="#1E3A8A", command=self.update_settings1)
        save_button.pack(side='left', padx=5)

        # Create the 'Address' frame
        address_frame = ctk.CTkFrame(top_frame, fg_color='#F2F2F2', height=250, width=380, corner_radius=0)
        address_frame.pack_propagate(False)
        address_frame.pack(padx=(10, 0), side='left', anchor='w')

        address_label = ctk.CTkLabel(address_frame, text="Address", font=("Helvetica", 16, "bold"))
        address_label.pack(pady=(20, 10), padx=20, anchor='w')

        self.shipping_entry1 = ctk.CTkEntry(address_frame, placeholder_text="Shipping Address", fg_color='#D3D3D3', border_color='#D3D3D3')
        self.shipping_entry1.pack(pady=5, padx=20, fill='x')

        self.billing_entry1 = ctk.CTkEntry(address_frame, placeholder_text="Billing Address", fg_color='#D3D3D3', border_color='#D3D3D3')
        self.billing_entry1.pack(pady=5, padx=20, fill='x')

        address_button_frame = ctk.CTkFrame(address_frame, fg_color='#F2F2F2')
        address_button_frame.pack(pady=10, padx=20, fill='x', side='bottom', anchor='e')

        cancel_button = ctk.CTkButton(address_button_frame, text="Cancel", fg_color="#E0E0E0", hover_color='#E0E0E0', text_color="black", command=lambda: self.clear_entries(address_frame))
        cancel_button.pack(side='left', padx=5)

        save_button = ctk.CTkButton(address_button_frame, text="Save Changes", fg_color="#1E3A8A", command=self.update_settings2)
        save_button.pack(side='left', padx=5)

        # Create the 'Update Password' frame
        update_frame = ctk.CTkFrame(self.main_frame, fg_color='#F2F2F2', height=250, width=800, corner_radius=0)
        update_frame.pack_propagate(False)
        update_frame.pack(pady=(10, 5), padx=60, fill='x', side='top', anchor='w')

        password_label = ctk.CTkLabel(update_frame, text="Update Password", font=("Helvetica", 16, "bold"))
        password_label.pack(pady=(20, 10), padx=20, anchor='w')

        self.current_password_entry1 = ctk.CTkEntry(update_frame, placeholder_text="Current Password", fg_color='#D3D3D3', border_color='#D3D3D3', show = "*")
        self.current_password_entry1.pack(pady=5, padx=20, fill='x')

        self.new_password_entry1 = ctk.CTkEntry(update_frame, placeholder_text="New Password", fg_color='#D3D3D3', border_color='#D3D3D3', show='*')
        self.new_password_entry1.pack(pady=5, padx=20, fill='x')

        self.confirm_password_entry1 = ctk.CTkEntry(update_frame, placeholder_text="Confirm Password", fg_color='#D3D3D3', border_color='#D3D3D3', show = '*')
        self.confirm_password_entry1.pack(pady=5, padx=20, fill='x')

        password_button_frame = ctk.CTkFrame(update_frame, fg_color='#F2F2F2')
        password_button_frame.pack(pady=10, padx=20, fill='x', side='bottom', anchor='e')

        cancel_button = ctk.CTkButton(password_button_frame, text="Cancel", fg_color="#E0E0E0", hover_color='#E0E0E0', text_color="black", command=lambda: self.clear_entries(update_frame))
        cancel_button.pack(side='left', padx=5)

        save_button = ctk.CTkButton(password_button_frame, text="Save Changes", fg_color="#1E3A8A", command=self.update_settings3)
        save_button.pack(side='left', padx=5)

    def clear_entries(self, frame):
        for widget in frame.winfo_children():
            if isinstance(widget, ctk.CTkEntry):
                widget.delete(0, 'end')


    def show_products(self):
        search_query = self.search_entry.get().lower()  
        self.search_results = crud.search_products_by_category(search_query)  

        self.display_results(search_query, self.search_results)

    def display_results(self, search_query, search_results):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        if search_query:
            title_label_main = ctk.CTkLabel(self.main_frame, text=f"Search results for: {search_query}", font=("Helvetica", 18, 'bold'))
            title_label_main.pack(anchor='w', padx=20, pady=(20, 30))

        if search_results:
            row_frame = None
            products_in_row = 0

            for i, (product_name, price, image) in enumerate(search_results):
                if products_in_row == 0:
                    row_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
                    row_frame.pack(fill="x", padx=20, pady=10)

                self.add_service_placeholder(row_frame, product_name, f"Rs.{price} Per Day", image)

                products_in_row += 1

                if products_in_row >= 3:
                    products_in_row = 0
        else:
            no_results_label = ctk.CTkLabel(self.main_frame, text="No results found.", font=("Helvetica", 18, 'bold'))
            no_results_label.pack(anchor="n", pady=(40, 20))

        
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

    def save_product(self):
        product_id = randint(1000, 9999)
        product_name = self.product_name_entry.get()
        base_price = self.price_entry.get()
        category = self.category_entry.get()
        image_path = self.image_path if hasattr(self, 'selected_image_path') else ""
        
        crud.add_admin_rental(product_id, product_name,category, base_price,'unsettled', image_path)

    def update_settings1(self):
        logged_in = crud.get_last_accessed_username()
        crud.update_user_info(logged_in, self.name_entry1.get(), self.email_entry1.get(), self.phone_entry1.get())
        messagebox.showinfo('sucess', 'User Info Sucessfully Saved')

    def update_settings2(self):
        messagebox.showinfo('sucess', 'User Info Sucessfully Saved')

    def update_settings3(self):
        logged_in = crud.get_last_accessed_username()
        if self.new_password_entry1.get() != self.confirm_password_entry1.get():
            messagebox.showinfo('error', 'your new password and confirm password does not match')
        else:
            crud.update_user_password(logged_in, self.confirm_password_entry1)
            messagebox.showinfo('sucess', 'Password Sucessfully Changed')

    def logout(self):
        self.destroy()
        app = login.Login()
        app.mainloop()

    def navigate_to_admin_profile(self):
        self.destroy()
        app = admin_profile.RentalApp()
        app.mainloop()
        
if __name__ == "__main__":
    app = RentalApp()
    app.mainloop()
