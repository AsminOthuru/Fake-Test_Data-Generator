import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from faker import Faker
import csv
import json

# Initialize Faker
fake = Faker()

# Available fake data fields categorized
AVAILABLE_FIELDS = {
    "General": {
        "Full Name": "name",
        "Email Address": "email",
        "Phone Number": "phone_number",
        "Job Title": "job",
        "Company Name": "company",
        "Street Address": "address",
        "City": "city",
        "State": "state",
        "Country": "country",
        "Postal Code": "postcode",
        "Date of Birth": "date_of_birth",
        "Random Text": "text",
    },
    "Finance": {
        "Credit Card Number": "credit_card_number",
        "Credit Card Expiry": "credit_card_expire",
        "IBAN": "iban",
        "Bank Name": "bank_country",
        "Bitcoin Address": "cryptocurrency_address",
    },
    "Healthcare": {
        "Blood Type": "blood_group",
        "Medical Condition": "sentence",
        "Insurance Number": "uuid4",
    },
    "E-commerce": {
        "Product Name": "word",
        "Price": "random_number",
        "SKU": "uuid4",
        "Discount Percentage": "random_int",
        "Stock Count": "random_int",
    },
    "Social Media": {
        "Username": "user_name",
        "Hashtag": "word",
        "Website URL": "url",
    },
    "Government": {
        "Passport Number": "uuid4",
        "Driving License": "uuid4",
    }
}

# Store generated data
generated_data = []

# Function to generate fake data
def generate_data():
    try:
        num_records = int(records_entry.get())
        selected_fields = [field_listbox.get(i) for i in field_listbox.curselection()]

        if not selected_fields:
            messagebox.showerror("Error", "Please select at least one field.")
            return

        generated_data.clear()
        table.delete(*table.get_children())

        for _ in range(num_records):
            record = {}
            for category in AVAILABLE_FIELDS.values():
                for field, method in category.items():
                    if field in selected_fields:
                        record[field] = getattr(fake, method)()
            generated_data.append(record)
            table.insert("", "end", values=[record[field] for field in selected_fields])

        messagebox.showinfo("Success", "Data generated successfully!")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number of records.")

# Function to export data
def export_data(file_type):
    if not generated_data:
        messagebox.showerror("Error", "Generate data first.")
        return

    file_ext = "csv" if file_type == "CSV" else "json"
    file_path = filedialog.asksaveasfilename(defaultextension=f".{file_ext}", filetypes=[(f"{file_type} Files", f"*.{file_ext}")])

    if not file_path:
        return

    try:
        if file_type == "CSV":
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(generated_data[0].keys())
                for row in generated_data:
                    writer.writerow(row.values())
        else:
            with open(file_path, "w") as file:
                json.dump(generated_data, file, indent=4)

        messagebox.showinfo("Success", f"Data exported as {file_ext.upper()} successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {e}")

# UI Setup
root = tk.Tk()
root.title("Fake Data Generator")
root.geometry("1000x700")
root.configure(bg="#f5f5f5")

# Title
title_label = tk.Label(root, text="✨ Fake Data Generator ✨", font=("Arial", 20, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

# Records Input
records_frame = tk.Frame(root, bg="#f5f5f5")
records_frame.pack(pady=10)
records_label = tk.Label(records_frame, text="Number of Records:", bg="#f5f5f5", font=("Arial", 12))
records_label.pack(side="left", padx=5)
records_entry = tk.Entry(records_frame, width=10, font=("Arial", 12))
records_entry.pack(side="left", padx=5)

# Field Selection
field_frame = tk.Frame(root, bg="#f5f5f5")
field_frame.pack(pady=10)
field_label = tk.Label(field_frame, text="Select Fields:", bg="#f5f5f5", font=("Arial", 12))
field_label.pack()

field_listbox = tk.Listbox(field_frame, selectmode="multiple", height=15, width=50, font=("Arial", 12))
for category, fields in AVAILABLE_FIELDS.items():
    field_listbox.insert(tk.END, f"--- {category} ---")
    for field in fields.keys():
        field_listbox.insert(tk.END, field)
field_listbox.pack()

# Generate Button
generate_button = tk.Button(root, text="Generate Data", bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), command=generate_data)
generate_button.pack(pady=10)

# Table for Preview
table_frame = tk.Frame(root)
table_frame.pack(pady=10, fill="both", expand=True)

table = ttk.Treeview(table_frame, columns=["Column"], show="headings")
table.pack(fill="both", expand=True)

# Export Buttons
export_frame = tk.Frame(root, bg="#f5f5f5")
export_frame.pack(pady=10)
csv_button = tk.Button(export_frame, text="Export to CSV", bg="#2196F3", fg="white", font=("Arial", 14, "bold"), command=lambda: export_data("CSV"))
csv_button.pack(side="left", padx=10)
json_button = tk.Button(export_frame, text="Export to JSON", bg="#FF9800", fg="white", font=("Arial", 14, "bold"), command=lambda: export_data("JSON"))
json_button.pack(side="left", padx=10)

# Run Application
root.mainloop()
