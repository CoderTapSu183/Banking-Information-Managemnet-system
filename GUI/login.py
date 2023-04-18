from tkinter import *
import os


def findButton():
    print("findButton")
def createButtonLogin():
    print("createButtonLogin")
    def createButton():
        print("createButton")
    def backButton():
        print("backButton")



    register = Toplevel()

    register.geometry("430x932")
    register.configure(bg = "#ffffff")
    register.title("Bankapp Register")
    canvas = Canvas(
        register,
        bg = "#ffffff",
        height = 932,
        width = 430,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    background1 = os.path.join(os.path.dirname(__file__), "background1.png"  )
    backgroundReg_img = PhotoImage(file =background1)
    backgroundReg = canvas.create_image(
        215.0, 466.0,
        image=backgroundReg_img)

    canvas.create_rectangle(
        22, 93, 22+386, 93+772,
        fill = "#ffffff",
        outline = "")

    canvas.create_text(
        214.0, 130.5,
        text = "Register new client",
        fill = "#206fa5",
        font = ("Arial", int(22.0)))


    fullNameReg = canvas.create_text(
        96.5, 182.0,
        text = "Full name",
        fill = "#206fa5",
        font = ("None", int(18.0)))

    img_textBox2 = os.path.join(os.path.dirname(__file__), "img_textBox2.png"  )
    fullName_img = PhotoImage(file = img_textBox2)
    fullName_bg = canvas.create_image(
        215.5, 234.5,
        image = fullName_img)

    fullName = Entry(register,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    fullName.place(
        x = 52.0, y = 205,
        width = 327.0,
        height = 61)

    gmailLog = canvas.create_text(
        72.5, 287.0,
        text = "Gmail",
        fill = "#206fa5",
        font = ("None", int(18.0)))
    img_textBox3 = os.path.join(os.path.dirname(__file__), "img_textBox3.png"  )
    gmail_img = PhotoImage(file = img_textBox3)
    gmail_bg = canvas.create_image(
        215.5, 339.5,
        image = gmail_img)

    gmail = Entry(register,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    gmail.place(
        x = 52.0, y = 310,
        width = 327.0,
        height = 61)

    passRegister = canvas.create_text(
        96.5, 392.0,
        text = "Password",
        fill = "#206fa5",
        font = ("None", int(18.0)))

    canvas.create_text(
        228.5, 392.5,
        text = "(Less than 18 characters)",
        fill = "#206fa5",
        font = ("None", int(10.0)))

    img_textBox4 = os.path.join(os.path.dirname(__file__), "img_textBox4.png"  )
    passReg_img = PhotoImage(file = img_textBox4)
    passReg_bg = canvas.create_image(
        215.5, 444.5,
        image = passReg_img)

    passReg = Entry(register,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    passReg.place(
        x = 52.0, y = 415,
        width = 327.0,
        height = 61)

    canvas.create_text(
        90.0, 497.0,
        text = "Address",
        fill = "#206fa5",
        font = ("None", int(18.0)))

    img_textBox5 = os.path.join(os.path.dirname(__file__), "img_textBox5.png"  )
    address_img = PhotoImage(file = img_textBox5)
    address_bg = canvas.create_image(
        215.5, 549.5,
        image = address_img)

    address = Entry(register,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    address.place(
        x = 52.0, y = 520,
        width = 327.0,
        height = 61)


    canvas.create_text(
        68.0, 602.0,
        text = "Age",
        fill = "#206fa5",
        font = ("None", int(18.0)))

    canvas.create_text(
        220.0, 602.0,
        text = "Gender",
        fill = "#206fa5",
        font = ("None", int(18.0)))

    img_textBox6 = os.path.join(os.path.dirname(__file__), "img_textBox6.png"  )
    phoneNum_img = PhotoImage(file = img_textBox6)
    phoneNum_bg = canvas.create_image(
        215.5, 759.5,
        image = phoneNum_img)

    phoneNum = Entry(register,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    phoneNum.place(
        x = 52.0, y = 730,
        width = 327.0,
        height = 61)

    img_textBox7 = os.path.join(os.path.dirname(__file__), "img_textBox7.png"  )
    age_img = PhotoImage(file =img_textBox7)
    age_bg = canvas.create_image(
        96.5, 654.5,
        image = age_img)

    age = Entry(register,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    age.place(
        x = 52.0, y = 625,
        width = 89.0,
        height = 61)


    canvas.create_text(
        124.5, 707.0,
        text = "Phone number",
        fill = "#206fa5",
        font = ("None", int(18.0)))

    img_textBox8 = os.path.join(os.path.dirname(__file__), "img_textBox8.png"  )
    gender_img = PhotoImage(file = img_textBox8)
    gender_bg = canvas.create_image(
        282.5, 654.5,
        image = gender_img)

    gender = Entry(register,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    gender.place(
        x = 186.0, y = 625,
        width = 193.0,
        height = 61)


    createim = os.path.join(os.path.dirname(__file__), "createim.png"  )
    imgcreateReg = PhotoImage(file = createim)
    bcreateReg = Button(
        image = imgcreateReg,
        borderwidth = 0,
        highlightthickness = 0,
        command = createButton,
        relief = "flat")

    bcreateReg.place(
        x = 136, y = 806,
        width = 158,
        height = 42)

    backim = os.path.join(os.path.dirname(__file__), "backim.png"  )
    imgbackReg = PhotoImage(file = f"backim.png")
    bbackReg = Button(
        image = imgbackReg,
        borderwidth = 0,
        highlightthickness = 0,
        command = backButton,
        relief = "flat")

    bbackReg.place(
        x = 28, y = 55,
        width = 14,
        height = 26)
        

AccesS = Tk()

AccesS.geometry("430x932")
AccesS.title("Bankapp Login")
AccesS.configure(bg = "#ffffff")
canvas = Canvas(
    AccesS,
    bg = "#ffffff",
    height = 932,
    width = 430,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

BackgroundFile = os.path.join(os.path.dirname(__file__), "background.png"  )
backgroundLogin_img = PhotoImage(file = BackgroundFile)
backgroundLogin = canvas.create_image(
    215.0, 466.0,
    image=backgroundLogin_img)

title = canvas.create_text(
    214.5, 109.5,
    text = "Banking Information\nManagement System",
    fill = "#105c90",
    font = ("Arial", int(24.0)))

canvas.create_text(
    215.0, 624.5,
    text = "or",
    fill = "#ffffff",
    font = ("Arial", int(24.0)))


canvas.create_rectangle(
    22, 183, 22+386, 183+393,
    fill = "#ffffff",
    outline = "")


access = canvas.create_text(
    214.5, 221.5,
    text = "Access Client Information",
    fill = "#206fa5",
    font = ("Arial", int(20.0)))


askName = canvas.create_text(
    72.5, 264.0,
    text = "Name",
    fill = "#206fa5",
    font = ("Arial", int(18.0)))

img_textBox0 = os.path.join(os.path.dirname(__file__), "img_textBox0.png"  )
nameGuest_img = PhotoImage(file = img_textBox0)
nameGuest_bg = canvas.create_image(
    214.5, 324.0,
    image = nameGuest_img)

nameGuest = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

nameGuest.place(
    x = 51.0, y = 291,
    width = 327.0,
    height = 66)

askPhone = canvas.create_text(
    118.5, 394.0,
    text = "Phone number",
    fill = "#206fa5",
    font = ("Arial", int(18.0)))

img_textBox1 = os.path.join(os.path.dirname(__file__), "img_textBox1.png"  )
phoneGuest_img = PhotoImage(file = img_textBox1)
phoneGuest_bg = canvas.create_image(
    214.5, 453.5,
    image = phoneGuest_img)

phoneGuest = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

phoneGuest.place(
    x = 51.0, y = 422,
    width = 327.0,
    height = 65)

img0 = os.path.join(os.path.dirname(__file__), "img0.png"  )
imgFind = PhotoImage(file = img0)
bFind = Button(
    image = imgFind,
    borderwidth = 0,
    highlightthickness = 0,
    command = findButton,
    relief = "flat")

bFind.place(
    x = 131, y = 510,
    width = 168,
    height = 56)

img1 = os.path.join(os.path.dirname(__file__), "img1.png"  )
imgCreate = PhotoImage(file = img1)
bCreate = Button(
    image = imgCreate,
    borderwidth = 0,
    highlightthickness = 0,
    command = createButtonLogin,
    relief = "flat")

bCreate.place(
    x = 135, y = 662,
    width = 158,
    height = 42)

AccesS.resizable(False, False)
AccesS.mainloop()
