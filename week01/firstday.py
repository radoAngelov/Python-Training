def sum_of_digits(n):
    result = 0
    for i in str(n):
        if i == '-':
            pass
        else:
            result += int(i)
    return result


def sum_of_digits_better(n):
    digits = [int(i) for i in str(n) if not i == '-']
    return sum(digits)


def to_digits(n):
    a = []

    for x in str(n):
        a.append(int(x))

    return a


def to_digits_better(n):
    array = [int(x) for x in str(n)]
    return array


def to_number(digits):
    string = ""

    for x in digits:
        string += str(x)

    number = int(string)
    return number


def to_number_better(digits):
    numbers = [str(x) for x in digits]
    return "".join(numbers)


def fact_digit(n):
    result = 0
    for x in str(n):
        fact = 1
        for i in range(1, int(x) + 1):
            fact *= i
        result += fact
    return result


def fibonacci(n):
    result = []
    temp = 0

    if n > 0:
        if n == 1:
            result.append(1)
        else:
            result.append(1)
            result.append(1)
            for _ in range(n-2):
                temp = result[-2] + result[-1]
                result.append(temp)
        return result
    else:
        print("Enter positive number.")


def fib_number(n):
    result = ""
    first, second, temp = 1, 1, 0

    if n > 0:
        if n == 1:
            result = result + "1"
        else:
            result = result + "11"
            for _ in range(n - 2):
                temp = first + second
                first = second
                second = temp
                result = result + str(temp)
        return result
    else:
        print("Enter positive number.")


def palindrome(obj):
    array_of_digits = [x for x in str(obj)]
    for _ in range(int(len(str(obj)) / 2)):
        if array_of_digits[0] != array_of_digits[-1]:
            return False
        else:
            array_of_digits.remove(array_of_digits[0])
            array_of_digits.pop()
    return True


def count_vowels(str):
    counter = 0
    for i in str:
        if i in 'aeiouy':
            counter += 1
    return counter


def count_vowels_better(str):
    matches = ['match' for x in str if x in 'aeiouy']
    return matches.count('match')


def count_consonants(str):
    counter = 0

    for i in str:
        if i not in ' aeiouy1234567890!@#$%^&*().,:"'';|\/?':
            counter += 1

    return counter


def count_consonants_better(str):
    matches = ['match' for x in str if x not in ' aeiouy1234567890!@#$%^&*().,:;|?\/']
    return matches.count('match')


def char_histogram(string):
    dictionary = {}

    for i in string:
        dictionary[i] = string.count(i)
        for _ in range(string.count(i)):
            string.replace(i, "")

    return dictionary