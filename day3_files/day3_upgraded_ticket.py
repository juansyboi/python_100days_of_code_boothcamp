bill = 0
isContinue = True
total_number_of_cust = 0
cust_num_iti = 1
customer_num = int(input("How many customer to take the ride? "))

while isContinue:

    if customer_num == 0:
        isContinue = False
        print(f"total number of customer {total_number_of_cust} \ntotal bill: {bill}")
    else:
        height_cust = int(input(f"Enter the height of Customer {cust_num_iti}: "))
        if height_cust > 120:
            age_cont = int(input(f"Please, enter the age of customer {cust_num_iti}: "))
            if age_cont < 10:
                ticket_conf = input("The Price is $1 \nDo you want to continue? Press 'y' for Yes and Press 'n' for No\nAnswer: ")
                if ticket_conf == 'y':
                    total_number_of_cust += 1
                    cust_num_iti += 1
                    bill += 1
                    customer_num -= 1
                else:
                    cust_num_iti += 1
                    customer_num -= 1
                    break
            elif age_cont >= 10 and age_cont < 18:
                ticket_conf = input("The Price is $3 \nDo you want to continue? Press 'y' for Yes and Press 'n' for No\nAnswer: ")
                if ticket_conf == 'y':
                    bill += 3
                    total_number_of_cust += 1
                    customer_num -= 1
                    cust_num_iti += 1
                else:
                    cust_num_iti += 1
                    customer_num -= 1
                    break
            elif age_cont >= 18 and age_cont < 60:
                ticket_conf = input("The Price is $5 \nDo you want to continue? Press 'y' for Yes and Press 'n' for No\nAnswer: ")
                if ticket_conf == 'y':
                    bill += 5
                    total_number_of_cust += 1
                    customer_num -= 1
                    cust_num_iti += 1
                else:
                    customer_num -= 1
                    cust_num_iti += 1
                    break
            else:
                ticket_conf = input("The Price is $3.5 \nDo you want to continue? Press 'y' for Yes and Press 'n' for No\nAnswer: ")
                if ticket_conf == 'y':
                    bill += 3.5
                    customer_num -= 1
                    cust_num_iti += 1
                else:
                    customer_num -= 1
                    cust_num_iti += 1
                    break
        else:
            print("You are free to enter!")
            cust_num_iti += 1
            total_number_of_cust += 1
            customer_num -= 1

#"The Price is $3 \nDo you want to continue? Press 'y' for Yes and Press 'n' for No\nAnswer: "