# 📊 Power BI Data Preprocessing Scripts in Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/CSV-Data-4B8BBE?style=for-the-badge" alt="CSV">
</p>

<p align="center">
  <b>Python scripts for cleaning and preparing datasets for Power BI analytics and visualization.</b><br>
  <i>Automate your data wrangling process for various datasets including Amazon, Netflix, and global internet usage.</i>
</p>

---

## 📚 Project Overview

This repository contains Python scripts and datasets designed to streamline the data preprocessing workflow for Power BI dashboards. The scripts focus on cleaning, transforming, and preparing raw CSV data from various sources, making them ready for insightful analytics and visualization in Power BI or similar BI tools.

---

## 🗂️ Folder Structure

```
Power_BI/
│
├── Data_Cleaning_Files/
│   ├── Cleaning_File_1.py
│   └── Cleaning_File_Main.py
├── Datasets/
│   ├── Amazon.csv
│   ├── Details.csv
│   ├── Global_Internet_Usage_50_Countries.csv
│   ├── Heart_Disease.csv
│   ├── Kidney_Disease.csv
│   ├── Netflix.csv
│   └── Orders.csv
├── Cleaned_Datasets/
│   ├── Amazon.csv
│   ├── Cleaned_Details.csv
│   ├── Cleaned_Orders.csv
│   ├── Global_Internet_Usage_50_Countries.csv
│   ├── Kidney_Disease.csv
│   └── Netflix.csv
├── DashBoards/
├── Backgrounds/
└── README.md
```

- **Data_Cleaning_Files/**: Contains Python scripts for data cleaning and preprocessing.
  - **Cleaning_File_1.py**: Script for cleaning Netflix dataset and general purpose cleaning functions.
  - **Cleaning_File_Main.py**: Main script for cleaning various datasets with improved performance.
- **Datasets/**: Contains raw datasets in CSV format.
- **Cleaned_Datasets/**: Contains cleaned/preprocessed datasets ready for Power BI visualization.
- **DashBoards/**: Contains Power BI dashboard files.
- **Backgrounds/**: Contains background images or resources.
- **README.md**: Project documentation (this file).

---

## 📂 Datasets

| **File** | **Description** |
|----------|-----------------|
| `Amazon.csv` | Raw data from Amazon (e.g., sales, products, etc.) |
| `Details.csv` | Detailed information dataset |
| `Global_Internet_Usage_50_Countries.csv` | Internet usage stats by country |
| `Heart_Disease.csv` | Medical dataset related to heart disease |
| `Kidney_Disease.csv` | Medical dataset related to kidney disease |
| `Netflix.csv` | Raw data from Netflix (e.g., titles, ratings, etc.) |
| `Orders.csv` | Order information dataset |

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.8 or higher
- `pip` package manager

### 2. Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/bchaitanya92/Power_BI.git
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
python Data_Cleaning_Files/Cleaning_File_Main.py
```

Or for specific dataset cleaning:

```sh
python Data_Cleaning_Files/Cleaning_File_1.py
```

- The scripts will read the raw CSV files from the [Datasets](Datasets/) folder, perform cleaning operations, and output the cleaned datasets to the [Cleaned_Datasets](Cleaned_Datasets/) folder.
- You can modify the scripts to adjust the cleaning logic as needed for your specific data or analysis requirements.

---

## 👨‍💻 Author & Credits

Developed by:

**B. Chaitanya**  
Data Science & Machine Learning

- GitHub: [bchaitanya92](https://github.com/bchaitanya92)
- LinkedIn: [BOURISETTI CHAITANYA](https://www.linkedin.com/in/b-chaitanya/)

Feel free to explore, modify, and use these scripts for your own data projects. Contributions and feedback are always welcome. Happy Data Cleaning! 🚀
