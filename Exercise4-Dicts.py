library = {
    "Data Structures": 20,
    "Machine Learning": 6,
    "Operating Systems": 12,
    "Computer Networks": 18,
    "Cybersecurity": 4
}

library["Artificial Intelligence"] = 9

library["Machine Learning"] = 10

def low_stock(lib):
    return {title:qty for title, qty in lib.items() if qty < 10}

del library["Cybersecurity"]

for title, qty in library.items():
    print(title, ":", qty)

print("Low stock books:", low_stock(library))
