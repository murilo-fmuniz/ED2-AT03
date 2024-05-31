import random
import time

def gerar_vetor(tamanho, metodo):
    if tamanho <= 0:
        print("O tamanho do vetor deve ser um numero positivo maior que zero.")
        return None
    if metodo == 'c':
        return list(range(1, tamanho + 1))
    elif metodo == 'd':
        return list(range(tamanho, 0, -1))
    elif metodo == 'r':
        vetor = list(range(1, tamanho + 1))
        random.shuffle(vetor)  # Embaralhar o vetor aleatoriamente
        return vetor
    else:
        print("Método de geração inválido.")
        return None


def insertion_sort(vetor):
    n = len(vetor)
    comparacoes = 0

    tempo_inicial = time.time()  # Inicia a contagem de tempo

    for i in range(1, n):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and chave < vetor[j]:
            comparacoes += 1
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave

    tempo_final = time.time()  # Finaliza a contagem de tempo
    tempo_gasto = (tempo_final - tempo_inicial) * 100000  # Tempo em milissegundos

    return comparacoes, tempo_gasto


def selection_sort(vetor):
    n = len(vetor)
    comparacoes = 0

    tempo_inicial = time.time()  # Inicia a contagem de tempo

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            comparacoes += 1
            if vetor[j] < vetor[min_index]:
                min_index = j
        
        if min_index != i:
            vetor[i], vetor[min_index] = vetor[min_index], vetor[i]

    tempo_final = time.time()  # Finaliza a contagem de tempo
    tempo_gasto = (tempo_final - tempo_inicial) * 100000  # Tempo em milissegundos

    return comparacoes, tempo_gasto


def bubble_sort(vetor):
    n = len(vetor)
    comparacoes = 0

    tempo_inicial = time.time()  # Inicia a contagem de tempo

    for i in range(n):
        trocou = False
        for j in range(0, n-i-1):
            comparacoes += 1
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
                trocou = True
        # Se nenhum elemento foi trocado nesta iteração, o vetor está ordenado
        if not trocou:
            break

    tempo_final = time.time()  # Finaliza a contagem de tempo
    tempo_gasto = (tempo_final - tempo_inicial) * 100000  # Tempo em milissegundos

    return comparacoes, tempo_gasto


def merge_sort(vetor):
    comparacoes = [0]  # Lista para armazenar o numero de comparacoes

    tempo_inicial = time.time()  # Inicia a contagem de tempo

    def merge(vetor, esquerda, meio, direita):
        n1 = meio - esquerda + 1
        n2 = direita - meio

        # Criar arrays temporários
        L = [0] * n1
        R = [0] * n2

        # Copiar dados para os arrays temporários L[] e R[]
        for i in range(n1):
            L[i] = vetor[esquerda + i]
        for j in range(n2):
            R[j] = vetor[meio + 1 + j]

        # Mesclar os arrays temporários de volta em vetor[]
        i = j = 0
        k = esquerda
        while i < n1 and j < n2:
            comparacoes[0] += 1
            if L[i] <= R[j]:
                vetor[k] = L[i]
                i += 1
            else:
                vetor[k] = R[j]
                j += 1
            k += 1

        # Copiar os elementos restantes de L[], se houver algum
        while i < n1:
            vetor[k] = L[i]
            i += 1
            k += 1

        # Copiar os elementos restantes de R[], se houver algum
        while j < n2:
            vetor[k] = R[j]
            j += 1
            k += 1

    def merge_sort_recursivo(vetor, esquerda, direita):
        if esquerda < direita:
            meio = (esquerda + direita) // 2

            merge_sort_recursivo(vetor, esquerda, meio)
            merge_sort_recursivo(vetor, meio + 1, direita)

            merge(vetor, esquerda, meio, direita)

    merge_sort_recursivo(vetor, 0, len(vetor) - 1)

    tempo_final = time.time()  # Finaliza a contagem de tempo
    tempo_gasto = (tempo_final - tempo_inicial) * 100000  # Tempo em milissegundos

    return comparacoes[0], tempo_gasto


def quick_sort(vetor):
    comparacoes = [0]  # Lista para armazenar o numero de comparacoes

    # Contador de tempo
    tempo_inicial = time.time()

    def particionar(vetor, baixo, alto):
        pivo = vetor[alto]
        i = baixo - 1

        for j in range(baixo, alto):
            comparacoes[0] += 1
            if vetor[j] <= pivo:  # Corrigido para ordenação crescente
                i += 1
                vetor[i], vetor[j] = vetor[j], vetor[i]

        vetor[i + 1], vetor[alto] = vetor[alto], vetor[i + 1]
        return i + 1

    def quick_sort_recursivo(vetor, baixo, alto):
        if baixo < alto:
            pi = particionar(vetor, baixo, alto)
            quick_sort_recursivo(vetor, baixo, pi - 1)
            quick_sort_recursivo(vetor, pi + 1, alto)

    quick_sort_recursivo(vetor, 0, len(vetor) - 1)

    # Contador de tempo
    tempo_final = time.time()

    # Calcular o tempo gasto (em milissegundos)
    tempo_gasto = (tempo_final - tempo_inicial) * 100000

    return comparacoes[0], tempo_gasto


def heap_sort(vetor):
    comparacoes = [0]  # Lista para armazenar o numero de comparacoes

    # Contador de tempo
    tempo_inicial = time.time()

    def max_heapify(vetor, n, i):
        maior = i
        esquerda = 2 * i + 1  # Corrigindo o cálculo do índice da esquerda
        direita = 2 * i + 2   # Corrigindo o cálculo do índice da direita

        if esquerda < n and vetor[esquerda] > vetor[maior]:
            maior = esquerda
        comparacoes[0] += 1

        if direita < n and vetor[direita] > vetor[maior]:
            maior = direita
        comparacoes[0] += 1

        if maior != i:
            vetor[i], vetor[maior] = vetor[maior], vetor[i]
            max_heapify(vetor, n, maior)

    def construir_max_heap(vetor, n):
        for i in range(n // 2 - 1, -1, -1):  # Corrigindo o intervalo e o passo
            max_heapify(vetor, n, i)

    def heap_sort_recursivo(vetor, n):
        construir_max_heap(vetor, n)
        for i in range(n - 1, 0, -1):  # Corrigindo o intervalo e o passo
            vetor[0], vetor[i] = vetor[i], vetor[0]
            max_heapify(vetor, i, 0)

    heap_sort_recursivo(vetor, len(vetor))

    # Contador de tempo
    tempo_final = time.time()

    # Calcular o tempo gasto (em milissegundos)
    tempo_gasto = (tempo_final - tempo_inicial) * 100000

    return comparacoes[0], tempo_gasto


def counting_sort(vetor):
    # Inicializar o contador de tempo
    tempo_inicial = time.time()

    # Encontre o valor máximo no vetor
    max_valor = max(vetor)
    # Encontre o valor mínimo no vetor
    min_valor = min(vetor)
    # Inicialize um array para contar as ocorrências de cada valor
    count = [0] * (max_valor - min_valor + 1)
    # Inicialize um array para armazenar o vetor ordenado
    ordenado = [0] * len(vetor)
    comparacoes = 0  # Inicializando o contador de comparações

    # Contar as ocorrências de cada valor no vetor
    for num in vetor:
        count[num - min_valor] += 1

    # Atualize o array de contagem para armazenar as posições reais no array ordenado
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Construa o array ordenado
    for num in reversed(vetor):
        ordenado[count[num - min_valor] - 1] = num
        for i in range(1, len(count)):
            if count[i] == num - min_valor:
                comparacoes += 1  # Incrementando o contador de comparações
        count[num - min_valor] -= 1

    # Finalizar o contador de tempo
    tempo_final = time.time()

    # Calcular o tempo gasto (em milissegundos)
    tempo_gasto = (tempo_final - tempo_inicial) * 1000

    return ordenado, comparacoes, tempo_gasto


# Função para ler o arquivo de entrada e obter o tamanho do vetor e o modo de geração
def ler_arquivo_entrada(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            tamanho = int(linhas[0].strip())
            metodo = linhas[1].strip()
            return tamanho, metodo
    except FileNotFoundError:
        print("Arquivo de entrada nao encontrado.")
    except IndexError:
        print("Arquivo de entrada mal formatado.")
    except ValueError:
        print("Tamanho do vetor deve ser um numero inteiro.")
    return None, None

# Teste da função de leitura do arquivo de entrada
tamanho, metodo = ler_arquivo_entrada("entrada.txt")
if tamanho is not None and metodo is not None:
    print("Tamanho do vetor:", tamanho)
    print("Modo de geração do vetor:", metodo)

# Teste do programa
def main(): 
    try:
        # Leitura do arquivo de entrada
        tamanho, metodo = ler_arquivo_entrada("entrada.txt")

        # Verificar se o arquivo de entrada está vazio
        if not tamanho or not metodo:
            print("Arquivo de entrada vazio.")
            return

        # Gerar o vetor
        vetor = gerar_vetor(tamanho, metodo)
        if vetor is None:
            return

        # Lista de métodos de ordenação
        metodos = [
            ("Insertion Sort", insertion_sort),
            ("Selection Sort", selection_sort),
            ("Bubble Sort", bubble_sort),
            ("Merge Sort", merge_sort),
            ("Quick Sort", quick_sort),
            ("Heap Sort", heap_sort),
            ("Counting Sort", counting_sort)
        ]

        # Execução dos métodos de ordenação e escrita no arquivo de saída
        with open("saida.txt", "w") as f:
            for nome_metodo, metodo_ordenacao in metodos:
                if nome_metodo == "Counting Sort":
                    vetor_copy, comparacoes, tempo_gasto = metodo_ordenacao(vetor.copy())
                    f.write(f"{nome_metodo}: {' '.join(map(str, vetor_copy))}, {comparacoes} comparacoes, {tempo_gasto:.0f} ms\n")
                else:
                    vetor_copy = vetor.copy()
                    tempo_inicial = time.time()
                    comparacoes = metodo_ordenacao(vetor_copy)
                    tempo_final = time.time()
                    tempo_gasto = (tempo_final - tempo_inicial) * 100000  # Tempo em milissegundos
                    f.write(f"{nome_metodo}: {' '.join(map(str, vetor_copy))}, {comparacoes} comparacoes, {tempo_gasto:.0f} ms\n")


    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()