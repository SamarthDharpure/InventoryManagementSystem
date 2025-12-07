#📦🚚 Inventory Management System

An intuitive, desktop **Inventory Management System** built with **Python (Tkinter)** and **SQL**. This application provides a complete GUI-based solution to manage employees, suppliers, categories, products, sales, and billing — ideal for small retail stores and inventory-based businesses.

---

## ✨ Features

* ✅ **User Authentication** (Employee login)
* 🧾 **Full CRUD** for Employees, Suppliers, Categories, and Products
* 🛒 **Sales & Billing Module** with printable customer bills
* 🔎 **Search & Filters** across records (Search By + Show All)
* 🧮 **Built-in Calculator** for quick arithmetic during billing
* 📦 **Stock Management** (in-stock tracking and quantity updates)
* 🖨 **Bill Generation & Print** (exports customer bill area)
* 🗂 **Bill history viewer** (list of saved bill files)
* 🎨 Clean, responsive desktop UI using Tkinter + ttk

---

## 📙 Description

**Inventory Management System** is a Python desktop application that simplifies inventory operations — employee records, supplier lists, product catalogs, and point-of-sale billing are all handled through a friendly graphical user interface. The app stores data in a local SQL database (SQLite by default) and provides utilities for generating printable bills, updating stock, and maintaining customer sales records.

This repository contains the full source code, UI assets (icons/screenshots), and instructions to run the app locally.

---

## 🧑🏻‍💻 Tech Stack

**Frontend / GUI:**

* Python 3.10+
* Tkinter (tk, ttk)
* Pillow (PIL) for image handling
* tkcalendar (optional, for date widgets)

**Database:**

* SQLite3 (default) — easily configurable to MySQL/MariaDB if needed

**Tools & Editors:**

* VS Code / PyCharm
* Git & GitHub

---

## 📂 Project Structure (example)

```
Inventory-Management-System/
│── main.py                    # App launcher (or inventory_system.py)
│── database.py                # DB connection & helpers (SQLite)
│── employees.py               # Employee CRUD + UI functions
│── suppliers.py               # Supplier CRUD + UI functions
│── categories.py              # Category CRUD + UI functions
│── products.py                # Product CRUD + UI functions
│── sales.py                   # Billing & sales flow
│── utils.py                   # Utility functions (calculator, printing)
│── requirements.txt
│── README.md
│── /images/                   # UI assets & screenshots
│   ├── Dashboard.jpg
│   ├── Employee.jpg
│   ├── Login.jpg
│   ├── Product.jpg
│   ├── Sales.jpg
│   ├── Shopping.jpg
│   └── Supplier.jpg
└── /data/
    └── inventory.db          # (created after first run)
```

> Note: File names above are examples — the actual file names in your repo might differ. Adjust commands accordingly.

---

## ⚙️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/inventory-management-system.git
cd inventory-management-system
```

2. **Create & activate a virtual environment**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

*If `requirements.txt` is not present, install commonly used packages:*

```bash
pip install pillow tkcalendar
```

4. **Database**

The application uses **SQLite** by default and will create `inventory.db` automatically on first run. If you prefer MySQL, update the DB configuration in `database.py` and install the appropriate connector (e.g. `mysql-connector-python`).

5. **Run the application**

```bash
python main.py
# or
python inventory_system.py
```

Open the application window and log in with a valid employee ID (or create an initial employee through the DB if needed).

---

## 🚀 Usage (quick walkthrough)

* **Login**: Enter Employee ID and password to access the system.
* **Dashboard**: Overview tiles show total employees, suppliers, categories, products, and total sales.
* **Employee / Supplier / Category / Product**: Use the left-side menu to open modules. Perform Add / Update / Delete and Search.
* **Sales**: Add customer details, select products, update quantities, apply discount, and generate printable bill files.
* **View Bills**: Open saved `.txt`/.pdf files from the bill history panel to review or print.

---

## 📊 Highlights & Benefits

* Friendly GUI that reduces manual paperwork for small shops
* End-to-end workflow: inventory → cart → bill generation
* Easily portable — runs on any machine with Python and Tkinter
* Configurable to use a server-based SQL DB if multi-user access is required

---

## 📸 Screenshots

### Login

![Login](images/Login.jpg)

### Dashboard

![Dashboard](images/Dashboard.jpg)

### Employee Management

![Employee](images/Employee.jpg)

### Product Management

![Product](images/Product.jpg)

### Supplier Management

![Supplier](images/Supplier.jpg)

### Sales & Billing

![Sales](images/Sales.jpg)

### POS / Shopping View

![Shopping](images/Shopping.jpg)

---

## 🤝 Contributing

Contributions are welcome! If you want to add features (multi-user mode, REST API, web frontend), please:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes and push
4. Open a Pull Request describing your changes

Please follow a consistent code style and include tests where applicable.

---

## 🧑‍💻 Author

**Samarth Dharpure**

🌐 [LinkedIn](https://www.linkedin.com/in/samarth-dharpure-88a10b248/) | 💻 [GitHub](https://github.com/SamarthDharpure)

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## ⭐ Note

If you like this project, don’t forget to star the repo.
