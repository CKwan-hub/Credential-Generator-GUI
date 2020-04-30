# TODO:
#
# -Wire up functionality
#   -toggle output to .txt
#   -toggle switch for length
#   -Fade/disable field input until URL checkbox active.
#   -Warning message toggle on/off for realistic password
#   -Bind/command for all other functionality.
# -Pull realistic password generator from github - Credential Generator
#   -(Chance to pick seed word instead of char string.
#       If char string, append rand 1-4 amt of num and 1-2 rand symbol)
# -Descriptions for line
# -Padding, spacing, formatting


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
window.geometry('400x255')
window.resizable(0, 0)

# Styling config.
# style = ttk.Style(window)
# style.configure('TLabel', background='black', foreground='red')
# style.configure('TFrame', background='red', foreground='blue')

# Parent Frame config.
parentFrame = tkinter.Frame(width=200, height=255,
                            borderwidth=2, relief='groove', bg='blue')
parentFrame.grid(row=0, column=0, rowspan=2)
parentFrame.grid_rowconfigure((0, 13), weight=1)
parentFrame.grid_columnconfigure((0, 2), weight=1)
parentFrame.grid_propagate(0)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
# dropdownFont = ("Courier", 8)

# Instructions frame config
secondFrame = tkinter.Frame(width=200, height=230,
                            borderwidth=2, relief='groove', bg='red')
secondFrame.grid(row=0, column=1)

# Run Button Frame.
runFrame = tkinter.Frame(
    width=200, height=60, borderwidth=2, relief='groove', bg='yellow')
runFrame.grid(row=1, column=1)

username = ''
password = ''

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

# list of text to act as the email base value.
email_text = json.loads(open('short_text.json').read())


def mainFunction():
    global username
    global password

    tkinter.Label(parentFrame, text="Generating UserData...").grid(
        row=11, columnspan=2)
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

outputText = tkinter.StringVar()
tkinter.Label(
    parentFrame, textvariable=outputText).grid(row=1, columnspan=2)
outputText.set('')


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


chkVal = tkinter.IntVar()
ttk.Checkbutton(
    parentFrame, text="Output To File", variable=chkVal, onvalue=1, offvalue=0, command=outputCheck).grid(row=0, columnspan=2)

tkinter.Label(parentFrame, text="Set Results Length").grid(row=2, columnspan=2)

lengthOptions = ttk.Combobox(parentFrame, values=[
    "Short (300)",
    "Medium (1,750)",
    "Long (7,500)",
    "Very Long (100k)",
    "Million! (~1.1m)"
], state="readonly").grid(row=3, columnspan=2)
# ^ before ".grid", add font if desired

# Wire up function on length selection.
# lengthOptions.bind("<<ComboboxSelected>>", lengthSelection)


def enableEntry():
    global urlLabel, urlEntry, emailLabel, emailEntry, passwordLabel, passwordEntry
    if (chkVal2.get() == 1):
        print('checked')
        urlLabel = tkinter.Label(parentFrame, text="Target URL")
        urlLabel.grid(row=5)
        urlEntry = tkinter.Entry(parentFrame,)
        urlEntry.grid(row=5, column=1)
        emailLabel = tkinter.Label(parentFrame, text="Email Value")
        emailLabel.grid(row=6)
        emailEntry = tkinter.Entry(parentFrame)
        emailEntry.grid(row=6, column=1)
        passwordLabel = tkinter.Label(
            parentFrame, text="Password Value")
        passwordLabel.grid(row=7)
        passwordEntry = tkinter.Entry(parentFrame)
        passwordEntry.grid(row=7, column=1)
    if (chkVal2.get() == 0):
        print('unchecked')
        urlLabel.grid_remove()
        urlEntry.grid_remove()
        emailLabel.grid_remove()
        emailEntry.grid_remove()
        passwordLabel.grid_remove()
        passwordEntry.grid_remove()


chkVal2 = tkinter.IntVar()
ttk.Checkbutton(
    parentFrame, text="Send to URL", command=enableEntry, variable=chkVal2, onvalue=1, offvalue=0).grid(row=4, columnspan=2)


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


# passwordComplex =
ttk.Checkbutton(
    parentFrame, text="Enable Realistic Password", command=showWarn, variable=chkShow, onvalue=1, offvalue=0).grid(row=8, columnspan=2)


tkinter.Label(parentFrame, textvariable=passwordText).grid(row=9, columnspan=2)


def runGenerator():

    tkinter.Label(parentFrame, text="Generating UserData...").grid(
        row=11, columnspan=2)
    print('running main')


btn1 = ttk.Button(runFrame, text="Run",  command=mainFunction)
btn1.grid(
    row=10, columnspan=2)
# btn1.bind(mainFunction)

tkinter.Label(parentFrame).grid(row=11)


window.mainloop()
