"""docs"""
from yaml import full_load, YAMLError

def get_secret() -> dict:
    """ 
    get telegram secret keys from yml file 

    [config.yml]
        @path: project_dir/config.yml

    telegram:
      token: xxxxxxxxxxxxxxxxxxxxx
      chat_id: xxxxxxxxxx
    ```
    [note] 
        - file should be valid `yml` format.
        - below logic extracting 'telegram' keys directly, so in case more keys
          are needed we need to return the full stream.

        # change below
        return full_load(stream)['telegram'].values()
        # to
        return full_load(stream)

        then you can get specific value by getting telegram parent first,
        then its children.
        
    """
    with open("config.yml", 'r', encoding="utf-8") as stream:
        try:
            return full_load(stream)['telegram'].values()
        except YAMLError as exception:
            raise exception

file_path: str = "./storage.txt"

def write(content):
    """ replace all existing file data will the new data """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

def append(content):
    """ add more the existing data """
    with open(file_path, "a",encoding="utf-8") as file:
        file.write(content)

def read():
    """ read current file data """
    content = ""
    with open(file_path, "r",encoding="utf-8") as file:
        content = file.read()
    return content

def compare(new: list, prev: list) -> list:
    """
    @current: the first list which will be the origianl source of the ids.
    @new: the second list which will be compared against to get missing ids.

    @difference: the finalized ids after getting the difference between
                original and prev lists.

    """
    if len(prev) > 0:
        return prev - new
    return []