# Type all other functions here
def get_num_of_non_WS_characters(usrStr):
    new_text = usrStr.replace(" ", "")
    num_char = len(new_text)

    return num_char


def get_num_of_words(usrStr):
    num_words = len(usrStr.split())

    return num_words


def fix_capitalization(usrStr):
    new_str = usrStr.split('. ')

    edit = []
    for i in new_str:
        for s, c in enumerate(i):
            if not c.isspace():
                break
        edit.append(i[:s] + i[s:].capitalize())

    count_cap_words = 0
    for i in edit:
        if not i.islower():
            count_cap_words += 1
    usrStr = ". ".join(edit)

    return usrStr, count_cap_words


def replace_punctuation(usrStr, exclamationCount=0, semicolonCount=0):
    while usrStr.find('!') != -1:
        usrStr = usrStr.replace('!', '.', 1)
        exclamationCount += 1

    while usrStr.find(';') != -1:
        usrStr = usrStr.replace(';', ',', 1)
        semicolonCount += 1

    return usrStr, exclamationCount, semicolonCount


def shorten_space(usrStr):
    new_str = " ".join(usrStr.split())

    return new_str


def print_menu(usrStr):
    menuOp = ''
    # Complete print_menu() function
    menu = ("\nMENU\n"
            "c - Number of non-whitespace characters\n"
            "w - Number of words\n"
            "f - Fix capitalization\n"
            "r - Replace punctuation\n"
            "s - Shorten spaces\n"
            "q - Quit\n"
            )

    while menuOp != 'q':
        print(menu)
        menuOp = input("Choose an option: \n")

        if menuOp == 'q':
            print("\nBye!")
            break
        elif menuOp == 'c':
            print("Number of non-whitespace characters: " + str(get_num_of_non_WS_characters(usrStr)))
        elif menuOp == 'w':
            print("Number of words: " + str(get_num_of_words(usrStr)))
        elif menuOp == 'f':
            userStr, capWords = fix_capitalization(usrStr)
            print("Number of letters capitalized: %d\nEdited text: %s" % (capWords, userStr))
        elif menuOp == 'r':
            userStr, exclamations, semicolons = replace_punctuation(usrStr)
            print("Punctuation replaced\nexclamationCount: %d\nsemicolonCount: %d\nEdited text: %s" % (exclamations, semicolons, userStr))
        elif menuOp == 's':
            print("Edited text: " + shorten_space(usrStr))
        else:
            print("Invalid option")

    return menuOp, usrStr


if __name__ == '__main__':
    # Complete main section of code
    user_text = input("Enter a sample text: \n")
    print("You entered: " + user_text)

    print_menu(user_text)
