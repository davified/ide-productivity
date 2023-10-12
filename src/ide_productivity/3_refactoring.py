import pandas as pd

from ide_productivity.helpers import do_something

df = pd.DataFrame(
    {
        "name": ['Alice', 'Bob', 'Charlie'],
        'seat_number': ['1A', '10C', '42G'], 'age': ['30', '45', '12'],
    }
)

# Exercise 3.1: Rename variable
# Task: Rename `df` to something more meaningful (e.g. `passengers`)
# Task: Rename `do_something()` to something else (e.g. `greet()`). Notice how all references to that method has been renamed (see `src/helpers.py`)
print(df)
do_something()


# Exercise 3.2: Extract method
# Task: Select the next 3 lines of code in this exercise, hit the shortcut for extract method, and give the function a name (e.g. add_prettified_ticket_column)
prettified_name = "Passenger: " + df["name"]
prettified_seat_number = "Seat Number: " + df["seat_number"]
df["prettified_ticket"] = prettified_name + ", " + prettified_seat_number
print(df)
