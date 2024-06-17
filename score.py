

def main():
    """Get user's score and print the result, then generate a random score and print the result"""
    import random

    score = float(input("Enter your score (0-100): "))
    result = determine_result(score)
    print(f"Your result: {result}")

    random_score = random.randint(0, 100)
    random_result = determine_result(random_score)
    print(f"Random score: {random_score} - {random_result}")


def determine_result(score):
    """Determine the result for a given score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == "__main__":
    main()
