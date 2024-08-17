from tkinter import *
from tkinter import filedialog
import sqlite3
import uuid
import io, os 


# Database setup
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS product(
        product_id TEXT PRIMARY KEY,
        product_name TEXT,
        category TEXT,
        price INT,
        description TEXT,
        image TEXT,
        image1 TEXT,
        image2 TEXT,
        image3 TEXT
        )"""
)
conn.commit()
conn.close()

# User Databse 
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS Users(
        User_id TEXT PRIMARY KEY,
        Role TEXT,
        Fullname TEXT,
        Email TEXT,
        Password TEXT,
        Phone_number TEXT
        )"""
)
conn.commit()
conn.close()


# Function definitions
def generate_unique_id():
    return str(uuid.uuid4())

def add():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    unique_id = generate_unique_id()
    with open(image_path.get(), 'rb') as file:
        blob_data = file.read()
    c.execute(
        "INSERT INTO product(product_id, product_name, category, price, description, image) VALUES(?,?,?,?,?,?)",
        (unique_id, product_name.get(), category.get(), price.get(), description.get("1.0", END), image_path.get(), image_path1.get(), image_path2.get(), image_path3.get()),
    )
    conn.commit()
    conn.close()
    product_name.delete(0, END)
    category.delete(0, END)
    price.delete(0, END)
    description.delete("1.0", END)
    image_path.delete(0, END)

def delete():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("DELETE FROM product WHERE product_id=?", (delete_box.get(),))
    conn.commit()
    conn.close()
    delete_box.delete(0, END)

def browse_image(entry_widget=None):
    filename = filedialog.askopenfilename(initialdir="/", title="Select an Image",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    if entry_widget:
        entry_widget.delete(0, END)
        entry_widget.insert(0, filename)
    else:
        image_path.delete(0, END)
        image_path.insert(0, filename)

        

def get_product_id_by_image(image_path):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT product_id FROM product WHERE image=?', (image_path,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]  # Return the product_id
    return None  # Return None if no product matches the image path


def get_product_name(product_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT product_name FROM product WHERE product_id=?', (product_id,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    return None

def get_price(product_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT price FROM product WHERE product_id=?', (product_id,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    return None

def get_description(product_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT description FROM product WHERE product_id=?', (product_id,))
    result = c.fetchone() 
    conn.close()
    if result:
        return result[0]
    return None

def get_category(product_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT category FROM product WHERE product_id=?', (product_id,))
    result = c.fetchone() 
    conn.close()
    if result:
        return result[0]
    return None

def get_product_image(product_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT image FROM product WHERE product_id=?", (product_id,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]  # Return the image path as a string
    return ".\\photos\\no-image.png"

def get_product_images(product_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT image1, image2, image3 FROM product WHERE product_id=?", (product_id,))
    result = c.fetchone()
    conn.close()
    
    no_image_path = ".\\photos\\no-image.png"
    
    if result:
        # Ensure that each image path is valid, otherwise use the placeholder
        return [img if img and os.path.exists(img) else no_image_path for img in result]
    
    # If no images are found, return placeholders
    return [no_image_path, no_image_path, no_image_path]



def update():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute(
        """UPDATE product SET
            product_name = :product_name,
            category = :category,
            price = :price,
            description = :description,
            image = :image,
            image1 = :image1,
            image2 = :image2,
            image3 = :image3
            WHERE product_id = :id""",
        {
            "product_name": product_name_editor.get(),
            "category": category_editor.get(),
            "price": price_editor.get(),
            "description": description_editor.get("1.0", END),
            "image": image_path_editor.get(),
            "image1": image_path1_editor.get(),
            "image2": image_path2_editor.get(),
            "image3": image_path3_editor.get(),
            "id": global_product_id,
        },
    )
    
    conn.commit()
    conn.close()
    editor.destroy()

def edit():
    global editor
    global global_product_id
    global product_name_editor
    global category_editor
    global price_editor
    global description_editor
    global image_path_editor
    global image_path1_editor
    global image_path2_editor
    global image_path3_editor

    editor = Tk()
    editor.title("Update Product")
    editor.geometry("600x500")

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    global_product_id = delete_box.get()
    c.execute("SELECT * FROM product WHERE product_id=?", (global_product_id,))
    records = c.fetchall()

    product_name_editor = Entry(editor, width=30)
    product_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    category_editor = Entry(editor, width=30)
    category_editor.grid(row=1, column=1)
    price_editor = Entry(editor, width=30)
    price_editor.grid(row=2, column=1)
    description_editor = Text(editor, width=30, height=10)
    description_editor.grid(row=3, column=1)
    image_path_editor = Entry(editor, width=30)
    image_path_editor.grid(row=4, column=1)
    image_path1_editor = Entry(editor, width=30)
    image_path1_editor.grid(row=5, column=1)
    image_path2_editor = Entry(editor, width=30)
    image_path2_editor.grid(row=6, column=1)
    image_path3_editor = Entry(editor, width=30)
    image_path3_editor.grid(row=7, column=1)

    product_name_label = Label(editor, text="Product Name")
    product_name_label.grid(row=0, column=0, pady=(10, 0))
    category_label = Label(editor, text="Category")
    category_label.grid(row=1, column=0)
    price_label = Label(editor, text="Price")
    price_label.grid(row=2, column=0)
    description_label = Label(editor, text="Description")
    description_label.grid(row=3, column=0)
    image_path_label = Label(editor, text="Image Path")
    image_path_label.grid(row=4, column=0)
    image_path_label1 = Label(editor, text="Image Path")
    image_path_label1.grid(row=5, column=0)
    image_path_label2 = Label(editor, text="Image Path")
    image_path_label2.grid(row=6, column=0)
    image_path_label3 = Label(editor, text="Image Path")
    image_path_label3.grid(row=7, column=0)

    for record in records:
        product_name_editor.insert(0, record[1])
        category_editor.insert(0, record[2])
        price_editor.insert(0, record[3])
        description_editor.insert("1.0", record[4])
        image_path_editor.insert(0, "")
        image_path1_editor.insert(0, "")
        image_path2_editor.insert(0, "")
        image_path3_editor.insert(0, "")

    btn_browse_editor = Button(editor, text="Browse", command=lambda: browse_image(image_path_editor))
    btn_browse_editor.grid(row=4, column=2)
    btn_browse_editor1 = Button(editor, text="Browse", command=lambda: browse_image(image_path1_editor))
    btn_browse_editor1.grid(row=5, column=2)
    btn_browse_editor2 = Button(editor, text="Browse", command=lambda: browse_image(image_path2_editor))
    btn_browse_editor2.grid(row=6, column=2)
    btn_browse_editor3 = Button(editor, text="Browse", command=lambda: browse_image(image_path3_editor))
    btn_browse_editor3.grid(row=7, column=2)
    

    edit_btn = Button(editor, text="Save", command=update)
    edit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

# Adding search function to retrieve data 
def search_products_by_category(category):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    if category is None:
        category = ""  # Default value or handle as needed
    c.execute("SELECT product_name, price, image FROM product WHERE lower(category) LIKE ? OR lower(product_name) LIKE ?", ('%' + category + '%', '%' + category + '%'))
    results = c.fetchall()
    conn.close()
    return results

# Main loop
if __name__ == "__main__":
    root = Tk()

    label_product_name = Label(root, text="Product Name", font=("Arial Bold", 20))
    label_product_name.place(x=0, y=90)
    label_category = Label(root, text='Category', font=("Arial Bold", 20))
    label_category.place(x=0, y=140)
    label_price = Label(root, text='Price', font=("Arial Bold", 20))
    label_price.place(x=0, y=190)
    label_description = Label(root, text="Description", font=("Arial Bold", 20))
    label_description.place(x=0, y=240)
    label_image = Label(root, text='Image', font=("Arial Bold", 20))
    label_image.place(x=0, y=450)
    label_image1 = Label(root, text='Image1', font=("Arial Bold", 20))
    label_image1.place(x=0, y=500)
    label_image2 = Label(root, text='Image2', font=("Arial Bold", 20))
    label_image2.place(x=0, y=550)
    label_image3 = Label(root, text='Image3', font=("Arial Bold", 20))
    label_image3.place(x=0, y=600)


    product_name = Entry(root, width=30)
    product_name.place(x=200, y=100, height=30)
    category = Entry(root, width=30)
    category.place(x=200, y=150, height=30)
    price = Entry(root, width=30)
    price.place(x=200, y=200, height=30)
    description = Text(root, width=30, height=10)
    description.place(x=200, y=250)
    image_path = Entry(root, width=30)
    image_path.place(x=200, y=450, height=30)
    image_path1 = Entry(root, width = 30)
    image_path1.place(x=200, y = 500 , height = 30)
    image_path2 = Entry(root, width = 30)
    image_path2.place(x=200, y = 550 , height = 30)
    image_path3 = Entry(root, width = 30)
    image_path3.place(x=200, y = 600 , height = 30)



    btn_browse = Button(root, text="Browse", font=("Arial Bold", 10), command=browse_image, height = 1)
    btn_browse.place(x=400, y=450)
    btn_browse1 = Button(root, text="Browse", font=("Arial Bold", 10), command=browse_image, height = 1)
    btn_browse1.place(x=400, y=500)
    btn_browse2 = Button(root, text="Browse", font=("Arial Bold", 10), command=browse_image, height = 1)
    btn_browse2.place(x=400, y=550)
    btn_browse3 = Button(root, text="Browse", font=("Arial Bold", 10), command=browse_image, height = 1)
    btn_browse3.place(x=400, y=600)
    btn_add = Button(root, text="Add", font=("Arial Bold", 20), command=add)
    btn_add.place(x=0, y=650)
    btn_delete = Button(root, text="Delete", font=("Arial Bold", 20), command=delete)
    btn_delete.place(x=250, y=800)
    btn_update = Button(root, text="Update", font=("Arial Bold", 20), command=edit)
    btn_update.place(x=370, y=800)

    delete_box = Entry(root, width=40)
    delete_box.place(x=250, y=750, height=35)



    root.mainloop()
