name = ['david', 'billy', 'richard']

can_not_come = name[1]
print(can_not_come.title() + " can not come to have dinner.")

name[1] = 'tony'

message1 = "I invite " + name[0].title() + " to have dinner."
print(message1)

message2 = "I invite " + name[1].title() + " to have dinner."
print(message2)

message3 = "I invite " + name[2].title() + " to have dinner."
print(message3)

print('I ordered a bigger table.')

name.insert(0, 'tom')

name.insert(2, 'jack')

name.append('perry')

message1 = "I invite " + name[0].title() + " to have dinner."
print(message1)

message2 = "I invite " + name[1].title() + " to have dinner."
print(message2)

message3 = "I invite " + name[2].title() + " to have dinner."
print(message3)

message4 = "I invite " + name[3].title() + " to have dinner."
print(message4)

message5 = "I invite " + name[4].title() + " to have dinner."
print(message5)

message11 = "I invite " + name[5].title() + " to have dinner."
print(message11)

print("Because the restaurant doesn't have a bigger table, so I can only invite 2 people.")

poped_1 = name.pop(0)

poped_2 = name.pop(0)

poped_3 = name.pop(0)

poped_4 = name.pop(0)

message6 = "I'm sorry " + poped_1 + ", I can't invite you to have dinner."
print(message6)

message7 = "I'm sorry " + poped_2 + ", I can't invite you to have dinner."
print(message7)

message8 = "I'm sorry " + poped_3 + ", I can't invite you to have dinner."
print(message8)

message9 = "I'm sorry " + poped_4 + ", I can't invite you to have dinner."
print(message9)

message10 = "I'm glad to told you that " + name[0]+ ", you can come to the restaurant to have dinner with me."
print(message10)

message11 = "I'm glad to told you that " + name[1]+ ", you can come to the restaurant to have dinner with me."
print(message11)

del name[0]

del name[0]

print(name)