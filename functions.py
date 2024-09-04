# ARCHIVO PARA LAS FUNCIONES GLOBAL
# AVISAR ANTES DE PUSHEAR, SI SE MODIFICA SE PUEDE EXCLUIR DEL PUSH
import numpy as np
import warnings as wrn
import panda as pd


def clean_columns_names(data_frame, columns_to_drop=None): #Opción buena
    
    data_frame.columns = data_frame.columns.str.replace(' ', '_').str.lower()

    return data_frame

def columns_drops(data_frame, columns_to_drop=None): #Opción buena
    
    if columns_to_drop is not None:
        data_frame = data_frame.drop(columns=columns_to_drop, errors='ignore')

    return data_frame

def drop_rows_nulls(data_frame, thresh=2): #Opción buena

    if thresh > 1:
        raiserror('Threshold must be 1 or less.')

    data_frame_clean = data_frame.dropna(thresh=thresh)

    return data_frame_clean

def clean_and_filter_dates(dataframe, column_name, year): # Limpia la fecha y filtra por año
    
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

    return dataframe_filtered

def generate_case_numbers(data_frame, prefix = 'ND.', start_index = 1): # ESTA FUNCIÓN DEBE IR AL FINAL DEL TODO, PARA GENERAR LOS CÓDIGOS ÚNICOS PARA CADA CASO

    data_frame_reversed = data_frame.iloc[::-1].reset_index(drop=True)
    
    data_frame_reversed['case_number'] = data_frame_reversed.index + start_index
    data_frame_reversed['case_number'] = prefix + data_frame_reversed['case_number'].apply(lambda x: f'{x:04d}')

    data_frame_final = data_frame_reversed.iloc[::-1].reset_index(drop=True)

    return data_frame_final