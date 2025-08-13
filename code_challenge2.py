animal = eval(input("enter amount to deposit --> "))
animal = int(animal)
dog = animal // 1000
print ("this is the breakdown of the amount deposited : \n 1000 : ", dog )
animal = animal - dog * 1000
cat = animal // 500
print ("\n 500 : ", cat)
animal = animal - cat * 500
bird = animal // 200
print ("\n 200 : ", bird)
animal = animal - bird * 200
rubbit = animal // 100
print ("\n 100 : ", rubbit)
animal = animal - rubbit * 100
fish = animal // 50
print ("\n 50 : ", fish)
animal = animal - fish * 50
fly = animal // 20
print ("\n 20 : ", fly)
animal = animal - fly * 20
monkey = animal // 5
print ("\n 5 : ", monkey)
animal = animal - monkey * 5
bee = animal // 1
print ("\n 1 : ", bee)
animal = animal - bee * 1