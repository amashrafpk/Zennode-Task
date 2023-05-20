# Catalog of products with prices
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount rules
discount_rules = {
    "flat_10_discount": {"threshold": 200, "discount": 10},
    "bulk_5_discount": {"threshold": 10, "discount": 0.05},
    "bulk_10_discount": {"threshold": 20, "discount": 0.1},
    "tiered_50_discount": {"quantity_threshold": 30, "single_product_threshold": 15, "discount": 0.5}
}

# Constants for fees
GIFT_WRAP_FEE = 1
SHIPPING_UNIT_LIMIT = 10
SHIPPING_FEE_PER_PACKAGE = 5

# Function to calculate discount
def calculate_discount(cart):
    applicable_discounts = []
    for rule in discount_rules:
        if rule == "flat_10_discount" and cart["subtotal"] > discount_rules[rule]["threshold"]:
            applicable_discounts.append((rule, discount_rules[rule]["discount"]))
        elif rule == "bulk_5_discount":
            for product in cart["products"]:
                if cart["products"][product]["quantity"] > discount_rules[rule]["threshold"]:
                    applicable_discounts.append((rule, discount_rules[rule]["discount"]))
                    break
        elif rule == "bulk_10_discount" and cart["total_quantity"] > discount_rules[rule]["threshold"]:
            applicable_discounts.append((rule, discount_rules[rule]["discount"]))
        elif rule == "tiered_50_discount" and cart["total_quantity"] > discount_rules[rule]["quantity_threshold"]:
            for product in cart["products"]:
                if cart["products"][product]["quantity"] > discount_rules[rule]["single_product_threshold"]:
                    applicable_discounts.append((rule, discount_rules[rule]["discount"]))
                    break
    if applicable_discounts:
        applicable_discounts.sort(key=lambda x: x[1], reverse=True)
        return applicable_discounts[0]
    else:
        return None

# Function to calculate the cart details
def calculate_cart():
    cart = {
        "products": {},
        "subtotal": 0,
        "total_quantity": 0,
        "discount_name": "",
        "discount_amount": 0,
        "shipping_fee": 0,
        "gift_wrap_fee": 0,
        "total": 0
    }

    # Input quantity and gift wrap for each product
    for product in catalog:
        quantity = int(input("Enter the quantity of {}:".format(product)))
        gift_wrap = input("Is {} wrapped as a gift? (yes/no):".format(product))

        cart["products"][product] = {
            "quantity": quantity,
            "gift_wrap": gift_wrap.lower() == "yes",
            "total_amount": catalog[product] * quantity
        }

        cart["subtotal"] += cart["products"][product]["total_amount"]
        cart["total_quantity"] += quantity

    # Calculate discount
    discount = calculate_discount(cart)
    if discount:
        cart["discount_name"] = discount[0]
        cart["discount_amount"] = discount[1]

    # Calculate shipping fee
    cart["shipping_fee"] = (cart["total_quantity"] - 1) // SHIPPING_UNIT_LIMIT + 1 * SHIPPING_FEE_PER_PACKAGE

    # Calculate gift wrap fee
    for product in cart["products"]:
        if cart["products"][product]["gift_wrap"]:
            cart["gift_wrap_fee"] += cart["products"][product]["quantity"] * GIFT_WRAP_FEE

    # Calculate total
    cart["total"] = cart["subtotal"] - cart["discount_amount"] + cart["shipping_fee"] + cart["gift_wrap_fee"]

    return cart


