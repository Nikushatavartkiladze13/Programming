#მომხმარებელს შეაყვანინე სახელი და გვარი ერთ ხაზზე.გამოიყენე strip() და title().გამოიყენე split(), რათა სახელი და გვარი ცალ-ცალკე მიიღო.ეკრანზე გამოიტანე სახელი და გვარი ცალ-ცალკე.

full_name = input("enter your first name and last name: ").strip().title()
first, last = full_name.split()
print(f"enter your first name is {first}.")
print(f"enter your last name is {last}.")