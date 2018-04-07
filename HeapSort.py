import random
import time
import matplotlib.pyplot as plt

vetorHeapSort = []
vetorTempo = []

###################################################################

#Funcao responsavel pela ordenacao dos vetores
def heapSort(arr, n):
	i = (n / 2)-1
	while i >= 0:
		siftDown(arr, i, n)
		i = i - 1

	i = n
	while i >= 1:
		temp = arr[0]
		arr[0] = arr[i]
		arr[i] = temp
		siftDown(arr, 0, i-1)
		i = i - 1


def siftDown(arr, root, bottom):
	raiz = int(root)
	done = False
	while ((raiz*2 <= bottom) and (not(done))):
		if (raiz*2 == bottom):
			maxChild = raiz * 2
		elif ((arr[raiz * 2]) > (arr[raiz * 2 + 1])):
			maxChild = raiz * 2
		else:
			maxChild = raiz * 2 + 1

		if (arr[raiz] < arr[maxChild]):
			temp = arr[raiz]
			arr[raiz] = arr[maxChild]
			arr[maxChild] = temp
			raiz = maxChild
		
		else:
			done = True

###################################################################

#Funcao responsavel pela geracao dos vetores

def geraVetor(qtdElementosVetor):
	arr = []
	for x in range(qtdElementosVetor):	# --> Gera os numeros aleatorios para o vetor
		n = random.randint(1,1000)
		arr.append(n)

	return arr

###################################################################

#Funcao responsavel por plotar o grafico
def plotarGrafico(vetorQuickSort, vetorTempo):
	plt.xlabel('Tamanho vetor')
	plt.ylabel('Tempo')
	plt.title('HEAPSORT')
	plt.grid(True)
	plt.plot(vetorQuickSort, vetorTempo)
	plt.show()

###################################################################

for x in range(5):
	n = x*10000			#tamanho do vetor
	arr = geraVetor(n)		#Gera vetor para ordenacao

	inicio = time.time()		#Inicia a contagem de tempo
	arr = heapSort(arr, n-1)	#Executa a o algoritmo de ordenacao
	fim = time.time()		#Finaliza a contagem
	duracao = fim - inicio		#Calcula a duracao

	vetorHeapSort.append(n)
	vetorTempo.append(duracao)

plotarGrafico(vetorHeapSort, vetorTempo)
