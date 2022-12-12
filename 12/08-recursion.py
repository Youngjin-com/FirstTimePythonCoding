import sys
sys.setrecursionlimit(100)

def test(depth):
  depth += 1
  print(depth)
  test(depth)
test(0)
