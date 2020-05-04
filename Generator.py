

# TODO:
# URL WORK
# If URLchk = checked,
# get values from fields, pass as values for vars in main function.
#
# Strong vs Realistic password generation
# In main repo, create a function with random selection
# if hits "strong" vs the normal selection route,
# do random.choice(word from seed), plus 1-4 num/symbol
#
#
#

# Importing
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
# secondFrame.grid_rowconfigure((0, 12), weight=1)
secondFrame.grid_columnconfigure((0, 1), weight=1)

# Run Button Frame.
runFrame = tkinter.Frame(
    width=180, height=60, borderwidth=2, relief='groove')
runFrame.grid(row=1, column=1)
runFrame.grid_propagate(0)
# runFrame.grid_rowconfigure((0, 2), weight=1)
runFrame.grid_columnconfigure((0, 1), weight=1)

username = ''
password = ''

lengthOptionsArray = ['short_text.json', 'medium_text.json',
                      'long_text.json', 'longest_text.json', 'million_text.json']

# print(lengthOptionsArray[1])

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

# url to which the data can be sent.
# url = '#'


comboTxt = tkinter.StringVar()
comboTxt.set('M')
print('comboTxt', comboTxt.get())

lengthOptions = ttk.Combobox(secondFrame, values=[
    "S",
    "M",
    "L",
    "XL",
    "MILLION"
], state="readonly", font=dropdownFont, textvariable=comboTxt).grid(row=2, columnspan=2, pady=2)
# ^ before ".grid", add font if desired

# print(lengthOptions)


# testBtn = tkinter.Button(runFrame, text='X', command=setLength)
# testBtn.grid(row=1, columnspan=2)
# setLength()


def mainFunction():
    global username
    global password

    seedFile = tkinter.StringVar()
    seedFile.set('medium_text.json')
    print('seedFile', seedFile.get())

    def setLength():
        print('pressed')
        print('comboTxt', comboTxt.get())
        print('seedfile:', seedFile.get())
        if (comboTxt.get() == 'S'):
            print('matchedS')
            seedFile.set('short_text.json')
            print(seedFile.get())
        if (comboTxt.get() == 'M'):
            print('matchedM')
            seedFile.set('medium_text.json')
            print(seedFile.get())
        if (comboTxt.get() == 'L'):
            print('matchedL')
            seedFile.set('long_text.json')
            print(seedFile.get())
        if (comboTxt.get() == 'XL'):
            print('matchedXL')
            seedFile.set('longest_text.json')
            print(seedFile.get())
        if (comboTxt.get() == 'MILLION'):
            print('matchedMil')
            seedFile.set('million_text.json')
            print(seedFile.get())

    setLength()

    # list of text to act as the email base value.
    email_text = json.loads(open(seedFile.get()).read())

    tkinter.Label(runFrame, text="Generating UserData...", fg='red').grid(
        row=1, columnspan=2, pady=2)
    print('running main')

    # def lengthSelection(event)
    #

    for email_data in email_text:

        # additional values for randomly adding a second word to email.
        name_random = ["", random.choice(email_text), ""]

        # take a random amount of digits, at a random length between 0 and 4.
        name_digits = ''.join(random.choice(string.digits)
                              for i in range(random.choice(extra_length)))

        # lowercase values from email_text + random digits + random choice of email suffix.
        username = email_data.lower() + random.choice(name_random) + \
            name_digits + random.choice(email_list)

        # random selection of upper & lower case characters/digits/special characters at a length of 6-12.
        password = ''.join(random.choice(chars)
                           for i in range(random.choice(password_length)))

        # Post to the specified url, don't redirect and pass usernames and passwords.
        # !!Need to specify the var for username and password from submission form.
        # requests.post(url, allow_redirects=False, data={
        #     '#': username,
        #     '#': password
        # })

        # Output list of usernames and passwords.
        if (chkVal.get() == 1):
            output_file.write('\"Username:\" \'% s\' \"Password:\" \'% s\' \n' %
                              (username, password))
        if (chkVal.get() == 0):
            print('Username: %s Password: %s' % (username, password))


# label_widget = tk.Label(widget, option=placeholder)
# checkbutton_widget = tk.CheckButton(widget, option=placeholder)

# open output.txt in append mode.
output_file = open('output.txt', 'a')


def outputCheck():
    # global username
    # global password
    # global output
    if (chkVal.get() == 1):
        print('checked')
        outputText.set('Data Generated In \"Output.txt\"')
        # # Output list of usernames and passwords.
        # output = output_file.write('\"Username:\" \'% s\' \"Password:\" \'% s\' \n' %
        #                            (username, password))
    if (chkVal.get() == 0):
        print('unchecked')
        outputText.set('')
        # print('Username: %s Password: %s' % (username, password))


descInfoTxt = tkinter.StringVar()
descInfoTxt.set(
    'This is test text sample, will it exceed\n the width of the box for the text \n Fill with info for the user')
descInfo = tkinter.Label(parentFrame, textvariable=descInfoTxt)
descInfo.grid(row=0, columnspan=2, pady=2)


tkinter.Label(secondFrame).grid(row=0, columnspan=2)

tkinter.Label(secondFrame, text="Select Results Length:").grid(
    row=1, columnspan=2, pady=1)

# comboTxt = tkinter.StringVar()
# comboTxt.set('M - 1,750 Results')
# print(comboTxt.get())


# passwordComplex =
chkShow = tkinter.IntVar()
passwordText = tkinter.StringVar()
passwordText.set("")


def showWarn():
    if (chkShow.get() == 1):
        print('checked')
        passwordText.set("Generating realistic passwords.")
    if (chkShow.get() == 0):
        print('unchecked')
        passwordText.set("")


tkinter.Checkbutton(
    secondFrame, text="Realistic Passwords", command=showWarn, variable=chkShow, onvalue=1, offvalue=0).grid(row=3, columnspan=2, pady=1)

chkVal = tkinter.IntVar()
tkinter.Checkbutton(
    secondFrame, text="Output To Text File", variable=chkVal, onvalue=1, offvalue=0, command=outputCheck).grid(row=4, columnspan=2, pady=1)


# tkinter.Label(secondFrame, pady=1).grid(row=5, columnspan=2)
# Wire up function on length selection.
# lengthOptions.bind("<<ComboboxSelected>>", lengthSelection)

outputText = tkinter.StringVar()
tkinter.Label(
    secondFrame, textvariable=outputText, fg='red').grid(row=7, columnspan=2, pady=1)
outputText.set('')

urlLabel = tkinter.Label(
    parentFrame, text='Target URL', state='disabled')
urlLabel.grid(row=5, pady=3)
urlEntry = tkinter.Entry(parentFrame, state='disabled')
urlEntry.grid(row=5, column=1, pady=3)
emailLabel = tkinter.Label(
    parentFrame, text="Email Value", state='disabled')
emailLabel.grid(row=6, pady=3)
emailEntry = tkinter.Entry(parentFrame, state='disabled')
emailEntry.grid(row=6, column=1, pady=3)
passwordLabel = tkinter.Label(
    parentFrame, text="Password Value", state='disabled')
passwordLabel.grid(row=7, pady=3)
passwordEntry = tkinter.Entry(parentFrame, state='disabled')
passwordEntry.grid(row=7, column=1, pady=3)


def enableEntry():
    global urlLabel, urlEntry, emailLabel, emailEntry, passwordLabel, passwordEntry
    if (chkVal2.get() == 1):
        print('checked')
        urlLabel = tkinter.Label(
            parentFrame, text='Target URL', state='normal')
        urlLabel.grid(row=5, pady=3)
        urlEntry = tkinter.Entry(parentFrame, state='normal')
        urlEntry.grid(row=5, column=1, pady=3)
        emailLabel = tkinter.Label(
            parentFrame, text="Email Value", state='normal')
        emailLabel.grid(row=6, pady=3)
        emailEntry = tkinter.Entry(parentFrame, state='normal')
        emailEntry.grid(row=6, column=1, pady=3)
        passwordLabel = tkinter.Label(
            parentFrame, text="Password Value", state='normal')
        passwordLabel.grid(row=7, pady=3)
        passwordEntry = tkinter.Entry(parentFrame, state='normal')
        passwordEntry.grid(row=7, column=1, pady=3)
    if (chkVal2.get() == 0):
        print('unchecked')
        urlLabel = tkinter.Label(
            parentFrame, text='Target URL', state='disabled')
        urlLabel.grid(row=5, pady=3)
        urlEntry = tkinter.Entry(parentFrame, state='disabled')
        urlEntry.grid(row=5, column=1, pady=3)
        emailLabel = tkinter.Label(
            parentFrame, text="Email Value", state='disabled')
        emailLabel.grid(row=6, pady=3)
        emailEntry = tkinter.Entry(parentFrame, state='disabled')
        emailEntry.grid(row=6, column=1, pady=3)
        passwordLabel = tkinter.Label(
            parentFrame, text="Password Value", state='disabled')
        passwordLabel.grid(row=7, pady=3)
        passwordEntry = tkinter.Entry(parentFrame, state='disabled')
        passwordEntry.grid(row=7, column=1, pady=3)


tkinter.ttk.Separator(parentFrame, orient="horizontal").grid(
    row=3, sticky='ew', columnspan=2)


chkVal2 = tkinter.IntVar()
tkinter.Checkbutton(
    parentFrame, text="Send to URL", command=enableEntry, variable=chkVal2, onvalue=1, offvalue=0, pady=5).grid(row=4, columnspan=2)


tkinter.Label(secondFrame, textvariable=passwordText, fg='red').grid(
    row=6, columnspan=2, pady=1)


def runGenerator():

    # tkinter.Label(parentFrame, text="Generating UserData...").grid(
    #     row=11, columnspan=2)
    print('running main')


btn1 = tkinter.Button(runFrame, text="Generate",  command=mainFunction)
btn1.grid(
    row=0, columnspan=2, pady=3)
# btn1.bind(mainFunction)

# tkinter.Label(parentFrame).grid(row=11)


window.mainloop()
