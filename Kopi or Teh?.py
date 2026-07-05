drink = '' #empty string
#select drink type
choice = input('Do you want Kopi (1) or Teh (2)? Select:')
if choice == '1':
    drink = drink + ' Kopi'
elif choice == '2':
    drink = drink + ' Teh'
else:
    print("Not a choice- press 1 or 2.")
#select milk
choice = input("Do you want milk(1) or no milk(2)? Select:")
if choice == '1':
    choice = input("Condensed milk(1) or Evaporated milk(2)? Select:")
    if choice == '1':
        drink = drink
    elif choice == '2':
        drink = drink + ' -C'
    else:
        print("Not a choice- press 1 or 2.")
elif choice == '2':
    drink = drink + ' -O'
else:
    print("Not a choice,- select 1 or 2.")
#select sugar
choice = input("Do you want sugar(1) or no sugar(2)? Select:")
if choice == '1':
    choice = input('Do you want less sweetness(1), Normal sweetness(2) or more sweetness(3)? Select:')
    if choice == '1':
        drink = drink + ' Siew Dai'
    elif choice == '2':
        drink = drink 
    elif choice == '3':
        drink = drink + " Gah Dai"
    else:
        print("Not a option- choose (1), (2) or (3)")
elif choice == '2':
    drink = drink + ' Kosong'
#print out order
print('Your order is' + drink)
