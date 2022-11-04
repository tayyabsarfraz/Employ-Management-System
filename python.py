from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Employee Management System")
        label_title=Label(self.root,text="EMPLOYEE MANAGEMENT SYSTEM",font=("times new roman",37,"bold"),fg="#2ad624",bg="#6b315a")
        label_title.place(x=0,y=0,width=1500,height=50)
        
        # set variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_desiginition=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()
        
         # image frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg="#e9c4aa")
        img_frame.place(x=0,y=50,width=1530,height=160)
          # 1st image
        img1=Image.open("desktop/img_1.jpg")
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)
        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,height=160,width=540)
        # 2nd image
        img2=Image.open("desktop/img_2.jpg")
        img2=img2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)
        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,height=160,width=540)
        # 3rd image
        img3=Image.open("desktop/img_3.jpg")
        img3=img3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)
        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,height=160,width=540)
        # Main frame
        Main_frame=Frame(self.root,relief=RIDGE,bd=2,bg="#e9c4aa")
        Main_frame.place(x=0,y=220,width=1400,height=560)
         # upper frame
        upper_frame=LabelFrame(Main_frame,relief=RIDGE,bd=2,bg="#e9c4aa",text="Employee Information",font=("arial",17,"bold"),fg="red")
        upper_frame.place(x=0,y=10,width=1480,height=270)
        
        # labels and entry
        
        #combo box
        lbl_dep=Label(upper_frame,text="Department",font=("arial",11,"bold"),bg="#e9c4aa")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=("arial",12,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Select","PUCIT","STAT","SOCIALOGY","PHYSICS","MATH","GENDER STUDY","IER","POLITICAL SCIENCES")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        # Name
        lbl_dep=Label(upper_frame,text="Name",font=("arial",11,"bold"),bg="#e9c4aa")
        lbl_dep.grid(row=0,column=2,padx=2,pady=7,sticky=W)
        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",12,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7,sticky=W)
        # Desigination
        lbl_desig=Label(upper_frame,text="Designition",font=("arial",11,"bold"),bg="#e9c4aa")
        lbl_desig.grid(row=1,column=0,padx=2,pady=7,sticky=W)
        txt_desig=ttk.Entry(upper_frame,textvariable=self.var_desiginition,width=19,font=("arial",12,"bold"))
        txt_desig.grid(row=1,column=1,padx=2,pady=7,sticky=W)
        # Email 
        lbl_email=Label(upper_frame,text="Email",font=("arial",11,"bold"),bg="#e9c4aa")
        lbl_email.grid(row=1,column=2,padx=2,pady=7,sticky=W)
        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=("arial",12,"bold"))
        txt_email.grid(row=1,column=3,padx=2,pady=7,sticky=W)
        # Address
        lbl_address=Label(upper_frame,text="Address",font=("arial",11,"bold"),bg="#e9c4aa")
        lbl_address.grid(row=2,column=0,padx=2,pady=7,sticky=W)
        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=19,font=("arial",12,"bold"))
        txt_address.grid(row=2,column=1,padx=2,pady=7,sticky=W)
        # Married
        lbl_Married=Label(upper_frame,text="Married Status",font=("arial",11,"bold"),bg="#e9c4aa")
        lbl_Married.grid(row=2,column=2,padx=2,sticky=W)
        combo_Married=ttk.Combobox(upper_frame,textvariable=self.var_married,font=("arial",12,"bold"),width=20,state="readonly")
        combo_Married["value"]=("Select","Married","Unmarried")
        combo_Married.current(0)
        combo_Married.grid(row=2,column=3,padx=2,pady=10,sticky=W)
        # DOB
        lbl_dob=Label(upper_frame,text="DOB",font=("arial",11,"bold"),bg="#e9c4aa")
        lbl_dob.grid(row=3,column=0,padx=2,pady=7,sticky=W)
        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=19,font=("arial",12,"bold"))
        txt_dob.grid(row=3,column=1,padx=2,pady=7,sticky=W)
        # DOJ
        lbl_doj=Label(upper_frame,text="Date Of Joining",font=("arial",11,"bold"),bg="#e9c4aa")
        lbl_doj.grid(row=3,column=2,padx=2,pady=7,sticky=W)
        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=("arial",12,"bold"))
        txt_doj.grid(row=3,column=3,padx=2,pady=7,sticky=W)
        # ID proof
        combo_id_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,font=("arial",12,"bold"),width=20,state="readonly")
        combo_id_proof["value"]=("Select Id Proof","ID Card","Driving License")
        combo_id_proof.current(0)
        combo_id_proof.grid(row=4,column=0,padx=2,pady=10,sticky=W)
        txt_id_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=19,font=("arial",12,"bold"))
        txt_id_proof.grid(row=4,column=1,padx=2,pady=7,sticky=W)
        # Gender
        lbl_gender=Label(upper_frame,text="Gender",font=("arial",11,"bold"),bg="#e9c4aa")
        lbl_gender.grid(row=4,column=2,padx=2,sticky=W)
        combo_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=("arial",12,"bold"),width=20,state="readonly")
        combo_gender["value"]=("Select","Male","Female")
        combo_gender.current(0)
        combo_gender.grid(row=4,column=3,padx=2,pady=10,sticky=W)
        # Phone
        lbl_phone=Label(upper_frame,text="Phone No",font=("arial",11,"bold"),bg="#e9c4aa")
        lbl_phone.grid(row=0,column=4,padx=2,pady=7,sticky=W)
        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=19,font=("arial",12,"bold"))
        txt_phone.grid(row=0,column=5,padx=2,pady=7,sticky=W)
        # Country
        lbl_country=Label(upper_frame,text="Country",font=("arial",11,"bold"),bg="#e9c4aa")
        lbl_country.grid(row=1,column=4,padx=2,pady=7,sticky=W)
        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=19,font=("arial",12,"bold"))
        txt_country.grid(row=1,column=5,padx=2,pady=7,sticky=W)
        # Salary
        lbl_salary=Label(upper_frame,text="Salary",font=("arial",11,"bold"),bg="#e9c4aa")
        lbl_salary.grid(row=2,column=4,padx=2,pady=7,sticky=W)
        txt_salary=ttk.Entry(upper_frame,textvariable=self.var_salary,width=19,font=("arial",12,"bold"))
        txt_salary.grid(row=2,column=5,padx=2,pady=7,sticky=W)
        # side image in upper frame 
        img4=Image.open("desktop/img_4.png")
        img4=img4.resize((170,170),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img4)
        self.img_4=Label(upper_frame,image=self.photo4)
        self.img_4.place(x=1000,y=0,height=180,width=190)
        
        # Button Frame
        button_frame=Frame(upper_frame,relief=RIDGE,bd=2,bg="#a2b0a2")
        button_frame.place(x=1220,y=3,width=170,height=173)
        # save button
        btn_add=Button(button_frame,command=self.add_data,text="Save",font=("arial",11,"bold"),width=13,fg="white",bg="#515c57")
        btn_add.grid(row=0,column=0,padx=1,pady=5)
        # Update
        btn_update=Button(button_frame,command=self.update_data,text="Update",font=("arial",11,"bold"),width=13,fg="white",bg="#515c57")
        btn_update.grid(row=1,column=0,padx=1,pady=5)
        # Delete
        btn_delete=Button(button_frame,text="Delete",font=("arial",11,"bold"),width=13,fg="white",bg="#515c57")
        btn_delete.grid(row=2,column=0,padx=1,pady=5)
        # Clear
        btn_clear=Button(button_frame,text="Clear",font=("arial",11,"bold"),width=13,fg="white",bg="#515c57")
        btn_clear.grid(row=3,column=0,padx=1,pady=5)
        
         # down frame
        down_frame=LabelFrame(Main_frame,relief=RIDGE,bd=2,bg="white",text="Employee Information Table",font=("arial",11,"bold"),fg="red")
        down_frame.place(x=0,y=250,width=1480,height=250)
        
        # search frame
        search_frame=LabelFrame(down_frame,relief=RIDGE,bd=2,bg="white",text="Search Employee Information",font=("arial",11,"bold"),fg="red")
        search_frame.place(x=0,y=0,width=1470,height=90)
        search_by=Label(search_frame,font=("arial",11,"bold"),fg="white",text="Search By",bg="red")
        search_by.grid(row=0,column=0,padx=5,sticky=W)
        # search
        self.var_com_search=StringVar()
        combo_txt_search=ttk.Combobox(search_frame,font=("arial",12,"bold"),width=20,state="readonly")
        combo_txt_search["value"]=("Select Option","Phone","ID_Proof")
        combo_txt_search.current(0)
        combo_txt_search.grid(row=0,column=1,padx=5,sticky=W)
        txt_search=ttk.Entry(search_frame,width=22,font=("arial",12,"bold"))
        txt_search.grid(row=0,column=2,padx=2,pady=7,sticky=W)
        # button search
        btn_search=Button(search_frame,text="Search",font=("arial",11,"bold"),width=10,fg="white",bg="#515c57")
        btn_search.grid(row=0,column=3,padx=5)
        # button show all
        btn_showall=Button(search_frame,text="Show All",font=("arial",11,"bold"),width=10,fg="white",bg="#515c57")
        btn_showall.grid(row=0,column=4,padx=5)
        # Employee Quotation
        search_quot=Label(search_frame,font=("times new roman",15,"bold"),fg="black",text="Give thanks for a little and you will find a lot.",bg="white")
        search_quot.place(x=780,y=0,width=600,height=30)
        #=================Employee Table================
        # table frame 
        table_frame=Frame(down_frame,relief=RIDGE,bd=3,bg="#32a873")
        table_frame.place(x=0,y=50,width=1345,height=155)
        
        # scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.employee_table=ttk.Treeview(table_frame,column=("Dep","Name","Desg","email","address","married","dob","doj","idproofcombo","idproof","gender","phone","country","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        
        self.employee_table.heading("Dep",text="Department")
        self.employee_table.heading("Name",text="Name")
        self.employee_table.heading("Desg",text="Desiginition")
        self.employee_table.heading("email",text="Email")
        self.employee_table.heading("address",text="Address")
        self.employee_table.heading("married",text="Married Status")
        self.employee_table.heading("dob",text="DOB")
        self.employee_table.heading("doj",text="DOJ")
        self.employee_table.heading("idproofcombo",text="IDPROOFCOMBO")
        self.employee_table.heading("idproof",text="IDProof")
        self.employee_table.heading("gender",text="Gender")
        self.employee_table.heading("phone",text="Phone No")
        self.employee_table.heading("country",text="Country")
        self.employee_table.heading("salary",text="Salary")
        
        self.employee_table["show"]="headings"
        self.employee_table.column("Dep",width=100)
        self.employee_table.column("Name",width=100)
        self.employee_table.column("Desg",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("married",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("idproofcombo",width=100)
        self.employee_table.column("idproof",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("salary",width=100)
        
        self.employee_table.pack(fill=BOTH,expand=1)
        
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        
        self.fetch_data()
    #===========setting funtions====================
    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get() == "":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1998",database="employee_record")
                cursor=conn.cursor()
                cursor.execute('insert into employee_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_desiginition.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_married.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_doj.get(),
                                                                                                                self.var_idproofcomb.get(),
                                                                                                                self.var_idproof.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_country.get(),
                                                                                                                self.var_salary.get()
                
                
                
                
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                
                conn.close()
                messagebox.showinfo("Success","Employee has been added successfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to : {str(e)}",parent=self.root)
                
    # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1998",database="employee_record")
        cursor=conn.cursor()
        cursor.execute("select * from employee_data")
        data=cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    # Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content["values"]
        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_desiginition.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7]),
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])
        
    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get() == "":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure update the information")
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="1998",database="employee_record")
                    cursor=conn.cursor()
                    cursor.execute("update employee_data set Department=%s,Name=%s,Desiginition=%s,Email=%s,Address=%s,Married Status=%s,DOB=%s,DOJ=%s,Gender=%s,Phone No=%s,Country=%s,Salary=%s where IDProof=%s ",(
                                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                                                            self.var_desiginition.get(),
                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                                            self.var_married.get(),
                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                            self.var_doj.get(),
                                                                                                                                                                                                                            self.var_idproofcomb.get(),
                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                            self.var_country.get(),
                                                                                                                                                                                                                            self.var_salary.get(),
                                                                                                                                                                                                                            self.var_idproof.get()
                    ))
                else:
                    if not update:
                        return
                        
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Information updated successfully",parent=self.root)
            except Exception as e:
                      messagebox.showerror("Error",f"Due to : {str(e)}",parent=self.root)
                    
                    
                
                                                                                                                                                                                                                               
        
    
                
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      
       
        
        
        
        
        
      
        
        
     
       
        
        
        
        
        
        
        
       
        
        
        
        
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()