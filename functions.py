# Global functions file. 
# Warn before push (if there's a problem, the push can be rejected) 

import numpy as np
import warnings as wrn
import pandas as pd
import re
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


def clean_columns_names(data_frame): #Opción buena
    
    data_frame.columns = data_frame.columns.str.strip().str.replace(' ', '_').str.lower()

    return data_frame

def columns_drops(data_frame, columns_to_drop=None): #Opción buena
    
    if columns_to_drop is not None:
        data_frame = data_frame.drop(columns=columns_to_drop, errors='ignore')

    return data_frame

def drop_rows_nulls(data_frame, thresh=2): #Opción buena

    if thresh < 1:
        raise ValueError('Threshold must be 1 or less.') 
        

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
    dataframe_filtered[column_name] = pd.to_datetime(dataframe_filtered[column_name])

    return dataframe_filtered

def categorize_injury(injury_text):
    injury_text = str(injury_text).lower()

    fatal_keywords = ['fatal', 'death', 'died', 'deceased', 'dead']

    if any(keyword in injury_text for keyword in fatal_keywords):
        return 'Fatal'
    else:
        return 'No Fatal'

def temp_date_df(data_frame, column_name):

    data_frame[column_name] = pd.to_datetime(data_frame[column_name])

    data_frame_tmp = pd.DataFrame({
       'year' : data_frame[column_name].dt.year,
       'month' : data_frame[column_name].dt.month,
       'day' : data_frame[column_name].dt.day
    })

    return data_frame_tmp

def generate_case_numbers(data_frame, prefix = 'ND.', start_index = 1): # ESTA FUNCIÓN DEBE IR AL FINAL DEL TODO, PARA GENERAR LOS CÓDIGOS ÚNICOS PARA CADA CASO

    data_frame_reversed = data_frame.iloc[::-1].reset_index(drop=True)
    
    data_frame_reversed['case_number'] = data_frame_reversed.index + start_index
    data_frame_reversed['case_number'] = prefix + data_frame_reversed['case_number'].apply(lambda x: f'{x:04d}')

    data_frame_final = data_frame_reversed.iloc[::-1].reset_index(drop=True)

    return data_frame_final

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
        new_str = re.sub(r'[@!#$%^*?()"]', '', new_str)
        new_str = new_str.replace("-", " ")
        new_str = re.sub(r"\s+", " ", new_str)
        new_str = new_str.strip()
    return new_str



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






# Función para obtener las coordenadas a partir de un DataFrame con columnas genéricas
def get_coordinates(csv_path, file_name, column_name_1='location', column_name_2='state', column_name_3='country'):

    df= pd.read_csv('shark_attack_clean.csv')

    # Configure the geolocator
    geolocator = Nominatim(user_agent="mi_geocodificador")

    # Use RateLimiter to limit the queries
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.001)

    # Función interna para geocodificar en orden: column_name_1, column_name_2, luego column_name_3
    def obtener_coordenadas(fila):
        gps_location = None
        if pd.notna(fila[column_name_1]):
            gps_location = geocode(fila[column_name_1])
        if gps_location is None and pd.notna(fila[column_name_2]):
            gps_location = geocode(fila[column_name_2])
        if gps_location is None and pd.notna(fila[column_name_3]):
            gps_location = geocode(fila[column_name_3])
        return gps_location

    # Crear columnas de latitud y longitud en el DataFrame
    df['coordenadas'] = df.apply(obtener_coordenadas, axis=1)
    df['latitude'] = df['coordenadas'].apply(lambda loc: loc.latitude if loc else None)
    df['longitude'] = df['coordenadas'].apply(lambda loc: loc.longitude if loc else None)

    # Elimina la columna temporal 'coordenadas'
    df = df.drop(columns=['coordenadas'])

    return df.to_csv(file_name)