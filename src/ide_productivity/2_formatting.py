# Exercise: Format code
# Task: Open the file, notice the formatting inconsistencies (line spaces, mixed quotes, missing spaces, etc.), and hit the shortcut to format the code.
# Look at the git diff, and notice how the code style is now consistent (e.g. no more mix of single quotes and double quotes)

def add_derived_title(df):
    titles = df['Name'].str.extract(' ([A-Za-z]+)\.', expand = False)

    titles= titles.replace(['Lady', 'Countess', 'Capt', 'Col',
                             'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    titles= titles.replace(['Ms', 'Mlle'],'Miss')
    titles= titles.replace(['Mme'], 'Mrs')

    df['Title'] = titles

    return df

def impute_nans(df, categorical_columns, continuous_columns):
    for column in categorical_columns + continuous_columns:
      if column in categorical_columns:
        replacement = df[column].dropna().mode()[0]
      if column in continuous_columns:
        replacement = df[column].dropna().median()
      df[column] = df[column].fillna(replacement)

    return df


def add_categorical_columns(df):
    df =df.copy()

    df['Sex'] = df['Sex'].map({'female': 1, 'male': 0}).astype(int)
    df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2}).astype(int)
    df['Title'] = df['Title'].map(
                            {"Mr": 1, "Miss": 2, 
                            "Mrs": 3, "Master": 4, 
                            "Rare": 5}).fillna(0)

    return df