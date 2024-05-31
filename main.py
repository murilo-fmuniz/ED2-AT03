import os, sys
from hero import Hero
from file import verify_file_structure
from sorts import quick_sort, heap_sort, merge_sort, insertion_sort



if __name__ == "__main__":

    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]

    

    #verificando condições do arquivo de entrada
    if os.path.getsize(inputFileName) == 0:
        print('\t\tarquivo inválido: o arquivo de entrada está vazio!!\n')
        sys.exit(1)

    data = verify_file_structure(inputFileName)
    sort_type = data[0]
    sort_ordering_param = data[1]
    heroes_brute = data[2]
    header = data[3]

    heroes = []

    for linha in heroes_brute:
        dados = linha.strip().split('|')
        hero = Hero(
            key=int(dados[0]),
            Name=dados[1],
            Alignment=dados[2],
            Gender=dados[3],
            EyeColor=dados[4],
            Race=dados[5],
            HairColor=dados[6],
            Publisher=dados[7],
            SkinColor=dados[8],
            Height=dados[9],
            Weight=dados[10],
            Intelligence=dados[11],
            Strength=dados[12],
            Speed=dados[13],
            Durability=dados[14],
            Power=dados[15],
            Combat=dados[16],
            Total=dados[17]
        )
        heroes.append(hero)

#key, Name, Alignment, Gender, EyeColor, Race, HairColor, Publisher, SkinColor, Height, Weight, Intelligence, Strength, Speed, Durability, Power, Combat, Total

    with open(outputFileName, 'w', encoding='utf8') as file:
        file.write(f"{header}\n")
        if sort_type == "Q": #QuickSort
            quick_sort(heroes, sort_ordering_param)
            for hero in heroes:
                file.write(f"{hero.key}|{hero.Name}|{hero.Alignment}|{hero.Gender}|{hero.EyeColor}|{hero.Race}|{hero.HairColor}|{hero.Publisher}|{hero.SkinColor}|{hero.Height}|{hero.Weight}|{hero.Intelligence}|{hero.Strength}|{hero.Speed}|{hero.Durability}|{hero.Power}|{hero.Combat}|{hero.Total}\n")
            
        elif sort_type == "M": #MergeSort
            merge_sort(heroes, sort_ordering_param)
            for hero in heroes:
                file.write(f"{hero.key}|{hero.Name}|{hero.Alignment}|{hero.Gender}|{hero.EyeColor}|{hero.Race}|{hero.HairColor}|{hero.Publisher}|{hero.SkinColor}|{hero.Height}|{hero.Weight}|{hero.Intelligence}|{hero.Strength}|{hero.Speed}|{hero.Durability}|{hero.Power}|{hero.Combat}|{hero.Total}\n")
            
        elif sort_type == "H": #HeapSort
            heap_sort(heroes, sort_ordering_param)
            for hero in heroes:
                file.write(f"{hero.key}|{hero.Name}|{hero.Alignment}|{hero.Gender}|{hero.EyeColor}|{hero.Race}|{hero.HairColor}|{hero.Publisher}|{hero.SkinColor}|{hero.Height}|{hero.Weight}|{hero.Intelligence}|{hero.Strength}|{hero.Speed}|{hero.Durability}|{hero.Power}|{hero.Combat}|{hero.Total}\n")

        elif sort_type == "I": #InsertionSort
            insertion_sort(heroes, sort_ordering_param)
            for hero in heroes:
                file.write(f"{hero.key}|{hero.Name}|{hero.Alignment}|{hero.Gender}|{hero.EyeColor}|{hero.Race}|{hero.HairColor}|{hero.Publisher}|{hero.SkinColor}|{hero.Height}|{hero.Weight}|{hero.Intelligence}|{hero.Strength}|{hero.Speed}|{hero.Durability}|{hero.Power}|{hero.Combat}|{hero.Total}\n")
            
        else:
            print("Sort parameter not accepted!")