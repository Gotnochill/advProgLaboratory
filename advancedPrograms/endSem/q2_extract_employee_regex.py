import re

record = "Name: Ritvik, Email: ritvik@example.com, Emp_id: E123, Phone: 8114615476"

print("Name:", re.search(r"Name:\s*([\w\s]+)", record).group(1))
print("Email:", re.search(r"Email:\s*([\w.-]+@[\w.-]+)", record).group(1))
print("Emp_id:", re.search(r"Emp_id:\s*(\w+)", record).group(1))
print("Phone:", re.search(r"Phone:\s*(\d{10})", record).group(1))
