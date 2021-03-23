

# TODO:
#
# Rename combobox options
# additional styles or fonts?
# Icon
#
# Stagger generation/submission by X (input) time in seconds for URL submissions?
# Open readme button
# Integrated terminal window?
# Hide/show terminal toggle?

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
window.title('CredGen')
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
dropdownFont = ('tahoma', 8)

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

# Setting input variables.
url = ''
username = ''
password = ''

# Options for seed files.
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

# Setting User Input Values.
urlValue = tkinter.StringVar()
urlValue.set('')
userValue = tkinter.StringVar()
userValue.set('')
passValue = tkinter.StringVar()
passValue.set('')

# Setting ComboBox Default.
comboTxt = tkinter.StringVar()
comboTxt.set('M')

# Combobox object for output length/seedfile selection.
lengthOptions = ttk.Combobox(secondFrame, values=[
    'S',
    'M',
    'L',
    'XL',
    'MILLION'
], state='readonly', font=dropdownFont, textvariable=comboTxt).grid(row=2, columnspan=2, pady=2)

# Setting Password ComboBox Default.
passCmbTxt = tkinter.StringVar()
passCmbTxt.set('Randomized')

# Combobox object for password type selection.
passOptions = ttk.Combobox(secondFrame, values=[
    'Realistic',
    'Strong',
    'Randomized'
], state='readonly', font=dropdownFont, textvariable=passCmbTxt).grid(row=4, columnspan=2, pady=1)

# Main function for generation.


def mainFunction():
    # Importing globals for input.
    global urlValue
    global userValue
    global passValue

    # Default seed file/.json length.
    seedFile = tkinter.StringVar()
    seedFile.set('medium_text.json')

    # Get values from the length combobox and select the .json file associated.
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

    # User message for completion.
    tkinter.Label(runFrame, text='Data Generated!', fg='red').grid(
        row=1, columnspan=2, pady=2)

    for email_data in email_text:
        # additional values for randomly adding a second word to email.
        name_random = ['', random.choice(email_text), '']

        # take a random amount of digits, at a random length between 0 and 4.
        name_digits = ''.join(random.choice(string.digits)
                              for i in range(random.choice(extra_length)))

        # choices for generated password additions
        pass_length = [1, 2, 3]

        # Add random selection of characters (at random length) to realistic password generation
        pass_digits = ''.join(random.choice(chars)
                              for i in range(random.choice(pass_length)))

        # Strong password choice. (Random selection of characters at a random selection of lengths)
        strongPass = ''.join(random.choice(chars)
                             for i in range(random.choice(password_length)))

        # Realistic password generation. (Random Word +/- Random Word + random digits/chars at random selection of lengths)
        realPass = ''.join(random.choice(email_text) +
                           random.choice(name_random) + pass_digits)

        # Options for randomized password selection.
        passSelect = [strongPass, realPass, realPass]

        # lowercase values from email_text + random digits + random choice of email suffix.
        username = email_data.lower() + random.choice(name_random) + \
            name_digits + random.choice(email_list)

        # Initial value for password default behavior.
        passwordVal = tkinter.StringVar()
        passwordVal.set(random.choice(passSelect))

        # Combobox association for desired password type selection.
        def passStyle():
            if (passCmbTxt.get() == 'Randomized'):
                passwordVal.set(random.choice(passSelect))
            if (passCmbTxt.get() == 'Realistic'):
                passwordVal.set(realPass)
            if (passCmbTxt.get() == 'Strong'):
                passwordVal.set(strongPass)

        passStyle()

        # Retrieve selection of password output type.
        password = passwordVal.get()

        # Check for if sending to external URL is selected.
        def sendURL():
            if (chkVal2.get() == 1):
                requests.post((urlValue.get()), allow_redirects=False, data={
                    userValue.get(): username,
                    passValue.get(): password
                })

        sendURL()

        # Output list of usernames and passwords to external if checked, if not, print values.
        if (chkVal.get() == 1):
            output_file.write('\'Username:\' \'% s\' \'Password:\' \'% s\' \n' %
                              (username, password))
        if (chkVal.get() == 0):
            print('Username: %s Password: %s' % (username, password))


# open output.txt in append mode.
output_file = open('output.txt', 'a')


# Modal description info.
descInfoTxt = tkinter.StringVar()
descInfoTxt.set(
    'Select Output Preference\n Choose Desired Output Length \n Select Password Style \n Run Generator')
descInfo = tkinter.Label(parentFrame, textvariable=descInfoTxt)
descInfo.grid(row=0, columnspan=2, pady=2)

# Info for Length Combobox.
tkinter.Label(secondFrame, text='Select Results Length:').grid(
    row=1, columnspan=2, pady=(11, 1))

# Info for Password style Combobox.
tkinter.Label(secondFrame, text='Select Password Types:').grid(
    row=3, columnspan=2, pady=1)

# Toggle message showing where output can be found.


def outputCheck():
    if (chkVal.get() == 1):
        outputText.set('Data Generated In \'Output.txt\'')
    if (chkVal.get() == 0):
        outputText.set('')


# Checkbutton for external output.
chkVal = tkinter.IntVar()
tkinter.Checkbutton(
    secondFrame, text='Output To Text File', variable=chkVal, onvalue=1, offvalue=0, command=outputCheck).grid(row=5, columnspan=2, pady=1)

# Info message for external output.
outputText = tkinter.StringVar()
tkinter.Label(
    secondFrame, textvariable=outputText, fg='red').grid(row=6, columnspan=2, pady=1)
outputText.set('')

# Initial values and disabled state for URL/Email/Password input fields.
urlLabel = tkinter.Label(
    parentFrame, text='Target URL', state='disabled')
urlLabel.grid(row=5, pady=3)
urlEntry = tkinter.Entry(parentFrame, textvariable=urlValue, state='disabled')
urlEntry.grid(row=5, column=1, pady=3)
emailLabel = tkinter.Label(
    parentFrame, text='Email Value', state='disabled')
emailLabel.grid(row=6, pady=3)
emailEntry = tkinter.Entry(
    parentFrame, textvariable=userValue, state='disabled')
emailEntry.grid(row=6, column=1, pady=3)
passwordLabel = tkinter.Label(
    parentFrame, text='Password Value', state='disabled')
passwordLabel.grid(row=7, pady=3)
passwordEntry = tkinter.Entry(
    parentFrame, textvariable=passValue, state='disabled')
passwordEntry.grid(row=7, column=1, pady=3)

# Function for toggling and allowing input of URL/Email/Password fields. Disabled state on unchecked.


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
            parentFrame, text='Email Value', state='normal')
        emailLabel.grid(row=6, pady=3)
        emailEntry = tkinter.Entry(
            parentFrame, textvariable=userValue, state='normal')
        emailEntry.grid(row=6, column=1, pady=3)
        passwordLabel = tkinter.Label(
            parentFrame, text='Password Value', state='normal')
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
            parentFrame, text='Email Value', state='disabled')
        emailLabel.grid(row=6, pady=3)
        emailEntry = tkinter.Entry(
            parentFrame, textvariable=userValue, state='disabled')
        emailEntry.grid(row=6, column=1, pady=3)
        passwordLabel = tkinter.Label(
            parentFrame, text='Password Value', state='disabled')
        passwordLabel.grid(row=7, pady=3)
        passwordEntry = tkinter.Entry(
            parentFrame, textvariable=passValue, state='disabled')
        passwordEntry.grid(row=7, column=1, pady=3)


# Formatting.
tkinter.ttk.Separator(parentFrame, orient='horizontal').grid(
    row=3, sticky='ew', columnspan=2)

# Checkbutton allowing editing of URL/Email/Password fields.
chkVal2 = tkinter.IntVar()
tkinter.Checkbutton(
    parentFrame, text='Send to URL', command=enableEntry, variable=chkVal2, onvalue=1, offvalue=0, pady=5).grid(row=4, columnspan=2)

# Generation Button/
btn1 = tkinter.Button(runFrame, text='Generate',  command=mainFunction)
btn1.grid(
    row=0, columnspan=2, pady=3)


window.mainloop()
