import step1_read_csv as step1

# Step-1: Read the csv file
df = step1.read_csv_file("students.csv")

# Step-2: View first 5 rows
print("First five rows :-")
print(df.head)

# Step-3 Info about DataFrame
print("\nDataFrame Info :-")
print(df.info())

# Step-4 Statitical summary
print("\nStatistical Summary :-")
print(df.describe())




