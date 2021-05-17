
import tkinter as tk
from tkinter import ttk
import num2words
from num2words import num2words

# Application body()
body = tk.Tk()
body.title('Num To Words')


number_language = {'en' : 'English', 'de' : 'German', 'es' : 'Spanish', 'fi' : 'Finnish',
'fr' : 'French', 'hu' : 'Hungarian', 'it' : 'Italian', 'lt' : 'Lithuanian', 'lv' : 'Latvian',
'no' : 'Norwegian', 'pl' : 'Polish', 'pt' : 'Portuguese', 'ru' : 'Russian', 'uk' : 'Ukrainian'}

currency_objectives = {
        'USD' : 'USA',
        'AUD' : 'Australia',
        'CAD' : 'Canada',
        'EUR' : 'Euro',
        'GBP' : 'G-Britain',
        'HUF' : 'Hungaria',
        'NOK' : 'Norwegia',
        'PLN' : 'Poland',
        'RUB' : 'Russia',
        'UAH' : 'Ukraine',

    }

# Number_Type_Box_Label
type_box_label = ttk.Label(body, text='Num Type:')
type_box_label.grid(row=0, column=0, pady=3, padx=1)

# Type_Of_Numbers Combobox
type_of_number_box = ttk.Combobox(body, values=[ 'currency', 'ordinal', 'ordinal_num',
 'year', 'cardinal'], state="readonly", justify='center')

type_of_number_box.place(x=90, y=3, width=90)
#grid(row=0, column=1, pady=3, padx=1)
type_of_number_box.current(0)

# Language_Box_Label
language_box_label = ttk.Label(body, text='Language:')
language_box_label.place(x=190, y=3)
#grid(row=0, column=2)

# Language_Of_Numbers Combobox
#language_box = ttk.Combobox(body, values=list(number_language.values()), state='readonly', justify='center')
language_box = ttk.Combobox(body, values=list(number_language.items()), state='readonly', justify='center')
language_box.place(x=256, y=3, width=90)
#grid(row=0, column=2, pady=3, padx=1)
language_box.current(0)

# Currency_Box_Label
currency_box_label = ttk.Label(body, text='Currency:')
currency_box_label.place(x=355, y=3)
#grid(row=0, column=4)

# Currency_Box Combobox
#currency_box = ttk.Combobox(body, values=list(currency_objectives.items()), state='readonly', justify='center')
currency_box = ttk.Combobox(body, values=list(currency_objectives.items()), state='readonly', justify='center')
currency_box.place(x=417, y=3, width=104)
#grid(row=0, column=3, pady=3, padx=1)
currency_box.current(0)

# number_field_Label
number_field_label = ttk.Label(body, text='   Insert Number:  ')
number_field_label.grid(row=1, column=0)

# number Field
number_field = ttk.Entry(body, width=50)
number_field.grid(row=1, column=1)

# text_field_label
text_field_label = ttk.Label(body, text='  Converted Text: ')
text_field_label.grid(row=2, column=0)

# text_field
text_field = ttk.Entry(body, width=50)
text_field.grid(row=2, column=1)

# Method converts numbers from number field into text format and copy it into a text field
def num_to_words():
    number = number_field.get()
    type = type_of_number_box.get()

    cur = currency_box.get()

    language = language_box.get()

    #assign parameters:
    words = num2words(number, to=type, currency=cur[0:3], lang=language[0:2])

    text_field.delete(0, 'end')
    text_field.config(foreground='black')
    text_field.insert(0, words)


# Method copies the text field content into a clipboard
def word_to_clipboard():
    text_field.clipboard_clear()
    text_field.clipboard_append(text_field.get())
    body.update()

# Trying Exceptins
def except_check():
    check_number = False
    while check_number == False:
        try:
            number = float(number_field.get())
            check_number = True
            num_to_words()
        except ValueError:
            number_field.delete(0, 'end')
            text_field.delete(0, 'end')
            text_field.insert(0, 'Enter a numeric value')
            text_field.config(foreground='red')
            break

# Convert Button
def convertBtn():
    except_check()

# Convert Button pushing by "Enter"
def enterBtn(event):
    except_check()

# Copy To Clipboard Button
def copyBtn():
    word_to_clipboard()

#Copy To Clipboard Button Pushing by "Enter"
def copy_enterBtn(event):
    word_to_clipboard()

# making btn_convert()
btn_convert = ttk.Button(body, text='Convert To Words', width=18, command=convertBtn)
btn_convert.grid(row=1, column=2)

# function bind() waining for key "Return" or "Enter"
number_field.bind('<Return>', enterBtn)

# making btn_copy
btn_copy = ttk.Button(body, text='Copy To Clipboard', width=18, command=copyBtn)
btn_copy.grid(row=2, column=2)

# function bind() waining for key "Ctrl_Return"
text_field.bind('<Return>', copy_enterBtn)


# Function wm_attributes(with these parameters) keeps our programm in top of all windows.
body.wm_attributes('-topmost', True)
number_field.focus()

body.mainloop()
