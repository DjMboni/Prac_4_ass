from tkinter import *
from webbrowser import register

root = Tk()
root.title("Registration")
root.geometry("650x600")
root.resizable(False,False)

def register():
    name_info = nameValue.get()
    surname_info = surnameValue.get()
    gender_info = genderValue.get()
    stu_email_info = student_emailValue.get()
    amount_info = amount_paidValue.get()

    file = open(name_info + ".txt", "w")
    file.write(name_info + "\n")
    file.write(surname_info + "\n")
    file.write(gender_info + "\n")
    file.write(stu_email_info +"\n")
    file.write(amount_info +"\n")
    file.close()

    nameEntry.delete(0,END)
    surnameEntry.delete(0,END)
    genderEntry.delete(0,END)
    student_emailEntry.delete(0,END)
    amount_paidEntry.delete(0,END)

    Label(text= "Registration successful",fg= "green", font=("calibri",11)).place(x=250 ,y=500)

Label(root,text = "Comp Scie Gents Registration Form", font = "arial 25" ).pack(pady = 50)

Label(text = "Name", font=23).place(x=100, y=150)  #text co-ordination
Label(text = "Surname", font=23).place(x=100, y=200)
Label(text = "Gender", font=23).place(x=100, y=250)
Label(text = "Student email", font=23).place(x=100, y=300)
Label(text = "Amount paid", font=23).place(x=100, y=350)

nameValue = StringVar()               #entry bar
surnameValue = StringVar()
genderValue = StringVar()
student_emailValue = StringVar()
amount_paidValue = StringVar()

nameEntry = Entry(root,textvariable = nameValue,width=30,bd=2,font=20 ) #variables
surnameEntry = Entry(root,textvariable = surnameValue,width=30,bd=2,font=20 )
genderEntry = Entry(root,textvariable = genderValue,width=30,bd=2,font=20 )
student_emailEntry = Entry(root,textvariable = student_emailValue,width=30,bd=2,font=20 )
amount_paidEntry = Entry(root,textvariable = amount_paidValue,width=30,bd=2,font=20 )

nameEntry.place(x=240, y=150)    #typing space/bar
surnameEntry.place(x=240, y=200)
genderEntry.place(x=240, y=250)
student_emailEntry.place(x=240, y=300)
amount_paidEntry.place(x=240, y=350)

checkValue = IntVar             #button function
checkbtn = Checkbutton(text= "remember me?",variable= checkValue)
checkbtn.place(x=235, y=390)
Button(text= "Register Now", font=20, width=11, height=2,command=register).place(x=250, y=430)




root.mainloop()
print("the worst thing ive ever seen")
