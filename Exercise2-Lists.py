routes = ["Nairobi-Mombasa", "Kisumu-Nakuru", "Nanyuki-Meru", "Nairobi-Kisumu",
          "Mombasa-Malindi", "Nakuru-Eldoret", "Nyeri-Nairobi", "Garissa-Wajir",
          "Isiolo-Marsabit", "Lamu-Mombasa"]

routes.append("Thika-Nairobi")
routes.remove("Lamu-Mombasa")

routes.sort()
routes.reverse()

count_N = sum(1 for r in routes if r.startswith("N"))

long_routes = [r for r in routes if len(r) > 10]

print("Routes:", routes)
print("Count starting with N:", count_N)
print("Routes longer than 10 chars:", long_routes)
