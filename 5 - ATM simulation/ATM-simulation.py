def ATM_menu(balance):
	while True:
		# show menu
		print("===== ATM Menu =====")
		print("1. Check Balance")
		print("2. Deposit")
		print("3. Withdraw")
		print("4. Exit")
		pass	# (just a placeholder for now)

		#ask for choice
		choice = input("Enter your choice (1-4): ")
		print("You selected", choice)

		if choice == "1":
			print(f"Your balanc is: {balance}")
		elif choice == "2":
			deposit_amount = int(input("Enter amount to deposit: "))
			balance = balance + deposit_amount
			print(f"updated balance: {balance}")
		elif choice == "3":
			withdraw_amount = int(input("Enter amount to withdraw: "))
			if withdraw_amount <= balance:
				balance = balance - withdraw_amount
				print(f"Your withdraw amount is: {withdraw_amount}")
				print(f"Your account balance is: {balance}")
			else:
				print("Insufficient funds!")
		elif choice == "4":
			print("Thank you for using our ATM. Goodbye!")
			break	
		else:
			print("Invalid choice! Please enter 1-4")
	return balance
			
balance = 1000
pin = 1234
enter_pin = int(input("Enter the ATM pin: "))

if enter_pin == pin:
	balance = ATM_menu(balance)	# pass balance into function
	print(f"Final balance after session: {balance}")
else:
	print("Invalid PIN")