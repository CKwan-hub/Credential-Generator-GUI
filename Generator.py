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
# Code to add widgets will go here...
# checkbutton_widget = tk.CheckButton(widget, option=placeholder)
# checkbutton_widget = tk.CheckButton(widget, option=placeholder)
# checkbutton_widget = tk.CheckButton(widget, option=placeholder)
# checkbutton_widget = tk.CheckButton(widget, option=placeholder)

# label_widget = tk.Label(widget, option=placeholder)
# checkbutton_widget = tk.CheckButton(widget, option=placeholder)

# top_frame = tkinter.Frame(window).pack()
# bottom_frame = tkinter.Frame(window).pack(side="bottom")
# button_widget = tk.Button(widget, option=placeholder)

tkinter.Checkbutton(
    window, text="Output To File").grid(row=0, columnspan=2)

tkinter.Label(window, text="Generated List Size:").grid(row=1, columnspan=2)

lengthOptions = tkinter.ttk.Combobox(window, values=[
    "Short (300)",
    "Medium (1,750)",
    "Long (7,500)",
    "Very Long (100k)",
    "Million! (~1.1m)"
], state="readonly").grid(row=2, columnspan=2)
# ^ before ".grid", add font if desired

# Wire up function on length selection.
# lengthOptions.bind("<<ComboboxSelected>>", lengthSelection)

tkinter.Checkbutton(
    window, text="Send to URL").grid(row=3, columnspan=2)

tkinter.Label(window, text="Target URL").grid(row=4)
tkinter.Entry(window).grid(row=4, column=1)

tkinter.Label(window, text="Email Value").grid(row=5)
tkinter.Entry(window).grid(row=5, column=1)

tkinter.Label(window, text="Password Value").grid(row=6)
tkinter.Entry(window).grid(row=6, column=1)

# TODO: toggle display message on/off check.


def showWarn():
    tkinter.Label(window, text="Generating realistic passwords.").grid(
        row=8, columnspan=2)


# passwordComplex =
tkinter.Checkbutton(
    window, text="Enable Realistic Password", command=showWarn).grid(row=7, columnspan=2)


# passwordComplex.bind()

tkinter.Label(window, text="").grid(row=8, columnspan=2)


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
