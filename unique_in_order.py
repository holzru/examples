def splitter(iterable):
    try:
        new_str = iterable[0]
        for i in range(1, len(iterable)):
            if iterable[i-1] != iterable[i]:
                new_str += iterable[i]
        return list(new_str)
    except IndexError:
        return list(iterable)

def unique_in_order(iterable):
    if hasattr(iterable, '__iter__'):
        for items in iterable:
            if items == str(items):
                iterable = ''.join(iterable)
                return splitter(iterable)
            else:
                iterable = ''.join(str(x) for x in iterable)
                return map(int, splitter(iterable))
    else:
        return splitter(iterable)






unique_in_order('AAAABBBCCDdAABBB')
unique_in_order('AAD')
unique_in_order('ADD')
unique_in_order([1, 2, 3, 3])
unique_in_order(['a', 'b', 'c', 'c'])
