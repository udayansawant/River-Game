import read_csv


def show_welcome_note():
    with open('welcome_note.txt', 'r') as welcome_text:
        print(welcome_text.read())
    get_in = input("Do you want to Get in or not [Yes/No]:")
    if get_in.lower() == 'yes':
        return show_instructions()
    else:
        print("Game is shutting down")
        welcome_text.close()
        exit(0)


def show_instructions():
    with open('game_instruction.txt', 'r') as instructions_text:
        print(instructions_text.read())
    play = {'P': 'P'}
    while True:
        try:
            user_input = play[input("Press P to Play:")]
            break
        except:
            print("You Entered the wrong choice!")
    print("Game Started!")
    return get_matrix_input()


def get_matrix_input():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = [[int(input("Enter the matrix cell value (1/0):")) for j in range(cols)] for i in range(rows)]
    print("Input matrix is:")
    for i in range(rows):
        temp = []
        for j in range(cols):
            temp.append(matrix[i][j])
        print(temp)
    print()
    return matrix


def authenticate_user():
    users = read_csv.result
    attempt = 2
    logged_in_flag = False
    print("***Authenticating the user...***")
    while attempt > 0:
        username = input("Enter your username:")
        if username in users:
            email = input("Enter your email:")
            if users[username] == email:
                logged_in_flag = True
                break
            else:
                print("Invalid username and password")
        else:
            print("User does not exist")
        attempt -= 1
    if logged_in_flag:
        print("Successfully Logged In")
        return show_welcome_note()
    else:
        print("You attempted wrong credentials two times")
        print("Try again later!")
        exit(0)


result = authenticate_user()


