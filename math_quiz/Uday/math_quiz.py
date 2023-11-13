import random

def generate_random_integer(minimum, maximum):
    """Generate a random integer between the given minimum and maximum values."""
    return random.randint(minimum, maximum)

def generate_random_operator():
    """Generate a random arithmetic operator from the set {+, -, *}."""
    return random.choice(['+', '-', '*'])

def perform_operation(number1, number2, operator):
    """Perform the arithmetic operation based on the provided numbers and operator."""
    expression = f"{number1} {operator} {number2}"

    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2

    return expression, result

def math_quiz():
    """Run a math quiz game where the user needs to solve arithmetic problems."""
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = perform_operation(num1, num2, operator)

        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            user_answer = 0

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()

