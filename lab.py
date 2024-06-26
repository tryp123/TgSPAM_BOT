import math
def f(a, b, x):
  if b * x == 0:
    return None
  else:
    return (math.sin(b * x - a) / math.cos(b * x)) - math.sin(b * x) - math.log(b * x)
a = 0.5
b = 2.0
x = 1.5

y = f(a, b, x)

print(f"Y = {y}")
