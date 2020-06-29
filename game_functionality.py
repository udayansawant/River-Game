import authenticate_data


def find_river_size(mat):
    rows = len(mat)
    cols = len(mat[0])
    result = []
    queue = []
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for row in range(rows):
        for col in range(cols):
            if mat[row][col] == 1:
                mat[row][col] = 0
                size = 1
                queue.append((row, col))

                while queue:
                    r, c = queue.pop(0)
                    for d in directions:
                        new_r, new_c = r+d[0], c+d[1]
                        if 0 <= new_r < rows and 0 <= new_c < cols:
                            if mat[new_r][new_c] == 1:
                                mat[new_r][new_c] = 0
                                queue.append((new_r, new_c))
                                size += 1
                result.append(size)
    return result


def guess_the_river_size(river_sizes):
    number_of_rivers = len(river_sizes)
    right_guesses = 0
    guess_count = 1
    your_guess = []
    index = 0
    print("***Guess the River Size***")
    while guess_count <= number_of_rivers:
        print("Guess %d of %d" % (guess_count, number_of_rivers))
        guess = int(input("Enter the size:"))
        your_guess.append(guess)
        if river_sizes[index] == guess:
            right_guesses += 1
        guess_count += 1
        index += 1
    print()
    print("***Evaluating your guesses...***")
    print("River sizes:", river_sizes)
    print("Your guesses: ", your_guess)

    win_percentage = (right_guesses/number_of_rivers)*100
    if win_percentage == 100.0:
        print("You are the winner")
    elif win_percentage >= 60.0:
        print("You got second position")
    else:
        print("Invest more money on Almonds, then come back")
    print("Game Over!")


if __name__ == '__main__':
    matrix = authenticate_data.result
    river_sizes = find_river_size(matrix)
    guess_the_river_size(river_sizes)



