def breadth_first_search(top, get_children):
    inbox = [top]
    results = {top}
    while inbox:
        new_inbox = []
        for obj in inbox:
            for child in get_children(obj):
                if child not in results:
                    results.add(child)
                    new_inbox.append(child)
        inbox = new_inbox
    return results


def spicy(n, base_cases, split, combine):
    if n in base_cases:
        return base_cases[n]

    def get_children(i):
        return [j for j in split(i) if j not in base_cases]

    values = base_cases.copy()
    for i in sorted(breadth_first_search(n, get_children)):
        print(i)
        assert i not in values
        a, b = split(i)
        values[i] = combine(values[a], values[b])

    return values[n]
