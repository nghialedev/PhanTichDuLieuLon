import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('cleaned_data.csv')
statistics = data.describe().T  # Transpose for better readability
print(statistics)
# Kiểm tra số lượng bản ghi trùng lặp
num_duplicates = data.duplicated().sum()

# Thông báo kết quả
print(f"Số lượng bản ghi bị trùng lặp trong tập dữ liệu là: {num_duplicates}")
# Kiểm tra tổng số giá trị thiếu trong mỗi cột
print(data.isnull().sum())

# Kiểm tra tỷ lệ phần trăm dữ liệu thiếu
missing_percentage = data.isnull().mean() * 100
print(missing_percentage)

# Convert date columns to datetime format
data['release_date'] = pd.to_datetime(data['release_date'])
data['last_update'] = pd.to_datetime(data['last_update'])

# Normalize critic scores to a scale of 0-100
data['critic_score'] = data['critic_score'] * 10

# Remove rows with missing or NaN values
data = data.dropna()

# Save the cleaned data to a new CSV file
data.to_csv('clean_data.csv', index=False)
