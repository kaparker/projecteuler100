def fiboEvenSum(n):
  i = 0
  j = 1
  count = 1
  sum = 0
  while count <= n:
    output = i+j
    i = j
    j = output
    if output %2==0:
      sum+=output
    count += 1
  return sum
  
def testvalue(n, check):
  output = fiboEvenSum(n)
  if output != check:
    print('fiboEventSum(',n,') should return', check, 'returns:', output)
  else:
    print('Test for', n, 'passed')
 
testvalue(10,44)
testvalue(18,3382)
testvalue(23,60696)
testvalue(43,350704366)