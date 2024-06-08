from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
import mysql.connector
from tkinter import messagebox

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1525x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()

        # 1st
        img = Image.open("college_images/08.jpeg")
        img = img.resize((305, 160), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        self.btn_1 = Button(self.root, image=self.photoimg, cursor="hand2")
        self.btn_1.place(x=0, y=0, width=305, height=160)

        # 2nd
        img_2 = Image.open("college_images/09.jpeg")
        img_2 = img_2.resize((305, 160), Image.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        self.btn_2 = Button(self.root, image=self.photoimg_2, cursor="hand2")
        self.btn_2.place(x=305, y=0, width=305, height=160)

        # 3rd
        img_3 = Image.open("college_images/10.jpeg")
        img_3 = img_3.resize((305, 160), Image.LANCZOS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)

        self.btn_3 = Button(self.root, image=self.photoimg_3, cursor="hand2")
        self.btn_3.place(x=610, y=0, width=305, height=160)

        # 4th
        img_4 = Image.open("college_images/11.jpeg")
        img_4 = img_4.resize((305, 160), Image.LANCZOS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)

        self.btn_4 = Button(self.root, image=self.photoimg_4, cursor="hand2")
        self.btn_4.place(x=915, y=0, width=305, height=160)

        # 5th
        img_5 = Image.open("college_images/12.jpeg")
        img_5 = img_5.resize((305, 160), Image.LANCZOS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)

        self.btn_5 = Button(self.root, image=self.photoimg_5, cursor="hand2")
        self.btn_5.place(x=1220, y=0, width=305, height=160)

        # bg image
        img_6 = Image.open("college_images/uni.jpg")
        img_6 = img_6.resize((1525, 1710), Image.LANCZOS)
        self.photoimg_6 = ImageTk.PhotoImage(img_6)

        bg_lbl = Label(self.root, image=self.photoimg_6, bd=2, relief=RIDGE)
        bg_lbl.place(x=0, y=160, width=1525, height=710)

        lbl_title = Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM", font=("arial", 30, "bold"), fg="maroon", bg="white")
        lbl_title.place(x=0, y=0, width=1530, height=50)

        # Manage_frame
        Manage_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="white")
        Manage_frame.place(x=10, y=55, width=1500, height=560)

        # left frame
        DataLeftFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Information", font=("times new roman", 15, "bold"), fg="purple", bg="white")
        DataLeftFrame.place(x=10, y=10, width=660, height=540)

        # img
        img_7 = Image.open("college_images/15.jpeg")
        img_7 = img_7.resize((650, 120), Image.LANCZOS)
        self.photoimg_7 = ImageTk.PhotoImage(img_7)

        my_img = Label(DataLeftFrame, image=self.photoimg_7, bd=2, relief=RIDGE)
        my_img.place(x=0, y=0, width=650, height=120)

        # current course LabelFrame Information
        std_lbl_info_frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text="Current Course Information", font=("times new roman", 14, "bold"), fg="purple", bg="white")
        std_lbl_info_frame.place(x=0, y=130, width=650, height=115)

        # department
        lbl_dep = Label(std_lbl_info_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

        combo_dep = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_dep, font=("arial", 12, "bold"), width=17, state="readonly")
        combo_dep["value"] = ("Select Department", "CSE", "CM", "Civil", "ME", "EEE")
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course
        course_std = Label(std_lbl_info_frame, text="Courses", font=("times new roman", 12, "bold"), bg="white")
        course_std.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        com_txtcourse_std = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_course, font=("arial", 12, "bold"), width=17, state="readonly")
        com_txtcourse_std["value"] = ("Select Course", "Computer", "AI", "Civil", "Electrical", "Mechanical")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year
        current_year = Label(std_lbl_info_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        current_year.grid(row=1, column=0, padx=2, pady=10, sticky=W)

        com_text_current_year = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_year, font=("arial", 12, "bold"), width=17, state="readonly")
        com_text_current_year["value"] = ("Select Year", "1st", "2nd", "3rd", "4th")
        com_text_current_year.current(0)
        com_text_current_year.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester
        label_Semester = Label(std_lbl_info_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        label_Semester.grid(row=1, column=2, padx=2, pady=10, sticky=W)

        com_Semester = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_semester, font=("arial", 12, "bold"), width=17, state="readonly")
        com_Semester["value"] = ("Select Semester", "1st", "2nd")
        com_Semester.current(0)
        com_Semester.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Student class label information
        std_lbl_class_frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text="Class Course Information", font=("times new roman", 14, "bold"), fg="purple", bg="white")
        std_lbl_class_frame.place(x=0, y=250, width=650, height=200)

        # Student id
        lbl_id = Label(std_lbl_class_frame, text="Student ID:", font=("times new roman", 12, "bold"), bg="white")
        lbl_id.grid(row=0, column=0, padx=2, pady=7, sticky=W)

        id_entry = ttk.Entry(std_lbl_class_frame, textvariable=self.var_std_id, font=("times new roman", 13, "bold"), width=22)
        id_entry.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        # Student name
        lbl_name = Label(std_lbl_class_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
        lbl_name.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        txt_name = ttk.Entry(std_lbl_class_frame, textvariable=self.var_std_name, font=("times new roman", 13, "bold"), width=22)
        txt_name.grid(row=0, column=3, padx=2, pady=7, sticky=W)

        # roll no
        lbl_roll = Label(std_lbl_class_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        lbl_roll.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        txt_roll = ttk.Entry(std_lbl_class_frame, textvariable=self.var_roll, font=("times new roman", 13, "bold"), width=22)
        txt_roll.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        # Gender
        lbl_gender = Label(std_lbl_class_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        lbl_gender.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        com_txt_gender = ttk.Combobox(std_lbl_class_frame, textvariable=self.var_gender, font=("arial", 12, "bold"), width=18, state="readonly")
        com_txt_gender["value"] = ("Male", "Female")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=1, column=3, padx=2, pady=7, sticky=W)

        # Phone number
        lbl_phone = Label(std_lbl_class_frame, text="Phone No:", font=("times new roman", 12, "bold"), bg="white")
        lbl_phone.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        txt_phone = ttk.Entry(std_lbl_class_frame, textvariable=self.var_phone, font=("times new roman", 13, "bold"), width=22)
        txt_phone.grid(row=2, column=1, padx=2, pady=7, sticky=W)

        # Address
        lbl_address = Label(std_lbl_class_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white")
        lbl_address.grid(row=2, column=2, padx=2, pady=7, sticky=W)

        txt_address = ttk.Entry(std_lbl_class_frame, textvariable=self.var_address, font=("times new roman", 13, "bold"), width=22)
        txt_address.grid(row=2, column=3, padx=2, pady=7, sticky=W)

        # Button Frame
        btn_frame = Frame(DataLeftFrame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=440, width=652, height=38)

        btn_Add = Button(btn_frame, text="Save", command=self.add_data, font=("arial", 14, "bold"), width=12, bg="orange", fg="black")
        btn_Add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, text="Update",command=self.update_data, font=("arial", 14, "bold"), width=12, bg="orange", fg="black")
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Delete",command=self.delete_data, font=("arial", 14, "bold"), width=12, bg="orange", fg="black")
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset",command=self.reset_data, font=("arial", 14, "bold"), width=12, bg="orange", fg="black")
        btn_reset.grid(row=0, column=3, padx=1)

        # right frame
        DataRightFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Details", font=("times new roman", 15, "bold"), fg="purple", bg="white")
        DataRightFrame.place(x=680, y=10, width=800, height=540)

        # =============Search System=======================
        Search_Frame = LabelFrame(DataRightFrame, bd=4, relief=RIDGE, padx=2, text="Search Student Information", font=("times new roman", 15, "bold"), fg="purple", bg="white")
        Search_Frame.place(x=0, y=0, width=790, height=70)

        search_by = Label(Search_Frame, text="Search By:", font=("arial", 12, "bold"), bg="black", fg="white")
        search_by.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        
        #search
        self.var_com_search = StringVar()
        com_txt_search = ttk.Combobox(Search_Frame, textvariable=self.var_com_search, font=("arial", 12, "bold"), width=18, state="readonly")
        com_txt_search["value"] = ("Select Option", "Roll", "Phone", "Student_id")
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        self.var_search = StringVar()
        txt_search = ttk.Entry(Search_Frame, textvariable=self.var_search, font=("times new roman", 13, "bold"), width=22)
        txt_search.grid(row=0, column=2, padx=8, pady=5, sticky=W)

        btn_search = Button(Search_Frame,command=self.search_data, text="Search", font=("arial", 11, "bold"), width=12, bg="orange", fg="black")
        btn_search.grid(row=0, column=3, padx=7)

        btn_ShowAll = Button(Search_Frame,command=self.fetch_data, text="Show All", font=("arial", 11, "bold"), width=12, bg="orange", fg="black")
        btn_ShowAll.grid(row=0, column=4, padx=1)

        # ==============Student Table and Scrollbar=====================
        table_frame = Frame(DataRightFrame, bd=4, relief=RIDGE)
        table_frame.place(x=0, y=70, width=790, height=450)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "roll", "gender", "phone", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
        

    def add_data(self):
        if self.var_dep.get() == "" or self.var_phone.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="dipak22", database="students")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_address.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student has been added!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    
    #fetch function
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="dipak22", database="students")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
        
    #get cursor
    def get_cursor(self, event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]
        
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_roll.set(data[6])
        self.var_gender.set(data[7])
        self.var_phone.set(data[8])
        self.var_address.set(data[9])
        
     
    #UPDATE   
    def update_data(self):
        if self.var_dep.get() == "" or self.var_phone.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            try:
                update=messagebox.askyesno("Update", "Are you sure want to update this student data?", parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="dipak22", database="students")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update Student set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Roll=%s, Gender=%s, Phone=%s, Address=%s where Student_ID=%s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_std_id.get()
                        
                    ))
                    
        
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
        
                messagebox.showinfo("Success", "Student successfully updated", parent=self.root)                
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

           
    
    #DELETE
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete", "Are you sure want to delete this Student?", parent=self.root)  
                if Delete>0: 
                    conn = mysql.connector.connect(host="localhost", username="root", password="dipak22", database="students")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_ID=%s" 
                    value=(self.var_std_id.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Student has been Deleted", parent=self.root)  
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
       
        


    #RESET
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course ")
        self.var_year.set("SelectYear")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_address.set("")
        
    
    
    #SEARCH DATA
    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get() == "":   
            messagebox.showerror("Error", "Please select option and enter search term", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="dipak22", database="students")
                my_cursor = conn.cursor()
                search_query = f"SELECT * FROM student WHERE {self.var_com_search.get()} LIKE '%{self.var_search.get()}%'"
                my_cursor.execute(search_query)
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                else:
                    messagebox.showinfo("Info", "No records found", parent=self.root)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
                




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
