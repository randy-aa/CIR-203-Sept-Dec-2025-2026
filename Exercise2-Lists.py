cs_books = ["Introduction to Algorithms", "Clean Code", "Artificial Intelligence: A Modern Approach",
            "Design Patterns", "Structure and Interpretation of Computer Programs",
            "Operating System Concepts", "Computer Networks", "Programming Pearls",
            "The Pragmatic Programmer", "Code Complete"]

cs_books.append("Database System Concepts")

cs_books.remove("Programming Pearls")

cs_books.sort()
cs_books.reverse()

count_C = sum(1 for b in cs_books if b.startswith("C"))

long_titles = [b for b in cs_books if len(b) > 20]

print("Computer Science Books:", cs_books)
print("Count starting with C:", count_C)
print("Titles longer than 20 chars:", long_titles)
