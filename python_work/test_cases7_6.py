prompt = "You can choose some toppings."
prompt += "\nplease enter the toppings or enter 'quit' to finish: "

active = True
while active:
    message = input(prompt)

    if message != 'quit':
        print("Adding" + message)
    else:
    	break