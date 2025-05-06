# Discount calculator

def calculate_discount(price, discount=10):
    final_price = price - (price * discount / 100)
    return final_price
print("Discounted price (default 10%):", calculate_discount(100))
print("Discounted price (20%):", calculate_discount(200, 20))
