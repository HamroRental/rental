from tkinter import *
from tkinter import filedialog
import sqlite3
import uuid
import io

root = Tk()
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS product(
        product_id TEXT PRIMARY KEY,
        product_name TEXT,
        category TEXT,
        price INT,
        description TEXT,
        image BLOB
        )"""
)
conn.commit()
conn.close()

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
        (unique_id, product_name.get(), category.get(), price.get(), description.get("1.0", END), blob_data),
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
    result = c.fetchone() # result will come in tuple for eg ('adsflkjalskdf',)
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
        image_data = result[0]
        image = io.BytesIO(image_data)
        return image
    return None

def update():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    if image_path_editor.get():
        with open(image_path_editor.get(), 'rb') as file:
            blob_data = file.read()
        c.execute(
            """UPDATE product SET
                product_name = :product_name,
                category = :category,
                price = :price,
                description = :description,
                image = :image
                WHERE product_id = :id""",
            {
                "product_name": product_name_editor.get(),
                "category": category_editor.get(),
                "price": price_editor.get(),
                "description": description_editor.get("1.0", END),
                "image": blob_data,
                "id": global_product_id,
            },
        )
    else:
        c.execute(
            """UPDATE product SET
                product_name = :product_name,
                category = :category,
                price = :price,
                description = :description
                WHERE product_id = :id""",
            {
                "product_name": product_name_editor.get(),
                "category": category_editor.get(),
                "price": price_editor.get(),
                "description": description_editor.get("1.0", END),
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

    for record in records:
        product_name_editor.insert(0, record[1])
        category_editor.insert(0, record[2])
        price_editor.insert(0, record[3])
        description_editor.insert("1.0", record[4])
        image_path_editor.insert(0, "")  # Assuming you have a way to get the image path, otherwise leave it blank

    btn_browse_editor = Button(editor, text="Browse", command=lambda: browse_image(image_path_editor))
    btn_browse_editor.grid(row=4, column=2)

    edit_btn = Button(editor, text="Save", command=update)
    edit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

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

btn_browse = Button(root, text="Browse", font=("Arial Bold", 15), command=browse_image)
btn_browse.place(x=400, y=450)
btn_add = Button(root, text="Add", font=("Arial Bold", 20), command=add)
btn_add.place(x=0, y=500)
btn_delete = Button(root, text="Delete", font=("Arial Bold", 20), command=delete)
btn_delete.place(x=250, y=600)
btn_update = Button(root, text="Update", font=("Arial Bold", 20), command=edit)
btn_update.place(x=370, y=600)

delete_box = Entry(root, width=40)
delete_box.place(x=250, y=550, height=19)

root.mainloop()
