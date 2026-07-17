import customtkinter as ctk
from tkinter import messagebox
import csv
import os
import matplotlib.pyplot as plt

def save_to_csv(name, weight, height, bmi, category):
    try:
        file_name = "bmi_records.csv"
        file_exists = os.path.isfile(file_name)
        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Name", "Weight", "Height", "BMI", "Category"])
            writer.writerow([name, weight, height, bmi, category])
    except IOError as e:
        messagebox.showerror("File Error", f"Could not save data: {e}")

def show_graph():
    name_to_search = entry_name.get()
    if not name_to_search:
        messagebox.showwarning("Warning", "Please enter a name!")
        return
    
    try:
        bmi_values = []
        with open("bmi_records.csv", mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'].strip().lower() == name_to_search.strip().lower():
                    bmi_values.append(float(row['BMI']))
        
        if bmi_values:
            plt.figure(figsize=(6, 4))
            plt.plot(bmi_values, marker='o', linestyle='-', color='#3B8ED0')
            plt.title(f"BMI Trend: {name_to_search}")
            plt.xlabel("Attempts")
            plt.ylabel("BMI")
            plt.grid(True)
            plt.show()
        else:
            messagebox.showinfo("Info", "No history found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read data: {e}")


def calculate_bmi():
    try:
        w = float(entry_weight.get())
        h = float(entry_height.get()) / 100
        n = entry_name.get().strip()

        if w <= 0 or h <= 0:
            messagebox.showerror("Error", "Enter positive values!")
            return

        bmi = round(w / (h ** 2), 2)
        
        if bmi < 18.5: cat, col, desc = "Underweight", "#3B8ED0", "Below 18.5"
        elif 18.5 <= bmi <= 24.9: cat, col, desc = "Healthy", "#2CC985", "Between 18.5 - 24.9"
        elif 25 <= bmi <= 29.9: cat, col, desc = "Overweight", "#E07A5F", "Between 25 - 29.9"
        else: cat, col, desc = "Obese", "#D35460", "Above 30"

        save_to_csv(n, w, h*100, bmi, cat)
        
        lbl_bmi_value.configure(text=str(bmi), text_color=col)
        lbl_category.configure(text=cat, fg_color=col)
        lbl_desc.configure(text=f"Your BMI is in the {cat} range.\nA BMI of {bmi} falls in the {cat.lower()} category.")

    except ValueError:
        messagebox.showerror("Error", "Enter valid numeric values!")
ctk.set_appearance_mode("Light")  
ctk.set_default_color_theme("blue") 

app = ctk.CTk()
app.title("BMI Calculator Pro")
app.geometry("400x600")

main_frame = ctk.CTkFrame(app, corner_radius=20)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Title
ctk.CTkLabel(main_frame, text="BMI Tracker", font=("Roboto Medium", 24)).pack(pady=20)

input_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
input_frame.pack(pady=10, padx=20)

# Name
ctk.CTkLabel(input_frame, text="Name:").grid(row=0, column=0, padx=10, pady=10)
entry_name = ctk.CTkEntry(input_frame, placeholder_text="Enter your name")
entry_name.grid(row=0, column=1, padx=10, pady=10)

# Weight
ctk.CTkLabel(input_frame, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=10)
entry_weight = ctk.CTkEntry(input_frame, placeholder_text="e.g. 70")
entry_weight.grid(row=1, column=1, padx=10, pady=10)

# Height
ctk.CTkLabel(input_frame, text="Height (cm):").grid(row=2, column=0, padx=10, pady=10)
entry_height = ctk.CTkEntry(input_frame, placeholder_text="e.g. 175")
entry_height.grid(row=2, column=1, padx=10, pady=10)

# Calculate Button
btn_calc = ctk.CTkButton(main_frame, text="Calculate BMI", command=calculate_bmi, corner_radius=20, height=40)
btn_calc.pack(pady=20)

result_frame = ctk.CTkFrame(main_frame, fg_color="#f0f0f0", corner_radius=15)
result_frame.pack(pady=10, padx=20, fill="x")

result_header = ctk.CTkFrame(result_frame, fg_color="transparent")
result_header.pack(pady=(10, 5), padx=10)

lbl_bmi_value = ctk.CTkLabel(result_header, text="--", font=("Roboto Bold", 32))
lbl_bmi_value.pack(side="left", padx=5)

lbl_category = ctk.CTkLabel(result_header, text="Result", font=("Roboto Medium", 12), text_color="white", corner_radius=5, padx=5)
lbl_category.pack(side="left", padx=5)

lbl_desc = ctk.CTkLabel(result_frame, text="Enter details to calculate BMI.", font=("Roboto", 10), text_color="gray", wraplength=300)
lbl_desc.pack(pady=5, padx=10)

btn_graph = ctk.CTkButton(main_frame, text="Show History Graph", command=show_graph, fg_color="transparent", text_color="gray", hover_color="#e0e0e0")
btn_graph.pack(pady=10)

app.mainloop()
