class Hero:
    def __init__(self, key, Name, Alignment, Gender, EyeColor, Race, HairColor, Publisher, SkinColor, Height, Weight, Intelligence, Strength, Speed, Durability, Power, Combat, Total):
        self.key = key
        self.Name = Name
        self.Alignment = Alignment
        self.Gender = Gender
        self.EyeColor = EyeColor
        self.Race = Race
        self.HairColor = HairColor
        self.Publisher = Publisher
        self.SkinColor = SkinColor
        self.Height = Height
        self.Weight = Weight
        self.Intelligence = Intelligence
        self.Strength = Strength
        self.Speed = Speed
        self.Durability = Durability
        self.Power = Power
        self.Combat = Combat
        self.Total = Total

    def __repr__(self):
        return f"Hero(key={self.key}, Name={self.Name})"

def quick_sort(heroes, order):
    def partition(arr, low, high):
        pivot = arr[high].key
        i = low - 1
        for j in range(low, high):
            if (order == 'C' and arr[j].key <= pivot) or (order == 'D' and arr[j].key >= pivot):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)

    quick_sort_recursive(heroes, 0, len(heroes) - 1)

def heap_sort(heroes, order):
    def heapify(arr, n, i):
        largest = smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if order == 'C':
            if left < n and arr[left].key > arr[largest].key:
                largest = left
            if right < n and arr[right].key > arr[largest].key:
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        elif order == 'D':
            if left < n and arr[left].key < arr[smallest].key:
                smallest = left
            if right < n and arr[right].key < arr[smallest].key:
                smallest = right
            if smallest != i:
                arr[i], arr[smallest] = arr[smallest], arr[i]
                heapify(arr, n, smallest)

    n = len(heroes)
    for i in range(n // 2 - 1, -1, -1):
        heapify(heroes, n, i)
    for i in range(n - 1, 0, -1):
        heroes[i], heroes[0] = heroes[0], heroes[i]
        heapify(heroes, i, 0)

def merge_sort(heroes, order):
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = arr[l:m + 1]
        R = arr[m + 1:r + 1]
        i = j = 0
        k = l
        while i < n1 and j < n2:
            if (order == 'C' and L[i].key <= R[j].key) or (order == 'D' and L[i].key >= R[j].key):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort_recursive(arr, l, r):
        if l < r:
            m = l + (r - l) // 2
            merge_sort_recursive(arr, l, m)
            merge_sort_recursive(arr, m + 1, r)
            merge(arr, l, m, r)

    merge_sort_recursive(heroes, 0, len(heroes) - 1)

def insertion_sort(heroes, order):
    for i in range(1, len(heroes)):
        key = heroes[i]
        j = i - 1
        while j >= 0 and ((order == 'C' and heroes[j].key > key.key) or (order == 'D' and heroes[j].key < key.key)):
            heroes[j + 1] = heroes[j]
            j -= 1
        heroes[j + 1] = key
