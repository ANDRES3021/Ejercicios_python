word_list = [
    'hello',
    'holberton',
    'betty']

def paint(word, error):
    os.system('clear')
    attempts = 6 - error
    print("Remaining attempts: {:d}".format(attempts))
    for i in range(0,error):
        print("{}".format(muñeco[i]))
    print("\n{}\n".format(word))

guess = random.choice(word_list)
guess_lenght = len(guess)
error = 0
word = ""
muñeco = " +---+", " |   |", " O   |", "/|\  |", "/ \  |", "     |\n========="

for i in range(0,guess_lenght):
    word = word + "*"
paint(word, error)
print(" ")

while (error < 6):
    while (True):
        paint(word, error)
        letter= input("Please, input letter: ")
        if (len(letter) == 1 & letter.isalpha()):
            break
        elif (letter == guess):
            print("You Win")
            exit(0)
        else:
            error = error + 1

    letter = letter.lower()
    if (guess.find(letter) != -1):
        for i in range(0, guess_lenght):
            if (letter == guess[i]):
                new = list(word)
                new[i] = letter
                word = ''.join(new)
            paint(word, error)
        if (word == guess):
            print("You Win")
            exit(0)
    else:
        error = error + 1
        paint(word, error)

print("The word was: {}\nYou Lost".format(guess))
exit(1)
