def count_words(arr):
    words_counter = {}
    for word in arr:
        if word not in words_counter.keys():
            words_counter[word] = arr.count(word)
    return words_counter


def nan_expand(times):
    sentence = ""
    for _ in range(times):
        sentence = sentence + "Not a "
    if sentence is not "":
        return sentence + "NaN"
    return sentence


def iterations_of_nan_expand(expanded):
    reps = expanded.count('Not a ')
    expanded = expanded.replace("Not a ", "", reps)
    if expanded == 'NaN':
        return reps
    else:
        return False


def group(arr):
    single_group, all_groups = [], []

    for number in range(len(arr) - 1):
        single_group.append(arr[number])
        if arr[number + 1] != single_group[0]:
            all_groups.append(single_group)
            single_group = []

    if arr[-1] == all_groups[-1][0]:
        all_groups[-1].append(arr[-1])
    else:
        all_groups.append([arr[-1]])
    return all_groups