import pandas as pd
import matplotlib.pyplot as plt
import datetime
file_path = r"C:\Users\Tanveer\Downloads\archive\COVID_FINAL_DATA.xlsx"
df = pd.read_excel(file_path)
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.columns)
for col in df.columns:
    print(col)
print(len(df))
print(df.index)

df['Date'] = pd.to_datetime(df['Date']).dt.date
dates = df['Date'].value_counts().sort_index()
plt.figure(figsize=(5, 5))
axe = dates.plot(kind='line', color='blue')
axe.set_facecolor('pink')
plt.xlabel('Date')
plt.ylabel('Suspected Cases Last Date')
plt.title('Total COVID-19 Cases by Region')
plt.tight_layout()
plt.show()
print(df.columns)
plt.figure(figsize=(6, 6))
plt.bar(df['Date'], df['Cumulative  Test positive'], color='blue')
plt.xlabel('Date')
plt.ylabel('Cumulative Test positive')
plt.title('bar Plot of Cumulative Test Positive Cases Over Time')
plt.grid(True)
plt.tight_layout()
plt.show()
plt.figure(figsize=(6, 6))
plt.barh(df['Date'], df['Cumulative  tests performed'], color='blue')
plt.xlabel('Date')
plt.ylabel('Cumulative tests performed')
plt.title('barh Plot of Cumulative Test Performed Cases Over Time')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 6))
plt.bar(df['Date'], df['Discharged'], color='blue')
plt.xlabel('Date')
plt.ylabel('Discharged')
plt.title('line Plot of Discharged Cases Over Time')
plt.grid(True)
plt.tight_layout()
plt.show()

region_column = df['Region']
print(region_column)

plt.figure(figsize=(6, 6))
plt.bar(df['Region'], df['Still admitted'], color='blue')
plt.xlabel('Region')
plt.ylabel('Still admitted')
plt.title('line Plot of Still admitted over region')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 6))
plt.bar(df['Region'], df['Expired'], color='blue')
plt.xlabel('Region')
plt.ylabel('Expired')
plt.title('line Plot of Expired over region')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 6))
plt.bar(df['Region'], df['Home Quarantine'], color='blue')
plt.xlabel('Region')
plt.ylabel('Home Quarantine')
plt.title('line Plot of Home Quarantine over region')
plt.grid(True)
plt.tight_layout()
plt.show()
# Filter data for a specific region
region_name = ['Punjab', 'Sindh']
filtered_data = df[df['Region'].isin(region_name)]

# Plot the filtered data
plt.figure(figsize=(6, 6))
plt.bar(filtered_data['Region'], filtered_data['Home Quarantine'], color='blue')
plt.title(f'Home Quarantine in {", ".join(region_name)}')
plt.tight_layout()
plt.show()
region_name = ['Punjab', 'Sindh']
start_date = datetime.datetime.strptime('2020-6-6', '%Y-%m-%d').date()
end_date = datetime.datetime.strptime('2020-6-6', '%Y-%m-%d').date()

filtered_data = df[(df['Region'].isin(region_name)) & (df['Date'] >= start_date) & (df['Date'] <= end_date)]
# Plot the filtered data
plt.figure(figsize=(6, 6))
plt.barh(filtered_data['Date'], filtered_data['Home Quarantine'], color='blue')
plt.title(f'Home Quarantine in {", ".join(region_name)} from {start_date} to {end_date}')
plt.xlabel('Home Quarantine')
plt.ylabel('Date')
plt.tight_layout()
plt.show()