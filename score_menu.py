


def main():

    score = get_valid_score()
    while True:
        print("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
        choice = input(">>> ").upper()
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = determine_result(score)
            print(f"Score: {score} - {result}")
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell!")
            break
        else:
            print("Invalid choice")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive"""
    score = float(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        score = float(input("Invalid score. Enter a valid score (0-100): "))
    return score


def determine_result(score):

    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):

    print('*' * int(score))


if __name__ == "__main__":
    main()
