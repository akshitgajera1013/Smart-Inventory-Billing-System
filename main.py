from customers import Customers
from products import Products
from sales import Sales

import time




def main_menu():
    while True:
        print("1. Customer Mangment ")
        print("2. Product Mangment ")
        print("3. Sales Mangment ")
        print("0. Exit Application")
    
        choice=int(input("Enter Your Choice : "))

        if choice == 1:
            Customers().customer_menu()
        elif choice == 2:
            Products().product_menu()
        elif choice == 3:
            Sales().sales_menu()
        elif choice == 0:
            print(">>>>>>>> Exiting Application.....")
            time.sleep(1)
            break
        else:
            print("Invalid Choice! Try Again....")



if __name__ == "__main__":
    main_menu()