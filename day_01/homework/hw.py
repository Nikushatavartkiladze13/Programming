#მომხმარებელს შეაყვანინე სახელი, გვარი და ასაკი. სახელი და გვარი გაასუფთავე strip() ფუნქციით.გამოიყენე title(), რათა სახელისა და გვარის პირველი ასოები დიდი იყოს. ასაკი გადააქციე მთელ რიცხვად int() ფუნქციით. ეკრანზე გამოიტანე ყველა ინფორმაცია მოწესრიგებულად.

user_fullname = input("enter your First name and Last name: ").title().strip()
user_age = int(input("enter your age: "))

print(f"Hello {user_fullname}, you are {user_age} years old")