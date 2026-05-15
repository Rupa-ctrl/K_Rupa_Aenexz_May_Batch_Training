# Shopping Cart Program


# ---------- Part A : Mutable Default Argument Demo ----------

def add_item(item, cart=[]):
    cart.append(item)
    return cart


print("Mutable Default Argument Bug")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", ["bread"]))
print(add_item("eggs"))


# ---------- Part B : Correct Version ----------

def safe_add_item(item, cart=None):

    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("\nCorrect Function")
print(safe_add_item("pen"))
print(safe_add_item("book"))


# ---------- Part C : Shopping Cart System ----------

# Create cart
def create_cart(owner, discount=0):

    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


# Add products
def add_to_cart(cart, name, price, qty=1):

    product = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(product)


# Update tuple price
def update_price(price_tuple, new_price):

    # Tuples are immutable
    # So we create a NEW tuple instead of modifying
    return (price_tuple[0], new_price)


# Calculate total
def calculate_total(cart):

    total = 0

    for item in cart["items"]:

        subtotal = item["price"] * item["qty"]
        total += subtotal

    final_total = total - (total * cart["discount"] / 100)

    return final_total


# ---------- Customer 1 ----------

cart1 = create_cart("Manohar", 10)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 800, 2)


# ---------- Customer 2 ----------

cart2 = create_cart("Aarav", 5)

add_to_cart(cart2, "Phone", 20000, 1)
add_to_cart(cart2, "Charger", 1000, 1)


# ---------- Display ----------

print("\nCustomer 1 Cart")
print(cart1)

print("Total:", calculate_total(cart1))


print("\nCustomer 2 Cart")
print(cart2)

print("Total:", calculate_total(cart2))


# ---------- Tuple Demo ----------

price_info = ("Keyboard", 1500)

print("\nOld Tuple:", price_info)

new_price_info = update_price(price_info, 1800)

print("Updated Tuple:", new_price_info)


# ---------- Immutability Check ----------

try:

    price_info[1] = 3000

except TypeError:

    print("\nTuple cannot be modified (Immutable).")