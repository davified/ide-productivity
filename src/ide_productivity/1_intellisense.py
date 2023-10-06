import pandas as pd

passengers = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie"],
        "seat_number": ["1A", "10C", "42G"],
        "age": [30., 45., 12.],
    }
)

### 1. IntelliSense ###
# Exercise: Calculate the mean age of passengers
# TODO: Put a dot (.) after the series, and you can browse through a list of Series methods that you could use to calculate the mean for the series
# If you miss the suggestion, you can get it again by hitting the shortcut for Trigger Suggest (Ctrl + Space)
mean_age = passengers["age"]
print(f"The mean age of passengers is: {mean_age}")


# Exercise: Convert the age column from float to integers
# TODO: Place your cursor on the function astype, hit the shortcut for Quick Documentation. Can you scroll through and see documentation and examples on how you can convert data types?
# TODO: Place your cursor on the parenthesis of astype(), hit the shortcut for Parameter Hints. Can you identify the first parameter that this function accepts?
ages = passengers["age"].astype()
print(ages)


# Exercise: Auto Fix
# TODO: Uncomment the following line (it has an error!).
# Hover over the squiggly line to see the error and use the auto fix shortcut to fix the error
# directory_name = path.dirname("/the/path/to/somewhere")
# print(directory_name)


# Exercise: Linting
# TODO: Uncomment the last line. Notice the linter's warning for greet()? Can you read the error and find a fix?
def greet(name: str):
   print(f"Howdy {name}!")

# greet()

