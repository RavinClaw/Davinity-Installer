# Davinity-Installer
A little installer project that allows you to create a simple installer using python that can download files and / or store them locally

# Want to install it manually
The command I used to turn this into an application
```
pyinstaller --onefile --windowed --icon="Davinity Installer/davinity.ico" --name "Davinity Installer" --add-data "Davinity Installer/davinity.png;Davinity Installer" "Davinity Installer/__main__.py"
```

# How to use Davinity Installer
The `index.json` is the location where all of your files are specified, here is an exmaple
```json
{
    "version": "0.1", // This is the version of the installer and should not be changed!

    "package_name": "Davinity Installer", // The name of your package also used for the directory path on default installs or can be used with "%n"
    "package_version": "0.1", // The version of you package, this will be displayed on the installer install page
    "package_description": "The davinity installer is designed to mostly only use inbuilt python functions, this installer is intended for those who want to use a simple installer written in python.", // This is the description for your install, just give a breaf description of what your program is
    "package_default": "%appdata%/%n/", // This is the location to where your program will be installed. Default on download is ("%appdata%/%n/")
    "files": [ // This is where you specify the actual files that you want
        {
            "url": "https://raw.githubusercontent.com/jabbalaci/Elite/refs/heads/master/README.md", // Here is an example of a URL download (This Repo is a Planet Name Generator that I am using in another project of mine, show them some love :3)
            "path": "readme.md" // This is the location to where it will be installed within the specified directory
        },
        {
            "file": "temp.txt", // file thats stored within the `files/` folder, you don't need to say that it's in `files/` however you can create folders in the `files/` and then you must specify then like this `example/example.txt`
            "path": "temp.txt" // Once again the output location
        }
    ]
}
```



# Suggesting more content
I give you permission to use the `Issues` tab for this, but please keep in mind to use [Suggestion] in your title, also I will not accept suggestions that are about using a different language or making some sort of auto script installer like a plugins folder that runs scripts on completed install or during install, I won't accept those due to security reasons. and Yes I will be adding hashing in the future.

# What I have planned
Next Version: `v0.2`:
 - Hash the provided files so that they can be verified
 - Adding an `Author` and `Source-URL` to the installer `index.json` for people to say who they are
 - Updating the GUI for the installer to make it fancy and adding some more text durring the Install Page
