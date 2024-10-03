from tkinter import *
import tkinter.messagebox as msg
import mysql.connector
def insert():
    id=e_id.get()
    name=e_name.get()
    product=e_product.get()
    if id=="" or name=="" or product=="":
        msg.showinfo("INSERT STATUS","ALL FIELDS ARE REQUIRED!!!")
    else:
        try:
            mydb=mysql.connector.connect(host="localhost",user='root',passwd='achukichu',database='hello')
            cursor=mydb.cursor()
            cursor.execute("insert into product values({},'{}','{}')".format(id,name,product))
            msg.showinfo("INSERT STATUS","SUCCESSFULL!!!")
            mydb.commit()
            mydb.close()
        except mysql.connector.errors.IntegrityError:
            msg.showinfo("ERROR","DUPLICATE ENTRY DETECTED(PROBABLY ID)!!! PLEASE CHECK YOUR DATA")
            pass
        
        
root=Tk()
root.geometry("1920x1080")
root.title("MYSQL RECORD INSERT AND SELECTOR")
id=Label(root,text="Enter the ID:",font=("Berlin Sans FB",18))
id.place(x=20,y=30)
name=Label(root,text='Enter the Name:',font=("Berlin Sans FB",18))
name.place(x=20,y=60)
product=Label(root,text="Enter the product ID",font=("Berlin Sans FB",18))
product.place(x=20,y=90)
e_id=Entry()
e_id.place(x=300,y=30)
e_name=Entry()
e_name.place(x=300,y=60)
e_product=Entry()
e_product.place(x=300,y=90)
insert=Button(root,text="Insert",font=('Berlin Sans FB',15),bg='blue',fg='white',command=insert)
insert.place(x=20,y=300)
