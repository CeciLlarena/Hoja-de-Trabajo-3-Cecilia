def bubble_sort(arr):
  for i in range(0, len(arr)):
    for j in range(0, len(arr)-2):
      if arr[j] > arr[j + 1]:
        #swap python : a,b =b,a
        arr[j], arr[j+1] = arr[j+1], + arr[j]
  return arr

unsorted_list = [8, 30, 1, 13, -88]
print ("La lista desordenada es: ", unsorted_list)

sorted_list = bubble_sort(unsorted_list)
print("La lista ordenada es: ", sorted_list)