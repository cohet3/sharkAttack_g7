# ARCHIVO PARA LAS FUNCIONES GLOBAL
# AVISAR ANTES DE PUSHEAR, SI SE MODIFICA SE PUEDE EXCLUIR DEL PUSH
import re
import numpy as np
import warnings as wrn
import pandas as pd


def clean_columns_names(data_frame, columns_to_drop=None): #
    
    data_frame.columns = data_frame.columns.str.replace(' ', '_').str.lower()

    return data_frame

def columns_drops(data_frame, columns_to_drop=None): #
    
    if columns_to_drop is not None:
        data_frame = data_frame.drop(columns=columns_to_drop, errors='ignore')

    return data_frame

def drop_rows_nulls(data_frame, thresh=2): #

    if thresh < 1:
        raise ValueError('Threshold must be 1 or less.') 
        

    data_frame_clean = data_frame.dropna(thresh=thresh)

    return data_frame_clean

def clean_and_filter_dates(dataframe, column_name, year): # 

    def clean_datetimes(df_general):

        for fmt in ('%d %b %Y', '%d-%b-%Y', '%d %b-%Y', '%d-%b-%Y', '%d %b %y'):
            try:
                return pd.to_datetime(df_general, format=fmt)
            except ValueError:
                continue
            
        return pd.NaT
    
    with wrn.catch_warnings():
        wrn.simplefilter(action='ignore', category=pd.errors.SettingWithCopyWarning)
    
    dataframe_copy = dataframe.copy()
    
    dataframe_copy[column_name] = dataframe_copy[column_name].apply(clean_datetimes)

    limit_year = pd.Timestamp(f'{year}-12-31')
    dataframe_filtered = dataframe_copy[dataframe_copy[column_name] > limit_year].copy()
    dataframe_filtered[column_name] = dataframe_filtered[column_name].dt.strftime('%Y-%m-%d')
    dataframe_filtered[column_name] = pd.to_datetime(dataframe_filtered[column_name])

    return dataframe_filtered

def categorize_injury(injury_text):
    injury_text = str(injury_text).lower()

    fatal_keywords = ['fatal', 'death', 'died', 'deceased', 'dead']

    if any(keyword in injury_text for keyword in fatal_keywords):
        return 'Fatal'
    else:
        return 'No Fatal'
    
def filter_activity(activity_text):

    if pd.isna(activity_text):
        return "Unknown"
    
    activity_text = str(activity_text).lower()

    words = activity_text.split()

    common_words = ['a', 'an', 'the', 'in', 'of', 'on', 'for', 'with', 'and', 'while', 'from']

    for word in words:
        if word not in common_words:
            return word.capitalize()

def temp_date_df(data_frame, column_name):

    data_frame[column_name] = pd.to_datetime(data_frame[column_name])

    data_frame_tmp = pd.DataFrame({
       'year' : data_frame[column_name].dt.year,
       'month' : data_frame[column_name].dt.month,
       'day' : data_frame[column_name].dt.day
    })

    return data_frame_tmp

def generate_case_numbers(data_frame, prefix = 'ND.', start_index = 1): # 

    data_frame_reversed = data_frame.iloc[::-1].reset_index(drop=True)
    
    data_frame_reversed['case_number'] = data_frame_reversed.index + start_index
    data_frame_reversed['case_number'] = prefix + data_frame_reversed['case_number'].apply(lambda x: f'{x:04d}')

    data_frame_final = data_frame_reversed.iloc[::-1].reset_index(drop=True)

    return data_frame_final