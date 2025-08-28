name = input("What are you name ---> ")
fare = eval(input("How much is fare fee  ---> "))
student_ID = input("Are you currently a student (yes / no) ")

if student_ID.lower() == "yes":
            discount = fare * 0.2
            new_fare = fare - discount
            print("Hi", name, "Your discount is", discount, "Your new fare is", new_fare)
else:
            print("Hi", name, "you're only eligible for regular price:", fare)