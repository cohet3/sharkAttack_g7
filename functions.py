# ARCHIVO PARA LAS FUNCIONES GLOBAL
# AVISAR ANTES DE PUSHEAR, SI SE MODIFICA SE PUEDE EXCLUIR DEL PUSH

import re

def clean_strings(string): 
    """
    Function to clean strings by:
    - taking the first value if it contains a slash
    - replacing ' and ' with ' & '
    - removing all non-alphanumeric characters
    - stripping leading and trailing whitespace
    Args:
        string (str): string to clean
    Returns:
        str: cleaned string
    """
    new_str = string
    if isinstance(string, str):
        new_str = new_str.split("/")[0].strip() #when there are two possible values we'll pick the first one
        new_str = new_str.replace(" and ", " & ").replace(" AND ", " & ") #formatting
        new_str = re.sub(r"[@!#$%^*?()]", "", new_str)
        new_str = re.sub(r"\s+", " ", new_str)
        new_str = new_str.strip()
    return new_str