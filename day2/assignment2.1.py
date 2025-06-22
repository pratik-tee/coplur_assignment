price=[]
item=[]
while True:
  print('''
    1. Create Bill
    2. Display Item Price and total bill amount
    3. Display Total
    4. Exit
    ''')
  choice=int(input("Enter choice:"))
  if choice==1:
    m=int(input("Enter total item:"))
    i=0
    while i<=m:
        dish_name=input("Enter dish:")
        dish_price=int(input("Enter price:"))
        item.append(dish_name)
        price.append(dish_price)
        i=i+1
        print("successfully added")

  elif choice==2:
        print("Display bill")
        j=0
        while j<=m:
            print("Item name=",item[j],"Item price=",price[j])
            j=j+1
        print("Total bill amount=",sum(price))
  elif choice==3:
    print("Displaying total bill")
    print("Total bill amount=",sum(price))
  elif choice==4:
    print('Exiting from program successfully')
    break
  else:
    print('wrong choices')