# Code testing with module 'unittest'

# Build some test functions first.
from codetesting import get_formatted_name
from codetesting import city_name

print("Enter 'q' at any time to quit.")
active = False
while active:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")


# Create a test environment.
import unittest as ut

class NamesTestCase(ut.TestCase):
    """Tests for 'get_formatted_name()'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_fist_last_middle_name(self):
        formatted_name = get_formatted_name('janis', 'joplin', 'maria')
        self.assertEqual(formatted_name, 'Janis Maria Joplin')

class CityTestCase(ut.TestCase):
    """Tests for 'city_name()'."""

    def test_city_name(self):
        city = city_name('santiago', 'chile')
        self.assertEqual(city, 'Santiago, Chile') # Test Equality
        self.assertNotEqual(city, 'santiago, chile') # Test Inequality
        # self.assertTrue(x)
        # self.assertFalse(x)
        # self.assertIn(item, list)
        # self.assertNotIn(item, list)

    def test_city_name_with_population(self):
        city = city_name('beijing', 'china', 24000000)
        self.assertEqual(city, 'Beijing, China - population 24000000')
        self.assertNotEqual(city, 'Beijing, China')

'''
if __name__ == '__main__':
    ut.main()
'''

# Notes
'''
-------- The explanation of the structure above. --------
0. import required modules
        import unittest
        import the function that waiting for testing

1. create a class
        This class will contains a series of 'unit tests' for the
    function we want to test.
        The class must inherit from the class 'unittest.TestCase'.

2. methods in the test environment
        NamesTestCase contains 1 method: test_first_last_name.
    *   All the method that starts with 'test_' will be run
    automatically when we run this .py file.
        In the method, we use assertEqual() method, to compare
    the value of formatted_name and 'Janis Joplin'.

3. import file waiting for test to your test environment
        For now we will run the test code directly, but it is more
    often to import test files to the test framework.
        __name__ is a special variable, which will be set to
    '__main__' if the file is being run as the main program. In this
    case, we call unittest.main(), which runs the test case. On the
    other hand, if a testing framework import this file, __name__
    won't be '__main__', and unittest.main() won't be executed.

4. results - success
        After run the program, following result shows:
  <<==========================================================================>>
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s
    OK
  <<==========================================================================>>
        The dot tells that a single test passed.

5. result - error
        Try to remove 'joplin' in function get_formatted_name()
    and run the code, following result shows:
  <<==========================================================================>>
    E
    ======================================================================
    ERROR: test_first_last_name (__main__.NamesTestCase)
    Do names like 'Janis Joplin' work?
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "D:\Projects\PyLearning\Exercise\022_code_testing.py", line 27, in test_first_last_name
        formatted_name = get_formatted_name('janis')
    TypeError: get_formatted_name() missing 1 required positional argument: 'last'

    ----------------------------------------------------------------------
    Ran 1 test in 0.001s

    FAILED (errors=1)
  <<==========================================================================>>
        It tells that there's a missing argument.

6. change your code to match the test
        Consider add a new optional parameter 'middle' which saves the 
    middle name of a person. For more detail, see 'get_formatted_name'.
    *   Add a new method in class 'NamesTestCase' to test whether middle
    name can be successfully formatted or not.
'''


##### Try to test a class. #####
from codetesting import AnonymousSurvey # A class that defines a questionnaire.

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
active = False
while active:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

# Build test environment
# Method: convert as instances then test methods.
class TestAnonymousSurvey(ut.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?" # Not critical.
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses) # Main testing case.

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses) # Check all elements.

class TestAnonymousSurveyNew(ut.TestCase):
    """Compress the code."""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        Because of neither of these method creates instances or return value,
            so we can just create one instance.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question) # Create instance at here.
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response_new(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses_new(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


from codetesting import Employee

class TestEmployee(ut.TestCase):

    def setUp(self):
        self.employee = Employee('Test_first', 'Test_last')
    
    def test_default_salary(self):
        self.assertEqual(self.employee.annual_salary, 0)

    def test_give_raise_default(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 5000)

    def test_give_raise_10000(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 10000)

if __name__ == '__main__':
    ut.main()