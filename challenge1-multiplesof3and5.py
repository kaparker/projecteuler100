def multiplesOf3and5(number):
    value = 0
    for num in range(3, number):
        if num % 3 == 0 or num % 5 ==0:
            value += num
    return value

def testvalue(number, check):
    output = multiplesOf3and5(number)
    if output != check:
        print('multiplesOf3and5(',number,') should return', check, 'returns:', output)
    else:
        print('Test for', number, 'passed')

testvalue(1000,233168)
testvalue(49,543)
testvalue(19564,89301183)
testvalue(8456,16687353)