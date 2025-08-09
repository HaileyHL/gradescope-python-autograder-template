def count_exact_match(text, query):
    count = 0
    for i in range(min(len(text), len(query))):
        if text[i] == query[i]:
            count += 1
    return count
