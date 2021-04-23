def game_cubes(x, y, z):
    """Function checks if dice code is correct and return the result of the roll"""
    if y in cube_types:
        tab = []
        for i in y:
            tab.append(i)
        cube = tab[1::]
        split_cube = "".join(cube)
    else:
        return "Wrong cube \n You can use: D3, D4, D6, D8, D10, D12, D20, D100"
    if z == 0:
        return x * int(split_cube)
    elif z > 0:
        return x * int(split_cube) + z
    elif x == 0:
        return int(split_cube) + z



if __name__ == "__main__":
    try:
        x = int(input("Input number of throws: "))
        y = input("Input type of cube (e.g. D6, D10, D20): ")
        z = int(input("Input mod (optional): ") or "0")
        cube_types = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")
        print(game_cubes(x, y, z))
    except ValueError:
        print("Nr of throws and mod must be a numbers!")
