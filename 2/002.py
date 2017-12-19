def zip1(*iterables):
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    print(iterators)
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)


a = [1, 2, 3]
b = [4, 5, 6]
c = list(zip1(a, b))
print(c)
