def flatten_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    result = [num for row in matrix for num in row]

    print("Original Matrix:", matrix)
    print("Flattened List:", result)


flatten_matrix()
