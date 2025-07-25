def market(cart):
    hisob=0
    for i in cart.values():
        hisob+=(int(i['price'])*int(i['quantity']))
    return hisob
cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}
print(market(cart))