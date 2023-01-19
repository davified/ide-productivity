from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score

import numpy as np
import pandas as pd

from src.ide_productivity.helpers import do_something

df = pd.DataFrame(
    {
        "name": ['Alice', 'Bob', 'Charlie'],
        'seat_number': ['1A', '10C', '42G'], 'age': ['30', '45', '12'],
    }
)

### 2. Refactoring ###
# Exercise: Format code
# TODO: Hit shortcut for Format Document
# Notice how the code style is now consistent (e.g. no more mix of single quotes and double quotes)


# Exercise: Rename variable
# TODO: Rename `df` to something more meaningful (e.g. `passengers`)
# TODO: Rename `do_something()` to anything else (e.g. `greet()`). Notice how all references to that method has been renamed (see `src/helpers.py`)
print(df)
do_something()  # FIXME: enable the renaming of this variable


# Exercise: Extract variable / method / function



# Exercise: Sort imports