def next(array, function, wrap = False):
    next_array = []
    height = len(array)
    for y in range(len(array)):
        row = array[y]
        next_row = []
        width = len(row)

        for x in range(len(row)):
            # Coords x and y of cell
            # O O O for i in range(-1, 1)
            # O x O     for j in range(-1, 1)
            # O O O

            # Count adjacent cells
            n = 0

            for i in range(-1, 2):
                for j in range(-1, 2):

                    x2 = x+j
                    y2 = y+i

                    if wrap == False and ((x2<0 or y2<0) or (x2 >= width or y2 >= height)):
                        continue

                    x2 = x2%(width-1)
                    y2 = y2%(height-1)

                    if (i, j) != (0,0):
                        n += array[y2][x2]

            if function(n):
                next_row.append(1)
            else:
                next_row.append(0)

        next_array.append(next_row)

    return next_array
