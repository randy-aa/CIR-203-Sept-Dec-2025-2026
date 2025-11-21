patient = ("John Doe", 45, "120/80", 72)

print("Age:", patient[1], "Heart Rate:", patient[3])

patient_list = list(patient)
patient_list[3] = 75
patient = tuple(patient_list)

patients = (
    ("Alice", 30, "110/70", 68),
    ("Bob", 55, "130/85", 80),
    ("Carol", 40, "125/82", 76),
    ("David", 65, "140/90", 72),
    ("Eve", 50, "118/78", 70)
)

names = [p[0] for p in patients]
print("Updated patient:", patient)
print("All names:", names)
