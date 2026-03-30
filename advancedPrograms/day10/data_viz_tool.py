import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import statistics

def generate_chart():
    chart_type = chart_var.get()
    x_data_str = x_entry.get()
    y_data_str = y_entry.get()
    y2_data_str = y2_entry.get()
    
    if not x_data_str or not y_data_str:
        messagebox.showwarning("Input Error", "Please enter data in both X and Y1 fields.")
        return
        
    try:
        # Parse X
        x_data = [x.strip() for x in x_data_str.split(",")]
        # Parse Y1 
        y_data = [float(y.strip()) for y in y_data_str.split(",")]
        
        if len(x_data) != len(y_data):
            messagebox.showerror("Data Error", "X and Y1 must have the same number of elements.")
            return

        # Statistical analysis for Y1
        mean_y = statistics.mean(y_data)
        median_y = statistics.median(y_data)
        try:
            mode_y = statistics.mode(y_data)
        except statistics.StatisticsError:
            mode_y = "N/A"
            
        stats_text = f"Y1 Stats:\nMean: {mean_y:.2f}\nMedian: {median_y:.2f}\nMode: {mode_y}"

        if chart_type in ["Line Graph", "Bar Chart", "2-Line Chart"]:
            plt.figure(figsize=(9, 6))
            
            if chart_type == "Line Graph":
                plt.plot(x_data, y_data, marker='o', linestyle='-', color='b', label='Y1 Data')
            elif chart_type == "Bar Chart":
                plt.bar(x_data, y_data, color='skyblue', label='Y1 Data')
            elif chart_type == "2-Line Chart":
                plt.plot(x_data, y_data, marker='o', linestyle='-', color='b', label='Y1 Data')
                if not y2_data_str:
                    messagebox.showwarning("Input Error", "Please enter data for Y2.")
                    plt.close()
                    return
                y2_data = [float(y.strip()) for y in y2_data_str.split(",")]
                if len(x_data) != len(y2_data):
                    messagebox.showerror("Data Error", "X and Y2 must have the same number of elements.")
                    plt.close()
                    return
                plt.plot(x_data, y2_data, marker='s', linestyle='--', color='r', label='Y2 Data')
                
                # Stats for Y2
                mean_y2 = statistics.mean(y2_data)
                median_y2 = statistics.median(y2_data)
                try:
                    mode_y2 = statistics.mode(y2_data)
                except statistics.StatisticsError:
                    mode_y2 = "N/A"
                stats_text += f"\n\nY2 Stats:\nMean: {mean_y2:.2f}\nMedian: {median_y2:.2f}\nMode: {mode_y2}"
                
            plt.title(f"{chart_type}")
            plt.xlabel("X-Axis (Categories)")
            plt.ylabel("Y-Axis (Values)")
            plt.grid(True, linestyle='--', alpha=0.6)
            plt.legend()
            
            # Place text box with statistics
            plt.gcf().text(0.82, 0.5, stats_text, fontsize=9,
                           verticalalignment='center',
                           bbox=dict(boxstyle="round,pad=0.5", edgecolor="gray", facecolor="#f9f9f9"))
                        
            # Adjust layout to make room for stats box on the right
            plt.subplots_adjust(right=0.78)
            plt.show()
            
        elif chart_type == "Pie Chart":
            labels = x_data
            sizes = y_data
            
            plt.figure(figsize=(9, 6))
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
            plt.axis('equal') 
            plt.title("Pie Chart")
            
            plt.gcf().text(0.82, 0.5, stats_text, fontsize=9,
                           verticalalignment='center',
                           bbox=dict(boxstyle="round,pad=0.5", edgecolor="gray", facecolor="#f9f9f9"))
                        
            plt.subplots_adjust(right=0.78)
            plt.show()

    except ValueError:
        messagebox.showerror("Format Error", "Please ensure the Y Data contain valid numbers separated by commas.")

# Create the main window
root = tk.Tk()
root.title("Advanced Data Visualization Tool")
root.geometry("520x450")
root.configure(padx=20, pady=20)

# Title Label
title_label = tk.Label(root, text="Data Visualization & Stats Tool", font=("Helvetica", 16, "bold"))
title_label.pack(pady=(0, 15))

# Chart Type Selection
tk.Label(root, text="1. Select Chart Type:", font=("Helvetica", 10, "bold")).pack(anchor="w")
chart_var = tk.StringVar(value="Line Graph")
choices = ["Line Graph", "Bar Chart", "Pie Chart", "2-Line Chart"]

frame_choices = tk.Frame(root)
frame_choices.pack(fill="x", pady=5)
for choice in choices:
    tk.Radiobutton(frame_choices, text=choice, variable=chart_var, value=choice).pack(side="left", padx=5)

# X Data
tk.Label(root, text="2. Enter X Data / Labels (comma-separated):", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(10, 0))
x_entry = tk.Entry(root, width=60)
x_entry.pack(pady=5)
x_entry.insert(0, "A, B, C, D, E")

# Y Data
tk.Label(root, text="3. Enter Y Data / Values (comma-separated):", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(10, 0))
y_entry = tk.Entry(root, width=60)
y_entry.pack(pady=5)
y_entry.insert(0, "10, 25, 15, 30, 20")

# Y2 Data
tk.Label(root, text="4. Enter Y2 Data (For 2-Line Chart):", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(10, 0))
y2_entry = tk.Entry(root, width=60)
y2_entry.pack(pady=5)
y2_entry.insert(0, "15, 20, 10, 40, 25")

# Run Button
run_btn = tk.Button(root, text="Generate Chart", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", command=generate_chart)
run_btn.pack(pady=20)

root.mainloop()
