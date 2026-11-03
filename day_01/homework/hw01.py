# მომხმარებელს შეაყვანინე დაბადების წელი. გამოთვალე, დაახლოებით რამდენი წლის არის. შედეგი გამოიტანე f-string-ის გამოყენებით.

user_year = int(input("enter your year of birth: "))
now_year = int(input("what year is it now? "))

print(f"you are {now_year - user_year} years old.")