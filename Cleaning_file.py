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

    # Strip whitespaces from string data
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Fill missing values
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column].fillna(df[column].mode()[0], inplace=True)  # Most frequent for categorical
        else:
            df[column].fillna(df[column].mean(), inplace=True)  # Mean for numeric

    # Save cleaned dataset if output path is provided
    if output_path:
        df.to_csv(output_path, index=False)

    return df

# Example usage
cleaned_df = clean_dataset('global_internet_usage_2000_2023_50countries.csv', 'cleaned_dataset_global.csv')
print(cleaned_df.head())