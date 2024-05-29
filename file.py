import os

def verify_file_structure(file_name):

    absolute_path = os.path.abspath(file_name)
    
    # Verificar se o arquivo existe
    if not os.path.exists(absolute_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {absolute_path}")
    

    with open(absolute_path, 'r', encoding='utf8') as file:
        lines = file.readlines()
        
        if lines[0].startswith("SORT=") == False:
            raise ValueError("1st line incorret format.")
        
        sort_param = lines[0].split("SORT=")[1].split(",")[0]
        order_param = lines[0].split("ORDER=")[1].strip()
        
        expected_header = "key,Name,Alignment,Gender,EyeColor,Race,HairColor,Publisher,SkinColor,Height,Weight,Intelligence,Strength,Speed,Durability,Power,Combat,Total"
        if lines[1].strip() != expected_header:
            raise ValueError("Formato incorreto na linha de cabeçalhos")
        
        data = lines[2:]
        
        return sort_param, order_param, data
