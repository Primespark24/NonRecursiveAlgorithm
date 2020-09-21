Friend_Ages = {}

while(True):
    name = raw_input("\nWhat is your name?")
    age = input("\nHow old are you?")
    age = int(age)
    Friend_Ages[name] = age;

    question = raw_input("Are there more people to go?")
    if question == 'yes':
        continue
    else:
        break
    
sort_ages = sorted(Friend_Ages.items(), key = lambda x: x[1], reverse = True)
for name in sort_ages:
    print name
