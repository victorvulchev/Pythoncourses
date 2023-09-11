customers = {
 "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
 "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
}
min_price = 20
min_orders = 5
promo_list = []

for i, j in customers.items():
    counter = 0
    for k in j:
        if k >= min_price:
            counter +=1
    if counter >= min_orders:
        promo_list.append(i)
print(promo_list)