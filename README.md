# Cafe-and-Grocery(shop)-Program
# 1.
    <br>
    ct,cc,cp=0,0,0
    while True:
    ch=int(input("enter your choice\n1.tea\n2.coffee\n3.pizza"))
    match(ch):
    case 1:
      print("tea selected")
      ct+=1
    case 2:
      print("coffee selected")
      cc+=1
    case 3:
      print("pizza selected")
      cp+=1
    case _:
      total=(ct*10)+(cc*20)+(cp*100)
      print("welcome to the dolly ki tapri")
      print("-------------------------------")
      print("Items\t\tCount\t\tAmount")
      print("-------------------------------")
      print(f"Tea\t\t{ct}\t\t{ct*10}")
      print(f"Coffee\t\t{cc}\t\t{cc*20}")
      print(f"pizza\t\t{cp}\t\t{cp*100}")
      print("-----------------------------------")
      print(f"Total\t\t{ct+cc+cp}\t\t{total}")
      print("visit again!thank you")
      break
    <br>
# 2.( Initialize quantities for Super Bazar items)
    <br>
    sugar_q, rice_q, oil_q, milk_q = 0, 0, 0, 0

    print("Welcome to Super Bazar!")
    print("Enter the item number to add to your cart. Enter 0 or any other number to checkout.")

    while True:
    try:
        print("\n1. Sugar (1kg) - ₹45\n2. Rice (1kg) - ₹60\n3. Cooking Oil (1L) - ₹120\n4. Milk (1L) - ₹55")
        ch = int(input("Enter your choice: "))
        
        match(ch):
            case 1:
                qty = int(input("Enter quantity for Sugar: "))
                sugar_q += qty
                print(f"Added {qty}kg Sugar")
            case 2:
                qty = int(input("Enter quantity for Rice: "))
                rice_q += qty
                print(f"Added {qty}kg Rice")
            case 3:
                qty = int(input("Enter quantity for Oil: "))
                oil_q += qty
                print(f"Added {qty}L Oil")
            case 4:
                qty = int(input("Enter quantity for Milk: "))
                milk_q += qty
                print(f"Added {qty}L Milk")
            case _:
                # Calculate totals
                total_sugar = sugar_q * 45
                total_rice = rice_q * 60
                total_oil = oil_q * 120
                total_milk = milk_q * 55
                grand_total = total_sugar + total_rice + total_oil + total_milk
                
                # Generate Final Bill
                print("\n" + "="*35)
                print("         SUPER BAZAR RECEIPT")
                print("="*35)
                print("Items\t\tQty\tAmount")
                print("-" * 35)
                if sugar_q > 0: print(f"Sugar\t\t{sugar_q}\t₹{total_sugar}")
                if rice_q > 0:  print(f"Rice\t\t{rice_q}\t₹{total_rice}")
                if oil_q > 0:   print(f"Oil\t\t{oil_q}\t₹{total_oil}")
                if milk_q > 0:  print(f"Milk\t\t{milk_q}\t₹{total_milk}")
                print("-" * 35)
                print(f"TOTAL AMOUNT:\t\t₹{grand_total}")
                print("="*35)
                print("Thank you for shopping! Visit again.")
                break
    except ValueError:
        print("Invalid input. Please enter a number.")
    <br>
