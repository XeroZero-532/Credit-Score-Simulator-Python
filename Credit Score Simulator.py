debts = {}

def add_debt():de
name = input("Enter the name of the debt (e.g., Credit Card, Loan): ")
amount = float(input("Enter the amount owed: "))
interest_rate = float(input("Enter the interest rate (as a percentage): "))
min_payment = float(input("Enter the minimum payment: "))
debts[name] = {
    "amount": amount,
    "interest_rate": interest_rate,
    "min_payment": min_payment
}
print(f"Debt added: {name} - ${amount} at {interest_rate}% interest, minimum payment ${min_payment}")

def make_payment(): 
    name = input("Enter the name of the debt you want to pay off: ")
    if name in debts:
        payment= float(input("enter the payment amount: "))
        debts[name]["amount"] -= payment
        print(f"Payment of ${payment} made to {name}. New balance: ${debts[name]['amount']}")
    else:
        print("Debt not found")

def calculate_credit_score():
    total_debt = sum(debt["amount"] for debt in debt.values())
    on_time_paymnts = sum(1 for debt in debts.values() if debt["amount"] <= debt["min_payment"])
    credit_score = 800 - (total_debt / 100) + (on_time_paymnts * 5)
    print(f"Estimated credit score: {int(credit_score)}")

def main():
    while True:
        print("/n--- Credit Score Simulator ---")
        print("1. Add a new debt")
        print("2. Make a payment")
        print("3. Calculate credit score")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_debt()
        elif choice == "2":
            make_payment
        elif choice == "3":
            calculate_credit_score
        elif choice == "4":
            print("exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()