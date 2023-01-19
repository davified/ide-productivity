import pandas as pd

passengers = pd.DataFrame(
    {
        "name": ['Alice', 'Bob', 'Charlie'],
        'seat_number': ['1A', '10C', '42G'], 'age': ['30', '45', '12'],
    }
)

### 1. IntelliSense ###
# Exercise: Calculate the mean age of passengers
# TODO: Put a dot (.) after the series, and you can browse through a list of Series methods that you could use to calculate the mean for the series
# If you miss the suggestion, you can get it again by hitting the shortcut for Trigger Suggest (Ctrl + Space)
mean_age = passengers["name"]
print(mean_age)


# Exercise: Import `accuracy_score()` and `precision_recall_curve()` from `sklearn.metrics`
# TODO: at the top of the file, start typing: "from sklearn.metrics import" and hit the shortcut for Trigger Suggest (Ctrl + Space)
# Notice how you can simply browse through a list methods? No need to context switch and get distracted by browser tabs and ads!


# Exercise: Convert the age column to integers
# TODO: place your cursor within the parentheses of .astype(), hit the shortcut for Trigger Parameter Hints. Can you scroll through and see documentation and examples on how you can convert data types?
# To find out the exact shortcut, you can Open Command Palette (F1), type the shortcut name (e.g. Parameter Hints), and you'll see the associated shortcut
ages = passengers['name'].astype()
print(ages)


# Exercise: Quick Fix
# TODO: Uncomment the following line (it has an error!). 
# Hover over the squiggly line to see the error and use the Quick Fix shortcut to fix the error
# path.dirname("/the/path/to/somewhere")

