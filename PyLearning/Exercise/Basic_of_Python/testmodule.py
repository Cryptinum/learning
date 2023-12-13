# Example module

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

def show_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\n", toppings)