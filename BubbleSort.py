# Bubble sort
arr = [17, 28, 4, 63, 54, -6, 7]
print(f"Array = {arr}")

step = 1 # for counting the steps
for i in range(len(arr)):
	print(f"Iteration {i + 1}") # Iteration count
	for x in range(len(arr) - 1):	

		# Shows the sorts with the bubble elements as ''
		arr[x] = str(arr[x])
		print(f"{step}) {arr}")
		arr[x] = int(arr[x])
		
		# Swapping the elements
		if arr[x] > arr[x + 1]: # > for ascending, < for descending
			arr[x], arr[x + 1] = arr[x + 1], arr[x]
		step += 1
		
	# Shows the last step in an iteration
	arr[x + 1] = str(arr[x + 1])
	print(f"{step}) {arr}")
	arr[x + 1] = int(arr[x + 1])
	
	step += 1
	print()
	
# Final outcome
print("Sorted Array:")
for i in range(len(arr)):
	print("%d" %arr[i]) # I don't really understand this part
