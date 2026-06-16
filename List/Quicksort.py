"""
Scegli un valore nell'array che fungerà da elemento pivot. 
Ordina il resto dell'array in modo che i valori inferiori 
all'elemento pivot siano a sinistra e i valori superiori a destra. 
Scambia l'elemento pivot con il primo elemento dei valori superiori 
in modo che l'elemento pivot si trovi tra i valori inferiori e superiori. 
Esegui le stesse operazioni (ricorsivamente) per i sotto-array a sinistra 
e a destra dell'elemento pivot.
"""


lista = [ 11, 9, 12, 7, 3]


def partition(array, low, high):
  pivot = array[high]
  print("3 debug pivot",pivot)
  i = low - 1
  print("4 debug i",i)
  print("5 debug",low, high)
  for j in range(low, high):
     print("6 debug",j) 
     if array[j] <= pivot:
       print("7 debug >>>>" ,array[j] )  
       i += 1
       print("8 debug i ",i)
       array[i], array[j] = array[j], array[i]

  array[i+1], array[high] = array[high], array[i+1]
  return i+1



def quicksort(array, low=0, high=None):
  if high is None:
    high = len(array) - 1
    print(high)
  if low < high:
    print("1 debug : ",array, low, high)
    pivot_index = partition(array, low, high)
    print("2 debug >>> ",pivot_index)
    quicksort(array, low, pivot_index-1)
    quicksort(array, pivot_index+1, high)

mylist = [64, 34, 25, 5, 22, 11, 90, 12]
quicksort(mylist)
print(mylist)














