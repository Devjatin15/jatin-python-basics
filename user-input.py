name = input("what is your name?:")
print(f"Hello {name}") # This is called an f-string, it allows us to embed expressions inside string literals, using curly braces {}.


item = input("what item would you like to buy?: ")
price = float(input("what is the price?: "))
quantity = int(input("how many do you want?: "))
total = price * quantity

print(f"you have bought {quantity} {item}")
print(f"the total price is {total}")