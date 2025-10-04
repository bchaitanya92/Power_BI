import pandas as pd

def clean_dataset(file_path, output_path=None):
    # Load dataset
    df = pd.read_csv(file_path)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove duplicate columns by name
    df = df.loc[:, ~df.columns.duplicated()]

    # Strip whitespaces from column names
    df.columns = df.columns.str.strip()

    # Strip whitespaces from string data (faster than applymap)
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    # Fill missing values safely
    for column in df.columns:
        if df[column].dtype == 'object':
            if not df[column].mode().empty:
                df[column].fillna(df[column].mode()[0], inplace=True)
        else:
            if df[column].notna().any():
                df[column].fillna(df[column].mean(), inplace=True)

    # Save cleaned dataset if output path is provided
    if output_path:
        df.to_csv(output_path, index=False)

    return df

# Example usage
cleaned_df = clean_dataset(
    r'F:\Projects\001 Not Updated\Power_BI\Datasets\Global_Internet_Usage_50_Countries.csv',
    r'F:\Projects\001 Not Updated\Power_BI\Cleaned_Datasets\Global_Internet_Usage_50_Countries.csv'
)
print(cleaned_df.head())
