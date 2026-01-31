import pandas as pd
df=pd.read_csv(r"C:\Users\sudav\Desktop\Hospital_patient_analytics\hospital_patient_data.csv")
print(df)

# first 5 rows 
print(df.head())

# last 5 rows
print(df.tail())

# info of dataset
print(df.info())

df['Revenue'] = df['total_bill']

df.drop("total_bill", axis=1, inplace=True)

df["month"] = pd.to_datetime(df["admit_date"]).dt.month_name()

print(df.head())

df.to_csv("cleaned_hospital_data.csv", index=False)
