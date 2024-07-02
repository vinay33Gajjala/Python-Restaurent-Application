from typing import List

class PurchaseItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

def get_total_order_amount(order: List[PurchaseItem]) -> float:
    
    total_amount = sum(item.price for item in order)
    return total_amount

def get_service_charge(order: List[PurchaseItem]) -> float:
    
    total_amount = get_total_order_amount(order)
    service_charge_rate = 0.01  
    max_service_charge_rate = 0.20 

    service_charge = min(total_amount * service_charge_rate, total_amount * max_service_charge_rate)
    return service_charge

# McDonald's menu with price
MCDONALDS_MENU = [
    PurchaseItem("Veg Burger", 115.00),
    PurchaseItem("Veg Wrap", 130.00),
    PurchaseItem("Veg Happy Meal", 215.00),
    PurchaseItem("Chicken Burger", 175.00),
    PurchaseItem("Chicken Wrap", 195.00),
    PurchaseItem("Sprite (M)", 115.00),
    PurchaseItem("Sprite (L)", 130.00),
    PurchaseItem("Mango Smoothie", 215.00),
    PurchaseItem("Chocolate Smoothie", 175.00),
    PurchaseItem("Chocolate Smoothie w/ Icecream", 195.00),
]

def print_menu():
    
    print("\nMcDonald's Menu:")
    for i, item in enumerate(MCDONALDS_MENU, start=1):
        print(f"{i}. {item.name} - Rs. {item.price:.2f}")

def print_order_details(order: List[PurchaseItem]):
    
    total_amount = get_total_order_amount(order)
    service_charge = get_service_charge(order)
    final_amount = total_amount + service_charge

    print("\nFinal Order:")
    for i, item in enumerate(order, start=1):
        print(f"{i}. {item.name} - Rs. {item.price:.2f}")

    print(f"\nOrder Amount: Rs. {total_amount:.2f}")
    print(f"Service Charge: Rs. {service_charge:.2f}")
    print(f"Final Amount: Rs. {final_amount:.2f}")

def main():
    order = []
    while True:
        print_menu()
        choice = input("Enter item number to add to your order (or 'done' to finish): ")

        if choice.lower() == 'done':
            break
        
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(MCDONALDS_MENU):
                order.append(MCDONALDS_MENU[choice_idx])
                print(f"{MCDONALDS_MENU[choice_idx].name} added to your order.")
            else:
                print("Invalid choice! Please enter a valid item number.")
        except ValueError:
            print("Invalid input! Please enter a valid item number.")

    print_order_details(order)

if __name__ == "__main__":
    main()
