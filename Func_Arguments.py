# a & b are Positional Arguments (values, /)
# c & d are Keyword Arguments (*, values)

def my_function(a, b, /, *, c, d):
  print(a)
  print(b)
  print(c)
  print(d)

my_function(1, 2, c = 3, d = 4)
