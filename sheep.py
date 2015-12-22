def count_sheeps(arrayOfSheeps):
  # TODO May the force be with you
    count = 0
    for x in arrayOfSheeps:
        if x == True:
            count =+ 1
        else:
            count =+ 0
    return count

count_sheeps([True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ])
