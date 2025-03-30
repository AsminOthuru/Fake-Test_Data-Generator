# **Test Data Generation and Management Tool**  

## **Tech Stack:**  
Python, Faker, Tkinter, MySQL/PostgreSQL (Future Enhancement)  

## **Project Overview**  
This project is a **Fake Data Generator** designed to create realistic test data for **software testing, data analysis, and application development**. The tool enables developers and testers to populate databases, test scripts, and applications with **synthetic but meaningful data**.  

### **The tool supports:**  
✅ **Multiple Domains** — Business, Finance, Healthcare, Social Media, Government, and E-commerce.  
✅ **Various Export Formats** — CSV and JSON.  
✅ **Customizable Fields** — Users can select which data fields they need.  
✅ **Automated Data Generation** — Generates bulk test data with just one click.  

## **Why is Test Data Important?**  
🔹 **Real User Data is Sensitive** — Using real customer or business data for testing can lead to privacy violations.  

🔹 **Manual Data Entry is Time-Consuming** — Manually creating test data takes too long and can introduce human errors.  

🔹 **Scalability & Consistency** — Automated test data generation ensures **scalability and consistency** across multiple test runs, reducing variability in results.  

🔹 **Better Software Testing** — Having diverse and high-quality test data helps in **finding bugs faster** and ensures robust application performance.  

## **Key Features**  
### **📌 Generate Random Test Data**  
Using the **Faker** library, the tool can generate:  
- **General Data** – Names, emails, phone numbers, addresses, job titles.  
- **Finance Data** – Credit card numbers, IBAN, bank names, Bitcoin addresses.  
- **Healthcare Data** – Blood types, medical conditions, insurance numbers.  
- **E-commerce Data** – Product names, prices, stock counts, discount percentages.  
- **Government Data** – Passport numbers, driving license numbers.  
- **Social Media Data** – Usernames, hashtags, website URLs.  

### **📌 Flexible Export Options**  
- **CSV Export** – Easily import data into spreadsheets or databases.  
- **JSON Export** – Useful for software applications, APIs, and test scripts.  

### **📌 User-Friendly Interface**  
- Simple **Tkinter-based GUI** for easy data generation.  
- Users can select fields from multiple categories.  
- Large preview table to **view generated data before exporting**.  

## **How to Run This Tool on Your System**  

### **1️⃣ Install Dependencies**  
Before running the tool, install the required dependencies using the following command:  
pip install faker tkinter

### **2️⃣ Download the Python Script**  
Save the provided Python script (e.g., `test_data_generator.py`) on your local machine.  

### **3️⃣ Run the Application**  
Open a terminal or command prompt and navigate to the folder where the script is saved. Then run:  
python test_data_generator.py

### **4️⃣ Use the GUI to Generate Data**
✔ Enter the number of records to generate.
✔ Select the desired fields from multiple domains.
✔ Click "Generate Data" to create test data.
✔ Export data in CSV or JSON format for further use.

## **Future Enhancements 🚀**
🔹 Direct Database Insertion – Support for MySQL and PostgreSQL integration.
🔹 More Data Categories – Expanding fields for AI, cybersecurity, and logistics.
🔹 User-Defined Custom Fields – Allow users to define their own test data templates.
