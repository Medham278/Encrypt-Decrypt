from guizero import App,Text,Combo,PushButton,ButtonGroup,TextBox,info,Picture
from random import randint
from email.message import EmailMessage
import smtplib
import os
from io import BytesIO
import sys
from PIL import Image
from array import array
ALPHABET='abcdefghijklmnopqrstuvwxyz'
val=0
def load_sheet(filename):
    with open(filename,"r") as f:
        contents=f.read().splitlines()
    return contents

def load_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents

def save_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)
app=App(title="Encrypt-Decrypt",width=600,height=700,bg="turquoise")
app.text_color="firebrick4"
app.text_size=18
def encrypt():
    sheet = load_sheet("otp0.txt")
    filename=file_name.value
    filecontent=load_file(filename)
    ciphertext =''
    for position,character in enumerate(filecontent):
        if character not in ALPHABET:
            ciphertext += character
        else:
            encrypted = (ALPHABET.index(character) + int(sheet[position])) % 26
            ciphertext += ALPHABET[encrypted]
    filename=app.question("Encrypted File","Enter name of the file after encryption")
    save_file(filename, ciphertext)
    info("OUTPUT","Your file has been successfully Encrypted. Thank You!")
def decrypt():
    sheet = load_sheet("otp0.txt")
    filename =file_name.value
    ciphertext = load_file(filename)
    plaintext = ''
    for position, character in enumerate(ciphertext):
        if character not in ALPHABET:
            plaintext += character
        else:
            decrypted = (ALPHABET.index(character) - int(sheet[position])) % 26
            plaintext += ALPHABET[decrypted]
    if val>0:
        filename = app.question("Decrypted File","Enter name of the file after decryption")
        save_file(filename, plaintext)
        info("OUTPUT","Your file has been successfully Decrypted. Thank You!")
    else:
        info("After Decryption",plaintext)

def encrypt_im():
    fo=open(file_name.value,"rb")
    img=fo.read()
    fo.close()
    img=bytearray(img)
    key=64
    for index,value in enumerate(img):
        img[index]=value^key
    filename=app.question("Encrypted File","Enter name of the file after encryption")
    fo=open(filename,"wb")
    fo.write(img)
    fo.close()
    info("OUTPUT","Your file has been successfully Encrypted. Thank You!")

def decrypt_im():
    fo=open(file_name.value,"rb")
    img=fo.read()
    fo.close()
    img=bytearray(img)
    key=64
    for index,value in enumerate(img):
        img[index]=value^key
    if val>0:
        filename = app.question("Decrypted File","Enter name of the file after decryption")
        fo=open(filename,"wb")
        fo.write(img)
    else:
        fo=open("img.png","wb")
        fo.write(img)
        fo.close()
        Picture(app, image="img.png")
    info("OUTPUT","Your file has been successfully Decrypted. Thank You!")
    fo.close()
    
def mail():
    EMAIL='pypragmatics@gmail.com'
    PASSWORD='ssmm@py3.8'
    mail=app.question("Mail","Enter Email ID and click 'OK'")
    msg=EmailMessage()
    msg['Subject']="OTP"
    msg['From']=EMAIL
    msg['To']=[mail]
    otp=randint(100000, 999999)
    otp=str(otp)
    message="Your One Time Password is "+otp
    msg.set_content(message)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)
    num=app.question("OTP","Enter OTP received via mail")
    if num==otp:
        info("Status","Correct OTP! Decrypting file...")
        return 1
    else:
        info("Status","Wrong OTP. Cannot Decrypt File")
        return 0
    
def get_file():
    file_name.value = app.select_file(filetypes=[["Text documents", "*.txt"],["PNG File","*.png"]])

def pass_check():
    global val
    if option.value=="Admin":
        message=Text(app,text="Enter Admin Password:")
        message.text_color="gold2"
        password=TextBox(app,"",width=20,hide_text=True)
        password.bg="PaleTurquoise1"
        def do():
            global val
            if password.value=="abc$123":
                info("Status","Hello Admin!. You can Encrypt and  Decrypt files!")
                password.visible=False
                message.visible=False
                val=val+1
                eord()
            else:
                info("Status","Hello User. You can only Decrypt files!")
                password.visible=False
                message.visible=False
                val=0
                eord()
        password.when_mouse_leaves=do
    else:
        info("Status","Hello User. You can only Decrypt files!")
        val=0
        eord()

perm=Text(app,text="Admin or User? :")
option=Combo(app,options=["User","Admin"],command=pass_check)
option.bg="khaki1"
def eord():
    def call():
        if choice.value=="E":
            if ch.value=="T":
                encrypt()
            else :
                encrypt_im()
        else:
            value=mail()
            if value==1:
                if ch.value=="T":
                    decrypt()
                else:
                    decrypt_im()
    def check():
        if ch.value=="T":
            mes.value="Select File First"
            file_button.text="Get file"
        else:
            mes.value="Select Image First"
            file_button.text="Get Image"

    ques=Text(app,text="Choose Type:")
    ques.text_color="gold2"
    ch=ButtonGroup(app, options=[ ["Text File", "T"], ["Image", "I"]],selected="T", horizontal=True,command=check)
    ch.bg="SeaGreen1"
    mes=Text(app,text="Select File first")
    mes.text_color="gold2"
    file_button=PushButton(app,command=get_file,text="Get file")
    file_button.bg="ivory3"
    e_or_d=Text(app,text="Select operation to perform:")
    e_or_d.text_color="gold2"
    if val>0:
        choice = ButtonGroup(app, options=[ ["Encrypt", "E"], ["Decrypt", "D"]],selected="E", horizontal=True,command=call)
        choice.bg="SeaGreen1"
    else:
        choice = ButtonGroup(app, options=[["Decrypt", "D"]],selected="D", horizontal=True,command=call)
        choice.bg="SeaGreen1"
        
file_name = Text(app)



app.display()
