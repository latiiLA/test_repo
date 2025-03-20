def fizzbuzz(n):
    '''
    Fizz buzz function to generate the fizzbuzz for numbers from 0 to n
    '''
    result = []

    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            result.append("Fizz Buzz")
        if i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)


if __name__ == '__main__':
    n = 100
    output = fizzbuzz(n)
    print(output)