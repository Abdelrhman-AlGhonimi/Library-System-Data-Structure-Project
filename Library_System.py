import tkinter as tk
from tkinter import messagebox
import os
import json
from tkinter import PhotoImage

# Data file
DATA_FILE = "library_data.json"

# Load data from file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            # Ensure the key next_customer_id exists in the data
            if "next_customer_id" not in data:
                data["next_customer_id"] = 11111  # Add default value
            return data
    else:
        # Return default data if the file doesn't exist
        return {"books": [], "customers": [], "next_customer_id": 11111}

# Save data to the file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

class LibrarySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library System")
        self.root.geometry("1536x864")

        # Set background image
        self.background_image = PhotoImage(file="background.png")  # Replace with your image path
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        data = load_data()
        self.books = data["books"]
        self.customers = data["customers"]
        self.next_customer_id = data["next_customer_id"]

        self.create_widgets()
        # Load the logo image (use a smaller image for the logo)
        self.logo_image = PhotoImage(file="logo.png")  # استبدل المسار باسم الملف الخاص بالصورة
        self.logo_label = tk.Label(self.root, image=self.logo_image,)  # تأكد من أن الخلفية البيضاء
        self.logo_label.place(x=1200, y=20)  # ضبط الموضع في الجزء العلوي الأيسر من النافذة

        # Load the second logo image
        self.logo2_image = PhotoImage(file="logo2.png")  # استبدل المسار باسم الملف الخاص بالصورة الثانية
        self.logo2_label = tk.Label(self.root, image=self.logo2_image)  # تأكد من أن الخلفية بيضاء
        self.logo2_label.place(x=1350, y=20)  # ضبط الموضع تحت الصورة الأولى

    def create_widgets(self):
        # Books section
        self.book_frame = tk.LabelFrame(self.root, text="Books", padx=10, pady=10)
        self.book_frame.pack(padx=10, pady=10, fill="both")

        tk.Label(self.book_frame, text="Book Name:").grid(row=0, column=0)
        tk.Label(self.book_frame, text="Author:").grid(row=1, column=0)

        self.book_name_entry = tk.Entry(self.book_frame)
        self.book_name_entry.grid(row=0, column=1)

        self.author_name_entry = tk.Entry(self.book_frame)
        self.author_name_entry.grid(row=1, column=1)

        self.add_book_button = tk.Button(self.book_frame, text="Add Book",bg="cyan3" ,command=self.add_book)
        self.add_book_button.grid(row=2, column=0, columnspan=2)

        self.view_books_button = tk.Button(self.book_frame, text="View Books",bg="SeaGreen3", command=self.view_books)
        self.view_books_button.grid(row=3, column=0, columnspan=2)

        # Search Book
        tk.Label(self.book_frame, text="Search Book:").grid(row=4, column=0)
        self.search_book_entry = tk.Entry(self.book_frame)
        self.search_book_entry.grid(row=4, column=1)

        self.search_book_button = tk.Button(self.book_frame, text="Search",bg="salmon3", command=self.search_book)
        self.search_book_button.grid(row=5, column=0, columnspan=2)

        # Search Books by Author
        tk.Label(self.book_frame, text="Search by Author:").grid(row=6, column=0)
        self.search_author_entry = tk.Entry(self.book_frame)
        self.search_author_entry.grid(row=6, column=1)

        self.search_author_button = tk.Button(self.book_frame, text="Search",bg="pink3", command=self.search_by_author)
        self.search_author_button.grid(row=7, column=0, columnspan=2)

        # Borrow Book Section
        tk.Label(self.book_frame, text="Book Name to Borrow:").grid(row=8, column=0)
        self.borrow_book_entry = tk.Entry(self.book_frame)
        self.borrow_book_entry.grid(row=8, column=1)

        tk.Label(self.book_frame, text="Customer Name to Borrow:").grid(row=9, column=0)
        self.borrow_customer_entry = tk.Entry(self.book_frame)
        self.borrow_customer_entry.grid(row=9, column=1)

        # Text explaining ID request
        tk.Label(self.book_frame, text="Customer ID: ").grid(row=9, column=2)
        self.borrow_customer_id_entry = tk.Entry(self.book_frame)
        self.borrow_customer_id_entry.grid(row=9, column=3)

        self.borrow_book_button = tk.Button(self.book_frame, text="Borrow Book",bg="RoyalBlue1", command=self.borrow_book)
        self.borrow_book_button.grid(row=10, column=0, columnspan=4)

        # Return Book Section
        tk.Label(self.book_frame, text="Book Name to Return:").grid(row=11, column=0)
        self.return_book_entry = tk.Entry(self.book_frame)
        self.return_book_entry.grid(row=11, column=1)

        self.return_book_button = tk.Button(self.book_frame, text="Return Book",bg="green2", command=self.return_book)
        self.return_book_button.grid(row=12, column=0, columnspan=2)

        # Delete Book Section
        tk.Label(self.book_frame, text="Book Name to Delete:").grid(row=13, column=0)
        self.delete_book_entry = tk.Entry(self.book_frame)
        self.delete_book_entry.grid(row=13, column=1)

        self.delete_book_button = tk.Button(self.book_frame, text="Delete Book",bg="red", command=self.delete_book)
        self.delete_book_button.grid(row=14, column=0, columnspan=2)

        # Customers section
        self.customer_frame = tk.LabelFrame(self.root, text="Customers", padx=10, pady=10)
        self.customer_frame.pack(padx=10, pady=10, fill="both")

        tk.Label(self.customer_frame, text="Customer Name:").grid(row=0, column=0)
        self.customer_name_entry = tk.Entry(self.customer_frame)
        self.customer_name_entry.grid(row=0, column=1)

        self.add_customer_button = tk.Button(self.customer_frame, text="Add Customer", bg="tan1", command=self.add_customer_with_id_popup)
        self.add_customer_button.grid(row=1, column=0, columnspan=2)

        self.view_customers_button = tk.Button(self.customer_frame, text="View Customers",bg="firebrick4", command=self.view_customers)
        self.view_customers_button.grid(row=2, column=0, columnspan=2)

        # Search Customer by Name
        tk.Label(self.customer_frame, text="Search Customer:").grid(row=3, column=0)
        self.search_customer_entry = tk.Entry(self.customer_frame)
        self.search_customer_entry.grid(row=3, column=1)

        self.search_customer_button = tk.Button(self.customer_frame, text="Search", command=self.search_customer)
        self.search_customer_button.grid(row=4, column=0, columnspan=2)

        # Search Customer by ID
        self.search_by_id_button = tk.Button(self.customer_frame, text="Search by ID", command=self.search_customer_by_id)
        self.search_by_id_button.grid(row=5, column=0, columnspan=2)

        # Delete Customer Section
        tk.Label(self.customer_frame, text="Customer Name to Delete:").grid(row=6, column=0)
        self.delete_customer_entry = tk.Entry(self.customer_frame)
        self.delete_customer_entry.grid(row=6, column=1)

        self.delete_customer_button = tk.Button(self.customer_frame, text="Delete Customer", command=self.delete_customer)
        self.delete_customer_button.grid(row=7, column=0, columnspan=2)

    def add_book(self):
        book_name = self.book_name_entry.get().lower()  # إضافة lower
        author_name = self.author_name_entry.get().lower()  # إضافة lower

        if book_name and author_name:
            self.books.append({"book_name": book_name, "author_name": author_name, "borrowed_by": None})
            save_data({"books": self.books, "customers": self.customers, "next_customer_id": self.next_customer_id})
            messagebox.showinfo("Success", "Book added successfully!")
            self.book_name_entry.delete(0, tk.END)
            self.author_name_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please fill in all fields!")

    def view_books(self):
        if self.books:
            books_list = "\n".join([f"{book['book_name']} - {book['author_name']} - {'Borrowed by ' + book['borrowed_by'] if book['borrowed_by'] else 'Available'}" for book in self.books])
            messagebox.showinfo("Available Books", books_list)
        else:
            messagebox.showinfo("No Books", "There are no books in the library.")

    def search_book(self):
        search_term = self.search_book_entry.get().lower()  # إضافة lower
        found_books = [book for book in self.books if search_term in book['book_name'].lower() or search_term in book['author_name'].lower()]

        if found_books:
            books_list = "\n".join([f"{book['book_name']} - {book['author_name']} - {'Borrowed by ' + book['borrowed_by'] if book['borrowed_by'] else 'Available'}" for book in found_books])
            messagebox.showinfo("Matching Books", books_list)
            self.search_book_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("No Books", "No matching books found.")

    def search_by_author(self):
        author_name = self.search_author_entry.get().lower()  # إضافة lower
        found_books = [book for book in self.books if author_name in book['author_name'].lower()]

        if found_books:
            books_list = "\n".join([f"{book['book_name']} - {book['author_name']} - {'Borrowed by ' + book['borrowed_by'] if book['borrowed_by'] else 'Available'}" for book in found_books])
            messagebox.showinfo("Books by Author", books_list)
            self.search_author_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("No Books", "No books found for the specified author.")
    def borrow_book(self):
        book_name = self.borrow_book_entry.get().lower()  # إضافة lower
        customer_name = self.borrow_customer_entry.get().lower()  # إضافة lower
        customer_id = self.borrow_customer_id_entry.get()

        if book_name and customer_name and customer_id:
            for book in self.books:
                if book['book_name'].lower() == book_name and not book['borrowed_by']:  # إضافة lower
                    book['borrowed_by'] = f"{customer_name} (ID: {customer_id})"
                    save_data({"books": self.books, "customers": self.customers, "next_customer_id": self.next_customer_id})
                    messagebox.showinfo("Success", f"The book {book_name} has been borrowed successfully!")
                    self.borrow_book_entry.delete(0, tk.END)
                    self.borrow_customer_entry.delete(0, tk.END)
                    self.borrow_customer_id_entry.delete(0, tk.END)
                    return
            messagebox.showwarning("Warning", "The book is not available for borrowing.")
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")
    def return_book(self):
        book_name = self.return_book_entry.get().lower()  # إضافة lower

        if book_name:
            for book in self.books:
                if book['book_name'].lower() == book_name and book['borrowed_by']:  # إضافة lower
                    book['borrowed_by'] = None
                    save_data({"books": self.books, "customers": self.customers, "next_customer_id": self.next_customer_id})
                    messagebox.showinfo("Success", f"The book {book_name} has been returned successfully!")
                    self.return_book_entry.delete(0, tk.END)
                    return
            messagebox.showwarning("Warning", "The book is not borrowed.")
        else:
            messagebox.showwarning("Warning", "Please enter the book name.")
    def delete_book(self):
        book_name = self.delete_book_entry.get().lower()  # إضافة lower

        if book_name:
            self.books = [book for book in self.books if book['book_name'].lower() != book_name]  # إضافة lower
            save_data({"books": self.books, "customers": self.customers, "next_customer_id": self.next_customer_id})
            messagebox.showinfo("Success", f"The book {book_name} has been deleted successfully!")
            self.delete_book_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter the book name.")

    def add_customer_with_id_popup(self):
        customer_name = self.customer_name_entry.get()
        if customer_name:
            new_customer_id = self.next_customer_id
            self.customers.append({"customer_name": customer_name, "customer_id": new_customer_id})
            self.next_customer_id += 1
            save_data({"books": self.books, "customers": self.customers, "next_customer_id": self.next_customer_id})
            messagebox.showinfo("Success", f"Customer added successfully!\nName: {customer_name}\nID: {new_customer_id}")
            self.customer_name_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter the customer name.")


    def view_customers(self):
        if self.customers:
            customers_list = "\n".join([f"{customer['customer_name']} - {customer['customer_id']}" for customer in self.customers])
            messagebox.showinfo("Customers", customers_list)
        else:
            messagebox.showinfo("No Customers", "No customers registered.")

    def search_customer(self):
        search_term = self.search_customer_entry.get().lower()  # إضافة lower
        found_customers = [customer for customer in self.customers if search_term in customer['customer_name'].lower()]  # إضافة lower

        if found_customers:
            customers_list = []
            for customer in found_customers:
                # جمع كل الكتب المستعارة من العميل الحالي
                borrowed_books = [book['book_name'] for book in self.books if book['borrowed_by'] and str(customer['customer_id']) in book['borrowed_by']]
                borrowed_status = " & \n".join(borrowed_books) if borrowed_books else "No books borrowed."
                customers_list.append(
                f"->Customer Name: {customer['customer_name']}\n"
                f"->Customer ID: {customer['customer_id']}\n"
                f"->Borrowed Books:\n{borrowed_status}"
            )

            messagebox.showinfo("Matching Customers", "\n\n".join(customers_list))
            self.search_customer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("No Customers", "No matching customers found.")

    def search_customer_by_id(self):
        customer_id = self.search_customer_entry.get()
        found_customers = [customer for customer in self.customers if customer_id == str(customer['customer_id'])]

        if found_customers:
            customer = found_customers[0]  # نفترض أن الـ ID فريد ونأخذ أول عميل فقط
            borrowed_books = [book['book_name'] for book in self.books if book['borrowed_by'] and f"ID: {customer_id}" in book['borrowed_by']]
            borrowed_books_info = " & \n".join(borrowed_books) if borrowed_books else "No books borrowed."
            customer_info = (
                f"->Customer Name: {customer['customer_name']}\n"
                f"->Customer ID: {customer['customer_id']}\n"
                f"->Borrowed Books:\n{borrowed_books_info}"
            )
            messagebox.showinfo("Customer by ID", customer_info)
            self.search_customer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("No Customer", "No customer found with the entered ID.")


    def delete_customer(self):
        customer_name = self.delete_customer_entry.get().lower()  # إضافة lower

        if customer_name:
            self.customers = [customer for customer in self.customers if customer['customer_name'].lower() != customer_name]  # إضافة lower
            save_data({"books": self.books, "customers": self.customers, "next_customer_id": self.next_customer_id})
            messagebox.showinfo("Success", f"The customer {customer_name} has been deleted successfully!")
            self.delete_customer_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter the customer name.")
# Create the window
root = tk.Tk()
app = LibrarySystem(root)
root.mainloop()
