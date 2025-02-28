from installer import *
from tkinter import Tk
from tkinter import Label
from tkinter import W, CENTER
from sys import exit
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *
from os.path import dirname as pathdir
from os.path import join as pathjoin
from os import getenv
from os import mkdir


version, package_name, package_version, package_description, package_default, files = load_from_index()

print(f"This Davinity installer is made using version: v{version}")
script_dir = pathdir(__file__)

package_default = package_default.replace("%appdata%", getenv("APPDATA"))
package_default = package_default.replace("%APPDATA%", getenv("APPDATA"))
package_default = package_default.replace("%AppData%", getenv("APPDATA"))
package_default = package_default.replace("%LocalAppData%", getenv("LOCALAPPDATA"))
package_default = package_default.replace("%localappdata%", getenv("LOCALAPPDATA"))
package_default = package_default.replace("%LOCALAPPDATA%", getenv("LOCALAPPDATA"))
package_default = package_default.replace("%programfiles%", getenv("ProgramFiles"))
package_default = package_default.replace("%PROGRAMFILES%", getenv("ProgramFiles"))
package_default = package_default.replace("%ProgramFiles%", getenv("ProgramFiles"))
package_default = package_default.replace("%programfiles(x86)%", getenv("ProgramFiles(x86)"))
package_default = package_default.replace("%PROGRAMFILES(x86)%", getenv("ProgramFiles(x86)"))
package_default = package_default.replace("%ProgramFiles(x86)%", getenv("ProgramFiles(x86)"))


def installing():
    dav_files = pathjoin(script_dir, "files/")
    if not exists(package_default):
        mkdir(package_default)
    for file in files:
        print(file)
        if "url" in file:
            download_file(file.get("url"), package_default + file.get("path"))
        elif "file" in file:
            install_from_path(dav_files + file.get("file"), package_default + file.get("path"))
        else:
            print(f"Unknown install format in: {file.get('path')}")
    messagebox.showinfo("Davinity Installer", "Install Complete!")


root = Tk("Davinity Installer", "davinity-installer", sync=True)
root.geometry("500x300")
root.title("Davinity Installer")


lbl = Label(root, text="Do you want to install the following package?", anchor=CENTER)
lbl2 = Label(root, text=f"Name: {package_name}", anchor=W)
lbl3 = Label(root, text=f"Version: v{package_version}", anchor=W)
lbl4 = Label(root, text=f"{package_description}", anchor=W, wraplength=450)


def def_quit():
    messagebox.showerror("Davinity Installer", "Install Cancelled")
    root.quit()
    exit()

def def_install():
    global package_default
    if messagebox.askokcancel("Davinity Installer", "You are about install a python program, are you sure you want to install this program as it may have unrestricted access to your pc and preform functions / tasks as administrator"):
        messagebox.showinfo("Davinity Installer", "Installing will begin shortly")
        if messagebox.askyesno("Davinity Installer", f"Use this install directory?\nLocation: \"{package_default}\""):
            installing()
            exit()
        else:
            new_directory = ""
            while new_directory is None or new_directory == "" or new_directory == " ":
                new_directory = simpledialog.askstring("Davinity Installer", "Where would you like to install this program?", initialvalue=f"{package_default}")
            package_default = new_directory
            package_default = package_default.replace("%appdata%", getenv("APPDATA"))
            package_default = package_default.replace("%APPDATA%", getenv("APPDATA"))
            package_default = package_default.replace("%AppData%", getenv("APPDATA"))
            package_default = package_default.replace("%LocalAppData%", getenv("LOCALAPPDATA"))
            package_default = package_default.replace("%localappdata%", getenv("LOCALAPPDATA"))
            package_default = package_default.replace("%LOCALAPPDATA%", getenv("LOCALAPPDATA"))
            package_default = package_default.replace("%programfiles%", getenv("ProgramFiles"))
            package_default = package_default.replace("%PROGRAMFILES%", getenv("ProgramFiles"))
            package_default = package_default.replace("%ProgramFiles%", getenv("ProgramFiles"))
            package_default = package_default.replace("%programfiles(x86)%", getenv("ProgramFiles(x86)"))
            package_default = package_default.replace("%PROGRAMFILES(x86)%", getenv("ProgramFiles(x86)"))
            package_default = package_default.replace("%ProgramFiles(x86)%", getenv("ProgramFiles(x86)"))
            def_install()
    else:
        messagebox.showerror("Davinity Installer", "Install cancelled")
        exit()

btn = Button(root, text="Install", fg="black", command=def_install)
btn2 = Button(root, text="Cancel", fg="black", command=def_quit)

lbl.place(x=125, y=50)
lbl2.place(y=80, x=80)
lbl3.place(y=100, x=80)
lbl4.place(y=150, x=25)

btn.place(y=270, x=200)
btn2.place(y=270, x=250)

root.mainloop()
