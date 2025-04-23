
# Collecting all widgets on currrent window
def all_widgets (root) :
    global _list
    _list = root.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

#Clear window from all widgets
def delete_all_widgets():
    widget_list = all_widgets(root)
    for item in widget_list:
        item.destroy()
  
def save_existing():
    get_notes=existing_note.get('1.0',END)
    new_file=open(file_name,'w')
    new_file.write(get_notes)
    print("Saved")
    delete_all_widgets()
    options()
    
#Edit existing note page
def edit_note():
    global file_name
    global existing_note
    
    file_name=file_to_edit_entry.get()
    delete_all_widgets()
    root.title("Edit note")
    root.geometry("450x300")
    root.resizable(False,False)
    if os.path.exists(file_name):
        existing_note = scrolledtext.ScrolledText(root, wrap=tk.WORD,
                                      width=40, height=8)
                                      #font=("Times New Roman", 15)
        existing_note.grid(column=0, row=1, pady=10, padx=10)
        # placing cursor in text area
        existing_note.focus()
        current_notes=open(file_name,'r')
        for line in current_notes:
            existing_note.insert('insert',line)
        # Creating all widgets and display it edit_note window
        save_button=Button(root,text="Save",command=save_existing)
        save_button.grid(row=2,column=0)
        back_button=Button(root,text="Back",command=options)
        back_button.grid(row=3,column=0,padx=5,pady=5)
        log_out_button=Button(root,text="Log Out",command=log_out)
        log_out_button.grid(row=1,column=2,padx=5,pady=5)
    else:
        print("No such file '{}'".format(file_name), file=sys.stderr)
        existed_note()
#Page to enter existing file name 
def existed_note():
    global file_to_edit_entry
    root.title("Find existing file")
    root.geometry("450x100")
    root.resizable(False,False)
    delete_all_widgets()
    title_label=Label(root,text="Enter file name")
    title_label.grid(row=0,column=0,padx=5,pady=5)
    file_to_edit_entry=Entry(root)
    file_to_edit_entry.grid(row=0,column=1,padx=5,pady=5)
    edit_file_button=Button(root,text="Edit note",command=edit_note)
    edit_file_button.grid(row=1,column=1,padx=5,pady=5)
    back_button=Button(root,text="Back",command=options)
    back_button.grid(row=1,column=0,padx=5,pady=5)
    log_out_button=Button(root,text="Log Out",command=log_out)
    log_out_button.grid(row=1,column=2,padx=5,pady=5)

#Log out function
def log_out():
    delete_all_widgets()
    start()

#Homepage displayed after succesfully logging in
def options():
    root.title("Options")
    root.geometry("310x100")
    root.resizable(False,False)
    delete_all_widgets()
    new_note=Button(root,text="New note", command=create_new_file)
    new_note.grid(row=0,column=1,padx=5,pady=5)
    edit_notes=Button(root,text="Edit existing note",command=existed_note)
    edit_notes.grid(row=1,column=1,padx=5,pady=5)
    back_button=Button(root,text="Back",command=start)
    back_button.grid(row=1,column=0,padx=5,pady=5)

#Sign up for new member's page
def sign_up():
    global folder_name
    new_username = sign_up_username_text_box.get()
    new_password = sign_up_password_text_box.get()
    #Opening csv file in read mode
    with open('login.csv', 'r') as csvfile:
        username = csv.reader(open('login.csv','r'))
        for row in username:
            #If new username entered is available in the csv file,column 0
            if new_username==row[0] and new_username!="":
                break
            else:
                with open('login.csv', 'a', newline = '') as f:
                    dict_writer = DictWriter(f, fieldnames=['Username', 'Password'])
                    if os.stat('login.csv').st_size == 0:        #if file is not empty than header write else not
                        dict_writer.writeheader()
                    dict_writer.writerow({
                        'Username' : new_username,
                        'Password' : new_password,
                        })
                    done=True
                    break
        if done==True:
            print("Signed up!")
        else:
            print("Username already exist. Please choose another username")
            sys.stdout.write(CURSOR_UP_ONE)
            sys.stdout.write(ERASE_LINE)
        #sign_up_username_text_box.delete(0,END)
        #sign_up_password_text_box.delete(0,END)
        #csvfile.close()
    #write to csv file code here
    '''
    with open('login.csv', 'a', newline = '') as f:
        dict_writer = DictWriter(f, fieldnames=['Username', 'Password'])
        if os.stat('login.csv').st_size == 0:        #if file is not empty than header write else not
            dict_writer.writeheader()
       
        dict_writer.writerow({
            'Username' : new_username,
            'Password' : new_password,
        })
        '''
#Create new account function    
def create_acc():
    global sign_up_username_text_box
    global sign_up_password_text_box
    global back_button
    root.title("Create new account")
    root.geometry("320x150")
    root.resizable(False,False)
    username_text_box.destroy()
    password_text_box.destroy()
    log_in_button.destroy()
    exit_button.destroy()
    create_acc_button.destroy()
    new_username_label=Label(root,text="New username: ",pady=10)
    new_username_label.grid(row=1,column=0)    
    sign_up_username_text_box=Entry(root)
    sign_up_username_text_box.grid(row=1,column=1)
    password_label=Label(root,text="New password: ",pady=10)
    password_label.grid(row=2,column=0)    
    sign_up_password_text_box=Entry(root)
    sign_up_password_text_box.grid(row=2,column=1)
    sign_up_button=Button(root,text="Sign up",command=sign_up)
    sign_up_button.grid(row=5,column=1,pady=10,padx=10)
    back_button=Button(root,text="Back",command=start)
    back_button.grid(row=5,column=0)

#Save new file function
def save_new():
    get_notes=note.get('1.0',END)
    new_file=open(file_name,'w+')
    new_file.write(get_notes)
    print("Saved")
    delete_all_widgets()
    options()


    
def write_new_note():
    global note
    global file_name
    file_name=get_username_text_box+title_entry.get()
    folder_name=get_username_text_box
    new_file=open(file_name,'w+')
    delete_all_widgets()
    root.geometry("450x300")
    # Creating all widgets and display it on write_new_note window
    note = scrolledtext.ScrolledText(root, wrap=tk.WORD,
                                      width=40, height=8)
    note.grid(column=0, row=1, pady=10, padx=10)
    # placing cursor in text area
    note.focus()
    save_button=Button(root,text="Save",command=save_new)
    save_button.grid(row=2,column=0)
    back_button=Button(root,text="Back",command=options)
    back_button.grid(row=3,column=0,padx=5,pady=5)
    log_out_button=Button(root,text="Log Out",command=log_out)
    log_out_button.grid(row=3,column=2,padx=5,pady=5)

           
#Creating new file page
def create_new_file():
    global title_entry
    
    root.title("Create new file")
    root.geometry("450x100")
    root.resizable(False,False)
    delete_all_widgets()
    # Creating all widgets and display it on create_new_file window
    title_label=Label(root,text="Enter the file name")
    title_label.grid(row=0,column=0,padx=5,pady=5)
    title_entry=Entry(root)
    title_entry.grid(row=0,column=1,padx=5,pady=5)
    add_file_button=Button(root,text="Create note",command=write_new_note)
    add_file_button.grid(row=1,column=1,padx=5,pady=5)
    back_button=Button(root,text="Back",command=options)
    back_button.grid(row=1,column=0,padx=5,pady=5)
    log_out_button=Button(root,text="Log Out",command=log_out)
    log_out_button.grid(row=1,column=2,padx=5,pady=5)

#Starting page
def start():
    global username_label
    global get_username_text_box
    global username_text_box
    global sign_up_username_text_box
    global password_label
    global get_password_text_box
    global password_text_box
    global sign_up_password_text_box
    global log_in_button
    global exit_button
    global create_acc_button
    global sign_up_button
    global back_button
    #delete_all_widgets()
    root.title("Login")
    root.geometry("300x180")
    root.resizable(False,False)
    delete_all_widgets()
    # Creating all widgets and display it on start window
    sign_up_username_text_box=Label(root)
    sign_up_password_text_box=Label(root)
    sign_up_button=Button(root)
    back_button=Button(root)
    username_label=Label(root,text="Username: ",pady=10)
    username_label.grid(row=1,column=0)
    username_text_box=tk.Entry(root, borderwidth=2,width=20)
    username_text_box.grid(row=1,column=1)
    get_username_text_box=username_text_box.get()
    password_label=Label(root,text="Password: ",pady=10)
    password_label.grid(row=2,column=0)
    password_text_box=tk.Entry(root, borderwidth=2,width=20)
    password_text_box.grid(row=2,column=1)
    get_password_text_box=password_text_box.get()
    log_in_button=Button(root,text="Log in",command=log_in)
    log_in_button.grid(row=3,column=1)
    exit_button=Button(root,text="Exit",command=quit)
    exit_button.grid(row=5,column=0,padx=10,pady=10)
    create_acc_button=Button(root,text="Create account",command=create_acc)
    create_acc_button.grid(row=5,column=1,padx=10,pady=10)

#Action to take if the log in button is pressed
def log_in():
    #Opening csv file in read mode
    with open('login.csv', 'r') as csvfile:
        username = csv.reader(open('login.csv','r'))
        for row in username:
            try:
                #If username entered is available in the csv file,column 0
                #and if password is on the same row but in column 1
                if username_text_box.get()==row[0] and password_text_box.get()==row[1]:
                    delete_all_widgets()
                    have_username=True
                    break
                else:
                    have_username=False
            except TclError:
                pass
            
        if have_username==False:
            print("Invalid username or password")
            sys.stdout.write(CURSOR_UP_ONE)
            sys.stdout.write(ERASE_LINE)
            try:
                username_text_box.delete(0,END)
                password_text_box.delete(0,END)
            except TclError:
                pass
        else:
            options()
        
                
if __name__=='__main__':
    from tkinter import *
    from tkinter import scrolledtext
    from csv import *
    import csv as csv
    #import shutil,os
    import tkinter as tk
    import os
    import sys
    from tkinter import filedialog
    root=Tk()
    ERASE_LINE='\x1b[2K'
    CURSOR_UP_ONE='\x1b[1A'
    start()
    mainloop()