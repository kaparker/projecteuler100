def largestPrimeFactor(n):
  prime = 2
  factor = 1
  
  while prime<=n:
    print(n, prime, factor)
    if n%prime==0:
      factor = prime
      n = n/prime
    else:
      prime += 1

  return factor
  
def testvalue(n, check):
  output = largestPrimeFactor(n)
  if output != check:
    print('largestPrimeFactor(',n,') should return', check, 'returns:', output)
  else:
    print('Test for', n, 'passed:', check)
 

testvalue(2,2)
testvalue(3,3)
testvalue(5,5)
testvalue(7,7)
testvalue(13195,29)
testvalue(600851475143,6857)