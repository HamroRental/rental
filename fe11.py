import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Set up customtkinter appearance
ctk.set_appearance_mode("System")  # System, Light, Dark
ctk.set_default_color_theme("blue")  # blue, dark-blue, green

class ProductApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rent it.")
        self.root.geometry("600x750")
        self.root.resizable(False, False)

        # Sidebar with navigation
        self.sidebar_frame = ctk.CTkFrame(self.root, width=200)
        self.sidebar_frame.pack(side="left", fill="y")

        ctk.CTkLabel(self.sidebar_frame, text="Rent it.", font=("Arial", 20, "bold")).pack(pady=20)

        self.add_product_button = ctk.CTkButton(self.sidebar_frame, text="Add Product", command=self.add_product)
        self.add_product_button.pack(pady=10, fill="x")

        self.manage_product_button = ctk.CTkButton(self.sidebar_frame, text="Manage Product")
        self.manage_product_button.pack(pady=10, fill="x")

        self.finance_button = ctk.CTkButton(self.sidebar_frame, text="Finance")
        self.finance_button.pack(pady=10, fill="x")

        self.settings_button = ctk.CTkButton(self.sidebar_frame, text="Settings")
        self.settings_button.pack(side="bottom", pady=10, fill="x")

        self.logout_button = ctk.CTkButton(self.sidebar_frame, text="Log Out", fg_color="red")
        self.logout_button.pack(side="bottom", pady=10, fill="x")

        # Main content area for product details
        self.content_frame = ctk.CTkFrame(self.root, width=400)
        self.content_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(self.content_frame, text="Product Details", font=("Arial", 16, "bold")).grid(row=0, column=0, sticky="w", pady=10, columnspan=2)

        # General Information Section
        ctk.CTkLabel(self.content_frame, text="Product Name").grid(row=1, column=0, sticky="w")
        self.product_name_entry = ctk.CTkEntry(self.content_frame, width=300)
        self.product_name_entry.grid(row=1, column=1, pady=5)

        ctk.CTkLabel(self.content_frame, text="Description").grid(row=2, column=0, sticky="nw")
        self.description_text = tk.Text(self.content_frame, width=45, height=4)
        self.description_text.grid(row=2, column=1, pady=5)

        # Media Section
        ctk.CTkLabel(self.content_frame, text="Media").grid(row=3, column=0, sticky="w")
        self.add_image_button = ctk.CTkButton(self.content_frame, text="Add Image", command=self.add_image)
        self.add_image_button.grid(row=3, column=1, sticky="w")

        self.image_frame = ctk.CTkFrame(self.content_frame)
        self.image_frame.grid(row=4, column=1, sticky="w")

        self.image_labels = []
        self.image_paths = []

        # Pricing Section
        ctk.CTkLabel(self.content_frame, text="Base Price").grid(row=5, column=0, sticky="w")
        self.price_entry = ctk.CTkEntry(self.content_frame, width=100)
        self.price_entry.grid(row=5, column=1, sticky="w", pady=5)

        # Variation Section
        ctk.CTkLabel(self.content_frame, text="Variation").grid(row=6, column=0, sticky="nw")

        self.variations_frame = ctk.CTkFrame(self.content_frame)
        self.variations_frame.grid(row=6, column=1, sticky="w")

        self.variation_types = []
        self.variation_entries = []

        self.add_variation_row("Color", "Black")
        self.add_variation_row("Color", "Gray")

        self.add_variation_button = ctk.CTkButton(self.content_frame, text="+ Add Variant", command=self.add_variation_row)
        self.add_variation_button.grid(row=7, column=1, sticky="w", pady=10)

        # Save/Cancel Buttons
        self.buttons_frame = ctk.CTkFrame(self.content_frame)
        self.buttons_frame.grid(row=8, column=1, sticky="e", pady=20)

        self.save_button = ctk.CTkButton(self.buttons_frame, text="Save Product", command=self.save_product)
        self.save_button.grid(row=0, column=1, padx=10)

        self.cancel_button = ctk.CTkButton(self.buttons_frame, text="Cancel", command=self.root.quit)
        self.cancel_button.grid(row=0, column=0, padx=10)

    def add_product(self):
        print("Add Product Clicked")

    def add_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_paths.append(file_path)
            if len(self.image_labels) < 3:  # Allow up to 3 images
                label = ctk.CTkLabel(self.image_frame, text=file_path.split("/")[-1], fg_color="green")
                label.pack(side="left", padx=5)
                self.image_labels.append(label)

    def add_variation_row(self, var_type="Color", var_value=""):
        var_type_entry = ctk.CTkComboBox(self.variations_frame, values=["Color", "Size"], width=100)
        var_type_entry.set(var_type)
        var_type_entry.pack(side="left", padx=5, pady=5)
        var_value_entry = ctk.CTkComboBox(self.variations_frame, values=["Black", "Gray", "Red", "Blue"], width=100)
        var_value_entry.set(var_value)
        var_value_entry.pack(side="left", padx=5, pady=5)

        remove_button = ctk.CTkButton(self.variations_frame, text="X", width=10, command=lambda: self.remove_variation_row(var_type_entry, var_value_entry, remove_button))
        remove_button.pack(side="left", padx=5, pady=5)

        self.variation_types.append(var_type_entry)
        self.variation_entries.append(var_value_entry)

    def remove_variation_row(self, var_type_entry, var_value_entry, remove_button):
        var_type_entry.pack_forget()
        var_value_entry.pack_forget()
        remove_button.pack_forget()
        self.variation_types.remove(var_type_entry)
        self.variation_entries.remove(var_value_entry)

    def save_product(self):
        product_name = self.product_name_entry.get()
        description = self.description_text.get("1.0", tk.END).strip()
        price = self.price_entry.get()
        variations = [(var_type.get(), var_entry.get()) for var_type, var_entry in zip(self.variation_types, self.variation_entries)]

        if not product_name or not description or not price or not variations:
            messagebox.showwarning("Missing Information", "Please fill out all fields before saving.")
            return

        # Save product data
        print(f"Product Name: {product_name}")
        print(f"Description: {description}")
        print(f"Price: {price}")
        print(f"Variations: {variations}")
        print(f"Images: {self.image_paths}")

        messagebox.showinfo("Product Saved", f"Product '{product_name}' has been saved successfully!")

if __name__ == "__main__":
    root = ctk.CTk()
    app = ProductApp(root)
    root.mainloop()
