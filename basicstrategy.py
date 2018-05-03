'''
Player 6 vs Dealer 10 -> basic[6][10]
'''


# D   0      1      2      3      4      5      6      7      8      9     10

hard = (
    ["00", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["01", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["02", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["03", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["04", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["05", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["06", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["07", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["08", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["09", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["10", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["11", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["12", "Hit", "Hit", "Hit", "Std", "Std", "Std", "Hit", "Hit", "Hit", "Hit"],
    ["13", "Hit", "Std", "Std", "Std", "Std", "Std", "Hit", "Hit", "Hit", "Hit"],
    ["14", "Hit", "Std", "Std", "Std", "Std", "Std", "Hit", "Hit", "Hit", "Hit"],
    ["15", "Hit", "Std", "Std", "Std", "Std", "Std", "Hit", "Hit", "Hit", "Hit"],
    ["16", "Hit", "Std", "Std", "Std", "Std", "Std", "Hit", "Hit", "Hit", "Hit"],
    ["17", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std"],
    ["18", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std"],
    ["19", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std"],
    ["20", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std"],
    ["21", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std"]
)

# D   0      1      2      3      4      5      6      7      8      9     10


soft = (
    ["00", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["01", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["02", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["03", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["04", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["05", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["06", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["07", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["08", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["09", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["10", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["11", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["12", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit", "Hit"],
    ["13", "Hit", "Hit", "Hit", "Hit", "Dbl", "Dbl", "Hit", "Hit", "Hit", "Hit"],
    ["14", "Hit", "Hit", "Hit", "Hit", "Dbl", "Dbl", "Hit", "Hit", "Hit", "Hit"],
    ["15", "Hit", "Hit", "Hit", "Dbl", "Dbl", "Dbl", "Hit", "Hit", "Hit", "Hit"],
    ["16", "Hit", "Hit", "Hit", "Dbl", "Dbl", "Dbl", "Hit", "Hit", "Hit", "Hit"],
    ["17", "Hit", "Std", "Dbl", "Dbl", "Dbl", "Dbl", "Hit", "Hit", "Hit", "Hit"],
    ["18", "Hit", "Std", "Dbl", "Dbl", "Dbl", "Dbl", "Std", "Std", "Hit", "Hit"],
    ["19", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std"],
    ["20", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std"],
    ["21", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std", "Std"]
)

# D   0      1      2      3      4      5      6      7      8      9     10

split = (
    ["00", False, False, False, False, False, False, False, False, False, False],
    ["01", True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
    ["02", False, True,  True,  True,  True,  True,  True,  False, False, False],
    ["03", False, True,  True,  True,  True,  True,  True,  False, False, False],
    ["04", False, False, False, False, True,  True,  False, False, False, False],
    ["05", False, False, False, False, False, False, False, False, False, False],
    ["06", False, True,  True,  True,  True,  True,  False, False, False, False],
    ["07", False, True,  True,  True,  True,  True,  True,  False, False, False],
    ["08", True,  True,  True,  True,  True,  True,  True,  True,  True,  True],
    ["09", False, True,  True,  True,  True,  True,  False, True,  True,  False],
    ["10", False, False, False, False, False, False, False, False, False, False],
)
