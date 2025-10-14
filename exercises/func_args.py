def create_order(customer_name, table_number, *items, service_charge=0.1, **extras):
    print(f"Customer name: {customer_name}")
    print(f"Table number: {table_number}")

    for num, item in enumerate(items, start=1):
        print(f"{num}. {item}")

    subtotal = len(items) * 10  # assume $10 per item
    total = subtotal + (subtotal * service_charge)  # add service charge

    for key, value in extras.items():
        if key == "tip":
            total += value
        elif key == "coupon":
            total -= total * value / 100
        else:
            raise ValueError(f"Invalid keyword: {key}")

    print("--- Final bill ---")
    print(f"Total = {total}\n")

create_order("Ilia", 12, "pizza", "salad", tip=5)
create_order("Ilia", 12, "salad", "pizza", service_charge=0.2, tip=5)
create_order("Ilia", 12, "pizza", "salad", "cezar", "rocks", tip=5)
