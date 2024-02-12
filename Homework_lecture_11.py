
arr = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]

def buble_sort(arr):
  n = len(arr)

  for i in range(n - 1, 0, -1):
    for j in range(i):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  print(arr)
    

buble_sort(arr)

def merge_sort(arr):
  n = len(arr)
  
  if n == 1:
    return arr
  
  middle = n // 2
  left = merge_sort(arr[:middle])
  right = merge_sort(arr[middle:])
  
  return merge_two_list(left, right)


def merge_two_list(a, b):
  c = []
  i = j = 0
  
  while i < len(a) and j < len(b):
    if a[i] < b[j]:
      c.append(a[i])
      i += 1
    else:
      c.append(b[j])
      j += 1
  
    
  c += a[i:] + b[j:]
  
  return c


merge_sort(arr)
print(arr)


def insertion_sort(arr):
  n = len(arr)

  for i in range(1, n):
    j = i

    while j > 0 and arr[j-1] > arr[j]:
      arr[j - 1], arr[j] = arr[j], arr[j - 1]

      j -= 1
  print(arr)

insertion_sort(arr)