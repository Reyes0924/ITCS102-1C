temp = eval(input("enter temperature outside: "))

if temp >= 0:
	print ("tempereture is considered freezing temperature")

elif temp >= 1 and temp <= 20:
	print ("tempereture is considered as extremely cold")

elif temp <= 30 and temp >= 40:
	print ("tempereture is considered as moderately cold")

elif temp <= 50 and temp >= 60:
	print ("tempereture is considered as lukevarm")

elif temp <= 70 and temp >= 80:
	print ("tempereture is considered as hot")

elif temp <= 90 and temp >= 100:
	print ("tempereture is considered boiling cold")

elif temp >= 500 and temp <= 1000:
	print ("dangerou temperature")

else:
	print("Invalid temperature")
