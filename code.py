import pandas as pd
import matplotlib.pyplot as plt

data = {
    'EmpName': ['Amit', 'Riya', 'Karan', 'Riya', 'Amit', 'Sneha', 'Karan', 'Meena', 'Amit', 'Sneha'],
    'EmpId': [101, 102, 103, 102, 101, 104, 103, 105, 101, 104],
    'EmpSalary': [50000, 60000, 55000, 60000, 50000, 58000, 55000, 52000, 50000, 58000]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

plt.figure(figsize=(8, 5))
plt.bar(df['EmpName'], df['EmpSalary'], color='skyblue')
plt.title('Original Employee Salaries')
plt.xlabel('Employee Name')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

duplicates = df[df.duplicated()]
print("\nDuplicate Rows Detected:")
print(duplicates)

df_cleaned = df.drop_duplicates()
print("\n Cleaned Data (Duplicates Removed):")
print(df_cleaned)

plt.figure(figsize=(8, 5))
plt.bar(df_cleaned['EmpName'], df_cleaned['EmpSalary'], color='lightgreen')
plt.title('Cleaned Employee Salaries')
plt.xlabel('Employee Name')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
