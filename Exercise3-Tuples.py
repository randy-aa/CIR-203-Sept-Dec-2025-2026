laptop = ("Dell XPS 13", 2022, "Intel i7", 16)

print("Year:", laptop[1], "RAM (GB):", laptop[3])

laptop_list = list(laptop)
laptop_list[3] = 32
laptop = tuple(laptop_list)

laptops = (
    ("MacBook Air", 2020, "M1", 8),
    ("Lenovo ThinkPad", 2021, "Intel i5", 16),
    ("HP Spectre", 2022, "Intel i7", 16),
    ("Asus ZenBook", 2023, "AMD Ryzen 7", 32),
    ("Acer Swift", 2021, "Intel i3", 8)
)

models = [l[0] for l in laptops]
print("Updated laptop:", laptop)
print("All models:", models)
