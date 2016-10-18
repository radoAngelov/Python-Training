from firstday import palindrome


def is_number_balanced(n):
    array_numbers = [int(x) for x in str(n)]
    if len(str(n)) == 1:
        return True
    else:
        if len(str(n)) % 2 == 1:
            if sum(array_numbers[0:int(len(array_numbers) / 2)]) == sum(array_numbers[int(len(array_numbers) / 2 + 1):len(array_numbers)]):
                return True
            else:
                return False
        else:
            if sum(array_numbers[0:int(len(array_numbers) / 2)]) == sum(array_numbers[int(len(array_numbers) / 2):len(array_numbers)]):
                return True
            else:
                return False


def is_increasing(seq):
    i = 0
    for _ in range(len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            return False
        i += 1
    return True


def is_decreasing(seq):
    i = 0
    for _ in range(len(seq) - 1):
        if seq[i] <= seq[i + 1]:
            return False
        i += 1
    return True


def prime_numbers(n):
    result = [x for x in range(2, n + 1) if x % 2 != 0 and
              x % 3 != 0 and x % 5 != 0 and x % 7 != 0 or x in [2, 3, 5, 7]]
    return result


def is_anagram(a, b):
    if len(a) != len(b):
        return False

    for x in a:
        if x not in b:
            return False
        else:
            b = b.replace('x', "")
    return True


def birthday_ranges(birthdays, ranges):
    result = []
    for i in ranges:
        counter = 0
        for x in birthdays:
            if x >= i[0] and x <= i[1]:
                counter += 1
        result.append(counter)
    return result


def sum_matrix(m):
    sums = [sum(x) for x in m]
    return sum(sums)


def get_largest_palindrome(n):
    n = n - 1
    while not palindrome(n):
        n -= 1
    return n


def is_transversal(transversal, family):
    dictionary = {}
    for i in transversal:
        for j in family:
            if i in j:
                dictionary[i] = j
    for i in transversal:
        if i not in dictionary.keys():
            return False
    return True


def matrix_bombing_plan(m):
    matrix_dict, rows, cols = {}, 0, 0
    for i in m:
        rows += 1
        cols = 0
        for j in i:
            cols += 1
            matrix_dict[(m.index(i), i.index(j))] = j
    result = {}
    for x in matrix_dict:
        result[x] = sum(matrix_dict.values())
    for k1, k2 in result:
        if k1 - 1 >= 0:
            result[(k1, k2)] = result[(k1, k2)] - matrix_dict[(k1 - 1, k2)]
            if result[(k1, k2)] < 0:
                result[(k1, k2)] = 0
        if k2 - 1 >= 0:
            result[(k1, k2)] = result[(k1, k2)] - matrix_dict[(k1, k2 - 1)]
            if result[(k1, k2)] < 0:
                result[(k1, k2)] = 0
        if k1 - 1 >= 0 and k2 - 1 >= 0:
            result[(k1, k2)] = result[(k1, k2)] - matrix_dict[(k1 - 1, k2 - 1)]
            if result[(k1, k2)] < 0:
                result[(k1, k2)] = 0
        if k1 + 1 < rows:
            result[(k1, k2)] = result[(k1, k2)] - matrix_dict[(k1 + 1, k2)]
            if result[(k1, k2)] < 0:
                result[(k1, k2)] = 0
        if k2 + 1 < cols:
            result[(k1, k2)] = result[(k1, k2)] - matrix_dict[(k1, k2 + 1)]
            if result[(k1, k2)] < 0:
                result[(k1, k2)] = 0
        if k1 + 1 < rows and k2 + 1 < cols:
            result[(k1, k2)] = result[(k1, k2)] - matrix_dict[(k1 + 1, k2 + 1)]
            if result[(k1, k2)] < 0:
                result[(k1, k2)] = 0
        if k1 + 1 < rows and k2 - 1 >= 0:
            result[(k1, k2)] = result[(k1, k2)] - matrix_dict[(k1 + 1, k2 - 1)]
            if result[(k1, k2)] < 0:
                result[(k1, k2)] = 0
        if k1 - 1 >= 0 and k2 + 1 < cols:
            result[(k1, k2)] = result[(k1, k2)] - matrix_dict[(k1 - 1, k2 + 1)]
            if result[(k1, k2)] < 0:
                result[(k1, k2)] = 0
    return(result)