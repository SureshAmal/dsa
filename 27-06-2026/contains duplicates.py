# if array has duplicate return false


def containduplicates(l: list) -> bool:
    h = set()

    for key, v in enumerate(l):
        if v in h:
            return True
        h.add(v)

    return False


print(containduplicates([1, 2, 3, 4, 2]))
