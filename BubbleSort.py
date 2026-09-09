#Bubble Sort
arr = [23, 13, 5, 46, -3, 33]
print(f"Array = {arr}")

step = 1
for i in range(len(arr)):
	index = 0
	
	print(f"Iteration {i + 1}") # Iteration count
	for x in range(1, len(arr)):

		val_idx = arr[index]
		
		# Shows the sorts with the bubble elements as 'x''
		arr[index] = str(arr[index])
		print(f"{step}) {arr}")
		arr[index] = int(arr[index])
		
		# Swapping the elements
		if arr[index] > arr[index + 1]: # > for ascending, < for descending
			arr[index] = arr[index + 1]
			arr[index + 1] = val_idx
			
			index +=1
		else:
			index += 1
		step += 1
		
	# Shows the last step in an iteration
	arr[index] = str(arr[index])
	print(f"{step}) {arr}")
	arr[index] = int(arr[index])
	
	step += 1
	print()
	
# Final outcome
print("Sorted Array:")
for i in range(len(arr)):
	print("%d" %arr[i]),
