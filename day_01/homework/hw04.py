#მომხმარებელს შეაყვანინე საათობრივი ანაზღაურება და ნამუშევარი საათების რაოდენობა.გამოთვალე ერთი კვირის ხელფასი.გამოთვალე ერთი თვის სავარაუდო ხელფასი (4 კვირის გათვალისწინებით).ყველა ინფორმაცია გამოიტანე ეკრანზე.

Hourly_pay = int(input("enter your hourly pay: "))
number_hours = int(input("enter your Number of hours: "))
week_salary = Hourly_pay * number_hours
print(f"your month salary {week_salary * 4}")