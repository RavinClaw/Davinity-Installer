# Davinity-Installer
A little installer project that allows you to create a simple installer using python that can download files and / or store them locally


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
