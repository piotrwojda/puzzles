

def move_zeros_to_left(A):
  read_index = len(A) - 1
  write_index = read_index

  while(read_index >= 0):
    print(read_index)
    if A[read_index] != 0:
      A[write_index] = A[read_index]
      write_index -= 1
    read_index -= 1

  while(write_index >= 0):
    A[write_index] = 0
    write_index -= 1

  return A

