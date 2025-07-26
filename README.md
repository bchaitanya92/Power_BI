# 📊 Power BI Data Preprocessing Scripts in Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/CSV-Data-4B8BBE?style=for-the-badge" alt="CSV">
</p>

<p align="center">
  <b>Python scripts for cleaning and preparing datasets for Power BI analytics and visualization.</b><br>
  <i>Automate your data wrangling process for Amazon, Netflix, and global internet usage datasets.</i>
</p>

---

## 📚 Project Overview

This repository contains Python scripts and sample datasets designed to streamline the data preprocessing workflow for Power BI dashboards. The scripts focus on cleaning, transforming, and preparing raw CSV data from Amazon, Netflix, and global internet usage sources, making them ready for insightful analytics and visualization in Power BI or similar BI tools.

---

## 🗂️ Folder Structure

```
Power_BI_Data_PreProcessing_File/
│
├── a.py
├── Cleaning_file.py
├── Amazon.csv
├── Netflix.csv
├── global_internet_usage_2000_2023_50countries.csv
├── cleaned_dataset_amazon.csv
├── cleaned_dataset_netflix.csv
└── README.md
```

- **a.py**: Auxiliary or experimental script (purpose may vary).
- **Cleaning_file.py**: Main script for cleaning and preprocessing the datasets.
- **Amazon.csv**: Raw Amazon dataset (input).
- **Netflix.csv**: Raw Netflix dataset (input).
- **global_internet_usage_2000_2023_50countries.csv**: Raw global internet usage data (input).
- **cleaned_dataset_amazon.csv**: Cleaned output for Amazon data.
- **cleaned_dataset_netflix.csv**: Cleaned output for Netflix data.
- **README.md**: Project documentation (this file).

---

## 📂 Datasets

| **File**                                      | **Description**                                      |
|-----------------------------------------------|------------------------------------------------------|
| `Amazon.csv`                                 | Raw data from Amazon (e.g., sales, products, etc.)   |
| `Netflix.csv`                                | Raw data from Netflix (e.g., titles, ratings, etc.)  |
| `global_internet_usage_2000_2023_50countries.csv` | Internet usage stats by country (2000-2023)         |
| `cleaned_dataset_amazon.csv`                  | Cleaned/preprocessed Amazon data (output)            |
| `cleaned_dataset_netflix.csv`                 | Cleaned/preprocessed Netflix data (output)           |

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.8 or higher
- `pip` package manager

### 2. Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/bchaitanya92/Power_BI_Data_PreProcessing_File.git
    cd Power_BI_Data_PreProcessing_File
    ```

2. **(Optional) Create and activate a virtual environment:**
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install required libraries:**
    ```sh
    pip install pandas numpy
    ```

---

## 💡 Usage

To clean and preprocess the datasets, run the main script:

```sh
python Cleaning_file.py
```

- The script will read the raw CSV files, perform cleaning operations, and output the cleaned datasets as new CSV files in the same directory.
- You can modify `Cleaning_file.py` to adjust the cleaning logic as needed for your specific data or analysis requirements.

---

## 👨‍💻 Author & Credits

Developed by:

**B. Chaitanya**  
Data Science & Machine Learning

- GitHub: [bchaitanya92](https://github.com/bchaitanya92)
- LinkedIn: [BOURISETTI CHAITANYA](https://www.linkedin.com/in/b-chaitanya/)

Feel free to explore, modify, and use these scripts for your own data projects. Contributions and feedback are always welcome. Happy Data Cleaning! 🚀