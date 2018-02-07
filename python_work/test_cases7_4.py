prompt = "You can choose some toppings"
prompt += "\nplease enter the toppings or enter 'quit' to finish: "

request = ""
while request != "quit":
    request = input(prompt)

    if request != 'quit':
        print("Adding " + request)