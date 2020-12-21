fruits = [
    {
        "item": "apple",
        "quantity": 5,
        "price": 0.95
    },
    {
        "item": "orange",
        "quantity": 7,
        "price": 0.99
    }
]
total_spent = 0
quantity_of_items = 0
for fruit in fruits:
    total_spent += fruit["quantity"] * fruit["price"]
    quantity_of_items += fruit["quantity"]

average_per_item = total_spent / quantity_of_items
print("After purchasing a combination of", quantity_of_items, "apples and oranges, the average cost per item is", average_per_item)

   