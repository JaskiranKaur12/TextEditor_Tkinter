import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

#hashing is turnnig piece of data of arbitrary length to piece of data of specific length

text_contents=dict()

def check_for_changes():
    current=get_text_widget()
    content = current.get('1.0', 'end-1c')
    name=notebook.tab("current")['text']
    if hash(content)!=text_contents[str(current)]:
        if name[-1]!='*':
            notebook.tab('current',text=name+'*')
    elif name[-1]=='*':
        notebook.tab('current',text=name[:-1])


def get_text_widget():
    text_widget = root.nametowidget(notebook.select())
    return text_widget

def confirm_quit():
    unsaved=False
    for tab in notebook.tabs():
        text_widget=root.nametowidget(tab)
        content=text_widget.get('1.0','end-1c')

        if hash(content)!=text_contents[str(text_widget)]:
            unsaved=True
            break

    if unsaved:
        confirm=messagebox.askyesno(
            message="you have unsaved changes...Are you sure you want to quit?",
            icon='question',
            title='Confirm Quit',)


        if not confirm:
            return

    root.destroy()


def create_file(content="",title="Untitled"):#if no arguments are passed, then defined arguments will be used
    text_area = tk.Text(notebook)
    text_area.pack(fill="both", expand=True)
    text_area.insert("end",content)

    notebook.add(text_area, text=title)
    notebook.select(text_area)

    text_contents[str(text_area)]=hash(content)



def save_file():

    file_path=filedialog.asksaveasfilename()
    try:
        file_name=os.path.basename(file_path)
        text_widget=root.nametowidget(notebook.select())
        content=text_widget.get('1.0','end-1c')#1-0=>line 1 starting from 0 character till end removing last(next line character) automatically added by widget

        with open(file_name,'w') as f:
            f.write(content)
    except(AttributeError,FileNotFoundError):
        print('Save operation not completed')
        return
    notebook.tab('current',text=file_name)#current selected tab
    text_contents[str(text_widget)] = hash(content)


def open_file():
    file_path = filedialog.askopenfilename()
    try:
        file_name = os.path.basename(file_path)
        with open(file_path,'r') as f:
            content=f.read()
    except(AttributeError,FileNotFoundError):
        print('Open operation not completed')
        return

    create_file(content,file_name)


root = tk.Tk()
root.title("My Text Editor")
root.option_add("*tearOff", False)

main = ttk.Frame(root)
main.pack(fill="both", expand=True, padx=(1), pady=(4, 0))

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
edit_menu=tk.Menu(menubar)

menubar.add_cascade(menu=file_menu, label="File")
menubar.add_cascade(menu=edit_menu,label='Edit')

file_menu.add_command(label="New", command=create_file, accelerator='Ctrl+N')
file_menu.add_command(label="Open", command=open_file, accelerator='Ctrl+O')
file_menu.add_command(label="Save", command=save_file, accelerator='Ctrl+S')
file_menu.add_command(label='Quit', command=confirm_quit)


notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)
create_file()

root.bind('<KeyPress>',lambda event: check_for_changes())
root.bind('<Control-n>', lambda event:create_file())# we use event because we might use this
root.bind('<Control-o>', lambda event:open_file())
root.bind('<Control-s>', lambda event:save_file())


root.mainloop()
