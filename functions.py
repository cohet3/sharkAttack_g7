# ARCHIVO PARA LAS FUNCIONES GLOBAL
# AVISAR ANTES DE PUSHEAR, SI SE MODIFICA SE PUEDE EXCLUIR DEL PUSH

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

def generate_case_numbers(data_frame, prefix = 'ND.', start_index = 1): # ESTA FUNCIÓN DEBE IR AL FINAL DEL TODO, PARA GENERAR LOS CÓDIGOS ÚNICOS PARA CADA CASO

    data_frame_reversed = data_frame.iloc[::-1].reset_index(drop=True)
    
    data_frame_reversed['case_number'] = data_frame_reversed.index + start_index
    data_frame_reversed['case_number'] = prefix + data_frame_reversed['case_number'].apply(lambda x: f'{x:04d}')

    data_frame_final = data_frame_reversed.iloc[::-1].reset_index(drop=True)

    return data_frame_final