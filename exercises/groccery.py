#Grocery Receipt

#Ask for 3 items and their prices.

#Print a receipt with total and average price.

#Format the prices to 2 decimals.



item1 = input("enter the first item: ")
item1_price = float(input("enter the price for item 1 : "))
item2 = input("enter the second item: ")
item2_price = float(input("enter the price for item 2 : "))
item3 = input("enter the third item: ")
item3_price = float(input("enter the price for item 3 : "))


total_cost = float(item1_price) + float(item2_price) + float(item3_price)
avg_price = total_cost / 3

print("-----grocery receipt-------")
print( f"1) {item1} --- price: {round(item1_price,2)}")
print( f"2) {item2} --- price: {round(item2_price,2)}")
print( f"3) {item3} --- price: {round(item3_price,2)}")
print( f"=== average cost : {round(avg_price,2)} ===")
print( f"=== Total cost : {round(total_cost,2)} ===")




