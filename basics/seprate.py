def helper(list):
    formatted_items = []
    for item in list:
        formatted_items.append(f"{item[0]} → {item[1]}")

    return formatted_items
