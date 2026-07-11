todo_list=[]
while True:
    print ("==== Terminal Based To Do List ====")
    print("Menu-\n1.Add Task\n2.View Tasks\n3.Delete Task\n4.Exit")

    try:
        user_choice=int(input("Enter your choice (1-4):"))
    except ValueError:
        print("Invalid Choice! Please enter a number")
        continue
    if user_choice not in (1,5):
        print("Please enter your choice in (1-4)")