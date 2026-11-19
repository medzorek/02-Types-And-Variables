price = float(input('Enter price: '))
discount = float(input('Enter discount %: '))
discounted_price = price * (1 - discount / 100)
reduction = price - discounted_price
print(f'Price with discount: {discounted_price:.2f}')
print(f'Reduction: {reduction:.2f}')
