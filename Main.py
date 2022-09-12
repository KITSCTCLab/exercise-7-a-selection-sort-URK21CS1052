from typing import List
def selectionSort(array, size) -> List[int]:
  for step in range(size):
          min_idx = step
          for i in range(step + 1, size):
              # to sort in descending order, change > to < in this line
              # select the minimum element in each loop
              if array[i] < array[min_idx]:
                  min_idx = i
          # put min at the correct position
          (array[step], array[min_idx]) = (array[min_idx], array[step])

input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
