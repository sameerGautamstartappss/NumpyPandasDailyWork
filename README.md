## 📊 Data Used

The dataset (`students.csv`) contains sample student records:

- **Name**: Student's name  
- **Age**: Student's age  
- **Math, Science, English**: Subject scores  
- **City**: City of residence  

---

## 🧠 Learning Steps

### Step 0: Create CSV File
📄 File: `script.py`

- Creates a Python dictionary with sample student data
- Converts it into a DataFrame
- Saves it as `students.csv`

---

### Step 1: Read CSV File
📄 File: `step1_read_csv.py`

- Uses `pd.read_csv()` to load the CSV
- Stores it in a DataFrame for further processing

---

### Step 2: Explore the Data
📄 File: `step2_explore_data.py`

- Displays the first 5 rows using `df.head()`
- Prints DataFrame info using `df.info()`
- Shows basic statistics with `df.describe()`

---

## 🚀 Next Steps (Suggestions)

- Step 3: Filtering and selecting specific data
- Step 4: Grouping and aggregation
- Step 5: Adding calculated columns
- Step 6: Sorting and exporting

---

## 📦 Requirements

- Python 3.x
- pandas library

To install pandas:
```bash
pip install pandas
