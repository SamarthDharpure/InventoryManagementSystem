# 🚚 Inventory Management System

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

![Login](![WhatsApp Image 2025-12-08 at 00 15 44_83d5cc73](https://github.com/user-attachments/assets/98ca9f16-2b3b-4aa7-905e-94ab3687e2f8))

### Dashboard

![Dashboard](![WhatsApp Image 2025-12-08 at 00 15 46_71d1a85b](https://github.com/user-attachments/assets/2d48c696-3eec-4c11-bc8a-4f69e592ad0d))

### Employee Management

![Employee](![WhatsApp Image 2025-12-08 at 00 15 43_ebab1b28](https://github.com/user-attachments/assets/2abd50f1-419c-44ef-8246-b9d11b607e85))

### Product Management

![Product](![WhatsApp Image 2025-12-08 at 00 15 47_ff2e0499](https://github.com/user-attachments/assets/ffab792e-c9fa-4a2c-88a9-1701fa40248f))

### Supplier Management

![Supplier](![WhatsApp Image 2025-12-08 at 00 15 46_0933534b](https://github.com/user-attachments/assets/86a2e0ee-8a6b-4422-88b6-18967d409a82))

### Sales & Billing

![Sales](![WhatsApp Image 2025-12-08 at 00 15 43_27a3330e](https://github.com/user-attachments/assets/a06c46fa-7a47-4578-9658-4e6db1df67db))

### POS / Shopping View

![Shopping](![WhatsApp Image 2025-12-08 at 00 15 42_299b1a18](https://github.com/user-attachments/assets/67330101-824d-40e9-845f-3eab39c5beb5))

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
