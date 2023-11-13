import unittest
from math_quiz import function_A, function_B, function_C


import unittest
from unittest.mock import patch
from math_quiz import generate_random_integer, generate_random_operator, perform_operation, math_quiz

class TestMathQuizFunctions(unittest.TestCase):

    def test_generate_random_integer(self):
        minimum, maximum = 1, 10
        random_integer = generate_random_integer(minimum, maximum)
        self.assertGreaterEqual(random_integer, minimum)
        self.assertLessEqual(random_integer, maximum)

    def test_generate_random_operator(self):
        operators = {'+', '-', '*'}
        random_operator = generate_random_operator()
        self.assertIn(random_operator, operators)

    def test_perform_operation_addition(self):
        result = perform_operation(3, 4, '+')
        self.assertEqual(result, ('3 + 4', 7))

    def test_perform_operation_subtraction(self):
        result = perform_operation(8, 5, '-')
        self.assertEqual(result, ('8 - 5', 3))

    def test_perform_operation_multiplication(self):
        result = perform_operation(2, 6, '*')
        self.assertEqual(result, ('2 * 6', 12))

    @patch('builtins.input', side_effect=['7'])
    @patch('builtins.print')
    def test_math_quiz_correct_answer(self, mock_print, mock_input):
        math_quiz()
        mock_print.assert_any_call("Correct! You earned a point.")

    @patch('builtins.input', side_effect=['10'])
    @patch('builtins.print')
    def test_math_quiz_wrong_answer(self, mock_print, mock_input):
        math_quiz()
        mock_print.assert_any_call("Wrong answer. The correct answer is ")

if __name__ == '__main__':
    unittest.main()

