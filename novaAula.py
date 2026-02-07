print('Olá')
valore = [12, 5, 8, 3, 1, 9, 4, 6, 7, 2, 54, 23, 45, 67, 89, 34, 56, 78, 90]
print(valore)
valore.sort()
print(valore)
valore.sort(reverse=True)
print(valore)
def maximo(lista):
    max = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max
print(' 0 valor máximo da lista é' , maximo(valore))
import time
t1 = time.process_time()
maximo(valore)
t2 = time.process_time()
print('Tempo de execução:', t2 - t1, 'segundos')

l1 = list(range(1000))
l2 = list(range(2000))

t1 = time.process_time()
maximo(l1)
t2 = time.process_time()
print('Tempo de execução foi:', t2 - t1, 'segundos') 

t1 = time.process_time()
maximo(l2)
t2 = time.process_time()
print('Tempo de execução foi:', t2 - t1, 'segundos')
time.sleep(5)
print('Fim do programa')


