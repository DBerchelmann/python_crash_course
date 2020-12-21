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

fruits[0]
fruits[0]["quantity"]


total_spent_on_apples = fruits[0]["quantity"] * fruits[0]["price"]
print("The total spent on apples is", total_spent_on_apples)

total_quantity = 0
for fruit in fruits:
    total_quantity = fruit["quantity"]

total_quantity = fruits[0]["quantity"] + fruits[1]["quantity"]

print(total_quantity)

   

shopping_cart = {
    "tax": .08,
    "items": [
        {
            "title": "orange juice",
            "price": 3.99,
            "quantity": 1
        },
        {
            "title": "rice",
            "price": 1.99,
            "quantity": 3
        },
        {
            "title": "beans",
            "price": 0.99,
            "quantity": 3
        },
        {
            "title": "chili sauce",
            "price": 2.99,
            "quantity": 1
        },
        {
            "title": "chocolate",
            "price": 0.75,
            "quantity": 9
        }
    ]
}





total_spent = 0
quantity_of_items = 0

for item in shopping_cart['items']:
    total_spent += item["quantity"] * item["price"]
    quantity_of_items += item["quantity"]

shopping_cart = (total_spent / quantity_of_items)


print(shopping_cart)




total_quantity_shopping = (shopping_cart['items'][0]['quantity'] + shopping_cart['items'][1]['quantity'] + shopping_cart['items'][2]['quantity'] +
                            shopping_cart['items'][3]['quantity']  + shopping_cart['items'][4]['quantity'])

print(total_quantity_shopping)

#total_quantity_shopping = 0

#for item in shopping_cart['items']:
#total_quantity_shopping = ['items']['quantity']

#print((shopping_cart['items'][0]["price"] * shopping_cart['items'][0]["quantity"]) * shopping_cart['tax'])

#print(shopping_cart['tax'])


#print(shopping_cart['price'] * ['quantity'])

total_spent = 0
quantity_of_items = 0

for item in shopping_cart['items']:
    total_spent +=  item["price"]
    quantity_of_items = len(shopping_cart['items'])

average_per_item = (total_spent / quantity_of_items) 

print(average_per_item)

print(shopping_cart['items'][1])

#shopping_cart['items']["price"] * shopping_cart['items']["quantity"] 

