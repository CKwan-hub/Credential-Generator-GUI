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


window = tkinter.Tk()
window.title("CredGen")
window.geometry('230x300')
window.resizable(0, 0)
# dropdownFont = ("Courier", 8)

# label_widget = tk.Label(widget, option=placeholder)

# label_widget = tk.Label(widget, option=placeholder)
# checkbutton_widget = tk.CheckButton(widget, option=placeholder)

# top_frame = tkinter.Frame(window).pack()
# bottom_frame = tkinter.Frame(window).pack(side="bottom")
# button_widget = tk.Button(widget, option=placeholder)

outputText = tkinter.StringVar()
tkinter.Label(
    window, textvariable=outputText).grid(row=1, columnspan=2)
outputText.set('')


def outputCheck():
    if (chkVal.get() == 1):
        print('checked')
        outputText.set('Data Generated In \"Output.txt\"')
    if (chkVal.get() == 0):
        print('unchecked')
        outputText.set('')


chkVal = tkinter.IntVar()
tkinter.Checkbutton(
    window, text="Output To File", variable=chkVal, onvalue=1, offvalue=0, command=outputCheck).grid(row=0, columnspan=2)

tkinter.Label(window, text="Set Results Length").grid(row=2, columnspan=2)

lengthOptions = tkinter.ttk.Combobox(window, values=[
    "Short (300)",
    "Medium (1,750)",
    "Long (7,500)",
    "Very Long (100k)",
    "Million! (~1.1m)"
], state="readonly").grid(row=3, columnspan=2)
# ^ before ".grid", add font if desired

# Wire up function on length selection.
# lengthOptions.bind("<<ComboboxSelected>>", lengthSelection)


# urlLabel = tkinter.Label(window, text="Target URL").grid(row=5)
# urlVar = tkinter.StringVar()
# urlVar = 'disabled'
# urlEntry = tkinter.Entry(window, state='disabled').grid(row=5, column=1)
# print(urlEntry.window['state'])
# tkinter.Entry(window, state=urlVar).grid(row=5, column=1)
# print(urlVar)


def enableEntry():
    global urlLabel, urlEntry, emailLabel, emailEntry, passwordLabel, passwordEntry
    # global urlEntry
    # print(urlEntry)
    # global urlVar
    # print('global urlVar', urlVar)
    if (chkVal2.get() == 1):
        print('checked')
        urlLabel = tkinter.Label(window, text="Target URL")
        urlLabel.grid(row=5)
        urlEntry = tkinter.Entry(window,)
        urlEntry.grid(row=5, column=1)
        emailLabel = tkinter.Label(window, text="Email Value")
        emailLabel.grid(row=6)
        emailEntry = tkinter.Entry(window)
        emailEntry.grid(row=6, column=1)
        passwordLabel = tkinter.Label(
            window, text="Password Value")
        passwordLabel.grid(row=7)
        passwordEntry = tkinter.Entry(window)
        passwordEntry.grid(row=7, column=1)
        # urlEntry['state'] = tkinter.NORMAL
        # urlVar = 'normal'
        # print(urlVar)
    if (chkVal2.get() == 0):
        print('unchecked')
        urlLabel.grid_remove()
        urlEntry.grid_remove()
        emailLabel.grid_remove()
        emailEntry.grid_remove()
        passwordLabel.grid_remove()
        passwordEntry.grid_remove()

        # urlVar = 'disabled'
        # print(urlVar)


chkVal2 = tkinter.IntVar()
tkinter.Checkbutton(
    window, text="Send to URL", command=enableEntry, variable=chkVal2, onvalue=1, offvalue=0).grid(row=4, columnspan=2)


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
tkinter.Checkbutton(
    window, text="Enable Realistic Password", command=showWarn, variable=chkShow, onvalue=1, offvalue=0).grid(row=8, columnspan=2)


# passwordComplex.bind()

tkinter.Label(window, textvariable=passwordText).grid(row=9, columnspan=2)


def runGenerator():
    tkinter.Label(window, text="Generating UserData...").grid(
        row=11, columnspan=2)


btn1 = tkinter.Button(window, text="Run",
                      fg="red", command=runGenerator).grid(row=10, columnspan=2)

tkinter.Label(window).grid(row=11)


window.mainloop()

# def lengthSelection(event)
#
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
email_text = json.loads(open('medium_text.json').read())

# open output.txt in append mode.
output_file = open('output.txt', 'a')

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
    # output_file.write('\"Username:\" \'% s\' \"Password:\" \'% s\' \n' %
    #                   (username, password))
    # print('Username: %s Password: %s' % (username, password))
