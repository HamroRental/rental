import tkinter as tk

root = tk.Tk()
root.title("E-commerce Add Product")

# Add Product Button
add_product_button = tk.Button(root, text="Add Product")

# Product Details Entry Fields
product_name_label = tk.Label(root, text="Product Name:")
product_name_entry = tk.Entry(root)
product_price_label = tk.Label(root, text="Price:")
product_price_entry = tk.Entry(root)

# Add Product Functionality
def add_product():
    product_name = product_name_entry.get()
    product_price = product_price_entry.get()
    # Add code to save product details or display confirmation message
    print(f"Product Name: {product_name}, Price: {product_price} added")

add_button = tk.Button(root, text="Add", command=add_product)

add_product_button.pack()
product_name_label.pack()
product_name_entry.pack()
product_price_label.pack()
product_price_entry.pack()
add_button.pack()

root.mainloop()