import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw
import crud, homepage, search, payment, login
import tkinter as tk
from tkinter import ttk, font , Canvas, messagebox

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
        self.side_frame.pack(fill='y', side='left', padx=(20, 0), pady=20)

        self.home_image = ctk.CTkImage(light_image=Image.open(".\\photos\\home.png"), size=(20, 20))
        self.home_hover_image = ctk.CTkImage(light_image=Image.open(".\\photos\\home1.png"), size=(20, 20))
        self.cart_image = ctk.CTkImage(light_image=Image.open(".\\photos\\cart2.png"), size=(20, 20))
        self.cart_hover_image = ctk.CTkImage(light_image=Image.open(".\\photos\\cart1.png"), size=(20, 20))
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
        self.dashboard_button.pack(anchor="w", padx=(20, 30), pady=(40, 2))

        self.dashboard_button.bind("<Enter>", lambda e: self.on_enter(self.dashboard_button, self.home_hover_image))
        self.dashboard_button.bind("<Leave>", lambda e: self.on_leave(self.dashboard_button, self.home_image))

        self.cart_button = ctk.CTkButton(
            self.side_frame,
            text="My Cart",
            image=self.cart_image,
            compound="left",
            text_color='#97A8C3',
            font=("Helvetica", 12, 'bold'),
            fg_color='#F2F2F2',
            hover_color='#2F4D7D',
            height=50,
            width=180,
            anchor='w',
            command=lambda: self.on_click(self.cart_button, self.cart_hover_image, self.create_cart)
        )
        self.cart_button.pack(anchor="w", padx=(20, 30), pady=(2, 5))

        self.cart_button.bind("<Enter>", lambda e: self.on_enter(self.cart_button, self.cart_hover_image))
        self.cart_button.bind("<Leave>", lambda e: self.on_leave(self.cart_button, self.cart_image))

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
            command=lambda: self.on_click(self.logout_button, self.logout_image, self.navigate_to_login)
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
        elif button == self.cart_button:
            return self.cart_image
        elif button == self.logout_button:
            return self.logout_image
        elif button == self.settings_button:
            return self.settings_image
        return None
    
    
    def create_dashboard(self):
        # Clear the current contents of the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Configure main frame grid layout
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        # Adding a customer info frame
        self.info_frame = ctk.CTkFrame(self.main_frame, fg_color='#F2F2F2', bg_color='#F2F2F2', width=430, height=220)
        self.info_frame.grid(row=0, column=0, padx=(50, 15), pady=30, sticky="nsew")

        # Adding a title label inside the info frame
        title_container = ctk.CTkFrame(self.info_frame, fg_color='#F2F2F2', bg_color='#F2F2F2')
        title_container.pack(fill='x', pady=(20, 20), padx=20)

        title_label = ctk.CTkLabel(title_container, text="Customer", font=("Helvetica", 20), text_color="Black")
        title_label.pack(side='left')

        # Adding an edit button to the right of the title label
        edit_button = ctk.CTkButton(
            title_container,
            text="Edit",
            font=("Helvetica", 15),
            text_color="#4B7BCC",
            fg_color='transparent',
            bg_color='transparent',
            hover_color='#F2F2F2',
        )
        edit_button.pack(side='right', padx=(0, 10))

        userid = crud.get_last_accessed_userid()
        username = crud.get_last_accessed_username()
        record = crud.get_user_info(userid)


        # Adding three rows for Name, Email, and Phone below the title label
        self.create_row(self.info_frame, "Name", username, ".\\photos\\face.png")
        self.create_row(self.info_frame, "Email", record['Email'], ".\\photos\\email.png")
        self.create_row(self.info_frame, "Phone", record['Phone_number'], ".\\photos\\phone.png")

        # Adding an address info frame
        self.address_info_frame = ctk.CTkFrame(self.main_frame, fg_color='#F2F2F2', bg_color='#F2F2F2', width=400, height=210)
        self.address_info_frame.grid(row=0, column=1, padx=(15, 50), pady=30, sticky="nsew")

        # Adding a title label inside the address info frame
        address_container = ctk.CTkFrame(self.address_info_frame, fg_color='#F2F2F2', bg_color='#F2F2F2')
        address_container.pack(fill='x', pady=(5, 10), padx=5)

        title_label = ctk.CTkLabel(address_container, text="Address", font=("Helvetica", 20), text_color="Black")
        title_label.pack(pady=(20, 10), side='left', padx=30, anchor='n')

        # Adding an edit button inside address info frame
        edit_button = ctk.CTkButton(
            address_container,
            text="Edit",
            font=("Helvetica", 15),
            text_color="#4B7BCC",
            fg_color='transparent',
            bg_color='transparent',
            hover_color='#F2F2F2',
        )
        edit_button.pack(pady=(20, 10), side='right', padx=(30, 10), anchor='n')

        # Adding three rows for Name, Email, and Phone below the title label
        self.create_address_row(self.address_info_frame, "Billing : ", "Mahaboudha,Kathamandu", ".\\photos\\location.png")
        self.create_address_row(self.address_info_frame, "Shipping : ", "Sundarbasti, Bhangal Bus Stop -08 , Kathmandu", ".\\photos\\location.png")

        # Create Table Frame
        table_frame = ttk.Frame(self.main_frame)
        table_frame.grid(row=1, column=0, columnspan=2, padx=(70, 80), pady=(40, 20), sticky="nsew")

        # Configure column and row weights to fill available space
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_columnconfigure(1, weight=1)
        table_frame.grid_columnconfigure(2, weight=1)
        table_frame.grid_columnconfigure(3, weight=1)

        # Define the column names
        columns = ['Product', 'Category', 'Price', 'status']

        # Configure column and row weights to fill available space
        for i in range(len(columns)):  # Ensure to match the number of columns
            table_frame.grid_columnconfigure(i, weight=1)

        # Configure row weights (if needed)
        table_frame.grid_rowconfigure(0, weight=1)  # Header row
        table_frame.grid_rowconfigure(1, weight=1)  # For the data rows, adjust as needed

        # Example data for demonstration
        # Example data for demonstration
        data = crud.get_purchase_items()
        print(data)

        # Determine the number of items in data
        item_count = len(data)

        # Set the item_count text color and background color based on the item count
        if item_count > 0:
            item_count_text = f"{item_count} Products"
            item_count_fg_color = 'green'
            item_count_bg_color = '#D1FAE5'  # Light green background
        else:
            item_count_text = "0 Products"
            item_count_fg_color = 'darkgrey'
            item_count_bg_color = '#F0F1F3'  # Light grey background

        # Create a frame to hold the label and the button
        recent_frame = tk.Frame(table_frame, bg='#F2F2F2')
        recent_frame.grid(row=0, column=0, columnspan=len(columns), padx=15, pady=10, sticky="w")

        # Create a label for "Recent Rentals"
        recent_label = tk.Label(recent_frame, text="Recent Rentals", bg='#F2F2F2', font=('Arial', 16, 'bold'))
        recent_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Create a button for the item count
        recent_button = ctk.CTkButton(recent_frame, text=item_count_text, 
                                    fg_color=item_count_bg_color, 
                                    hover_color='#C3F9D8',  # Optional: color when hovered
                                    text_color=item_count_fg_color,
                                    font=('Arial', 12, 'bold'), 
                                    width=80, 
                                    height=30,
                                    border_width=0)

        # Place the button in the frame next to the label
        recent_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Create canvas for rounded header
        header_canvas = tk.Canvas(table_frame, height=30, bg='#F7F8FA', bd=0, highlightthickness=0)
        header_canvas.grid(row=1, column=0, columnspan=len(columns), padx=10, pady=5, sticky="nsew")

        # Draw the rounded rectangle on the canvas
        self.create_rounded_rectangle(header_canvas, 0, 0, 700, 30, radius=10, fill='#F7F8FA', outline='#F0F1F3')

        # Create the header row with column names
        for col, column_name in enumerate(columns):
            col_label = ttk.Label(table_frame, text=column_name, font=('Arial', 13, 'bold'), background='#F7F8FA', foreground='#6B7280', anchor='w')
            col_label.grid(row=1, column=col, padx=15, pady=(5, 20), sticky="nsew")


        # Insert data into the table
        for row, record in enumerate(data, start=2):  # Start from row 2 due to the label and header row
            for col, value in enumerate(record[:4]):
                if col == 0:  # Product column with image
                    cell_frame = ttk.Frame(table_frame)
                    cell_frame.grid(row=row, column=col, padx=15, pady=10, sticky="w")

                    # Load and resize the image
                    img_path = record[4]  # Assuming the image path is at index 4
                    img = Image.open(img_path)
                    img = img.resize((60, 60), Image.Resampling.LANCZOS)  # Increased image size
                    img_tk = ImageTk.PhotoImage(img)

                    img_label = tk.Label(cell_frame, image=img_tk, bg='#E5E7EB')
                    img_label.image = img_tk  # Keep a reference to prevent garbage collection
                    img_label.grid(row=0, column=0, padx=(0, 10), pady=0)

                    cell_label = ttk.Label(cell_frame, text=value, font=('Arial', 12), foreground='#111827', anchor='w')
                    cell_label.grid(row=0, column=1, sticky="w")

                elif col == 3:  # Status column with colored badge
                    if 'settled' == value.lower():
                        status_color = 'green'
                        status_bg = '#D1FAE5'  # Light green background
                    else:
                        status_color = 'red'
                        status_bg = '#FFEDD5'  # Light red background

                    # Create the label with centered text
                    status_label = tk.Label(
                        table_frame,
                        text=value,
                        font=('Arial', 12, 'bold'),
                        foreground=status_color,
                        background=status_bg,
                        anchor='center',  # Center the text horizontally
                        justify='center'  # Center the text horizontally
                    )
                    
                    # Grid placement
                    status_label.grid(row=row, column=col, padx=15, pady=10, sticky="nw")


                else:  # Other columns
                    cell_label = ttk.Label(table_frame, text=value, font=('Arial', 12), foreground='#111827', anchor='w')
                    cell_label.grid(row=row, column=col, padx=15, pady=5, sticky="nsew")

        # Add padding below the table
        table_frame.grid_rowconfigure(len(data) + 2, weight=1)

        # Adjust the spacing between the table and the last element
        self.main_frame.grid_rowconfigure(2, weight=1)

        
        

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
        



            

    def create_cart(self):
        data = crud.get_cart_items()

        for widget in self.main_frame.winfo_children():
            widget.destroy()

        list_frame = ctk.CTkFrame(self.main_frame, fg_color='#F2F2F2', bg_color='#F2F2F2', width=400, height=100)
        list_frame.pack(side='top', fill='both', padx=80, pady=(30,10))

        checkboxes = []

        def toggle_all():
            select_all = top_checkbox.get() == 1
            for checkbox in checkboxes:
                checkbox.select() if select_all else checkbox.deselect()

        top_checkbox = ctk.CTkCheckBox(
            list_frame,
            fg_color='#D3D3D3',
            bg_color='#F2F2F2',
            border_color='#D3D3D3',
            text='',
            hover_color='#D3D3D3',
            checkmark_color='black',
            checkbox_height=17,
            checkbox_width=16,
            width=10,
            command=toggle_all
        )
        top_checkbox.pack(side='left', padx=(10, 0), pady=10, anchor='w')

        select_label = ctk.CTkLabel(list_frame, text=str(len(data)) + ' items', text_color='gray')
        select_label.pack(side='left', padx=(0, 30), fill='x')

        def delete_selected():
            selected_items = [checkbox for checkbox in checkboxes if checkbox.get() == 1]
            for checkbox in selected_items:
                index = checkboxes.index(checkbox)
                crud.delete_cart(data[index][-1])  # Assume item[-1] is the identifier for the item
            self.create_cart()  # Refresh the cart display

        delete_button = ctk.CTkButton(
            list_frame,
            text="Delete",
            font=("Helvetica", 15),
            text_color="red",
            fg_color='transparent',
            bg_color='transparent',
            hover_color='#F2F2F2',
            command=delete_selected
        )
        delete_button.pack(pady=10, side='right', padx=(30, 10), anchor='e')

        if not data:
            no_product_frame = ctk.CTkFrame(self.main_frame, fg_color='transparent')
            no_product_frame.pack(expand=True, pady=130)

            no_product_img = Image.open(".\\photos\\no-product.png")
            no_product_img = no_product_img.resize((250, 250), Image.Resampling.LANCZOS)
            no_product_photo = ImageTk.PhotoImage(no_product_img)

            no_product_label = ctk.CTkLabel(no_product_frame, image=no_product_photo, text="")
            no_product_label.image = no_product_photo
            no_product_label.pack()

            no_product_title = ctk.CTkLabel(no_product_frame, text='No Products   ', font=("Helvetica", 16))
            no_product_title.pack(pady=10)

        else:
            for item in data:
                product_frame = ctk.CTkFrame(self.main_frame, fg_color='#F2F2F2', bg_color='#F2F2F2', height=150)
                product_frame.propagate(False)
                product_frame.pack(side='top', fill='x', padx=80, pady=10)

                checkbox = ctk.CTkCheckBox(
                    product_frame,
                    fg_color='#D3D3D3',
                    bg_color='#F2F2F2',
                    border_color='#D3D3D3',
                    text='',
                    hover_color='#D3D3D3',
                    checkmark_color='black',
                    checkbox_height=17,
                    checkbox_width=16,
                    width=10
                )
                checkbox.pack(side='left', padx=(10, 0), pady=10, anchor='w')
                checkboxes.append(checkbox)

                product_img = Image.open(item[0])
                product_img = product_img.resize((150, 150), Image.Resampling.LANCZOS)
                product_photo = ImageTk.PhotoImage(product_img)
                product_label = ctk.CTkLabel(product_frame, image=product_photo, text="")
                product_label.image = product_photo
                product_label.pack(side='left', padx=10)

                title_label = ctk.CTkLabel(product_frame, text=item[1], font=("Helvetica", 20))
                title_label.pack(side='left', padx=10, anchor='w')

                price_label = ctk.CTkLabel(product_frame, text='Rs ' + str(item[2]) + ' / Day', text_color='#2F4D7D', font=("Helvetica", 16, 'bold'))
                price_label.pack(side='right', padx=40, anchor='e')

            def rent_now():
                selected_items = [checkbox for checkbox in checkboxes if checkbox.get() == 1]
                print(f"Selected checkboxes: {selected_items}")  # Debugging line
                if not selected_items:
                    print("No items selected.")  # Debugging line
                for checkbox in selected_items:
                    index = checkboxes.index(checkbox)
                    item = data[index]
                    crud.add_purchase(
                        product_id=item[-1],  # Assuming the last element is the product_id
                        product_name=item[1],
                        price=item[2],
                        category=item[3],  # Assuming the category is in item[4]
                        status='Pending',
                        image=item[0]
                    )
                self.navigate_to_payment()

            rent_now_button = ctk.CTkButton(
                self.main_frame,
                text="Rent Now",
                font=("Helvetica", 12),
                width=100,
                height=30,
                fg_color='#2F4D7D',
                text_color='white',
                corner_radius=5,
                command=rent_now
            )
            rent_now_button.pack(side='bottom', pady=20, anchor='e', padx =80)



    def create_settings(self):
        # Clear the current contents of the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create the title label
        title_label = ctk.CTkLabel(self.main_frame, text="Settings", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=20, side='top', padx=60, anchor='w')

        # Create the top frame to hold Customer and Address sections
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
        # Clear all entries in the specified frame
        for widget in frame.winfo_children():
            if isinstance(widget, ctk.CTkEntry):
                widget.delete(0, 'end')



    # Function to create rounded rectangle
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

    def navigate_to_payment(self):
        self.destroy()
        payment_app = payment.RentalApp()
        payment_app.mainloop()

    def navigate_to_login(self):
        self.destroy()
        login_app = login.Login()
        login_app.mainloop()

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

    

    

# Run the application
if __name__ == "__main__":
    app = RentalApp()
    app.mainloop()
