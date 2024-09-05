# ARCHIVO PARA LAS FUNCIONES GLOBAL
# AVISAR ANTES DE PUSHEAR, SI SE MODIFICA SE PUEDE EXCLUIR DEL PUSH
import re
import numpy as np
import warnings as wrn
import pandas as pd


def clean_columns_names(data_frame): 
    """
    Matches the formats of all column names: replaces blanks with '_' and converts them to lowercase
    """
    
    data_frame.columns = data_frame.columns.str.replace(' ', '_').str.lower()

    return data_frame

def columns_drops(data_frame, columns_to_drop=None): 
    """
    Allows you to delete columns
    """
    
    if columns_to_drop is not None:
        data_frame = data_frame.drop(columns=columns_to_drop, errors='ignore')

    return data_frame

def drop_rows_nulls(data_frame, thresh=2): 
    """
    Allows you to delete rows that contain less than a minimum value of valid values
    """
    if thresh < 1:
        raise ValueError('Threshold must be 1 or less.') 
        

    data_frame_clean = data_frame.dropna(thresh=thresh)

    return data_frame_clean

def clean_and_filter_dates(dataframe, column_name, year): # 
    """
    This function focuses on cleaning dates: it converts these values ​​into a Year-Month-Day format and transforms it into datetime
    """

    def clean_datetimes(df_general):

        for fmt in ('%d %b %Y', '%d-%b-%Y', '%d %b-%Y', '%d-%b-%Y', '%d %b %y'):
            try:
                return pd.to_datetime(df_general, format=fmt)
            except ValueError:
                continue
            
        return pd.NaT
    
    with wrn.catch_warnings():
        wrn.simplefilter(action='ignore', category=pd.errors.SettingWithCopyWarning)
    
    
    dataframe_copy = dataframe.copy() # .copy() is used to avoid the error of working on the original dataframe
    
    dataframe_copy[column_name] = dataframe_copy[column_name].apply(clean_datetimes)

    limit_year = pd.Timestamp(f'{year}-12-31')
    dataframe_filtered = dataframe_copy[dataframe_copy[column_name] > limit_year].copy()
    dataframe_filtered[column_name] = dataframe_filtered[column_name].dt.strftime('%Y-%m-%d')
    dataframe_filtered[column_name] = pd.to_datetime(dataframe_filtered[column_name])

    return dataframe_filtered

def categorize_injury(injury_text):
    """
    Create a new column in the dataframe that allows splitting the 'Injury' values ​​between fatal and non-fatal
    """
    injury_text = str(injury_text).lower()

    fatal_keywords = ['fatal', 'death', 'died', 'deceased', 'dead']

    if any(keyword in injury_text for keyword in fatal_keywords):
        return 'Fatal'
    else:
        return 'No Fatal'
    
def filter_activity(activity_text):
    """
    Filters the activities that victims were doing by trying to clean common words
    """
    if pd.isna(activity_text):
        return "Unknown"
    
    activity_text = str(activity_text).lower()

    words = activity_text.split()

    common_words = ['a', 'an', 'the', 'in', 'of', 'on', 'for', 'with', 'and', 'while', 'from']

    for word in words:
        if word not in common_words:
            return word.capitalize()

def temp_date_df(data_frame, column_name):
    """
    Create a dataframe with the dates of the attacks divided into year, month and day to facilitate their management
    """
    data_frame[column_name] = pd.to_datetime(data_frame[column_name])

    data_frame_tmp = pd.DataFrame({
       'year' : data_frame[column_name].dt.year,
       'month' : data_frame[column_name].dt.month,
       'day' : data_frame[column_name].dt.day
    })

    return data_frame_tmp

def generate_case_numbers(data_frame, prefix = 'ND.', start_index = 1): 
    """
    Creates a column which generates a case number for each attack
    """
    data_frame_reversed = data_frame.iloc[::-1].reset_index(drop=True)
    
    data_frame_reversed['case_number'] = data_frame_reversed.index + start_index
    data_frame_reversed['case_number'] = prefix + data_frame_reversed['case_number'].apply(lambda x: f'{x:04d}')

    data_frame_final = data_frame_reversed.iloc[::-1].reset_index(drop=True)

    return data_frame_finalç

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