import numpy as np 
sales_data = np.array([
    [450, 520, 480, 500],
    [600, 580, 620, 610],
    [700, 750, 720, 740],
    [300, 350, 320, 310],
    [800, 820, 780, 810]
])

store_totals = sales_data.sum(axis=1)

top_store = np.argmax(store_totals) + 1  
overall_avg = sales_data.mean()

reshaped_sales = sales_data.reshape(2, 10)

print("Sales Data:\n", sales_data)
print("Total per store:", store_totals)
print("Top performing store:", top_store)
print("Overall average sales:", round(overall_avg, 2))
print("Reshaped (2x10):\n", reshaped_sales)
