def largestPalindromeProduct(n):
  
  maxPalindrome = 0
  for i in range(10**n-1, 10**(n-1), -1):
    for j in range(10**n-1, 10**(n-1), -1):
      if checkPalindrome(i*j) and i*j > maxPalindrome:
        maxPalindrome = i*j
  return maxPalindrome

def checkPalindrome(prod):
    number = prod
    reverse = str(prod)
    rev = int(reverse[::-1])

    if rev == prod:
      return True
    return False
    
def testvalue(number, check):
    output = largestPalindromeProduct(number)
    if output != check:
        print('largestPalindromeProduct(',number,') should return', check, 'returns:', output)
    else:
        print('Test for', number, 'passed')

testvalue(2,9009)
testvalue(3,906609)
