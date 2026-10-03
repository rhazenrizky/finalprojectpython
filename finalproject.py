# inisialisasi list untuk menyimpan semua object item
library_items = []

# Parent Class
class LibraryItem:
    def __init__(self, item_id, title, category, publication_year):
        self.item_id = item_id
        self.title = title
        self.category = category
        self.publication_year = publication_year
        self.is_borrowed = False

    def calculate_late_fee(self, days_late):
        return 0

# Child Class - Book
class Book(LibraryItem):
    def __init__(self, item_id, title, category, publication_year, author):
        super().__init__(item_id, title, category, publication_year)
        self.author = author
        self.type = "Book"

    # Method Overriding
    def calculate_late_fee(self, days_late):
        fee = days_late * 2000
        if days_late > 7:
            fee = fee + 10000
        return fee

# Child Class - Magazine
class Magazine(LibraryItem):
    def __init__(self, item_id, title, category, publication_year, issue_number):
        super().__init__(item_id, title, category, publication_year)
        self.issue_number = issue_number
        self.type = "Magazine"

    # Method Overriding
    def calculate_late_fee(self, days_late):
        fee = days_late * 3000
        if days_late > 5:
            fee = fee + 15000
        return fee

# Function untuk mencari item berdasarkan ID
def find_item(search_id):
    for item in library_items:
        if item.item_id == search_id:
            return item
    return None

# Function untuk menambahkan item baru
def add_item():
    print("===== ADD LIBRARY ITEM =====")
    print("1. Book")
    print("2. Magazine")
    pilihan_jenis = input("Pilih jenis item (1/2): ")

    if pilihan_jenis == "1" or pilihan_jenis == "2":
        if pilihan_jenis == "1":
            print("===== ADD BOOK =====")
        else:
            print("===== ADD MAGAZINE =====")

        # Validasi ID tidak boleh duplicate
        is_valid_id = False
        while is_valid_id == False:
            item_id = input("Item ID          : ")
            existing_item = find_item(item_id)
            if existing_item != None:
                print("ID sudah terdaftar, silakan masukkan ID lain.")
            else:
                is_valid_id = True

        title = input("Title            : ")
        category = input("Category         : ")

        # Validasi Publication Year
        is_valid_year = False
        while is_valid_year == False:
            year_string = input("Publication Year : ")
            publication_year = int(year_string)
            if publication_year > 0:
                is_valid_year = True
            else:
                print("Tahun publikasi tidak valid.")

        if pilihan_jenis == "1":
            author = input("Author           : ")
            buku_baru = Book(item_id, title, category, publication_year, author)
            library_items.append(buku_baru)
            print("Book successfully added.")
            
        elif pilihan_jenis == "2":
            # Validasi Issue Number
            is_valid_issue = False
            while is_valid_issue == False:
                issue_string = input("Issue Number     : ")
                issue_number = int(issue_string)
                if issue_number > 0:
                    is_valid_issue = True
                else:
                    print("Issue Number harus lebih besar dari 0.")
                    
            majalah_baru = Magazine(item_id, title, category, publication_year, issue_number)
            library_items.append(majalah_baru)
            print("Magazine successfully added.")
    else:
        print("Pilihan tidak valid.")

# Function untuk menampilkan semua item
def show_all_items():
    print("===== LIBRARY ITEMS =====")
    counter_item = 1
    total_items = 0
    
    # perulangan data
    for item in library_items:
        print("Item #", counter_item)
        print("ID               : ", item.item_id)
        print("Type             : ", item.type)
        print("Title            : ", item.title)
        print("Category         : ", item.category)
        print("Publication Year : ", item.publication_year)

        if item.type == "Book":
            print("Author           : ", item.author)
        elif item.type == "Magazine":
            print("Issue Number     : ", item.issue_number)

        if item.is_borrowed == True:
            print("Status           : Borrowed")
        else:
            print("Status           : Available")
            
        print("----------------------------------------")
        counter_item += 1
        total_items += 1

    print("Total Items : ", total_items)

# Function untuk meminjam item
def borrow_item():
    print("===== BORROW ITEM =====")
    item_id = input("Enter Item ID to borrow : ")
    item = find_item(item_id)

    if item != None:
        if item.is_borrowed == False:
            item.is_borrowed = True
            print(item.title, "successfully borrowed.")
        else:
            print("Item tidak tersedia (sedang dipinjam).")
    else:
        print("Item tidak ditemukan.")

# Function untuk mengembalikan item
def return_item():
    print("===== RETURN ITEM =====")
    item_id = input("Enter Item ID to return : ")
    item = find_item(item_id)

    if item != None:
        if item.is_borrowed == True:
            days_late_string = input("Days late               : ")
            days_late = int(days_late_string)

            late_fee = item.calculate_late_fee(days_late)

            print("Item Type : ", item.type)
            print("Days Late : ", days_late)
            print("Late Fee  : Rp", late_fee)

            item.is_borrowed = False
            print("Item successfully returned.")
        else:
            print("Item ini tidak sedang dipinjam.")
    else:
        print("Item tidak ditemukan.")

# Function untuk melihat summary per kategori
def category_summary():
    print("===== CATEGORY SUMMARY =====")
    summary_dict = {}

    for item in library_items:
        kategori = item.category
        
        if kategori in summary_dict:
            summary_dict[kategori]["total_items"] += 1
            if item.is_borrowed == True:
                summary_dict[kategori]["borrowed_items"] += 1
        else:
            summary_dict[kategori] = {
                "total_items": 1,
                "borrowed_items": 0
            }
            if item.is_borrowed == True:
                summary_dict[kategori]["borrowed_items"] = 1

    print(summary_dict)

# Function untuk melihat summary keseluruhan perpustakaan
def library_summary():
    print("===== LIBRARY SUMMARY =====")
    total_items = 0
    total_books = 0
    total_magazines = 0
    borrowed_items = 0
    available_items = 0

    newest_year = 0
    oldest_year = 9999
    newest_title = ""
    oldest_title = ""

    for item in library_items:
        total_items += 1

        if item.type == "Book":
            total_books += 1
        elif item.type == "Magazine":
            total_magazines += 1

        if item.is_borrowed == True:
            borrowed_items += 1
        else:
            available_items += 1

        # mencari tahun terbaru tanpa max()
        if item.publication_year > newest_year:
            newest_year = item.publication_year
            newest_title = item.title

        # mencari tahun terlama tanpa min()
        if item.publication_year < oldest_year:
            oldest_year = item.publication_year
            oldest_title = item.title

    print("Total Items       : ", total_items)
    print("Total Books       : ", total_books)
    print("Total Magazines   : ", total_magazines)
    print("Borrowed Items    : ", borrowed_items)
    print("Available Items   : ", available_items)
    print("Newest Item       : ", newest_title)
    print("Oldest Item       : ", oldest_title)

# Function untuk menyimpan laporan ke file txt
def save_report():
    file = open("library_report.txt", "w")
    file.write("===== LIBRARY REPORT =====\n")

    for item in library_items:
        file.write("ID               : " + item.item_id + "\n")
        file.write("Title            : " + item.title + "\n")
        file.write("Type             : " + item.type + "\n")
        file.write("Category         : " + item.category + "\n")
        file.write("Publication Year : " + str(item.publication_year) + "\n")

        if item.type == "Book":
            file.write("Author           : " + item.author + "\n")
        elif item.type == "Magazine":
            file.write("Issue Number     : " + str(item.issue_number) + "\n")

        if item.is_borrowed == True:
            file.write("Status           : Borrowed\n")
        else:
            file.write("Status           : Available\n")
        file.write("----------------------------------------\n")

    file.write("========================================\n")
    file.write("LIBRARY SUMMARY\n")
    file.write("========================================\n")

    total_items = 0
    total_books = 0
    total_magazines = 0
    borrowed_items = 0
    available_items = 0
    newest_year = 0
    oldest_year = 9999
    newest_title = ""
    oldest_title = ""

    for item in library_items:
        total_items += 1
        if item.type == "Book":
            total_books += 1
        elif item.type == "Magazine":
            total_magazines += 1

        if item.is_borrowed == True:
            borrowed_items += 1
        else:
            available_items += 1

        if item.publication_year > newest_year:
            newest_year = item.publication_year
            newest_title = item.title

        if item.publication_year < oldest_year:
            oldest_year = item.publication_year
            oldest_title = item.title

    file.write("Total Items       : " + str(total_items) + "\n")
    file.write("Total Books       : " + str(total_books) + "\n")
    file.write("Total Magazines   : " + str(total_magazines) + "\n")
    file.write("Borrowed Items    : " + str(borrowed_items) + "\n")
    file.write("Available Items   : " + str(available_items) + "\n")
    file.write("Newest Item       : " + newest_title + "\n")
    file.write("Oldest Item       : " + oldest_title + "\n")
    file.write("========================================\n")

    file.close()
    print("Report successfully saved to library_report.txt")

# Function untuk membaca laporan dari file txt
def read_report():
    print("===== READ REPORT =====")
    file = open("library_report.txt", "r")
    data_report = file.readlines()
    file.close()

    for baris in data_report:
        print(baris.strip())

# Main Menu Loop
while True:
    print("\n===== LIBRARY BORROWING MANAGEMENT SYSTEM =====")
    print("1. Add Library Item")
    print("2. Show All Items")
    print("3. Find Item")
    print("4. Borrow Item")
    print("5. Return Item")
    print("6. Category Summary")
    print("7. Library Summary")
    print("8. Save Report")
    print("9. Read Report")
    print("10. Exit")
    pilihan_menu = input("Choose menu: ")

    if pilihan_menu == "1":
        add_item()
    elif pilihan_menu == "2":
        show_all_items()
    elif pilihan_menu == "3":
        search_id = input("Enter Item ID to find: ")
        item = find_item(search_id)
        if item != None:
            print("Item Found!")
            print("Title : ", item.title)
            print("Type  : ", item.type)
        else:
            print("Item not found.")
    elif pilihan_menu == "4":
        borrow_item()
    elif pilihan_menu == "5":
        return_item()
    elif pilihan_menu == "6":
        category_summary()
    elif pilihan_menu == "7":
        library_summary()
    elif pilihan_menu == "8":
        save_report()
    elif pilihan_menu == "9":
        read_report()
    elif pilihan_menu == "10":
        print("Exiting program...")
        break
    else:
        print("Menu tidak valid.")