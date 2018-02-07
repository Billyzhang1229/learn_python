prompt = "age < 3: free , 3 ~ 12: $10 , age > 12: $15"
prompt += "\nPlease enter you age: "

age = ""
while age != 'quit':
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("Free")
    elif age <= 12:
        print("$10")
    else:
        print("$15")