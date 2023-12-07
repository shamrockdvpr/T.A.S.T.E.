from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


def main():
    current_file = ''
    first_save = True

    helpbox = open('user_manual.txt', 'r')
    help_text = helpbox.read()
    helpbox.close()

    def open_file():
        # Opens file to edit
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if not filepath:
            return

        text_edit.delete('1.0', END)

        global current_file, first_save
        current_file = filepath
        first_save = False

        with open(filepath, mode='r', encoding='utf-8') as input_file:
            text = input_file.read()
            text_edit.insert(END, text)

        main.title(f"T.A.S.T.E. - {filepath}")

    def new_file():
        text_edit.delete('1.0', END)
        main.title("T.A.S.T.E. - New File")

        global first_save
        first_save = True

    def save_asfile():
        filepath = asksaveasfilename(
            defaultextension='.txt',
            filetypes=[("Text Files", "*.txt"), ('All Files', '*.*')]
        )

        if not filepath:
            return

        global current_file
        current_file = filepath

        with open(filepath, mode='w', encoding='utf-8') as output_file:
            text = text_edit.get('1.0', END)
            output_file.write(text)

        main.title(f"T.A.S.T.E - {filepath}")

    def save_file():
        global first_save

        if first_save:
            save_asfile()
            first_save = False

        with open(current_file, mode='w', encoding='utf-8') as output_file:
            text = text_edit.get('1.0', END)
            output_file.write(text)

    def help_window():
        help_win = Tk()  # spawn window
        help_win.title("Help")  # name window
        help_win.resizable(width=False, height=False)  # set unresizeable

        text_box = Text(master=help_win, height=30, width=100)  # instantiate text box

        text_box.insert("1.0", help_text)  # add manual text

        text_box.pack()  # send to window
        text_box.config(state='disabled')  # make uneditable

        help_win.mainloop()  # run window loop

    # Initialize window

    main = Tk()
    main.title("T.A.S.T.E. - New File")

    main.rowconfigure(1, minsize=600, weight=1)
    main.columnconfigure(1, minsize=800, weight=1)

    # Generate elements

    # Frames
    frm_buttons = Frame(
        master=main,
        relief=RAISED,
        bd=2
    )

    # Text Window
    text_edit = Text(
        master=main,
    )

    # File Buttons
    btn_open = Button(
        master=frm_buttons,
        text='Open',
        command=open_file
    )

    btn_save_as = Button(
        master=frm_buttons,
        text='Save As',
        command=save_asfile
    )

    btn_save = Button(
        master=frm_buttons,
        text='Save',
        command=save_file
    )

    btn_new = Button(
        master=frm_buttons,
        text='New',
        command=new_file
    )

    btn_help = Button(
        master=frm_buttons,
        text='Help',
        command=help_window
    )

    # Add elements to buttons frame

    btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
    btn_new.grid(row=1, column=0, sticky='ew', padx=5, pady=5)
    btn_save_as.grid(row=2, column=0, sticky='ew', padx=5, pady=5)
    btn_save.grid(row=3, column=0, sticky='ew', padx=5, pady=5)
    btn_help.grid(row=4, column=0, sticky='ew', padx=5, pady=5)

    frm_buttons.grid(row=1, column=0, sticky='ns')

    # add in text box
    text_edit.grid(row=1, column=1, sticky='nsew')

    main.mainloop()

main()
