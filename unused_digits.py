def unused_digits(*numbers):
    digits = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    unused = []
    for num in numbers:
        digits = digits - set(map(int, list(str(num))))
        new_digits = sorted(digits)
    print ''.join(str(s) for s in new_digits)


unused_digits(12, 34, 56, 78)
unused_digits(2015, 8, 26)
unused_digits(276, 575)
unused_digits(643)
unused_digits(864, 896, 744)
