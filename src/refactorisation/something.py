def print_list(output):
	for i in range(len(output)):
		print(str(output[i]))

def input_to_int(output):
	return int(input(output))

def input_to_string(output):
	return str(input(output))

def print_list_index(output):
	for i, item in enumerate(output):
		print(f"{i + 1}. {item}")

todo_list = []

intro = ["Options", "1. Add item","2. Mark item as done","3. View list","4. Exit"]
invalid = ["Invalid choice."," Please try again."]
intro_choice = "Enter your choice (1/2/3/4): "
intro_todolist = ["To-Do List:"]
prompt_noitem = ["No items in the list."]
prompt_additem = "Enter a new item: "
prompt_itemadded = ["Item added to the list."]
prompt_index = ["Enter the index of the item you want to mark as done: "]
ending = ["Goodbye!"]

while True:
	print_list(intro)
	choice = input_to_int(intro_choice)
	bool_empty_list = len(todo_list) <= 0
	if choice < 0 or 4 < choice:
		print_list(invalid)
		continue
	if choice == 4:
		break

	if choice == 1:
		todo_list.append(input_to_string(prompt_additem))
		print_list(prompt_itemadded)
		print(len(todo_list))

	if bool_empty_list:
		print_list(prompt_noitem)
		continue

	if choice == 2:
		print_list(intro_todolist)
		print_list_index(todo_list)
		index = input_to_int(prompt_index) - 1
		if index < 0 or len(todo_list)-1 < index:
			print_list(invalid)
			continue
		item = todo_list.pop(index)
		print(f"'{item}' marked as done.")
	if choice == 3:
		print(intro_todolist)
		print_list_index(todo_list)

print_list(ending)