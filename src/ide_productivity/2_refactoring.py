from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score

import numpy as np
import pandas as pd

from src.ide_productivity.helpers import do_something

df = pd.DataFrame(
    {
        "name": ['Alice', "Bob", 'Charlie'],
        'seat_number': ['1A', '10C', '42G'], 'age': ['30', '45', '12'],
    }
)

### 2. Refactoring ###

# Exercise: Rename variable
# TODO: Rename `df` to something more meaningful (e.g. `passengers`)
# TODO: Rename `do_something()` to anything else (e.g. `greet()`). Notice how all references to that method has been renamed (see `src/helpers.py`)
print(df)
do_something()  # FIXME: enable the renaming of this variable


# Exercise: Extract method
# TODO: Select the last 4 lines of code in this exercise, hit the shortcut for extract method, and give the function a name (e.g. add_prettified_ticket_column)
prettified_name = "Passenger: " + df["name"]
prettified_seat_number = "Seat Number: " + df["seat_number"]
df["prettified_ticket"] = prettified_name + ", " + prettified_seat_number
print(df)



# Exercise: Fix coding formatting
# TODO: Notice the formatting inconsistencies (e.g. mixed single and double quotes in df)? Hit the shortcut to format the code.
# Notice how the code style is now consistent (e.g. no more mix of single quotes and double quotes)


# Exercise: Sort imports
# TODO: Notice the unused imports at the top? Hit the shortcut the organize imports, and notice the imports are now tidy