def calculate_subtotal(items):
    subtotal = 0

    for item in items:
        subtotal += item["price"] * item["quantity"]

    return subtotal


def calculate_discount(subtotal):
    if subtotal >= 3000:
        return subtotal * 0.10
    elif subtotal >= 1000:
        return subtotal * 0.05
    else:
        return 0


def calculate_tax(amount, tax_rate):
    return amount * (tax_rate / 100)


def generate_receipt(items, tax_rate):

    # Validate tax rate
    if not 0 <= tax_rate <= 100:
        raise ValueError("Invalid tax rate")

    # Validate products
    for item in items:
        if item["price"] < 0:
            raise ValueError("Price cannot be negative")

        if item["quantity"] < 0:
            raise ValueError("Quantity cannot be negative")

    # Calculate subtotal
    subtotal = calculate_subtotal(items)

    # Calculate discount
    discount = calculate_discount(subtotal)

    # Subtract discount from subtotal
    discounted_amount = subtotal - discount

    # Calculate tax on discounted amount
    tax = calculate_tax(discounted_amount, tax_rate)

    # Calculate final amount
    final_amount = discounted_amount + tax

    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "final_amount": final_amount
    }


# Sample products
items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]

# Tax rate (example: 15%)
tax_rate = 15

# Generate receipt
receipt = generate_receipt(items, tax_rate)

# Display receipt
print("========== SHOPPING RECEIPT ==========")

for item in items:
    print(f'{item["name"]}: {item["price"]} x {item["quantity"]}')

print("--------------------------------------")
print(f'Subtotal:     {receipt["subtotal"]:.2f} Birr')
print(f'Discount:     {receipt["discount"]:.2f} Birr')
print(f'Tax:          {receipt["tax"]:.2f} Birr')
print("--------------------------------------")
print(f'Final Amount: {receipt["final_amount"]:.2f} Birr')
print("======================================")
