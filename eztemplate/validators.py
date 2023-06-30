import os

def validate_file_path(path: str):    
    if os.path.isfile(path):
        return path
    else:
        raise FileNotFoundError
    
def validate_new_values(values: str):
    if "," in values:
        return values.split(",")
    return [values]
