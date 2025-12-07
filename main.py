from tkinter import *
from tkinter import ttk

# Functionality Part
from tkinter import *
from tkinter import ttk


def employee_form():
    global back_image
    employee_frame = Frame(window, width=1070, height=567)
    employee_frame.place(x=200, y=100)

    heading_label = Label(employee_frame, text='Manage Employee Details',
                          font=('times new roman', 16, 'bold'),
                          bg='#0f4d7d', fg='white')
    heading_label.place(x=0, y=0, relwidth=1)

    back_image = PhotoImage(file='back.png')
    back_button = Button(employee_frame, image=back_image, bd=0, cursor='hand2', bg='white',
                         command=lambda: employee_frame.place_forget())
    back_button.place(x=10, y=30)

    top_frame = Frame(employee_frame, bg='white')
    top_frame.place(x=0, y=60, relwidth=1, height=235)
    search_frame = Frame(top_frame, bg='white')
    search_frame.pack()

    search_combobox = ttk.Combobox(search_frame,
                                   values=('Id', 'Name', 'Email'),
                                   font=('times new roman', 12),
                                   state='readonly')
    search_combobox.set('Search By')
    search_combobox.grid(row=0, column=0, padx=20)

    search_entry = Entry(search_frame, font=('times new roman', 12), bg='lightyellow')
    search_entry.grid(row=0, column=1)

    search_button = Button(search_frame, text='Search',
                           font=('times new roman', 12),
                           width=10, cursor='hand2',
                           fg='white', bg='#0f4d7d')
    search_button.grid(row=0, column=2, padx=20)

    show_button = Button(search_frame, text='Show All',
                         font=('times new roman', 12),
                         width=10, cursor='hand2',
                         fg='white', bg='#0f4d7d')
    show_button.grid(row=0, column=3)

    employee_treeview = ttk.Treeview(top_frame,
                                     columns=('empid', 'name', 'email', 'gender', 'dob', 'contact', 'employment_type',
                                              'education', 'work_shift', 'address', 'doj', 'salary', 'usertype'),
                                     show='headings')
    employee_treeview.pack(padx=10)

    employee_treeview.heading('empid', text='EmpId')
    employee_treeview.heading('name', text='Name')
    employee_treeview.heading('email', text='Email')
    employee_treeview.heading('gender', text='Gender')
    employee_treeview.heading('dob', text='Date of Birth')
    employee_treeview.heading('contact', text='Contact')
    employee_treeview.heading('employment_type', text='Employment Type')
    employee_treeview.heading('education', text='Education')
    employee_treeview.heading('work_shift', text='Work Shift')
    employee_treeview.heading('address', text='Address')
    employee_treeview.heading('doj', text='Date of Joining')
    employee_treeview.heading('salary', text='Salary')
    employee_treeview.heading('usertype', text='User Type')

    employee_treeview.column('empid',width=60)
    employee_treeview.column('name',width=60)
    employee_treeview.column('email',width=60)
    employee_treeview.column('gender',width=60)
    employee_treeview.column('contact',width=60)
    employee_treeview.column('dob',width=60)
    employee_treeview.column('employment_type',width=60)
    employee_treeview.column('education',width=60)
    employee_treeview.column('work_shift',width=60)
    employee_treeview.column('address',width=60)
    employee_treeview.column('doj',width=60)
    employee_treeview.column('salary',width=60)

# GUI Part
window = Tk()

window.title('Dashboard')
window.geometry('1270x668+0+0')
window.resizable(0, 0)
window.config(bg='white')

bg_image = PhotoImage(file='inventory.png')
titleLabel = Label(window, image=bg_image, compound=LEFT, text='  Inventory Management System',
                   font=('times new roman', 40, 'bold'), bg='#010c48', fg='white', anchor='w', padx=20)
titleLabel.place(x=0, y=0, relwidth=1)

logoutButton = Button(window, text='Logout', font=('times new roman', 20, 'bold'), fg='#010c48')
logoutButton.place(x=1100, y=10)

subtitleLabel = Label(window, text='Welcome Admin\t\t Date: 08-07-2024\t\t Time: 12:36:17 pm',
                      font=('times new roman', 15), bg='#4d636d', fg='white')
subtitleLabel.place(x=0, y=70, relwidth=1)

leftFrame = Frame(window)
leftFrame.place(x=0, y=102, width=200, height=555)

logoImage = PhotoImage(file='logo.png')
imageLabel = Label(leftFrame, image=logoImage)
imageLabel.pack()

menuLabel = Label(leftFrame, text='Menu', font=('times new roman', 20), bg='#009688')
menuLabel.pack(fill=X)

employee_icon = PhotoImage(file='employee.png')
employee_button = Button(leftFrame, image=employee_icon, compound=LEFT, text=' Employees',
                         font=('times new roman', 20, 'bold'), anchor='w', padx=10, command=employee_form)
employee_button.pack(fill=X)

supplier_icon = PhotoImage(file='supplier.png')
supplier_button = Button(leftFrame, image=supplier_icon, compound=LEFT, text=' Suppliers',
                         font=('times new roman', 20, 'bold'), anchor='w', padx=10)
supplier_button.pack(fill=X)

category_icon = PhotoImage(file='category.png')
category_button = Button(leftFrame, image=category_icon, compound=LEFT, text=' Categories',
                         font=('times new roman', 20, 'bold'), anchor='w', padx=10)
category_button.pack(fill=X)

products_icon = PhotoImage(file='product.png')
products_button = Button(leftFrame, image=products_icon, compound=LEFT, text=' Products',
                         font=('times new roman', 20, 'bold'), anchor='w', padx=10)
products_button.pack(fill=X)

sales_icon = PhotoImage(file='sales.png')
sales_button = Button(leftFrame, image=sales_icon, compound=LEFT, text=' Sales', font=('times new roman', 20, 'bold'),
                      anchor='w', padx=10)
sales_button.pack(fill=X)

exit_icon = PhotoImage(file='exit.png')
exit_button = Button(leftFrame, image=exit_icon, compound=LEFT, text=' Exit', font=('times new roman', 20, 'bold'),
                     anchor='w', padx=10)
exit_button.pack(fill=X)

# employees
emp_frame = Frame(window, bg='#2C3E50', bd=3, relief=RIDGE)
emp_frame.place(x=400, y=125, height=170, width=280)
total_emp_icon = PhotoImage(file='total_emp.png')
total_emp_icon_label = Label(emp_frame, image=total_emp_icon, bg='#2C3E50')
total_emp_icon_label.pack(pady=10)

total_emp_icon_label = Label(emp_frame, text='Total Employees', bg='#2C3E50', fg='white',
                             font=('times new roman', 15, 'bold'))
total_emp_icon_label.pack()

total_emp_count_label = Label(emp_frame, text='0', bg='#2C3E50', fg='white', font=('times new roman', 30, 'bold'))
total_emp_count_label.pack()

# suppliers
sup_frame = Frame(window, bg='#8E44AD', bd=3, relief=RIDGE)
sup_frame.place(x=800, y=125, height=170, width=280)
total_sup_icon = PhotoImage(file='total_sup.png')
total_sup_icon_label = Label(sup_frame, image=total_sup_icon, bg='#8E44AD')
total_sup_icon_label.pack(pady=10)

total_sup_icon_label = Label(sup_frame, text='Total Suppliers', bg='#8E44AD', fg='white',
                             font=('times new roman', 15, 'bold'))
total_sup_icon_label.pack()

total_sup_count_label = Label(sup_frame, text='0', bg='#8E44AD', fg='white', font=('times new roman', 30, 'bold'))
total_sup_count_label.pack()

# categories
cat_frame = Frame(window, bg='#27AE60', bd=3, relief=RIDGE)
cat_frame.place(x=400, y=310, height=170, width=280)
total_cat_icon = PhotoImage(file='total_cat.png')
total_cat_icon_label = Label(cat_frame, image=total_cat_icon, bg='#27AE60')
total_cat_icon_label.pack(pady=10)

total_cat_icon_label = Label(cat_frame, text='Total Categories', bg='#27AE60', fg='white',
                             font=('times new roman', 15, 'bold'))
total_cat_icon_label.pack()

total_cat_count_label = Label(cat_frame, text='0', bg='#27AE60', fg='white', font=('times new roman', 30, 'bold'))
total_cat_count_label.pack()

# product
prod_frame = Frame(window, bg='#2C3E50', bd=3, relief=RIDGE)
prod_frame.place(x=800, y=310, height=170, width=280)
total_prod_icon = PhotoImage(file='total_prod.png')
total_prod_icon_label = Label(prod_frame, image=total_prod_icon, bg='#2C3E50')
total_prod_icon_label.pack(pady=10)

total_prod_icon_label = Label(prod_frame, text='Total Products', bg='#2C3E50', fg='white',
                              font=('times new roman', 15, 'bold'))
total_prod_icon_label.pack()

total_prod_count_label = Label(prod_frame, text='0', bg='#2C3E50', fg='white', font=('times new roman', 30, 'bold'))
total_prod_count_label.pack()

# sales
sales_frame = Frame(window, bg='#E74C3C', bd=3, relief=RIDGE)
sales_frame.place(x=600, y=495, height=170, width=280)
total_sales_icon = PhotoImage(file='total_sales.png')
total_sales_icon_label = Label(sales_frame, image=total_sales_icon, bg='#E74C3C')
total_sales_icon_label.pack(pady=10)

total_sales_icon_label = Label(sales_frame, text='Total Sales', bg='#E74C3C', fg='white',
                               font=('times new roman', 15, 'bold'))
total_sales_icon_label.pack()

total_sales_count_label = Label(sales_frame, text='0', bg='#E74C3C', fg='white', font=('times new roman', 30, 'bold'))
total_sales_count_label.pack()

window.mainloop()
