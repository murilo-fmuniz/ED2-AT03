from hero import Hero
from file import verify_file_structure
from sorts import quick_sort, heap_sort, merge_sort, insertion_sort



if __name__ == "__main__":

    data = verify_file_structure('input01.txt')
    sort_type = data[0]
    sort_order_type = data[1]
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
        print(f"{hero.Name}")
    with open('out1.txt', 'w', encoding='utf8') as file:
        print("Original list:")
        file.write(f'\told\n')
        for hero in heroes:
            file.write(f'{hero.key}|{hero.Name}\n')
        # Quick Sort
        quick_sort(heroes, 'C')
        print("\nQuick Sort (Ascending):")
        file.write(f'\tquick Ascending\n')
        for hero in heroes:
            file.write(f'{hero.key}|{hero.Name}\n')

        # Heap Sort
        heap_sort(heroes, 'D')
        print("\nHeap Sort (Descending):")
        file.write(f'\tHeap Descending\n')
        for hero in heroes:
            file.write(f'{hero.key}|{hero.Name}\n')

        # Merge Sort
        merge_sort(heroes, 'C')
        print("\nMerge Sort (Ascending):")
        file.write(f'\tMerge Ascending\n')
        for hero in heroes:
            file.write(f'{hero.key}|{hero.Name}\n')

        # Insertion Sort
        insertion_sort(heroes, 'D')
        print("\nInsertion Sort (Descending):")
        file.write(f'\tInsertion Descending\n')
        for hero in heroes:
            file.write(f'{hero.key}|{hero.Name}\n')