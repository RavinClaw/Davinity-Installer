from requests import get
from requests import Response
from os.path import exists
from json import load as jsonload


def download_file(url: str, path_plus_filename: str) -> bool:
    """ Downloads from a specified url into a file """
    response: Response = get(url)
    if response.status_code == 200:
        with open(path_plus_filename, "w") as file:
            file.write(response.text)
        return True
    else:
        return False


def download_files(urls: list[str], paths_plus_filenames: list[str]) -> list[bool]:
    """ Downloads from specified urls into files """
    successes: list[bool] = []

    for num in range(0, len(urls), 1):
        url: str = urls[num]
        path_plus_filename: str = paths_plus_filenames[num]
        response: Response = get(url)
        if response.status_code == 200:
            with open(path_plus_filename, "w") as file:
                file.write(response.text)
            successes.append(True)
        else:
            successes.append(False)

    return successes


def install_from_path(index_file, path_plus_filename: str) -> bool:
    """ Install files from the Index File """
    if not exists(path_plus_filename):
        file_data: str = ""
        if exists(index_file):
            with open(index_file, "r") as file:
                file_data = file.read()
        with open(path_plus_filename, "w") as file:
            file.write(file_data)
        return True
    else:
        return False


def install_from_paths(index_files: list[str], paths_plus_filenames: list[str]) -> list[bool]:
    """ Installs multiple files from the Index File """
    successes: list[bool] = []
    for num in range(0, len(index_files), 1):
        if install_from_path(index_files[num], paths_plus_filenames[num]):
            successes.append(True)
        else:
            successes.append(False)
    return successes


def load_from_index() -> tuple[str, str, str, str, str, list[dict]] | None:
    """ Loads the Index File """
    if exists("./index.json"):
        with open("./index.json", "r") as file:
            index = jsonload(file)
        version: str = index["version"]
        package_name: str = index["package_name"]
        package_version: str = index["package_version"]
        package_description: str = index["package_description"]
        package_default: str = index["package_default"]
        package_default = package_default.replace("%n", f"{package_name}")
        files: list[dict] = index["files"]
        return version, package_name, package_version, package_description, package_default, files
    else:
        return None
