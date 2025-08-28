
name = input("Please enter your name: ")
fare = eval(input("Please enter your fare fee: "))
print("Invalid input. Please enter a valid number for the fare fee.")


student = input("Are you a student? (yes/no): ").lower()

if student not in ['yes', 'no']:
    print("Invalid input. Please answer 'yes' or 'no'.")

if student == 'yes':
    discount = fare * 0.2
    discounted_fare = fare - discount
    print(f"Hello {name}!")
    print("Hi", name, "Your discount is", discount, "Your new fare is", fare)
else:
    print(f"Hello {name}!")
    print("Hi", name, "you're only eligible for regular price:", fare)
