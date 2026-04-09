#( Initialize quantities for Super Bazar items)
# Item Database: Easily add or change prices here
items = {
            1: {"name": "Sugar", "price": 45, "unit": "kg"},
            2: {"name": "Rice", "price": 60, "unit": "kg"},
            3: {"name": "Cooking Oil", "price": 120, "unit": "L"},
            4: {"name": "Milk", "price": 55, "unit": "L"}
        }
        cart = {} # Stores {item_id: quantity}
        print("Welcome to Super Bazar!")
        while True:
            print("\n" + "-"*20 + " MENU " + "-"*20)
            for idx, info in items.items():
                print(f"{idx}. {info['name']} ({1}{info['unit']}) - ₹{info['price']}")
            try:
                ch = int(input("\nEnter item number to add (0 to Checkout): "))
                if ch == 0:
                    break
                elif ch in items:
                    qty = int(input(f"Enter quantity for {items[ch]['name']}: "))
                    if qty > 0:
                        cart[ch] = cart.get(ch, 0) + qty
                        print(f"Added {qty}{items[ch]['unit']} {items[ch]['name']}")
                else:
                    print("Item not found. Try again.")
            except ValueError:
                print("Please enter a valid number.")

# Final Bill Generation
# Item Database: Easily add or change prices here

        items = {
            1: {"name": "Sugar", "price": 45, "unit": "kg"},
            2: {"name": "Rice", "price": 60, "unit": "kg"},
            3: {"name": "Cooking Oil", "price": 120, "unit": "L"},
            4: {"name": "Milk", "price": 55, "unit": "L"}
        }

        cart = {} # Stores {item_id: quantity}
        print("Welcome to Super Bazar!")

        while True:
            print("\n" + "-"*20 + " MENU " + "-"*20)
            for idx, info in items.items():
                print(f"{idx}. {info['name']} ({1}{info['unit']}) - ₹{info['price']}")
    
            try:
                ch = int(input("\nEnter item number to add (0 to Checkout): "))
        
                if ch == 0:
                    break
                elif ch in items:
                    qty = int(input(f"Enter quantity for {items[ch]['name']}: "))
                if qty > 0:
                    cart[ch] = cart.get(ch, 0) + qty
                    print(f"Added {qty}{items[ch]['unit']} {items[ch]['name']}")
            else:
                print("Item not found. Try again.")
            
            except ValueError:
                print("Please enter a valid number.")

# Final Bill Generation

        print(f"\n{'='*40}\n{'SUPER BAZAR RECEIPT':^40}\n{'='*40}")
        print(f"{'Item':<15} {'Qty':<10} {'Price':<10} {'Total'}")
        print("-" * 40)

        grand_total = 0
        for item_id, quantity in cart.items():
            details = items[item_id]
            item_total = quantity * details['price']
            grand_total += item_total
            print(f"{details['name']:<15} {quantity:<10} ₹{details['price']:<10} ₹{item_total}")

        print("-" * 40)
        print(f"{'GRAND TOTAL:':<32} ₹{grand_total}")
        print(f"{'='*40}\nThank you for shopping!")
