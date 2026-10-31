# print(*objects,) ეს ნიშნავს რომ ჩვენ შეგვიძლია print ფუნქციას გადავცეთ იმდენი არგუმენტი რამდენიც ჩვენ გვინდა .
name = input("enter your name: ")
print("Hello", name, "how are you doing?") # ჩვენ შეგვიძლია ამ კოდიდან ამოვიღოთ კონკატენაცია(+) და ჩავანაცვლოთ "," 

# print(*objects, sep=' ') პრინტს აქვს ასევე sep(separator) დასახელებული არგუმენტი, რომელშიც ვხედავთ რომ დეფაულთ მნიშვნელობა აქვს მას სფეის. ზუსტად ამიტომ მუშაობდა მესამე ხაზის კოდში print("Hello", name, "how are you doing?") და ავტომატურად სვამდა მძიმეებს არგუმენტებს შორის.
# ჩვენ პროგრამისტებს გვაქვს იმის საშუალება რომ ვნახოთ დასახელებულია არგუმენტების მნიშვნელობები და შევცვალოთ ისინი მაგ: 
print("Hello", name, "how are your doing?", sep="-")
# Hello Nika how are you doing? - მესამე ხაზის კოდის შედეგი სადაც სეპარატოს დეფაულთ მნიშვნელობა ქონდა 
# Hello-Nika-how are your doing - მეშვიდე ხაზის კოდის შედეგი სადაც სეპარატორს მე მნიშვნელობად გადავეცი "-"

# # print(*objects, sep=' ', end='\n')-  newline character - ახალი ხაზის სიმბოლო 


print("Hello", name, "how are your doing?", sep=" ", end= " You are awesome!\n")