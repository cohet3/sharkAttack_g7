# ARCHIVO PARA LAS FUNCIONES GLOBAL
# AVISAR ANTES DE PUSHEAR, SI SE MODIFICA SE PUEDE EXCLUIR DEL PUSH

def clean_columns_names(shark_attack_raw):
    shark_attack_raw_1 = shark_attack_raw.columns.map(lambda col: col.replace(' ', '_'))
    shark_attack_raw_2 = shark_attack_raw_1.rename(columns=lambda x: x.lower())
    shark_attack_raw_3 = shark_attack_raw_2.drop(columns=['unnamed:_11', 'unnamed:_21', 'unnamed:_22', 'case_number.1'])

    shark_attack_clean = shark_attack_raw_3

    return shark_attack_clean


def clean_columns_rows(shark_attack_raw):

    shark_attack_clean = shark_attack_raw.dropna(thresh = 2)

    return shark_attack_clean

def generate_case_numbers(shark_attack_clean): # ESTA FUNCIÓN DEBE IR AL FINAL DEL TODO, PARA GENERAR LOS CÓDIGOS ÚNICOS PARA CADA CASO

    shark_attack_clean = shark_attack_clean.iloc[::-1]
    shark_attack_clean['case_number'] = shark_attack_clean.reset_index(drop=True).index + 1
    shark_attack_clean['case_number'] = 'ND.' + shark_attack_clean['case_number'].apply(lambda x: f'{x:04d}')
    shark_attack_clean = shark_attack_clean.iloc[::-1]

    return shark_attack_clean