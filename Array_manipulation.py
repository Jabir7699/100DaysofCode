from collections import Counter
def arraymanipulation(n,queries):
  c=Counter
  for a,b,k in queries :
    c[a] += k
    c[b+1] -= k
  arrsum = 0
  maxsum = 0
  for i in sorted(c)[:-1]:
    arrsum += c[i]
    maxsum = max(maxsum,arrsum)
  return maxsum
n,m = map(int,input().split())
queries = [list(map(int,input().split()) for _ in range(m)]
print(arraymanipulation(n,queries))
