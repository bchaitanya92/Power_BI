"""

import pandas as pd

def clean_dataset(file_path, output_path=None):
    # Load dataset
    df = pd.read_csv(file_path)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove duplicate columns
    df = df.loc[:, ~df.columns.duplicated()]

    # Strip whitespaces from column names
    df.columns = df.columns.str.strip()

    # Strip whitespaces from string data (only apply to object type columns)
    df_obj = df.select_dtypes(include=['object'])
    df[df_obj.columns] = df_obj.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Fill missing values carefully
    for column in df.columns:
        if df[column].dtype == 'object':  # For categorical columns
            if not df[column].mode().empty:
                df[column].fillna(df[column].mode()[0], inplace=True)
        else:  # For numerical columns
            if not df[column].isnull().all():
                df[column].fillna(df[column].mean(), inplace=True)

    # Save cleaned dataset if output path is provided
    if output_path:
        df.to_csv(output_path, index=False)

    return df

# Example usage
cleaned_df = clean_dataset('Full netflix Dataset.csv', 'cleaned_dataset.csv')
print(cleaned_df.head())

"""


