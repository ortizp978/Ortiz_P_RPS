# set up a variable, check its value, and choose a path to follow based on that condition
temperature = int(input("input a value between 0 and 150: "))

if (temperature <= 4):
	print(ICE)

elif (temperature < 100):
	print(LIQUID)

else:
	print(vapor)