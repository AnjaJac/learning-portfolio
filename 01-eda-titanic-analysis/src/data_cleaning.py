import os
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_data(filename="Titanic-Dataset.csv"):
    path = os.path.join(DATA_DIR, filename)
    return pd.read_csv(path)

def clean_missing(df):
    df = df.copy()
    # Age: fill with median
    df['Age'] = df['Age'].fillna(df['Age'].median())
    # Embarked: fill with mode
    if 'Embarked' in df.columns:
        df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    # Cabin known
    df['CabinKnown'] = df['Cabin'].notnull().astype(int) if 'Cabin' in df.columns else 0
    if 'Cabin' in df.columns:
        df = df.drop(columns=['Cabin'])
    return df

def add_features(df):
    df = df.copy()
    df['FamilySize'] = df.get('SibSp', 0) + df.get('Parch', 0) + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

    if 'Name' in df.columns:
        # Make extraction robust: ensure strings, extract the first matching group, then strip whitespace.
        # Use expand=False to get a Series; missing matches will be NaN.
        names = df['Name'].astype(str)
        titles = names.str.extract(r',\s*([^\.]+)\.', expand=False)
        df['Title'] = titles.str.strip()
    else:
        df['Title'] = pd.NA  # or skip entirely

    return df


def save_cleaned_data(df, filename="titanic_clean.csv"):
    path = os.path.join(DATA_DIR, filename)
    df.to_csv(path, index=False)
    return path

def main():
    df = load_data()
    df = clean_missing(df)
    df = add_features(df)
    out = save_cleaned_data(df)
    print("Saved cleaned data to:", out)

if __name__ == "__main__":
    main()
