# Test methods

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

def city_name(city, country, population=''):
    """Generate a neatly formatted city location."""
    if population:
        full = f"{city.title()}, {country.title()} - population {population}"
    else:
        full = f"{city.title()}, {country.title()}"
    return full

# Test classes

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

class Employee(object):

    def __init__(self, first, last, salary=0):
        self.first_name = first
        self.last_name = last
        self.annual_salary = salary

    def give_raise(self, raised=5000):
        self.annual_salary += raised
