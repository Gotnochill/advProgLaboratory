import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

def generate_chart():
    chart_type = chart_var.get()
    x_data_str = x_entry.get()
    y_data_str = y_entry.get()
    
    if not x_data_str or not y_data_str:
        messagebox.showwarning("Input Error", "Please enter data in both fields.")
        return
        
    try:
        if chart_type in ["Line Graph", "Bar Chart"]:
            # Parse x (can be strings/categories) and y (must be numeric)
            x_data = [x.strip() for x in x_data_str.split(",")]
            y_data = [float(y.strip()) for y in y_data_str.split(",")]
            
            if len(x_data) != len(y_data):
                messagebox.showerror("Data Error", "X and Y must have the same number of elements.")
                return
            
            plt.figure(figsize=(6, 4))
            if chart_type == "Line Graph":
                plt.plot(x_data, y_data, marker='o', linestyle='-', color='b')
            elif chart_type == "Bar Chart":
                plt.bar(x_data, y_data, color='skyblue')
                
            plt.title(f"{chart_type}")
            plt.xlabel("X-Axis (Categories)")
            plt.ylabel("Y-Axis (Values)")
            plt.grid(True, linestyle='--', alpha=0.6)
            plt.tight_layout()
            plt.show()
            
        elif chart_type == "Pie Chart":
            # For pie chart, X is labels, Y is values
            labels = [x.strip() for x in x_data_str.split(",")]
            sizes = [float(y.strip()) for y in y_data_str.split(",")]
            
            if len(labels) != len(sizes):
                messagebox.showerror("Data Error", "Labels and values must have the same number of elements.")
                return
                
            plt.figure(figsize=(6, 6))
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
            plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.title("Pie Chart")
            plt.tight_layout()
            plt.show()

    except ValueError:
        messagebox.showerror("Format Error", "Please ensure the Y Data / Values contain valid numbers separated by commas.")

# Create the main window
root = tk.Tk()
root.title("Simple Data Visualization Tool")
root.geometry("450x350")
root.configure(padx=20, pady=20)

# Title Label
title_label = tk.Label(root, text="Data Visualization Tool", font=("Helvetica", 16, "bold"))
title_label.pack(pady=(0, 15))

# Chart Type Selection
tk.Label(root, text="1. Select Chart Type:", font=("Helvetica", 10, "bold")).pack(anchor="w")
chart_var = tk.StringVar(value="Line Graph")
choices = ["Line Graph", "Bar Chart", "Pie Chart"]

frame_choices = tk.Frame(root)
frame_choices.pack(fill="x", pady=5)
for choice in choices:
    tk.Radiobutton(frame_choices, text=choice, variable=chart_var, value=choice).pack(side="left", padx=10)

# X Data
tk.Label(root, text="2. Enter X Data / Labels (comma-separated):", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(10, 0))
x_entry = tk.Entry(root, width=50)
x_entry.pack(pady=5)
x_entry.insert(0, "A, B, C, D, E")

# Y Data
tk.Label(root, text="3. Enter Y Data / Values (comma-separated):", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(10, 0))
y_entry = tk.Entry(root, width=50)
y_entry.pack(pady=5)
y_entry.insert(0, "10, 25, 15, 30, 20")

# Run Button
run_btn = tk.Button(root, text="Generate Chart", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", command=generate_chart)
run_btn.pack(pady=25)

root.mainloop()
