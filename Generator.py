

# TODO:
#
# Comment on all new functions
# Rename combobox options
# Complete info box on main frame
# additional styles or fonts?
#
# Strong vs Realistic password generation
# In main repo, create a function with random selection
# if hits "strong" vs the normal selection route,
# do random.choice(word from seed), plus 1-4 num/symbol
#
#
#

# Importing.
import tkinter
from tkinter import ttk
import requests
import os
import random
import string
import json

# Window config.
window = tkinter.Tk()
window.configure(background='black')
window.title("CredGen")
window.geometry('400x230')
window.resizable(0, 0)

# Styling config.
# style = ttk.Style(window)
# style.configure('TLabel', background='black', foreground='red')
# style.configure('TFrame', background='red', foreground='blue')

# Parent Frame config.
parentFrame = tkinter.Frame(width=220, height=230,
                            borderwidth=2, relief='groove')
parentFrame.grid(row=0, column=0, rowspan=2)
parentFrame.grid_rowconfigure((0, 11), weight=1)
parentFrame.grid_columnconfigure((0, 1), weight=1)
parentFrame.grid_propagate(0)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
dropdownFont = ("tahoma", 8)

# Instructions frame config
secondFrame = tkinter.Frame(width=180, height=170,
                            borderwidth=2, relief='groove')
secondFrame.grid(row=0, column=1)
secondFrame.grid_propagate(0)
secondFrame.grid_columnconfigure((0, 1), weight=1)

# Run Button Frame.
runFrame = tkinter.Frame(
    width=180, height=60, borderwidth=2, relief='groove')
runFrame.grid(row=1, column=1)
runFrame.grid_propagate(0)
runFrame.grid_columnconfigure((0, 1), weight=1)

url = ''
username = ''
password = ''

lengthOptionsArray = ['short_text.json', 'medium_text.json',
                      'long_text.json', 'longest_text.json', 'million_text.json']


# string of ascii letters in both upppercase & lowercase + string of digits  + spec characters
chars = string.ascii_letters + string.digits + '!?@#$%&*'

# seed basis for random numbers
random.seed = (os.urandom(1024))

# choices for email suffix.
email_list = ['@yahoo.com', '@gmail.com',
              '@mail.com', '@outlook.com', '@aol.com']

# choices for generated password length.
password_length = [6, 7, 8, 9, 10, 11, 12]

# choices for generated extra email numbers length.
extra_length = [0, 1, 2, 3, 4]

urlValue = tkinter.StringVar()
urlValue.set('')
userValue = tkinter.StringVar()
userValue.set('')
passValue = tkinter.StringVar()
passValue.set('')


comboTxt = tkinter.StringVar()
comboTxt.set('M')

lengthOptions = ttk.Combobox(secondFrame, values=[
    "S",
    "M",
    "L",
    "XL",
    "MILLION"
], state="readonly", font=dropdownFont, textvariable=comboTxt).grid(row=2, columnspan=2, pady=2)

passCmbTxt = tkinter.StringVar()
passCmbTxt.set('Randomized')

passOptions = ttk.Combobox(secondFrame, values=[
    "Realistic",
    "Strong",
    "Ramdomized"
], state="readonly", font=dropdownFont, textvariable=passCmbTxt).grid(row=4, columnspan=2, pady=1)


def mainFunction():

    global urlValue
    global userValue
    global passValue

    seedFile = tkinter.StringVar()
    seedFile.set('medium_text.json')

    def setLength():
        if (comboTxt.get() == 'S'):
            seedFile.set('short_text.json')
        if (comboTxt.get() == 'M'):
            seedFile.set('medium_text.json')
        if (comboTxt.get() == 'L'):
            seedFile.set('long_text.json')
        if (comboTxt.get() == 'XL'):
            seedFile.set('longest_text.json')
        if (comboTxt.get() == 'MILLION'):
            seedFile.set('million_text.json')

    setLength()

    # list of text to act as the email base value.
    email_text = json.loads(open(seedFile.get()).read())

    tkinter.Label(runFrame, text="Generating UserData...", fg='red').grid(
        row=1, columnspan=2, pady=2)

    for email_data in email_text:
        # additional values for randomly adding a second word to email.
        name_random = ["", random.choice(email_text), ""]

        # take a random amount of digits, at a random length between 0 and 4.
        name_digits = ''.join(random.choice(string.digits)
                              for i in range(random.choice(extra_length)))

        # choices for generated password additions
        pass_length = [1, 2, 3]

        pass_digits = ''.join(random.choice(chars)
                              for i in range(random.choice(pass_length)))

        # Strong password choice.
        strongPass = ''.join(random.choice(chars)
                             for i in range(random.choice(password_length)))

        # Realistic password generation.
        realPass = ''.join(random.choice(email_text) +
                           random.choice(name_random) + pass_digits)

        # Realistic password chance.
        passSelect = [strongPass, realPass, realPass]

        # lowercase values from email_text + random digits + random choice of email suffix.
        username = email_data.lower() + random.choice(name_random) + \
            name_digits + random.choice(email_list)

        passwordVal = tkinter.StringVar()
        passwordVal.set(random.choice(passSelect))
        # random selection of upper & lower case characters/digits/special characters at a length of 6-12.

        def passStyle():
            if (passCmbTxt.get() == 'Randomized'):
                passwordVal.set(random.choice(passSelect))
            if (passCmbTxt.get() == 'Realistic'):
                passwordVal.set(realPass)
            if (passCmbTxt.get() == 'Strong'):
                passwordVal.set(strongPass)

        passStyle()
        password = passwordVal.get()

        def sendURL():
            if (chkVal2.get() == 1):
                requests.post((urlValue.get()), allow_redirects=False, data={
                    userValue.get(): username,
                    passValue.get(): password
                })

        sendURL()

        # Output list of usernames and passwords.
        if (chkVal.get() == 1):
            output_file.write('\"Username:\" \'% s\' \"Password:\" \'% s\' \n' %
                              (username, password))
        if (chkVal.get() == 0):
            print('Username: %s Password: %s' % (username, password))


# open output.txt in append mode.
output_file = open('output.txt', 'a')


def outputCheck():
    if (chkVal.get() == 1):
        outputText.set('Data Generated In \"Output.txt\"')
    if (chkVal.get() == 0):
        outputText.set('')


descInfoTxt = tkinter.StringVar()
descInfoTxt.set(
    'Select Output Preference\n Choose Desired Output Length \n Select Password Style \n Run Generator')
descInfo = tkinter.Label(parentFrame, textvariable=descInfoTxt)
descInfo.grid(row=0, columnspan=2, pady=2)


# tkinter.Label(secondFrame).grid(row=0, columnspan=2)

tkinter.Label(secondFrame, text="Select Results Length:").grid(
    row=1, columnspan=2, pady=(11, 1))


# passwordComplex =
# chkShow = tkinter.IntVar()
# passwordText = tkinter.StringVar()
# passwordText.set("")


# def showWarn():
#     if (chkShow.get() == 1):
#         passwordText.set("Generating realistic passwords.")
#     if (chkShow.get() == 0):
#         passwordText.set("")


tkinter.Label(secondFrame, text="Select Password Types:").grid(
    row=3, columnspan=2, pady=1)
# tkinter.Checkbutton(
#     secondFrame, text="Realistic Passwords", command=showWarn, variable=chkShow, onvalue=1, offvalue=0).grid(row=3, columnspan=2, pady=1)

chkVal = tkinter.IntVar()
tkinter.Checkbutton(
    secondFrame, text="Output To Text File", variable=chkVal, onvalue=1, offvalue=0, command=outputCheck).grid(row=5, columnspan=2, pady=1)


outputText = tkinter.StringVar()
tkinter.Label(
    secondFrame, textvariable=outputText, fg='red').grid(row=6, columnspan=2, pady=1)
outputText.set('')

urlLabel = tkinter.Label(
    parentFrame, text='Target URL', state='disabled')
urlLabel.grid(row=5, pady=3)
urlEntry = tkinter.Entry(parentFrame, textvariable=urlValue, state='disabled')
urlEntry.grid(row=5, column=1, pady=3)
emailLabel = tkinter.Label(
    parentFrame, text="Email Value", state='disabled')
emailLabel.grid(row=6, pady=3)
emailEntry = tkinter.Entry(
    parentFrame, textvariable=userValue, state='disabled')
emailEntry.grid(row=6, column=1, pady=3)
passwordLabel = tkinter.Label(
    parentFrame, text="Password Value", state='disabled')
passwordLabel.grid(row=7, pady=3)
passwordEntry = tkinter.Entry(
    parentFrame, textvariable=passValue, state='disabled')
passwordEntry.grid(row=7, column=1, pady=3)


def enableEntry():
    global urlLabel, urlEntry, emailLabel, emailEntry, passwordLabel, passwordEntry, urlValue, userValue, passValue
    if (chkVal2.get() == 1):
        urlLabel = tkinter.Label(
            parentFrame, text='Target URL', state='normal')
        urlLabel.grid(row=5, pady=3)
        urlEntry = tkinter.Entry(
            parentFrame, textvariable=urlValue, state='normal')
        urlEntry.grid(row=5, column=1, pady=3)
        emailLabel = tkinter.Label(
            parentFrame, text="Email Value", state='normal')
        emailLabel.grid(row=6, pady=3)
        emailEntry = tkinter.Entry(
            parentFrame, textvariable=userValue, state='normal')
        emailEntry.grid(row=6, column=1, pady=3)
        passwordLabel = tkinter.Label(
            parentFrame, text="Password Value", state='normal')
        passwordLabel.grid(row=7, pady=3)
        passwordEntry = tkinter.Entry(
            parentFrame, textvariable=passValue, state='normal')
        passwordEntry.grid(row=7, column=1, pady=3)
    if (chkVal2.get() == 0):
        urlLabel = tkinter.Label(
            parentFrame, text='Target URL', state='disabled')
        urlLabel.grid(row=5, pady=3)
        urlEntry = tkinter.Entry(
            parentFrame, textvariable=urlValue, state='disabled')
        urlEntry.grid(row=5, column=1, pady=3)
        emailLabel = tkinter.Label(
            parentFrame, text="Email Value", state='disabled')
        emailLabel.grid(row=6, pady=3)
        emailEntry = tkinter.Entry(
            parentFrame, textvariable=userValue, state='disabled')
        emailEntry.grid(row=6, column=1, pady=3)
        passwordLabel = tkinter.Label(
            parentFrame, text="Password Value", state='disabled')
        passwordLabel.grid(row=7, pady=3)
        passwordEntry = tkinter.Entry(
            parentFrame, textvariable=passValue, state='disabled')
        passwordEntry.grid(row=7, column=1, pady=3)


tkinter.ttk.Separator(parentFrame, orient="horizontal").grid(
    row=3, sticky='ew', columnspan=2)


chkVal2 = tkinter.IntVar()
tkinter.Checkbutton(
    parentFrame, text="Send to URL", command=enableEntry, variable=chkVal2, onvalue=1, offvalue=0, pady=5).grid(row=4, columnspan=2)

#
# tkinter.Label(secondFrame, textvariable=passwordText, fg='red').grid(
#     row=6, columnspan=2, pady=1)


btn1 = tkinter.Button(runFrame, text="Generate",  command=mainFunction)
btn1.grid(
    row=0, columnspan=2, pady=3)


window.mainloop()
