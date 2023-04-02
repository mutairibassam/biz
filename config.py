
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