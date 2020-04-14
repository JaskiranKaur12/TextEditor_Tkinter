import tkinter as tk #alias
from tkinter import ttk

# def talk_to_me():
#     print(f"Hello, my name is {user_name.get() or 'World'}")

# user_name=tk.StringVar()
# name_label=ttk.Label(root,text='Name:')
# name_label.pack(side='left',padx=(0,10))
# name_entry=ttk.Entry(root, width=20, textvariable=user_name)#themed tk
# name_entry.pack(side='left')
# name_entry.focus()
#
# me_button=ttk.Button(root,text="Say Hi",command=talk_to_me)
# me_button.pack(side='left',fill='x',expand=True)
#
# quit_button=ttk.Button(root,text="Quit Application",command=root.destroy)#if we want to end the application intentionally
# quit_button.pack(side='right',fill='x',expand=True)
root=tk.Tk()#parent
root.title('Hello')
tk.Label(root, text="Label 0", bg="red").pack(side="right",fill='both',expand=True)
tk.Label(root, text="Label 1", bg="green").pack(side="top",fill='both',expand=True)
tk.Label(root, text="Label 2", bg="red").pack(side="left",fill='both',expand=True)
tk.Label(root, text="Label 3", bg="red").pack(side="left",fill='both',expand=True)
root.mainloop()# this will pause the program until the exit button is clicked

