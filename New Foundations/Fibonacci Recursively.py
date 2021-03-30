#runtime is O(2^N)

def fibonacci(n):
  if n == 1 or n == 0:
    return n
  else:
    return fibonacci(n - 2) + fibonacci(n - 1)
    
fibonacci(5)
